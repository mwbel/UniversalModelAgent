from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

from backend.config import SETTINGS
from backend.services.llm_gateway import LLM_GATEWAY, LlmGateway
from backend.services.llm_registry import LLM_REGISTRY, LlmEndpoint, LlmRegistry


MATH_MARKERS = (
    "数学",
    "公式",
    "推导",
    "证明",
    "计算",
    "误差",
    "坐标",
    "星历",
    "开普勒",
    "轨道",
    "vsop",
    "de440",
    "ephemeris",
)


@dataclass(slots=True)
class RouteDecision:
    task: str
    selected: LlmEndpoint | None
    fallbacks: list[LlmEndpoint]
    reason: str
    required_capabilities: tuple[str, ...]
    scores: list[dict[str, Any]]

    def public_dict(self) -> dict[str, Any]:
        return {
            "task": self.task,
            "selectedModel": self.selected.id if self.selected else "",
            "selectedProvider": self.selected.provider if self.selected else "",
            "selectedModelName": self.selected.model if self.selected else "",
            "fallbacks": [endpoint.id for endpoint in self.fallbacks],
            "reason": self.reason,
            "requiredCapabilities": list(self.required_capabilities),
            "scores": self.scores[:5],
        }


class LlmRouter:
    def __init__(
        self,
        *,
        registry: LlmRegistry | None = None,
        gateway: LlmGateway | None = None,
    ) -> None:
        self.registry = registry or LLM_REGISTRY
        self.gateway = gateway or LLM_GATEWAY
        self._recent_failures: dict[str, list[float]] = {}

    def route(
        self,
        *,
        task: str,
        question: str = "",
        privacy: str = "normal",
    ) -> RouteDecision:
        if not SETTINGS.llm_router_enabled:
            return RouteDecision(
                task=task,
                selected=None,
                fallbacks=[],
                reason="LLM router is disabled.",
                required_capabilities=(),
                scores=[],
            )

        required = self._required_capabilities(task, question)
        candidates = self.registry.list_chat_models()
        scored: list[tuple[float, LlmEndpoint, dict[str, Any]]] = []
        for endpoint in candidates:
            score, detail = self._score(endpoint, task, question, required, privacy)
            scored.append((score, endpoint, detail))

        scored.sort(key=lambda item: item[0], reverse=True)
        public_scores = [detail for _, _, detail in scored]
        if not scored:
            return RouteDecision(
                task=task,
                selected=None,
                fallbacks=[],
                reason="没有可用的 chat 模型。",
                required_capabilities=required,
                scores=[],
            )

        selected = scored[0][1]
        reason = self._reason(selected, task, required, public_scores[0])
        return RouteDecision(
            task=task,
            selected=selected,
            fallbacks=[endpoint for _, endpoint, _ in scored[1:4]],
            reason=reason,
            required_capabilities=required,
            scores=public_scores,
        )

    def generate(
        self,
        *,
        task: str,
        question: str,
        messages: list[dict[str, Any]],
        privacy: str = "normal",
        temperature: float = 0.2,
        max_tokens: int | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        decision = self.route(task=task, question=question, privacy=privacy)
        if not decision.selected:
            return {
                "ok": False,
                "answer": "",
                "usage": None,
                "error": decision.reason,
                "route": decision.public_dict(),
            }

        attempts: list[dict[str, Any]] = []
        endpoints = [decision.selected, *decision.fallbacks]
        for index, endpoint in enumerate(endpoints):
            result = self.gateway.generate(
                endpoint,
                messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
            )
            attempt = {
                "model": endpoint.id,
                "provider": endpoint.provider,
                "status": "ok" if result.ok else "error",
                "latencyMs": result.latency_ms,
            }
            if result.error:
                attempt["error"] = result.error
            attempts.append(attempt)

            if result.ok and result.answer.strip():
                self._record_success(endpoint.id)
                route_payload = decision.public_dict()
                route_payload["actualModel"] = endpoint.id
                route_payload["fallbackUsed"] = index > 0
                route_payload["attempts"] = attempts
                return {
                    "ok": True,
                    "answer": result.answer,
                    "usage": result.usage,
                    "route": route_payload,
                    "finishReason": result.finish_reason,
                }
            self._record_failure(endpoint.id)

        route_payload = decision.public_dict()
        route_payload["actualModel"] = ""
        route_payload["fallbackUsed"] = False
        route_payload["attempts"] = attempts
        return {
            "ok": False,
            "answer": "",
            "usage": None,
            "error": "所有候选模型均调用失败。",
            "route": route_payload,
        }

    def _required_capabilities(self, task: str, question: str) -> tuple[str, ...]:
        required = {"chat", "chinese"}
        normalized_task = task.strip().lower()
        if normalized_task == "rag_synthesis":
            required.add("rag_synthesis")
        if normalized_task == "computed_explanation" or self._looks_math_heavy(question):
            required.add("math")
        if normalized_task == "long_context_summary":
            required.add("long_context")
        return tuple(sorted(required))

    def _score(
        self,
        endpoint: LlmEndpoint,
        task: str,
        question: str,
        required: tuple[str, ...],
        privacy: str,
    ) -> tuple[float, dict[str, Any]]:
        capabilities = set(endpoint.capabilities)
        matched = sum(1 for capability in required if capability in capabilities)
        capability_score = 40 * (matched / max(len(required), 1))

        specialty_score = 0
        if task in capabilities:
            specialty_score += 15
        if task == "computed_explanation" and "reasoning" in capabilities:
            specialty_score += 10
        if task == "visual_explanation":
            specialty_score += endpoint.latency_score * 3
        if self._looks_math_heavy(question) and "math" in capabilities:
            specialty_score += 8
        specialty_score = min(25, specialty_score)

        health_score = 15 - self._failure_penalty(endpoint.id)
        privacy_score = self._privacy_score(endpoint, privacy)
        cost_score = endpoint.cost_score
        latency_score = endpoint.latency_score
        priority_score = max(0, min(endpoint.priority, 100)) / 10
        total = (
            capability_score
            + specialty_score
            + health_score
            + privacy_score
            + cost_score
            + latency_score
            + priority_score
        )
        detail = {
            "model": endpoint.id,
            "score": round(total, 2),
            "capabilityScore": round(capability_score, 2),
            "specialtyScore": round(specialty_score, 2),
            "healthScore": round(health_score, 2),
            "privacyScore": privacy_score,
            "costScore": cost_score,
            "latencyScore": latency_score,
            "priorityScore": round(priority_score, 2),
            "capabilities": list(endpoint.capabilities),
        }
        return total, detail

    def _privacy_score(self, endpoint: LlmEndpoint, privacy: str) -> int:
        normalized = privacy.strip().lower()
        if normalized in {"local", "private"}:
            return 10 if endpoint.privacy == "local" else -20
        if endpoint.privacy == "local":
            return 10
        return 4

    def _failure_penalty(self, model_id: str) -> int:
        now = time.time()
        recent = [item for item in self._recent_failures.get(model_id, []) if now - item < 300]
        self._recent_failures[model_id] = recent
        return min(15, len(recent) * 5)

    def _record_failure(self, model_id: str) -> None:
        self._recent_failures.setdefault(model_id, []).append(time.time())

    def _record_success(self, model_id: str) -> None:
        self._recent_failures.pop(model_id, None)

    def _looks_math_heavy(self, question: str) -> bool:
        lowered = question.lower()
        return any(marker in lowered or marker in question for marker in MATH_MARKERS)

    def _reason(
        self,
        endpoint: LlmEndpoint,
        task: str,
        required: tuple[str, ...],
        detail: dict[str, Any],
    ) -> str:
        matched = [capability for capability in required if capability in endpoint.capabilities]
        return (
            f"任务 `{task}` 需要 {', '.join(required)}；"
            f"选择 `{endpoint.id}`，匹配 {', '.join(matched) or '无'}，"
            f"综合分 {detail.get('score')}。"
        )


LLM_ROUTER = LlmRouter()
