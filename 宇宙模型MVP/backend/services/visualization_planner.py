from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from backend.services.question_understanding import QUESTION_UNDERSTANDING
from backend.visualization_catalog import VISUALIZATION_CAPABILITIES, VisualizationCapability

VISUALIZATION_INTENT_MARKERS = (
    "可视化",
    "展示",
    "画",
    "图",
    "演示",
    "模拟",
    "visualize",
    "show me",
    "diagram",
    "demo",
)


@dataclass(slots=True)
class VisualizationMatch:
    capability: VisualizationCapability
    score: float
    reasons: list[str]
    concepts: list[dict[str, object]]

    def public_dict(self) -> dict[str, Any]:
        payload = self.capability.public_dict()
        payload["matchScore"] = round(self.score, 3)
        payload["matchReasons"] = self.reasons
        payload["matchedConcepts"] = self.concepts
        payload["renderMode"] = "a2ui-compatible-inline"
        payload["generatorType"] = self.capability.implementation_kind
        payload["a2uiInstruction"] = self.capability.a2ui_instruction()
        payload["embedUrl"] = (
            f"./interactive-visualizations/index.html?page={payload['pageId']}&embed=1"
        )
        payload["galleryUrl"] = f"./interactive-visualizations/index.html?page={payload['pageId']}"
        return payload


class VisualizationPlanner:
    def __init__(self) -> None:
        self.capabilities = VISUALIZATION_CAPABILITIES

    def plan(self, question: str, answer: str = "", max_items: int = 2) -> list[dict[str, Any]]:
        concepts = QUESTION_UNDERSTANDING.analyze(question=question, answer=answer)

        matches: list[VisualizationMatch] = []
        for capability in self.capabilities:
            score, reasons, matched_concepts = self._score_capability(concepts, capability)
            if score >= 1.0 and matched_concepts:
                matches.append(
                    VisualizationMatch(
                        capability=capability,
                        score=score,
                        reasons=reasons,
                        concepts=matched_concepts,
                    )
                )

        matches.sort(key=lambda item: (item.score, item.capability.priority), reverse=True)
        if matches:
            return [match.public_dict() for match in matches[:max_items]]

        if self._wants_visualization(question):
            return [self._generic_visualization(question)]

        return []

    def _score_capability(
        self,
        concepts: list,
        capability: VisualizationCapability,
    ) -> tuple[float, list[str], list[dict[str, object]]]:
        score = 0.0
        reasons: list[str] = []
        matched_concepts: list[dict[str, object]] = []

        for concept in concepts:
            if concept.concept_id not in capability.concepts:
                continue
            score += concept.confidence * 1.6
            reasons.append(f"concept:{concept.concept_id}")
            matched_concepts.append(concept.public_dict())

        if matched_concepts:
            score += capability.priority / 100.0

        return score, reasons, matched_concepts

    def _wants_visualization(self, question: str) -> bool:
        lowered = question.lower()
        return any(marker in lowered for marker in VISUALIZATION_INTENT_MARKERS)

    def _generic_visualization(self, question: str) -> dict[str, Any]:
        title = "通用概念探索面板"
        description = f"当前问题还没有专用组件，先用参数化 A2UI 面板承接：{question[:80]}"
        return {
            "id": "generic-concept-explorer",
            "title": title,
            "description": description,
            "concepts": [],
            "keywords": [],
            "tags": ["generic", "a2ui", "fallback"],
            "expresses": ["概念关键参数", "关系强度", "显示证据开关"],
            "educational_use": "作为新概念进入专用组件库之前的临时交互承接层。",
            "cannot_express": ["高保真领域模拟", "专用几何结构", "精确计算结果"],
            "pageId": "generic-concept-explorer",
            "sourceEntry": "frontend-react/src/a2ui-engine/GenericVisualization.tsx",
            "implementationKind": "schema_driven_generic_component",
            "triggerPatterns": list(VISUALIZATION_INTENT_MARKERS),
            "pluginId": "astronomy-core",
            "componentId": "astronomy-core.generic-concept-explorer",
            "intentType": "generic_concept_exploration",
            "propsSchema": {
                "focus": {"type": "string"},
                "relationStrength": {"type": "number", "minimum": 0, "maximum": 100},
                "showEvidence": {"type": "boolean"},
            },
            "defaultProps": {
                "focus": question[:120],
                "relationStrength": 50,
                "showEvidence": True,
            },
            "interactionEvents": ["relationStrengthChanged", "evidenceToggled"],
            "feedbackContract": {
                "eventPayload": "component returns selected relation strength and evidence visibility",
                "agentUse": "use the generic state to decide whether this concept needs a dedicated component",
            },
            "matchScore": 0.5,
            "matchReasons": ["visualization_intent:fallback"],
            "matchedConcepts": [],
            "renderMode": "a2ui-compatible-inline",
            "generatorType": "schema_driven_generic_component",
            "a2uiInstruction": {
                "protocol": "a2ui-compatible",
                "surface": "chat.inline.learning-visualization",
                "pluginId": "astronomy-core",
                "componentId": "astronomy-core.generic-concept-explorer",
                "intentType": "generic_concept_exploration",
                "initialProps": {
                    "focus": question[:120],
                    "relationStrength": 50,
                    "showEvidence": True,
                },
                "propsSchema": {
                    "focus": {"type": "string"},
                    "relationStrength": {"type": "number", "minimum": 0, "maximum": 100},
                    "showEvidence": {"type": "boolean"},
                },
                "events": ["relationStrengthChanged", "evidenceToggled"],
                "feedbackContract": {
                    "eventPayload": "component returns selected relation strength and evidence visibility",
                    "agentUse": "use the generic state to decide whether this concept needs a dedicated component",
                },
                "fallback": {
                    "renderMode": "generic",
                    "pageId": "generic-concept-explorer",
                },
            },
            "embedUrl": "",
            "galleryUrl": "",
        }


VISUALIZATION_PLANNER = VisualizationPlanner()
