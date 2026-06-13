from __future__ import annotations

import time
import uuid
from collections import OrderedDict
from typing import Any

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


def _resolve_api_key(payload: dict[str, Any]) -> str:
    return str(payload.get("apiKey") or SETTINGS.model_tester_api_key or "").strip()


def _resolve_base_url(payload: dict[str, Any]) -> str:
    return str(payload.get("baseUrl") or SETTINGS.model_tester_base_url or "").strip().rstrip("/")


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


class ModelTesterService:
    def config(self) -> dict[str, Any]:
        return {
            "ok": True,
            "baseUrl": SETTINGS.model_tester_base_url,
            "hasApiKey": bool(SETTINGS.model_tester_api_key),
            "modelsPath": SETTINGS.model_tester_models_path,
            "chatPath": SETTINGS.model_tester_chat_path,
            "defaultModels": SETTINGS.model_tester_models,
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
        base_url = _resolve_base_url(payload)
        api_key = _resolve_api_key(payload)
        model = str(payload.get("model") or "").strip()
        messages = payload.get("messages") if isinstance(payload.get("messages"), list) else []
        chat_path = str(payload.get("chatPath") or SETTINGS.model_tester_chat_path)
        base_url, _, chat_path = _extract_endpoint_config(
            base_url,
            str(payload.get("modelsPath") or SETTINGS.model_tester_models_path),
            chat_path,
        )

        if not base_url:
            return {"ok": False, "error": "请先填写模型服务 Base URL，或设置 MODEL_TESTER_BASE_URL。"}
        if not model:
            return {"ok": False, "error": "请先选择一个模型。"}
        if not messages:
            return {"ok": False, "error": "请先输入一条消息。"}

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

ATTACHMENT_STORE: "OrderedDict[str, dict[str, Any]]" = OrderedDict()
MODEL_TESTER_SERVICE = ModelTesterService()
