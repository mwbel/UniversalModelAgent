from __future__ import annotations

import base64
import time
import uuid
from collections import OrderedDict
from typing import Any
from urllib.parse import quote

import requests

from backend.config import SETTINGS


def _compact_error(response: requests.Response) -> str:
    body = response.text.strip()
    if len(body) > 600:
        body = f"{body[:600]}..."
    return f"HTTP {response.status_code}: {body or response.reason}"


def _join_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"


def _path_candidates(path: str, fallback: str) -> list[str]:
    paths = [path or fallback, fallback]
    if fallback.startswith("/v1/"):
        paths.append(fallback.removeprefix("/v1"))
    return list(dict.fromkeys(item for item in paths if item))


def _extract_model_id(item: Any) -> str | None:
    if isinstance(item, str):
        return item.strip() or None
    if not isinstance(item, dict):
        return None
    for key in ("id", "name", "model"):
        value = str(item.get(key) or "").strip()
        if value:
            return value
    return None


def _parse_models(payload: Any) -> list[str]:
    if isinstance(payload, list):
        source_items = payload
    elif isinstance(payload, dict):
        source_items = payload.get("data") or payload.get("models") or payload.get("items") or []
    else:
        source_items = []
    models = [_extract_model_id(item) for item in source_items]
    return list(dict.fromkeys(item for item in models if item))


def _parse_gemini_models(payload: Any) -> list[str]:
    if not isinstance(payload, dict):
        return []
    models = payload.get("models") or []
    items: list[str] = []
    for item in models:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "").strip()
        generation_methods = item.get("supportedGenerationMethods") or []
        if not name.startswith("models/gemini"):
            continue
        if "generateContent" not in generation_methods:
            continue
        model_id = name.removeprefix("models/").strip()
        if model_id:
            items.append(model_id)
    return list(dict.fromkeys(items))


def _resolve_api_key(payload: dict[str, Any]) -> str:
    return str(payload.get("apiKey") or SETTINGS.model_tester_api_key or "").strip()


def _resolve_base_url(payload: dict[str, Any]) -> str:
    return str(payload.get("baseUrl") or SETTINGS.model_tester_base_url or "").strip().rstrip("/")


def _normalize_provider_preset(value: str) -> str:
    normalized = value.strip().lower()
    aliases = {
        "openai": "openai-compatible",
        "openai-compatible": "openai-compatible",
        "gemini": "gemini",
        "google-gemini": "gemini",
        "yunwu": "yunwu-gpt55",
        "yunwu-openai": "yunwu-gpt55",
        "yunwu-gpt55": "yunwu-gpt55",
    }
    return aliases.get(normalized, normalized or "openai-compatible")


def _extract_endpoint_config(base_url: str, models_path: str, chat_path: str) -> tuple[str, str, str]:
    normalized_base = base_url.rstrip("/")
    normalized_models_path = models_path or SETTINGS.model_tester_models_path
    normalized_chat_path = chat_path or SETTINGS.model_tester_chat_path

    if normalized_base.endswith("/chat/completions"):
        normalized_base = normalized_base[: -len("/chat/completions")]
        normalized_chat_path = "/chat/completions"
    elif normalized_base.endswith("/models"):
        normalized_base = normalized_base[: -len("/models")]
        normalized_models_path = "/models"

    return normalized_base, normalized_models_path, normalized_chat_path


def _headers(api_key: str) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _parse_data_url(data_url: str) -> tuple[str, str] | None:
    if not data_url.startswith("data:") or "," not in data_url:
        return None
    header, data = data_url.split(",", 1)
    mime_type = header[5:].split(";", 1)[0].strip() or "application/octet-stream"
    if ";base64" not in header:
        data = base64.b64encode(data.encode("utf-8")).decode("ascii")
    return mime_type, data


def _trim_attachment_store() -> None:
    while len(ATTACHMENT_STORE) > 200:
        ATTACHMENT_STORE.popitem(last=False)


def _has_message_content(content: Any) -> bool:
    if isinstance(content, str):
        return bool(content.strip())
    if not isinstance(content, list):
        return False
    return any(
        isinstance(item, dict)
        and (
            item.get("text")
            or item.get("image_url")
            or str(item.get("type") or "").strip() == "model_tester_attachment"
        )
        for item in content
    )


def _normalize_message_content(content: Any) -> str | list[dict[str, Any]]:
    if isinstance(content, list):
        normalized: list[dict[str, Any]] = []
        for item in content:
            if not isinstance(item, dict):
                continue
            item_type = str(item.get("type") or "").strip()
            if item_type == "text":
                text = str(item.get("text") or "").strip()
                if text:
                    normalized.append({"type": "text", "text": text})
            elif item_type == "image_url":
                image_url = item.get("image_url")
                if isinstance(image_url, dict) and image_url.get("url"):
                    normalized.append({"type": "image_url", "image_url": {"url": str(image_url["url"])}})
            elif item_type == "model_tester_attachment":
                attachment_id = str(item.get("attachment_id") or "").strip()
                attachment = ATTACHMENT_STORE.get(attachment_id)
                if not attachment:
                    continue
                if attachment.get("kind") == "image" and attachment.get("data_url"):
                    normalized.append({"type": "image_url", "image_url": {"url": str(attachment["data_url"])}})
                elif attachment.get("kind") == "text" and attachment.get("text"):
                    normalized.append(
                        {
                            "type": "text",
                            "text": f"[附件: {attachment.get('name') or 'text'}]\n{attachment.get('text')}",
                        }
                    )
                else:
                    normalized.append(
                        {
                            "type": "text",
                            "text": (
                                f"[附件: {attachment.get('name') or 'file'}]\n"
                                f"文件类型: {attachment.get('mime_type') or attachment.get('kind') or 'unknown'}"
                            ),
                        }
                    )
        return normalized
    return str(content or "")


def _normalize_messages(messages: list[Any]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for item in messages[-30:]:
        if not isinstance(item, dict):
            continue
        content = item.get("content")
        if not _has_message_content(content):
            continue
        normalized.append(
            {
                "role": str(item.get("role") or "user"),
                "content": _normalize_message_content(content),
            }
        )
    return normalized


def _text_from_content(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if not isinstance(content, list):
        return ""
    return "\n\n".join(
        str(item.get("text") or "").strip()
        for item in content
        if isinstance(item, dict) and str(item.get("type") or "").strip() == "text" and str(item.get("text") or "").strip()
    )


def _gemini_parts_from_content(content: Any) -> list[dict[str, Any]]:
    if isinstance(content, str):
        return [{"text": content.strip()}] if content.strip() else []
    if not isinstance(content, list):
        return []

    parts: list[dict[str, Any]] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        item_type = str(item.get("type") or "").strip()
        if item_type == "text":
            text = str(item.get("text") or "").strip()
            if text:
                parts.append({"text": text})
        elif item_type == "image_url":
            image_url = item.get("image_url")
            url = str(image_url.get("url") or "").strip() if isinstance(image_url, dict) else ""
            parsed = _parse_data_url(url)
            if parsed:
                mime_type, data = parsed
                parts.append({"inline_data": {"mime_type": mime_type, "data": data}})
            elif url:
                parts.append({"text": f"[image] {url}"})
    return parts


def _gemini_contents(messages: list[dict[str, Any]]) -> tuple[str, list[dict[str, Any]]]:
    system_lines: list[str] = []
    contents: list[dict[str, Any]] = []
    for message in messages:
        role = str(message.get("role") or "user")
        content = message.get("content")
        if role == "system":
            text = _text_from_content(content)
            if text:
                system_lines.append(text)
            continue
        parts = _gemini_parts_from_content(content)
        if not parts:
            continue
        contents.append({"role": "model" if role == "assistant" else "user", "parts": parts})
    return "\n\n".join(system_lines).strip(), contents


def _provider_default_models(provider: str) -> list[str]:
    if provider == "gemini":
        return SETTINGS.gemini_models
    if provider == "yunwu-gpt55":
        return [SETTINGS.yunwu_gpt55_model] if SETTINGS.yunwu_gpt55_model else []
    return SETTINGS.model_tester_models


def _provider_config(provider: str) -> dict[str, Any]:
    if provider == "gemini":
        return {
            "id": "gemini",
            "label": "Gemini",
            "description": "使用后端环境变量中的 Gemini key 池轮值调用。",
            "baseUrl": SETTINGS.gemini_base_url,
            "modelsPath": "/v1beta/models",
            "chatPath": "/v1beta/models/{model}:generateContent",
            "defaultModels": SETTINGS.gemini_models,
            "configured": bool(SETTINGS.gemini_api_keys),
            "usesEnvKey": True,
            "keyStatusLabel": (
                f"使用后端 Gemini key 池（{len(SETTINGS.gemini_api_keys)} 个）"
                if SETTINGS.gemini_api_keys
                else "未配置 Gemini key 池"
            ),
        }
    if provider == "yunwu-gpt55":
        return {
            "id": "yunwu-gpt55",
            "label": "云雾 GPT-5.5",
            "description": "调用云雾侧的 GPT-5.5 环境变量配置。",
            "baseUrl": SETTINGS.yunwu_api_base_url,
            "modelsPath": "/v1/models",
            "chatPath": SETTINGS.yunwu_chat_path,
            "defaultModels": [SETTINGS.yunwu_gpt55_model] if SETTINGS.yunwu_gpt55_model else [],
            "configured": bool(SETTINGS.yunwu_api_base_url and SETTINGS.yunwu_api_key),
            "usesEnvKey": True,
            "keyStatusLabel": "使用后端云雾 API key" if SETTINGS.yunwu_api_key else "未配置云雾 API key",
        }
    return {
        "id": "openai-compatible",
        "label": "OpenAI-compatible",
        "description": "兼容 OpenAI 的模型服务，可手动填写 Base URL 和临时 API key。",
        "baseUrl": SETTINGS.model_tester_base_url,
        "modelsPath": SETTINGS.model_tester_models_path,
        "chatPath": SETTINGS.model_tester_chat_path,
        "defaultModels": SETTINGS.model_tester_models,
        "configured": bool(SETTINGS.model_tester_base_url),
        "usesEnvKey": False,
        "keyStatusLabel": "使用后端环境变量 key" if SETTINGS.model_tester_api_key else "未配置默认 API key",
    }


def _resolve_openai_provider_config(payload: dict[str, Any], provider: str) -> tuple[str, str, str, str]:
    if provider == "yunwu-gpt55":
        return (
            str(payload.get("baseUrl") or SETTINGS.yunwu_api_base_url).rstrip("/"),
            str(payload.get("apiKey") or SETTINGS.yunwu_api_key or "").strip(),
            str(payload.get("model") or SETTINGS.yunwu_gpt55_model or "").strip(),
            str(payload.get("chatPath") or SETTINGS.yunwu_chat_path or "/v1/chat/completions"),
        )
    return (
        _resolve_base_url(payload),
        _resolve_api_key(payload),
        str(payload.get("model") or "").strip(),
        str(payload.get("chatPath") or SETTINGS.model_tester_chat_path),
    )


GEMINI_KEY_CURSOR = 0


def _gemini_key_attempt_order() -> list[str]:
    global GEMINI_KEY_CURSOR

    keys = SETTINGS.gemini_api_keys
    if not keys:
        return []
    start = GEMINI_KEY_CURSOR % len(keys)
    GEMINI_KEY_CURSOR = (start + 1) % len(keys)
    return [keys[(start + offset) % len(keys)] for offset in range(len(keys))]


class ModelTesterService:
    def config(self) -> dict[str, Any]:
        return {
            "ok": True,
            "baseUrl": SETTINGS.model_tester_base_url,
            "hasApiKey": bool(SETTINGS.model_tester_api_key),
            "modelsPath": SETTINGS.model_tester_models_path,
            "chatPath": SETTINGS.model_tester_chat_path,
            "defaultModels": SETTINGS.model_tester_models,
            "defaultPreset": "openai-compatible",
            "presets": [
                _provider_config("openai-compatible"),
                _provider_config("gemini"),
                _provider_config("yunwu-gpt55"),
            ],
        }

    def upload_attachment(self, payload: dict[str, Any]) -> dict[str, Any]:
        attachment_id = uuid.uuid4().hex
        name = str(payload.get("name") or "attachment").strip() or "attachment"
        kind = str(payload.get("kind") or "metadata").strip() or "metadata"
        item = {
            "id": attachment_id,
            "name": name,
            "kind": kind,
            "mime_type": str(payload.get("mimeType") or "").strip(),
            "size": int(payload.get("size") or 0),
            "created_at": time.time(),
        }
        if kind == "image":
            item["data_url"] = str(payload.get("dataUrl") or "")
        elif kind == "text":
            item["text"] = str(payload.get("text") or "")

        ATTACHMENT_STORE[attachment_id] = item
        _trim_attachment_store()
        return {
            "ok": True,
            "id": attachment_id,
            "name": item["name"],
            "kind": item["kind"],
            "mimeType": item["mime_type"],
            "size": item["size"],
        }

    def list_models(self, payload: dict[str, Any]) -> dict[str, Any]:
        provider = _normalize_provider_preset(str(payload.get("providerPreset") or "openai-compatible"))
        if provider == "gemini":
            if not SETTINGS.gemini_api_keys:
                return {"ok": False, "items": SETTINGS.gemini_models, "source": "gemini-env", "error": "未配置 GEMINI_API_KEYS。"}

            errors: list[str] = []
            fallback_items = SETTINGS.gemini_models
            for index, api_key in enumerate(_gemini_key_attempt_order(), start=1):
                url = f"{SETTINGS.gemini_base_url}/v1beta/models?key={quote(api_key)}"
                try:
                    response = requests.get(url, timeout=SETTINGS.request_timeout_seconds)
                    if not response.ok:
                        errors.append(f"key#{index} -> {_compact_error(response)}")
                        if response.status_code not in {401, 403, 429, 500, 502, 503, 504}:
                            break
                        continue
                    models = _parse_gemini_models(response.json())
                    if models:
                        return {"ok": True, "items": models, "source": "gemini-api"}
                    errors.append(f"key#{index} -> 响应里没有可识别的 Gemini 文本/多模态模型")
                except Exception as error:
                    errors.append(f"key#{index} -> {error}")
            return {"ok": False, "items": fallback_items, "source": "gemini-env", "error": "；".join(errors) or "Gemini 模型列表请求失败。"}
        if provider == "yunwu-gpt55":
            models = [SETTINGS.yunwu_gpt55_model] if SETTINGS.yunwu_gpt55_model else []
            if not (SETTINGS.yunwu_api_base_url and SETTINGS.yunwu_api_key and models):
                return {"ok": False, "items": models, "source": "yunwu-env", "error": "未配置云雾 GPT-5.5 环境变量。"}
            return {"ok": True, "items": models, "source": "yunwu-env"}

        base_url = _resolve_base_url(payload)
        api_key = _resolve_api_key(payload)
        models_path = str(payload.get("modelsPath") or SETTINGS.model_tester_models_path)
        base_url, models_path, _ = _extract_endpoint_config(
            base_url,
            models_path,
            str(payload.get("chatPath") or SETTINGS.model_tester_chat_path),
        )

        if not base_url:
            return {
                "ok": True,
                "items": SETTINGS.model_tester_models,
                "source": "default",
                "warning": "未配置模型服务地址，已使用本地默认模型列表。",
            }

        errors: list[str] = []
        for path in _path_candidates(models_path, "/v1/models"):
            try:
                response = requests.get(
                    _join_url(base_url, path),
                    headers=_headers(api_key),
                    timeout=SETTINGS.request_timeout_seconds,
                )
                if not response.ok:
                    errors.append(f"{path} -> {_compact_error(response)}")
                    continue
                models = _parse_models(response.json())
                if models:
                    return {"ok": True, "items": models, "source": path}
                errors.append(f"{path} -> 响应里没有可识别的模型名称")
            except Exception as error:
                errors.append(f"{path} -> {error}")

        return {
            "ok": False,
            "items": SETTINGS.model_tester_models,
            "source": "default",
            "error": "；".join(errors) or "模型列表请求失败",
        }

    def chat(self, payload: dict[str, Any]) -> dict[str, Any]:
        provider = _normalize_provider_preset(str(payload.get("providerPreset") or "openai-compatible"))
        model = str(payload.get("model") or "").strip()
        messages = payload.get("messages") if isinstance(payload.get("messages"), list) else []
        if not model:
            return {"ok": False, "error": "请先选择一个模型。"}
        if not messages:
            return {"ok": False, "error": "请先输入一条消息。"}

        if provider == "gemini":
            return self._chat_with_gemini(payload, model, messages)

        base_url, api_key, model, chat_path = _resolve_openai_provider_config(payload, provider)
        base_url, _, chat_path = _extract_endpoint_config(
            base_url,
            str(payload.get("modelsPath") or SETTINGS.model_tester_models_path),
            chat_path,
        )

        if not base_url:
            return {"ok": False, "error": "请先填写模型服务 Base URL，或设置后端环境变量。"}

        request_body: dict[str, Any] = {
            "model": model,
            "messages": _normalize_messages(messages),
            "temperature": float(payload.get("temperature", 0.7)),
            "stream": False,
        }
        max_tokens = payload.get("maxTokens")
        if max_tokens not in (None, ""):
            request_body["max_tokens"] = int(max_tokens)

        errors: list[str] = []
        started_at = time.perf_counter()
        for path in _path_candidates(chat_path, "/v1/chat/completions"):
            try:
                response = requests.post(
                    _join_url(base_url, path),
                    headers=_headers(api_key),
                    json=request_body,
                    timeout=SETTINGS.ocr_correction_timeout_seconds,
                )
                if not response.ok:
                    errors.append(f"{path} -> {_compact_error(response)}")
                    if response.status_code not in {404, 405}:
                        break
                    continue

                data = response.json()
                choice = (data.get("choices") or [{}])[0]
                message = choice.get("message") or {}
                content = str(message.get("content") or choice.get("text") or "").strip()
                reasoning = str(message.get("reasoning_content") or "").strip()
                return {
                    "ok": True,
                    "answer": content,
                    "reasoning": reasoning,
                    "model": model,
                    "path": path,
                    "latencyMs": round((time.perf_counter() - started_at) * 1000),
                    "usage": data.get("usage"),
                    "finishReason": choice.get("finish_reason"),
                    "raw": data,
                }
            except Exception as error:
                errors.append(f"{path} -> {error}")

        return {"ok": False, "error": "；".join(errors) or "模型请求失败"}

    def _chat_with_gemini(self, payload: dict[str, Any], model: str, messages: list[Any]) -> dict[str, Any]:
        if not SETTINGS.gemini_api_keys:
            return {"ok": False, "error": "未配置 GEMINI_API_KEYS。"}

        normalized_messages = _normalize_messages(messages)
        system_instruction, gemini_contents = _gemini_contents(normalized_messages)
        if not gemini_contents:
            return {"ok": False, "error": "Gemini 请求里没有可发送的消息内容。"}

        request_body: dict[str, Any] = {
            "contents": gemini_contents,
            "generationConfig": {
                "temperature": float(payload.get("temperature", 0.7)),
            },
        }
        if system_instruction:
            request_body["systemInstruction"] = {"parts": [{"text": system_instruction}]}
        max_tokens = payload.get("maxTokens")
        if max_tokens not in (None, ""):
            request_body["generationConfig"]["maxOutputTokens"] = int(max_tokens)

        started_at = time.perf_counter()
        errors: list[str] = []
        encoded_model = quote(model.removeprefix("models/"), safe="")
        for index, api_key in enumerate(_gemini_key_attempt_order(), start=1):
            url = f"{SETTINGS.gemini_base_url}/v1beta/models/{encoded_model}:generateContent?key={quote(api_key)}"
            try:
                response = requests.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    json=request_body,
                    timeout=SETTINGS.ocr_correction_timeout_seconds,
                )
                if not response.ok:
                    errors.append(f"key#{index} -> {_compact_error(response)}")
                    if response.status_code not in {401, 403, 429, 500, 502, 503, 504}:
                        break
                    continue

                data = response.json()
                candidates = data.get("candidates") or []
                candidate = candidates[0] if candidates else {}
                parts = candidate.get("content", {}).get("parts", []) if isinstance(candidate, dict) else []
                answer = "\n".join(
                    str(part.get("text") or "").strip()
                    for part in parts
                    if isinstance(part, dict) and str(part.get("text") or "").strip()
                ).strip()
                usage = data.get("usageMetadata") or {}
                usage_payload = {
                    "prompt_tokens": usage.get("promptTokenCount"),
                    "completion_tokens": usage.get("candidatesTokenCount"),
                    "total_tokens": usage.get("totalTokenCount"),
                }
                return {
                    "ok": True,
                    "answer": answer,
                    "reasoning": "",
                    "model": model,
                    "path": "/v1beta/models/{model}:generateContent",
                    "latencyMs": round((time.perf_counter() - started_at) * 1000),
                    "usage": usage_payload,
                    "finishReason": candidate.get("finishReason"),
                    "raw": data,
                }
            except Exception as error:
                errors.append(f"key#{index} -> {error}")

        return {"ok": False, "error": "；".join(errors) or "Gemini 请求失败"}

ATTACHMENT_STORE: "OrderedDict[str, dict[str, Any]]" = OrderedDict()
MODEL_TESTER_SERVICE = ModelTesterService()
