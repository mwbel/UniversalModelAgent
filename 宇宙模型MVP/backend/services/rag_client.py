from __future__ import annotations

import json
import math
import re
import time
import zipfile
from collections import Counter
from dataclasses import dataclass
from email.parser import BytesParser
from email.policy import default
from pathlib import Path
from time import perf_counter
from typing import Any
from xml.etree import ElementTree

import requests

from backend.config import SETTINGS
from backend.rag_catalog import DEFAULT_RAG_STRATEGIES, build_strategy_catalog

ROOT_DIR = Path(__file__).resolve().parents[2]
UNIVMODEL_DIR = ROOT_DIR.parent
PLANET_MOTION_DIR = UNIVMODEL_DIR / "行星运动模型"
PLANET_MOTION_KB_ID = "planet-motion"
PLANET_MOTION_DOCS = [
    "行星运动数值分析作业.md",
    "README.md",
    "README_DE_MODEL.md",
    "DE模型实现说明.md",
    "数值积分与插值详解.md",
]
LOCAL_RAG_DIR = ROOT_DIR / ".local_rag"
LOCAL_RAG_DB_PATH = LOCAL_RAG_DIR / "store.json"
TOKEN_PATTERN = re.compile(r"[\u4e00-\u9fff]|[A-Za-z0-9_]+")
LATIN_TERM_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9_]{1,}|\d{2,}")
CHINESE_SEQUENCE_PATTERN = re.compile(r"[\u4e00-\u9fff]{2,}")
CHUNK_SIZE = 520
CHUNK_OVERLAP = 120
PARENT_WINDOW = 3
AUTO_RAG_MIN_SCORE = 0.12
AUTO_RAG_STOP_TERMS = {
    "什么",
    "为什么",
    "怎么",
    "如何",
    "是否",
    "请问",
    "这个",
    "那个",
    "一个",
    "一下",
    "可以",
    "进行",
    "解释",
    "介绍",
    "说明",
    "问题",
    "内容",
    "你好",
}


def _tokenize(text: str) -> list[str]:
    return [item.group(0).lower() for item in TOKEN_PATTERN.finditer(text or "")]


def _auto_rag_terms(question: str) -> list[str]:
    terms: set[str] = set()
    lowered = question.lower()
    for match in LATIN_TERM_PATTERN.finditer(lowered):
        value = match.group(0).strip()
        if value and value not in AUTO_RAG_STOP_TERMS:
            terms.add(value)
    for match in CHINESE_SEQUENCE_PATTERN.finditer(question):
        sequence = match.group(0)
        if sequence in AUTO_RAG_STOP_TERMS:
            continue
        max_len = min(6, len(sequence))
        for size in range(2, max_len + 1):
            for start in range(0, len(sequence) - size + 1):
                term = sequence[start : start + size]
                if term not in AUTO_RAG_STOP_TERMS:
                    terms.add(term)
    return sorted(terms, key=lambda item: (-len(item), item))


def _has_auto_rag_evidence(question_terms: list[str], context: dict[str, Any]) -> bool:
    content = str(context.get("content") or "").lower()
    source = str(context.get("source") or "").lower()
    haystack = f"{source}\n{content}"
    return any(term.lower() in haystack for term in question_terms)


def _safe_excerpt(text: str, limit: int = 220) -> str:
    compact = " ".join((text or "").split())
    if len(compact) <= limit:
        return compact
    return f"{compact[: limit - 3]}..."


def _normalize_citation(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": item.get("title") or "未命名来源",
        "snippet": item.get("snippet") or "",
        "url": item.get("url") or "",
    }


def _coerce_number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isfinite(number):
        return number
    return None


def _split_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    cleaned = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not cleaned:
        return []
    chunks: list[str] = []
    start = 0
    text_length = len(cleaned)
    while start < text_length:
        end = min(text_length, start + chunk_size)
        chunk = cleaned[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= text_length:
            break
        start = max(end - overlap, start + 1)
    return chunks


def _read_docx_text(file_bytes: bytes) -> str:
    from io import BytesIO

    with zipfile.ZipFile(BytesIO(file_bytes)) as archive:
        xml_bytes = archive.read("word/document.xml")
    root = ElementTree.fromstring(xml_bytes)
    texts = [node.text for node in root.iter() if node.tag.endswith("}t") and node.text]
    return "\n".join(texts)


def _decode_text(file_bytes: bytes, filename: str) -> str:
    suffix = Path(filename).suffix.lower()
    if suffix == ".docx":
        return _read_docx_text(file_bytes)
    if suffix == ".pdf":
        raise ValueError("当前本地 RAG 还没有接入 PDF 文本提取，建议先上传 TXT、MD 或 DOCX。")

    for encoding in ("utf-8", "utf-8-sig", "gb18030", "gbk"):
        try:
            return file_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue
    return file_bytes.decode("utf-8", errors="ignore")


def _suggest_kb_id(filename: str) -> str:
    stem = Path(filename or "").stem.strip()
    parts = [item.strip() for item in re.split(r"[\s._\-()（）【】\[\]、，,]+", stem) if item.strip()]
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    if parts:
        return parts[0]
    return "default"


def _parse_multipart(body: bytes, content_type: str) -> tuple[bytes, str, str]:
    header_bytes = f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode("utf-8")
    message = BytesParser(policy=default).parsebytes(header_bytes + body)
    file_bytes = b""
    filename = ""
    kb_id = "default"

    for part in message.iter_parts():
        disposition = part.get("Content-Disposition", "")
        if "form-data" not in disposition:
            continue
        name = part.get_param("name", header="Content-Disposition")
        if name == "file":
            payload = part.get_payload(decode=True) or b""
            file_bytes = payload
            filename = part.get_filename() or "upload.txt"
        elif name == "kb_id":
            payload = part.get_payload(decode=True) or b""
            kb_id = payload.decode("utf-8", errors="ignore").strip() or kb_id

    if not file_bytes:
        raise ValueError("请求里没有解析到文件内容。")
    if not kb_id or kb_id.lower() == "default":
        kb_id = _suggest_kb_id(filename)
    return file_bytes, filename, kb_id


def _term_overlap_score(query_tokens: list[str], chunk_tokens: list[str]) -> float:
    if not query_tokens or not chunk_tokens:
        return 0.0
    query_counter = Counter(query_tokens)
    chunk_counter = Counter(chunk_tokens)
    overlap = sum(min(count, chunk_counter[token]) for token, count in query_counter.items())
    return overlap / max(len(query_tokens), 1)


def _keyword_position_boost(query_tokens: list[str], chunk_text: str) -> float:
    lowered = chunk_text.lower()
    hits = 0
    for token in set(query_tokens):
        index = lowered.find(token)
        if index >= 0:
            hits += 1
    return hits / max(len(set(query_tokens)), 1)


def _score_naive(query_tokens: list[str], chunk_text: str, chunk_tokens: list[str]) -> float:
    overlap = _term_overlap_score(query_tokens, chunk_tokens)
    density = overlap / max(len(chunk_tokens), 1) * 12
    return min(1.0, overlap * 0.72 + density * 0.28)


def _score_hybrid(query_tokens: list[str], chunk_text: str, chunk_tokens: list[str]) -> float:
    naive = _score_naive(query_tokens, chunk_text, chunk_tokens)
    keyword = _keyword_position_boost(query_tokens, chunk_text)
    lexical = len(set(query_tokens) & set(chunk_tokens)) / max(len(set(query_tokens)), 1)
    return min(1.0, naive * 0.45 + keyword * 0.2 + lexical * 0.35)


def _json_load(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"knowledge_bases": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _json_dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _build_document_record(doc_id: str, filename: str, text: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    chunks = _split_text(text)
    return {
        "doc_id": doc_id,
        "filename": filename,
        "title": filename,
        "metadata": metadata or {},
        "chunks": [
            {
                "chunk_id": f"{doc_id}-chunk-{index + 1}",
                "chunk_index": index,
                "content": chunk,
                "tokens": _tokenize(chunk),
            }
            for index, chunk in enumerate(chunks)
        ],
    }


@dataclass(slots=True)
class RetrievalItem:
    doc_id: str
    doc_title: str
    chunk_id: str
    chunk_index: int
    chunk_text: str
    score: float


class RagClient:
    def __init__(self) -> None:
        LOCAL_RAG_DIR.mkdir(parents=True, exist_ok=True)

    def _load_store(self) -> dict[str, Any]:
        return _json_load(LOCAL_RAG_DB_PATH)

    def _save_store(self, payload: dict[str, Any]) -> None:
        _json_dump(LOCAL_RAG_DB_PATH, payload)

    def _get_kb(self, kb_id: str) -> dict[str, Any] | None:
        if kb_id == PLANET_MOTION_KB_ID:
            self.ensure_builtin_knowledge_bases()
        store = self._load_store()
        return (store.get("knowledge_bases") or {}).get(kb_id)

    def _kb_items(self, kb_id: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
        kb = self._get_kb(kb_id)
        if not kb:
            return None, []
        return kb, kb.get("documents") or []

    def _build_contexts(
        self,
        kb_id: str,
        documents: list[dict[str, Any]],
        retrieved: list[RetrievalItem],
        variant: str,
    ) -> list[dict[str, Any]]:
        if variant == "parent_document":
            grouped: dict[str, list[RetrievalItem]] = {}
            for item in retrieved:
                grouped.setdefault(item.doc_id, []).append(item)

            contexts: list[dict[str, Any]] = []
            documents_by_id = {doc["doc_id"]: doc for doc in documents}
            for doc_id, items in list(grouped.items())[:4]:
                document = documents_by_id.get(doc_id)
                if not document:
                    continue
                chunks = document.get("chunks") or []
                focus_indexes = sorted({item.chunk_index for item in items})
                expanded_parts: list[str] = []
                for index in focus_indexes:
                    start = max(0, index - 1)
                    end = min(len(chunks), index + PARENT_WINDOW)
                    expanded_parts.extend(chunk["content"] for chunk in chunks[start:end])
                content = "\n\n".join(dict.fromkeys(expanded_parts))
                score = max(item.score for item in items)
                contexts.append(
                    {
                        "content": content,
                        "score": round(score, 4),
                        "source": document.get("filename") or document.get("title") or doc_id,
                        "page": None,
                        "metadata": {
                            "kb_id": kb_id,
                            "doc_id": doc_id,
                            "matched_chunk_indexes": focus_indexes,
                            "strategy": variant,
                        },
                    }
                )
            return contexts[:4]

        contexts: list[dict[str, Any]] = []
        for item in retrieved[:6]:
            contexts.append(
                {
                    "content": item.chunk_text,
                    "score": round(item.score, 4),
                    "source": item.doc_title,
                    "page": None,
                    "metadata": {
                        "kb_id": kb_id,
                        "doc_id": item.doc_id,
                        "chunk_id": item.chunk_id,
                        "chunk_index": item.chunk_index,
                        "strategy": variant,
                    },
                }
            )
        return contexts

    def _build_citations(self, contexts: list[dict[str, Any]]) -> list[dict[str, Any]]:
        citations: list[dict[str, Any]] = []
        for context in contexts[:4]:
            citations.append(
                _normalize_citation(
                    {
                        "title": context.get("source") or "本地知识库片段",
                        "snippet": _safe_excerpt(str(context.get("content") or "")),
                        "url": "",
                    }
                )
            )
        return citations

    def ensure_builtin_knowledge_bases(self) -> None:
        source_files = [PLANET_MOTION_DIR / filename for filename in PLANET_MOTION_DOCS]
        existing_files = [path for path in source_files if path.exists()]
        if not existing_files:
            return

        signature = {
            str(path): {
                "mtime": path.stat().st_mtime,
                "size": path.stat().st_size,
            }
            for path in existing_files
        }
        store = self._load_store()
        knowledge_bases = store.setdefault("knowledge_bases", {})
        kb = knowledge_bases.get(PLANET_MOTION_KB_ID)
        if kb and (kb.get("metadata") or {}).get("signature") == signature:
            return

        documents: list[dict[str, Any]] = []
        for index, path in enumerate(existing_files, start=1):
            text = path.read_text(encoding="utf-8", errors="ignore")
            document = _build_document_record(
                doc_id=f"builtin-planet-motion-{index}",
                filename=path.name,
                text=text,
                metadata={
                    "builtin": True,
                    "source_path": str(path),
                },
            )
            if document.get("chunks"):
                documents.append(document)

        knowledge_bases[PLANET_MOTION_KB_ID] = {
            "documents": documents,
            "updated_at": time.time(),
            "metadata": {
                "builtin": True,
                "source_dir": str(PLANET_MOTION_DIR),
                "signature": signature,
            },
        }
        self._save_store(store)

    def _generate_answer(
        self,
        question: str,
        contexts: list[dict[str, Any]],
        history: list[dict[str, Any]],
    ) -> tuple[str, dict[str, Any] | None]:
        if not contexts:
            return "", None

        joined_context = "\n\n".join(
            f"[来源 {index + 1}] {context.get('source')}\n{context.get('content')}"
            for index, context in enumerate(contexts[:4])
        )
        recent_history = [
            {
                "role": item.get("role", "user"),
                "content": str(item.get("content") or "")[:1200],
            }
            for item in history[-6:]
            if str(item.get("content") or "").strip()
        ]

        if SETTINGS.llm_base_url and SETTINGS.llm_api_key and SETTINGS.llm_model:
            try:
                response = requests.post(
                    f"{SETTINGS.llm_base_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {SETTINGS.llm_api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": SETTINGS.llm_model,
                        "temperature": 0.2,
                        "messages": [
                            {
                                "role": "system",
                                "content": (
                                    "你是一个基于本地知识库回答问题的助手。"
                                    "请优先依据给定上下文作答，不要编造没有出现的信息。"
                                    "如果用户要求可视化，请只给简洁文字解释；"
                                    "不要输出 ASCII 字符画、Markdown 代码块图、Mermaid 或伪图，"
                                    "交互式图形会由 A2UI 组件单独渲染。"
                                ),
                            },
                            *recent_history,
                            {
                                "role": "user",
                                "content": (
                                    f"问题：{question}\n\n"
                                    f"知识库上下文：\n{joined_context}\n\n"
                                    "请给出简洁、直接的中文回答。"
                                    "不要用字符画模拟图形。"
                                ),
                            },
                        ],
                    },
                    timeout=SETTINGS.request_timeout_seconds,
                )
                response.raise_for_status()
                payload = response.json()
                answer = (
                    (((payload.get("choices") or [{}])[0]).get("message") or {}).get("content")
                    or ""
                ).strip()
                if answer:
                    return answer, payload.get("usage")
            except Exception:
                pass

        answer = (
            f"我在本地知识库里找到了 {len(contexts)} 段相关内容。"
            f"最相关的材料来自《{contexts[0].get('source') or '本地文档'}》。\n\n"
            f"{_safe_excerpt(str(contexts[0].get('content') or ''), limit=320)}"
        )
        return answer, None

    def ask(
        self,
        question: str,
        history: list[dict[str, Any]],
        variant: str | None = None,
        kb_id: str | None = None,
    ) -> dict[str, Any]:
        started = perf_counter()
        strategy = (variant or SETTINGS.default_rag_strategy or "naive").strip() or "naive"
        normalized_strategy = strategy.lower().replace("-", "_")
        kb_name = kb_id or SETTINGS.default_kb_id
        if kb_name == PLANET_MOTION_KB_ID:
            self.ensure_builtin_knowledge_bases()
        kb, documents = self._kb_items(kb_name)
        if not kb or not documents:
            return {
                "ok": False,
                "error": f"本地知识库 `{kb_name}` 还没有文档，请先上传文件。",
                "raw": None,
                "answer": "",
                "citations": [],
                "contexts": [],
            }

        retrieval = self.retrieve_contexts(
            question=question,
            variant=normalized_strategy,
            kb_id=kb_name,
            limit=6,
            started=started,
        )
        contexts = retrieval["contexts"]
        citations = retrieval["citations"]
        answer, usage = self._generate_answer(question, contexts, history)

        return {
            "ok": bool(answer),
            "answer": answer,
            "citations": citations,
            "contexts": contexts,
            "strategy": normalized_strategy,
            "resolvedStrategy": normalized_strategy,
            "latencyMs": round((perf_counter() - started) * 1000, 2),
            "tokenUsage": usage,
            "raw": retrieval["raw"],
        }

    def ask_auto(
        self,
        question: str,
        history: list[dict[str, Any]],
        variant: str | None = None,
        preferred_kb_id: str | None = None,
    ) -> dict[str, Any]:
        started = perf_counter()
        self.ensure_builtin_knowledge_bases()
        store = self._load_store()
        knowledge_bases = store.get("knowledge_bases") or {}
        if not knowledge_bases:
            return {
                "ok": False,
                "error": "本地知识库还没有文档。",
                "answer": "",
                "citations": [],
                "contexts": [],
                "strategy": (variant or SETTINGS.default_rag_strategy or "hybrid").lower().replace("-", "_"),
                "resolvedStrategy": None,
                "latencyMs": round((perf_counter() - started) * 1000, 2),
                "raw": None,
            }

        question_terms = _auto_rag_terms(question)
        if not question_terms:
            return {
                "ok": False,
                "error": "问题中没有足够明确的本地检索关键词。",
                "answer": "",
                "citations": [],
                "contexts": [],
                "strategy": (variant or SETTINGS.default_rag_strategy or "hybrid").lower().replace("-", "_"),
                "resolvedStrategy": None,
                "latencyMs": round((perf_counter() - started) * 1000, 2),
                "raw": None,
            }

        kb_ids = list(knowledge_bases.keys())
        if preferred_kb_id and preferred_kb_id in knowledge_bases:
            kb_ids = [preferred_kb_id, *[kb_id for kb_id in kb_ids if kb_id != preferred_kb_id]]

        all_contexts: list[dict[str, Any]] = []
        raw_retrieved: list[dict[str, Any]] = []
        normalized_strategy = (variant or "hybrid").strip().lower().replace("-", "_") or "hybrid"
        for kb_id in kb_ids:
            retrieval = self.retrieve_contexts(
                question=question,
                variant=normalized_strategy,
                kb_id=kb_id,
                limit=4,
                started=started,
            )
            for context in retrieval.get("contexts") or []:
                score = _coerce_number(context.get("score")) or 0
                if score < AUTO_RAG_MIN_SCORE:
                    continue
                if not _has_auto_rag_evidence(question_terms, context):
                    continue
                all_contexts.append(context)
            raw = retrieval.get("raw") or {}
            for item in raw.get("retrieved") or []:
                raw_retrieved.append({"kb_id": kb_id, **item})

        all_contexts.sort(key=lambda item: float(item.get("score") or 0), reverse=True)
        contexts = all_contexts[:6]
        citations = self._build_citations(contexts)
        answer, usage = self._generate_answer(question, contexts, history)

        return {
            "ok": bool(answer and contexts),
            "answer": answer,
            "citations": citations,
            "contexts": contexts,
            "strategy": normalized_strategy,
            "resolvedStrategy": "auto_local_first",
            "latencyMs": round((perf_counter() - started) * 1000, 2),
            "tokenUsage": usage,
            "raw": {
                "kb_ids": kb_ids,
                "question_terms": question_terms[:20],
                "retrieved": raw_retrieved[:12],
            },
        }

    def retrieve_contexts(
        self,
        question: str,
        variant: str | None = None,
        kb_id: str | None = None,
        limit: int = 6,
        started: float | None = None,
    ) -> dict[str, Any]:
        started_at = started or perf_counter()
        strategy = (variant or SETTINGS.default_rag_strategy or "naive").strip() or "naive"
        normalized_strategy = strategy.lower().replace("-", "_")
        kb_name = kb_id or SETTINGS.default_kb_id
        if kb_name == PLANET_MOTION_KB_ID:
            self.ensure_builtin_knowledge_bases()
        kb, documents = self._kb_items(kb_name)
        if not kb or not documents:
            return {
                "ok": False,
                "error": f"本地知识库 `{kb_name}` 还没有文档，请先上传文件。",
                "citations": [],
                "contexts": [],
                "strategy": normalized_strategy,
                "resolvedStrategy": normalized_strategy,
                "latencyMs": round((perf_counter() - started_at) * 1000, 2),
                "raw": None,
            }

        query_tokens = _tokenize(question)
        retrieved: list[RetrievalItem] = []
        for document in documents:
            for chunk in document.get("chunks") or []:
                chunk_text = str(chunk.get("content") or "")
                chunk_tokens = chunk.get("tokens") or _tokenize(chunk_text)
                if normalized_strategy == "hybrid":
                    score = _score_hybrid(query_tokens, chunk_text, chunk_tokens)
                else:
                    score = _score_naive(query_tokens, chunk_text, chunk_tokens)
                if score <= 0:
                    continue
                retrieved.append(
                    RetrievalItem(
                        doc_id=document["doc_id"],
                        doc_title=document.get("filename") or document.get("title") or document["doc_id"],
                        chunk_id=chunk["chunk_id"],
                        chunk_index=int(chunk.get("chunk_index") or 0),
                        chunk_text=chunk_text,
                        score=score,
                    )
                )

        retrieved.sort(key=lambda item: item.score, reverse=True)
        contexts = self._build_contexts(kb_name, documents, retrieved[:limit], normalized_strategy)
        citations = self._build_citations(contexts)
        return {
            "ok": bool(contexts),
            "citations": citations,
            "contexts": contexts,
            "strategy": normalized_strategy,
            "resolvedStrategy": normalized_strategy,
            "latencyMs": round((perf_counter() - started_at) * 1000, 2),
            "raw": {
                "kb_id": kb_name,
                "retrieved": [
                    {
                        "doc_id": item.doc_id,
                        "chunk_id": item.chunk_id,
                        "score": round(item.score, 4),
                    }
                    for item in retrieved[:8]
                ],
            },
        }

    def get_strategies(self) -> dict[str, Any]:
        items = build_strategy_catalog(
            [
                {
                    "id": strategy["id"],
                    "label": strategy["label"],
                    "summary": strategy["summary"],
                    "workflow": strategy["workflow"],
                }
                for strategy in DEFAULT_RAG_STRATEGIES
            ]
        )
        for item in items:
            item["available"] = True
        return {"ok": True, "error": None, "items": items}

    def get_knowledge_bases(self) -> dict[str, Any]:
        self.ensure_builtin_knowledge_bases()
        store = self._load_store()
        knowledge_bases = store.get("knowledge_bases") or {}
        items = []
        for kb_id, kb in knowledge_bases.items():
            documents = kb.get("documents") or []
            chunk_count = sum(len(doc.get("chunks") or []) for doc in documents)
            items.append(
                {
                    "kb_id": kb_id,
                    "doc_count": len(documents),
                    "chunk_count": chunk_count,
                    "updated_at": kb.get("updated_at"),
                }
            )
        items.sort(key=lambda item: item["kb_id"])
        return {"ok": True, "error": None, "items": items}

    def ingest_markdown_documents(
        self,
        kb_id: str,
        documents: list[dict[str, Any]],
        replace: bool = True,
    ) -> dict[str, Any]:
        if not kb_id.strip():
            return {"ok": False, "error": "kb_id 不能为空。"}
        if not documents:
            return {"ok": False, "error": "没有可摄入的 Markdown 文档。"}

        store = self._load_store()
        knowledge_bases = store.setdefault("knowledge_bases", {})
        if replace:
            kb = {"documents": []}
            knowledge_bases[kb_id] = kb
        else:
            kb = knowledge_bases.setdefault(kb_id, {"documents": []})

        indexed_documents = kb.setdefault("documents", [])
        start_index = len(indexed_documents)
        added = 0
        skipped = 0
        chunk_count = 0

        for index, item in enumerate(documents, start=start_index + 1):
            text = str(item.get("text") or "")
            if not text.strip():
                skipped += 1
                continue
            filename = str(item.get("filename") or item.get("title") or f"document-{index}.md")
            doc_id = str(item.get("id") or f"doc-{index}")
            document_record = _build_document_record(
                doc_id=doc_id,
                filename=filename,
                text=text,
                metadata=item.get("metadata") if isinstance(item.get("metadata"), dict) else {},
            )
            if not document_record.get("chunks"):
                skipped += 1
                continue
            indexed_documents.append(document_record)
            added += 1
            chunk_count += len(document_record.get("chunks") or [])

        kb["updated_at"] = time.time()
        kb["metadata"] = {
            **(kb.get("metadata") or {}),
            "last_ingest_source": "markdown_library",
            "replace": replace,
        }
        self._save_store(store)
        return {
            "ok": added > 0,
            "kbId": kb_id,
            "documents": added,
            "skipped": skipped,
            "chunks": chunk_count,
            "indexedChunks": {strategy["id"]: chunk_count for strategy in DEFAULT_RAG_STRATEGIES},
        }

    def upload_document(self, body: bytes, content_type: str) -> dict[str, Any]:
        try:
            file_bytes, filename, kb_id = _parse_multipart(body, content_type)
            text = _decode_text(file_bytes, filename)
            chunks = _split_text(text)
            if not chunks:
                return {"ok": False, "error": "文档内容为空，无法建立本地知识库。"}

            store = self._load_store()
            knowledge_bases = store.setdefault("knowledge_bases", {})
            kb = knowledge_bases.setdefault(kb_id, {"documents": []})
            documents = kb.setdefault("documents", [])

            doc_id = f"doc-{len(documents) + 1}"
            document_record = _build_document_record(doc_id=doc_id, filename=filename, text=text)
            documents.append(document_record)
            kb["updated_at"] = time.time()
            self._save_store(store)
            return {
                "ok": True,
                "kbId": kb_id,
                "chunks": len(chunks),
                "indexedChunks": {strategy["id"]: len(chunks) for strategy in DEFAULT_RAG_STRATEGIES},
                "raw": {"filename": filename, "doc_id": doc_id},
            }
        except ValueError as error:
            return {"ok": False, "error": str(error)}
        except zipfile.BadZipFile:
            return {"ok": False, "error": "DOCX 文件读取失败，请确认文件没有损坏。"}
        except Exception as error:  # noqa: BLE001
            return {"ok": False, "error": f"本地知识库上传失败：{error}"}


RAG_CLIENT = RagClient()
