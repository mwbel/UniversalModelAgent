from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - PyYAML is declared, this keeps startup defensive.
    yaml = None

from backend.config import SETTINGS


def _normalize_provider(value: str) -> str:
    normalized = (value or "").strip().lower()
    aliases = {
        "local": "openai-compatible",
        "openai": "openai-compatible",
        "openai-compatible": "openai-compatible",
        "yunwu": "openai-compatible",
        "yunwu-openai": "openai-compatible",
        "yunwu-gpt55": "openai-compatible",
        "gemini": "gemini",
        "google-gemini": "gemini",
    }
    return aliases.get(normalized, normalized or "openai-compatible")


def _split_list(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (list, tuple)):
        return tuple(str(item).strip() for item in value if str(item).strip())
    text = str(value).strip()
    if not text:
        return ()
    return tuple(item.strip() for item in text.split(",") if item.strip())


def _env_value(name: str | None) -> str:
    return os.getenv(str(name or "").strip(), "").strip()


def _env_list(name: str | None) -> tuple[str, ...]:
    return _split_list(_env_value(name))


def _cost_score_value(cost: str) -> int:
    normalized = (cost or "").strip().lower()
    if normalized in {"free", "free_local", "local"}:
        return 5
    if normalized in {"low", "cheap"}:
        return 4
    if normalized in {"medium", "paid"}:
        return 2
    if normalized in {"high", "expensive"}:
        return 1
    return 3


def _latency_score_value(latency: str) -> int:
    normalized = (latency or "").strip().lower()
    if normalized in {"fast", "low"}:
        return 5
    if normalized in {"medium", "normal"}:
        return 3
    if normalized in {"slow", "high"}:
        return 1
    return 3


def infer_capabilities(model: str, provider: str, configured: tuple[str, ...] = ()) -> tuple[str, ...]:
    lowered = model.lower()
    capabilities: set[str] = {item.strip() for item in configured if item.strip()}

    if any(token in lowered for token in ("embed", "embedding", "nomic-embed")):
        capabilities.add("embedding")
        return tuple(sorted(capabilities))

    capabilities.add("chat")
    capabilities.add("chinese")

    if any(token in lowered for token in ("qwen", "deepseek", "gpt", "gemini", "claude", "yi", "glm")):
        capabilities.add("reasoning")
        capabilities.add("rag_synthesis")

    if any(token in lowered for token in ("math", "qwen", "deepseek", "gpt", "gemini", "reason")):
        capabilities.add("math")

    if any(token in lowered for token in ("long", "128k", "32k", "gpt-5", "gpt-4", "gemini", "pro")):
        capabilities.add("long_context")

    if provider == "gemini":
        capabilities.update({"reasoning", "rag_synthesis", "long_context"})

    return tuple(sorted(capabilities))


@dataclass(slots=True)
class LlmEndpoint:
    id: str
    provider: str
    model: str
    base_url: str = ""
    api_key: str = ""
    api_keys: tuple[str, ...] = ()
    chat_path: str = "/chat/completions"
    capabilities: tuple[str, ...] = ()
    privacy: str = "remote"
    cost: str = "unknown"
    latency: str = "medium"
    priority: int = 50
    enabled: bool = True
    source: str = "configured"
    timeout_seconds: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def configured(self) -> bool:
        if not self.enabled or not self.model:
            return False
        if self.provider == "gemini":
            return bool(self.api_keys)
        return bool(self.base_url)

    @property
    def cost_score(self) -> int:
        return _cost_score_value(self.cost)

    @property
    def latency_score(self) -> int:
        return _latency_score_value(self.latency)

    def has_capability(self, capability: str) -> bool:
        return capability in self.capabilities

    def public_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "provider": self.provider,
            "model": self.model,
            "chatPath": self.chat_path,
            "capabilities": list(self.capabilities),
            "privacy": self.privacy,
            "cost": self.cost,
            "latency": self.latency,
            "priority": self.priority,
            "enabled": self.enabled,
            "configured": self.configured,
            "source": self.source,
        }


def _endpoint_from_config(item: dict[str, Any], index: int) -> LlmEndpoint | None:
    provider = _normalize_provider(str(item.get("provider") or "openai-compatible"))
    model = str(item.get("model") or _env_value(item.get("model_env"))).strip()
    if not model:
        return None

    raw_id = str(item.get("id") or "").strip()
    endpoint_id = raw_id or f"{provider}:{model}"
    base_url = str(item.get("base_url") or _env_value(item.get("base_url_env"))).strip().rstrip("/")
    api_key = str(item.get("api_key") or _env_value(item.get("api_key_env"))).strip()
    api_keys = _split_list(item.get("api_keys")) or _env_list(item.get("api_keys_env"))
    if api_key and not api_keys:
        api_keys = (api_key,)
    chat_path = str(item.get("chat_path") or _env_value(item.get("chat_path_env")) or "/chat/completions").strip()
    configured_caps = _split_list(item.get("capabilities"))
    capabilities = infer_capabilities(model, provider, configured_caps)
    return LlmEndpoint(
        id=endpoint_id,
        provider=provider,
        model=model,
        base_url=base_url,
        api_key=api_key,
        api_keys=api_keys,
        chat_path=chat_path,
        capabilities=capabilities,
        privacy=str(item.get("privacy") or "remote"),
        cost=str(item.get("cost") or "unknown"),
        latency=str(item.get("latency") or "medium"),
        priority=int(item.get("priority") or 50),
        enabled=item.get("enabled", True) is not False,
        source=f"models.yaml:{index}",
        timeout_seconds=float(item["timeout_seconds"]) if item.get("timeout_seconds") else None,
        metadata={key: value for key, value in item.items() if key.startswith("meta_")},
    )


class LlmRegistry:
    def __init__(
        self,
        *,
        config_path: str | Path | None = None,
        endpoints: list[LlmEndpoint] | None = None,
    ) -> None:
        self.config_path = Path(config_path or SETTINGS.llm_models_config_path)
        self._injected_endpoints = endpoints

    def list_models(self) -> list[LlmEndpoint]:
        if self._injected_endpoints is not None:
            return list(self._injected_endpoints)

        configured = self._load_configured_models()
        fallback = self._fallback_models()
        merged: dict[str, LlmEndpoint] = {}
        seen_targets: set[tuple[str, str, str, str]] = set()
        for endpoint in [*configured, *fallback]:
            target = (endpoint.provider, endpoint.base_url, endpoint.model, endpoint.chat_path)
            if endpoint.id in merged or target in seen_targets:
                continue
            merged[endpoint.id] = endpoint
            seen_targets.add(target)
        return list(merged.values())

    def list_chat_models(self) -> list[LlmEndpoint]:
        return [
            endpoint
            for endpoint in self.list_models()
            if endpoint.configured and endpoint.has_capability("chat")
        ]

    def _load_configured_models(self) -> list[LlmEndpoint]:
        if not self.config_path.exists() or yaml is None:
            return []
        try:
            payload = yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {}
        except Exception:
            return []
        raw_models = payload.get("models") if isinstance(payload, dict) else None
        if not isinstance(raw_models, list):
            return []
        endpoints: list[LlmEndpoint] = []
        for index, item in enumerate(raw_models, start=1):
            if not isinstance(item, dict):
                continue
            endpoint = _endpoint_from_config(item, index)
            if endpoint:
                endpoints.append(endpoint)
        return endpoints

    def _fallback_models(self) -> list[LlmEndpoint]:
        endpoints: list[LlmEndpoint] = []

        if SETTINGS.llm_base_url and SETTINGS.llm_model:
            endpoints.append(
                LlmEndpoint(
                    id=f"default:{SETTINGS.llm_model}",
                    provider="openai-compatible",
                    model=SETTINGS.llm_model,
                    base_url=SETTINGS.llm_base_url,
                    api_key=SETTINGS.llm_api_key,
                    api_keys=(SETTINGS.llm_api_key,) if SETTINGS.llm_api_key else (),
                    chat_path=SETTINGS.llm_chat_path,
                    capabilities=infer_capabilities(SETTINGS.llm_model, "openai-compatible", ("rag_synthesis",)),
                    privacy="remote",
                    cost="unknown",
                    latency="medium",
                    priority=60,
                    source="LLM_* env",
                )
            )

        if SETTINGS.model_tester_base_url:
            for model in SETTINGS.model_tester_models:
                endpoints.append(
                    LlmEndpoint(
                        id=f"local:{model}",
                        provider="openai-compatible",
                        model=model,
                        base_url=SETTINGS.model_tester_base_url,
                        api_key=SETTINGS.model_tester_api_key,
                        api_keys=(SETTINGS.model_tester_api_key,) if SETTINGS.model_tester_api_key else (),
                        chat_path=SETTINGS.model_tester_chat_path,
                        capabilities=infer_capabilities(model, "openai-compatible", ("rag_synthesis",)),
                        privacy="local",
                        cost="free_local",
                        latency="medium",
                        priority=70,
                        source="MODEL_TESTER_* env",
                    )
                )

        if SETTINGS.yunwu_api_base_url and SETTINGS.yunwu_gpt55_model:
            endpoints.append(
                LlmEndpoint(
                    id=f"yunwu:{SETTINGS.yunwu_gpt55_model}",
                    provider="openai-compatible",
                    model=SETTINGS.yunwu_gpt55_model,
                    base_url=SETTINGS.yunwu_api_base_url,
                    api_key=SETTINGS.yunwu_api_key,
                    api_keys=(SETTINGS.yunwu_api_key,) if SETTINGS.yunwu_api_key else (),
                    chat_path=SETTINGS.yunwu_chat_path,
                    capabilities=infer_capabilities(
                        SETTINGS.yunwu_gpt55_model,
                        "openai-compatible",
                        ("rag_synthesis", "long_context", "math"),
                    ),
                    privacy="remote",
                    cost="paid",
                    latency="medium",
                    priority=90,
                    source="YUNWU_* env",
                )
            )

        if SETTINGS.gemini_api_keys:
            for model in SETTINGS.gemini_models:
                endpoints.append(
                    LlmEndpoint(
                        id=f"gemini:{model}",
                        provider="gemini",
                        model=model,
                        base_url=SETTINGS.gemini_base_url,
                        api_keys=tuple(SETTINGS.gemini_api_keys),
                        chat_path="/v1beta/models/{model}:generateContent",
                        capabilities=infer_capabilities(model, "gemini", ("rag_synthesis", "math")),
                        privacy="remote",
                        cost="paid",
                        latency="fast" if "flash" in model.lower() else "medium",
                        priority=75,
                        source="GEMINI_* env",
                    )
                )

        return endpoints


LLM_REGISTRY = LlmRegistry()
