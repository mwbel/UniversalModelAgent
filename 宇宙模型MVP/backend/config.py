from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any


def _parse_rag_variants(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("["):
        parsed = json.loads(value)
        return [str(item) for item in parsed]
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(slots=True)
class Settings:
    host: str = os.getenv("APP_HOST", "127.0.0.1")
    port: int = int(os.getenv("APP_PORT", "8787"))
    app_name: str = os.getenv("APP_NAME", "Universe Model Agent")
    mineru_base_url: str = os.getenv("MINERU_BASE_URL", "https://mineryou.cpolar.top").rstrip("/")
    mineru_convert_path: str = os.getenv("MINERU_CONVERT_PATH", "/api/convert")
    rag_base_url: str = os.getenv("RAG_BASE_URL", "https://manyragsbackend.cpolar.top").rstrip("/")
    rag_chat_path: str = os.getenv("RAG_CHAT_PATH", "/api/query")
    rag_variants: list[str] = None  # type: ignore[assignment]
    default_rag_strategy: str = os.getenv("DEFAULT_RAG_STRATEGY", "naive")
    default_kb_id: str = os.getenv("DEFAULT_KB_ID", "chapterOne")
    request_timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "25"))
    llm_base_url: str = os.getenv("LLM_BASE_URL", "").rstrip("/")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "")

    def __post_init__(self) -> None:
        if self.rag_variants is None:
            self.rag_variants = _parse_rag_variants(os.getenv("RAG_VARIANTS", ""))

    def public_dict(self) -> dict[str, Any]:
        return {
            "appName": self.app_name,
            "mineruBaseUrl": self.mineru_base_url,
            "ragBaseUrl": self.rag_base_url,
            "ragVariants": self.rag_variants,
            "defaultRagStrategy": self.default_rag_strategy,
            "defaultKbId": self.default_kb_id,
            "llmConfigured": bool(self.llm_base_url and self.llm_model),
        }


SETTINGS = Settings()
