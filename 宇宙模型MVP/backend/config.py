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


def _parse_model_list(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("["):
        parsed = json.loads(value)
        return [str(item) for item in parsed if str(item).strip()]
    return [item.strip() for item in value.split(",") if item.strip()]


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UNIVMODEL_DIR = os.path.abspath(os.path.join(ROOT_DIR, ".."))
DEFAULT_MARKDOWN_LIBRARY_DIR = os.path.join(
    UNIVMODEL_DIR,
    "RAG",
    "宇宙模型资料202605-仅留md 和图片",
)


def _load_local_env() -> None:
    env_path = os.path.join(ROOT_DIR, ".env")
    if not os.path.exists(env_path):
        return

    with open(env_path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key:
                os.environ.setdefault(key, value)


_load_local_env()


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
    model_tester_base_url: str = os.getenv("MODEL_TESTER_BASE_URL", os.getenv("LLM_BASE_URL", "")).rstrip("/")
    model_tester_api_key: str = os.getenv("MODEL_TESTER_API_KEY", os.getenv("LLM_API_KEY", ""))
    model_tester_models_path: str = os.getenv("MODEL_TESTER_MODELS_PATH", "/v1/models")
    model_tester_chat_path: str = os.getenv("MODEL_TESTER_CHAT_PATH", "/v1/chat/completions")
    model_tester_models: list[str] = None  # type: ignore[assignment]
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
        if self.model_tester_models is None:
            self.model_tester_models = _parse_model_list(
                os.getenv(
                    "MODEL_TESTER_MODELS",
                    (
                        "qwen3.6-27b:latest,"
                        "batiai/qwen3.6-27b:q4,"
                        "medgemma:1.5-4b,"
                        "gemma4:e4b,"
                        "gemma2:27b,"
                        "qwen2.5:14b,"
                        "nomic-embed-text:latest,"
                        "llama3:latest"
                    ),
                )
            )

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
