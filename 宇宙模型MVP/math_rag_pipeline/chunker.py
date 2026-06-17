from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


BOUNDARY_RE = re.compile(
    r"^(#{1,6}\s+|(?:\*\*)?(?:Theorem|Lemma|Proof|Example|Definition|Corollary|定理|引理|证明|例|定义|推论)\b)",
    flags=re.IGNORECASE,
)
METADATA_RE = re.compile(r"<!--\s*block_metadata:\s*(\{.*?\})\s*-->", flags=re.DOTALL)


def split_markdown_for_rag(
    markdown: str,
    metadata: dict[str, Any] | None = None,
    chunk_size: int = 1200,
    chunk_overlap: int = 150,
) -> list[dict[str, Any]]:
    """Split Markdown into RAG chunks without cutting math/table blocks."""

    units = _parse_units(markdown)
    chunks: list[dict[str, Any]] = []
    current: list[str] = []
    current_meta: list[dict[str, Any]] = []
    current_tokens = 0

    for unit in units:
        unit_tokens = _estimate_tokens(unit["text"])
        starts_boundary = bool(BOUNDARY_RE.search(unit["text"].lstrip().splitlines()[0] if unit["text"].strip() else ""))
        if current and (current_tokens + unit_tokens > chunk_size or (starts_boundary and current_tokens >= chunk_size * 0.55)):
            chunks.append(_make_chunk(current, current_meta, metadata, len(chunks)))
            current, current_meta, current_tokens = _overlap_tail(current, current_meta, chunk_overlap)
        current.append(unit["text"])
        current_meta.extend(unit["metadata"])
        current_tokens += unit_tokens

    if current:
        chunks.append(_make_chunk(current, current_meta, metadata, len(chunks)))
    return chunks


def avoid_splitting_math_blocks(markdown: str) -> list[str]:
    return [unit["text"] for unit in _parse_units(markdown) if unit["kind"] == "math"]


def avoid_splitting_tables(markdown: str) -> list[str]:
    return [unit["text"] for unit in _parse_units(markdown) if unit["kind"] == "table"]


def write_chunks_jsonl(chunks: list[dict[str, Any]], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")


def _parse_units(markdown: str) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    lines = markdown.splitlines()
    buffer: list[str] = []
    metadata_buffer: list[dict[str, Any]] = []
    in_math = False
    in_html_table = False

    def flush(kind: str = "text") -> None:
        nonlocal buffer, metadata_buffer
        text = "\n".join(buffer).strip()
        if text:
            units.append({"text": text, "kind": kind, "metadata": list(metadata_buffer)})
        buffer = []
        metadata_buffer = []

    for line in lines:
        meta_match = METADATA_RE.match(line.strip())
        if meta_match:
            try:
                metadata_buffer.append(json.loads(meta_match.group(1)))
            except json.JSONDecodeError:
                pass
            buffer.append(line)
            continue

        stripped = line.strip()
        if stripped.startswith("<table"):
            if buffer:
                flush()
            in_html_table = True
        if stripped.startswith("$$"):
            if not in_math and buffer:
                flush()
            in_math = not in_math
            buffer.append(line)
            if not in_math:
                flush("math")
            continue

        if not in_math and not in_html_table and not stripped:
            flush(_guess_kind("\n".join(buffer)))
            continue

        buffer.append(line)
        if in_html_table and stripped.endswith("</table>"):
            in_html_table = False
            flush("table")

    flush(_guess_kind("\n".join(buffer)))
    return units


def _guess_kind(text: str) -> str:
    if not text.strip():
        return "text"
    if "$$" in text or re.search(r"\\begin\{(align|equation|matrix|cases|array)", text):
        return "math"
    if re.search(r"<\s*/?\s*table\b", text, re.IGNORECASE) or sum(1 for line in text.splitlines() if "|" in line) >= 2:
        return "table"
    return "text"


def _make_chunk(parts: list[str], block_meta: list[dict[str, Any]], base_meta: dict[str, Any] | None, index: int) -> dict[str, Any]:
    text = "\n\n".join(part.strip() for part in parts if part.strip()).strip()
    pages = sorted({item.get("page") for item in block_meta if item.get("page") is not None})
    engines = sorted({item.get("ocr_engine") for item in block_meta if item.get("ocr_engine")})
    metadata = dict(base_meta or {})
    metadata.update(
        {
            "chunk_index": index,
            "pages": pages,
            "ocr_engines": engines,
            "block_ids": [item.get("block_id") for item in block_meta if item.get("block_id")],
            "chapter": _last_non_empty(block_meta, "chapter"),
            "section": _last_non_empty(block_meta, "section"),
            "token_estimate": _estimate_tokens(text),
        }
    )
    return {"id": f"chunk-{index:05d}", "text": text, "metadata": metadata}


def _overlap_tail(
    parts: list[str],
    block_meta: list[dict[str, Any]],
    overlap_tokens: int,
) -> tuple[list[str], list[dict[str, Any]], int]:
    if overlap_tokens <= 0:
        return [], [], 0
    tail: list[str] = []
    total = 0
    for part in reversed(parts):
        total += _estimate_tokens(part)
        tail.insert(0, part)
        if total >= overlap_tokens:
            break
    return tail, block_meta[-len(tail) :] if tail else [], total


def _estimate_tokens(text: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    words = len(re.findall(r"[A-Za-z0-9_\\]+", text))
    symbols = len(re.findall(r"[=+\-*/^{}[\]()]|∑|∫|∂|≤|≥", text))
    return max(1, cjk + words + symbols // 2)


def _last_non_empty(items: list[dict[str, Any]], key: str) -> Any:
    for item in reversed(items):
        if item.get(key):
            return item[key]
    return None
