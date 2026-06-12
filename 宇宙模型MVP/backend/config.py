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


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UNIVMODEL_DIR = os.path.abspath(os.path.join(ROOT_DIR, ".."))
DEFAULT_MARKDOWN_LIBRARY_DIR = os.path.join(
    UNIVMODEL_DIR,
    "RAG",
    "宇宙模型资料202605-仅留md 和图片",
)


@dataclass(slots=True)
class Settings:
    host: str = os.getenv("APP_HOST", "127.0.0.1")
    port: int = int(os.getenv("APP_PORT", "8787"))
    app_name: str = os.getenv("APP_NAME", "Universe Model Agent")
    mineru_base_url: str = os.getenv("MINERU_BASE_URL", "https://mineryou.cpolar.top").rstrip("/")
    mineru_convert_path: str = os.getenv("MINERU_CONVERT_PATH", "/api/convert")
    markdown_library_dir: str = os.getenv("MARKDOWN_LIBRARY_DIR", DEFAULT_MARKDOWN_LIBRARY_DIR)
    rag_base_url: str = os.getenv("RAG_BASE_URL", "local://builtin-rag").rstrip("/")
    rag_chat_path: str = os.getenv("RAG_CHAT_PATH", "/api/query")
    rag_variants: list[str] = None  # type: ignore[assignment]
    default_rag_strategy: str = os.getenv("DEFAULT_RAG_STRATEGY", "naive")
    default_kb_id: str = os.getenv("DEFAULT_KB_ID", "chapterOne")
    request_timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "25"))
    upload_timeout_seconds: float = float(os.getenv("UPLOAD_TIMEOUT_SECONDS", "180"))
    llm_base_url: str = os.getenv("LLM_BASE_URL", "").rstrip("/")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "")
    ocr_correction_provider: str = os.getenv("OCR_CORRECTION_PROVIDER", "openai-compatible")
    ocr_correction_base_url: str = os.getenv("OCR_CORRECTION_BASE_URL", os.getenv("LLM_BASE_URL", "")).rstrip("/")
    ocr_correction_api_key: str = os.getenv("OCR_CORRECTION_API_KEY", os.getenv("LLM_API_KEY", ""))
    ocr_correction_model: str = os.getenv("OCR_CORRECTION_MODEL", os.getenv("LLM_MODEL", ""))
    ocr_correction_path: str = os.getenv("OCR_CORRECTION_PATH", "/v1/chat/completions")
    ocr_correction_timeout_seconds: float = float(os.getenv("OCR_CORRECTION_TIMEOUT_SECONDS", "90"))
    ocr_correction_max_candidates: int = int(os.getenv("OCR_CORRECTION_MAX_CANDIDATES", "12"))
    ocr_correction_max_output_tokens: int = int(os.getenv("OCR_CORRECTION_MAX_OUTPUT_TOKENS", "2048"))

    def __post_init__(self) -> None:
        if self.rag_variants is None:
            self.rag_variants = _parse_rag_variants(os.getenv("RAG_VARIANTS", ""))

    def public_dict(self) -> dict[str, Any]:
        return {
            "appName": self.app_name,
            "mineruBaseUrl": self.mineru_base_url,
            "markdownLibraryDir": self.markdown_library_dir,
            "ragBaseUrl": self.rag_base_url,
            "ragVariants": self.rag_variants,
            "defaultRagStrategy": self.default_rag_strategy,
            "defaultKbId": self.default_kb_id,
            "uploadTimeoutSeconds": self.upload_timeout_seconds,
            "llmConfigured": bool(self.llm_base_url and self.llm_model),
            "ocrCorrectionConfigured": bool(self.ocr_correction_api_key and self.ocr_correction_model),
        }


SETTINGS = Settings()
