from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote

import requests

from backend.config import SETTINGS
from backend.services.llm_registry import LlmEndpoint


@dataclass(slots=True)
class LlmCallResult:
    ok: bool
    answer: str = ""
    model_id: str = ""
    provider: str = ""
    model: str = ""
    path: str = ""
    latency_ms: int = 0
    usage: dict[str, Any] | None = None
    finish_reason: str | None = None
    error: str = ""


def _join_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"


def _compact_error(response: requests.Response) -> str:
    body = response.text.strip()
    if len(body) > 500:
        body = f"{body[:500]}..."
    return f"HTTP {response.status_code}: {body or response.reason}"


def _headers(api_key: str) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _path_candidates(path: str, fallback: str) -> list[str]:
    paths = [path or fallback, fallback]
    if fallback.startswith("/v1/"):
        paths.append(fallback.removeprefix("/v1"))
    return list(dict.fromkeys(item for item in paths if item))


def _normalize_messages(messages: list[dict[str, Any]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for item in messages[-30:]:
        if not isinstance(item, dict):
            continue
        content = str(item.get("content") or "").strip()
        if not content:
            continue
        role = str(item.get("role") or "user").strip() or "user"
        if role not in {"system", "user", "assistant"}:
            role = "user"
        normalized.append({"role": role, "content": content})
    return normalized


def _gemini_contents(messages: list[dict[str, str]]) -> tuple[str, list[dict[str, Any]]]:
    system_parts: list[str] = []
    contents: list[dict[str, Any]] = []
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "system":
            system_parts.append(content)
            continue
        contents.append(
            {
                "role": "model" if role == "assistant" else "user",
                "parts": [{"text": content}],
            }
        )
    return "\n\n".join(system_parts).strip(), contents


class LlmGateway:
    def generate(
        self,
        endpoint: LlmEndpoint,
        messages: list[dict[str, Any]],
        *,
        temperature: float = 0.2,
        max_tokens: int | None = None,
        timeout: float | None = None,
    ) -> LlmCallResult:
        if endpoint.provider == "gemini":
            return self._generate_gemini(
                endpoint,
                messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
            )
        return self._generate_openai_compatible(
            endpoint,
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )

    def _generate_openai_compatible(
        self,
        endpoint: LlmEndpoint,
        messages: list[dict[str, Any]],
        *,
        temperature: float,
        max_tokens: int | None,
        timeout: float | None,
    ) -> LlmCallResult:
        if not endpoint.base_url:
            return LlmCallResult(
                ok=False,
                model_id=endpoint.id,
                provider=endpoint.provider,
                model=endpoint.model,
                error="模型缺少 Base URL。",
            )

        request_body: dict[str, Any] = {
            "model": endpoint.model,
            "messages": _normalize_messages(messages),
            "temperature": temperature,
            "stream": False,
        }
        if max_tokens is not None:
            request_body["max_tokens"] = int(max_tokens)

        errors: list[str] = []
        started = time.perf_counter()
        for path in _path_candidates(endpoint.chat_path, "/v1/chat/completions"):
            try:
                response = requests.post(
                    _join_url(endpoint.base_url, path),
                    headers=_headers(endpoint.api_key),
                    json=request_body,
                    timeout=timeout or endpoint.timeout_seconds or SETTINGS.request_timeout_seconds,
                )
            except Exception as error:  # noqa: BLE001
                errors.append(f"{path} -> {error}")
                continue

            if not response.ok:
                errors.append(f"{path} -> {_compact_error(response)}")
                if response.status_code not in {404, 405}:
                    break
                continue

            data = response.json()
            choice = (data.get("choices") or [{}])[0]
            message = choice.get("message") or {}
            answer = str(message.get("content") or choice.get("text") or "").strip()
            if not answer:
                errors.append(f"{path} -> 模型返回为空")
                continue
            return LlmCallResult(
                ok=True,
                answer=answer,
                model_id=endpoint.id,
                provider=endpoint.provider,
                model=endpoint.model,
                path=path,
                latency_ms=round((time.perf_counter() - started) * 1000),
                usage=data.get("usage"),
                finish_reason=choice.get("finish_reason"),
            )

        return LlmCallResult(
            ok=False,
            model_id=endpoint.id,
            provider=endpoint.provider,
            model=endpoint.model,
            latency_ms=round((time.perf_counter() - started) * 1000),
            error="；".join(errors) or "模型请求失败。",
        )

    def _generate_gemini(
        self,
        endpoint: LlmEndpoint,
        messages: list[dict[str, Any]],
        *,
        temperature: float,
        max_tokens: int | None,
        timeout: float | None,
    ) -> LlmCallResult:
        normalized_messages = _normalize_messages(messages)
        system_instruction, contents = _gemini_contents(normalized_messages)
        if not contents:
            return LlmCallResult(
                ok=False,
                model_id=endpoint.id,
                provider=endpoint.provider,
                model=endpoint.model,
                error="Gemini 请求里没有可发送的消息内容。",
            )

        request_body: dict[str, Any] = {
            "contents": contents,
            "generationConfig": {"temperature": temperature},
        }
        if system_instruction:
            request_body["systemInstruction"] = {"parts": [{"text": system_instruction}]}
        if max_tokens is not None:
            request_body["generationConfig"]["maxOutputTokens"] = int(max_tokens)

        errors: list[str] = []
        started = time.perf_counter()
        encoded_model = quote(endpoint.model.removeprefix("models/"), safe="")
        for index, api_key in enumerate(endpoint.api_keys, start=1):
            url = f"{endpoint.base_url.rstrip('/')}/v1beta/models/{encoded_model}:generateContent?key={quote(api_key)}"
            try:
                response = requests.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    json=request_body,
                    timeout=timeout or endpoint.timeout_seconds or SETTINGS.request_timeout_seconds,
                )
            except Exception as error:  # noqa: BLE001
                errors.append(f"key#{index} -> {error}")
                continue

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
            if not answer:
                errors.append(f"key#{index} -> 模型返回为空")
                continue
            usage = data.get("usageMetadata") or {}
            return LlmCallResult(
                ok=True,
                answer=answer,
                model_id=endpoint.id,
                provider=endpoint.provider,
                model=endpoint.model,
                path="/v1beta/models/{model}:generateContent",
                latency_ms=round((time.perf_counter() - started) * 1000),
                usage={
                    "prompt_tokens": usage.get("promptTokenCount"),
                    "completion_tokens": usage.get("candidatesTokenCount"),
                    "total_tokens": usage.get("totalTokenCount"),
                },
                finish_reason=candidate.get("finishReason") if isinstance(candidate, dict) else None,
            )

        return LlmCallResult(
            ok=False,
            model_id=endpoint.id,
            provider=endpoint.provider,
            model=endpoint.model,
            latency_ms=round((time.perf_counter() - started) * 1000),
            error="；".join(errors) or "Gemini 请求失败。",
        )


LLM_GATEWAY = LlmGateway()
