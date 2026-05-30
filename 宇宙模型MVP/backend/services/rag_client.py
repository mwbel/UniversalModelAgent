from __future__ import annotations

from typing import Any

from backend.config import SETTINGS
from backend.services.http_json import safe_get_json, safe_post_json


def _normalize_citations(payload: dict[str, Any]) -> list[dict[str, Any]]:
    raw_items = payload.get("citations") or payload.get("sources") or payload.get("references") or []
    citations: list[dict[str, Any]] = []
    if isinstance(raw_items, list):
        for item in raw_items[:6]:
            if isinstance(item, dict):
                citations.append(
                    {
                        "title": item.get("title") or item.get("name") or "未命名来源",
                        "snippet": item.get("snippet") or item.get("content") or item.get("text") or "",
                        "url": item.get("url") or "",
                    }
                )
            else:
                citations.append({"title": str(item), "snippet": "", "url": ""})
    return citations


def _normalize_contexts(payload: dict[str, Any]) -> list[dict[str, Any]]:
    raw_items = payload.get("contexts") or []
    contexts: list[dict[str, Any]] = []
    if isinstance(raw_items, list):
        for item in raw_items[:8]:
            if isinstance(item, dict):
                metadata = item.get("metadata") or {}
                contexts.append(
                    {
                        "content": item.get("content") or "",
                        "score": item.get("score"),
                        "source": metadata.get("source") or "",
                        "page": metadata.get("page"),
                        "metadata": metadata,
                    }
                )
            else:
                contexts.append({"content": str(item), "score": None, "source": "", "page": None, "metadata": {}})
    return contexts


class RagClient:
    def ask(
        self,
        question: str,
        history: list[dict[str, Any]],
        variant: str | None = None,
        kb_id: str | None = None,
    ) -> dict[str, Any]:
        url = f"{SETTINGS.rag_base_url}{SETTINGS.rag_chat_path}"
        strategy = variant or SETTINGS.default_rag_strategy
        payload = {
            "question": question,
            "strategy": strategy,
            "kb_id": kb_id or SETTINGS.default_kb_id,
            "params": {},
        }

        data, error = safe_post_json(url, payload, SETTINGS.request_timeout_seconds)
        if error:
            return {
                "ok": False,
                "error": error,
                "raw": None,
                "answer": "",
                "citations": [],
            }

        body = data or {}
        answer = (
            body.get("answer")
            or body.get("response")
            or body.get("content")
            or body.get("message")
            or ""
        )
        return {
            "ok": True,
            "answer": answer,
            "citations": _normalize_citations(body),
            "contexts": _normalize_contexts(body),
            "strategy": body.get("strategy") or strategy,
            "latencyMs": body.get("latency_ms"),
            "tokenUsage": body.get("token_usage"),
            "raw": body,
        }

    def get_strategies(self) -> dict[str, Any]:
        url = f"{SETTINGS.rag_base_url}/api/strategies"
        data, error = safe_get_json(url, SETTINGS.request_timeout_seconds)
        if error:
            return {"ok": False, "error": error, "items": []}
        items = (data or {}).get("strategies") or []
        return {"ok": True, "items": items}

    def get_knowledge_bases(self) -> dict[str, Any]:
        url = f"{SETTINGS.rag_base_url}/api/docs/list"
        data, error = safe_get_json(url, SETTINGS.request_timeout_seconds)
        if error:
            return {"ok": False, "error": error, "items": []}
        items = (data or {}).get("knowledge_bases") or []
        return {"ok": True, "items": items}


RAG_CLIENT = RagClient()
