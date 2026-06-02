from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from backend.services.question_understanding import QUESTION_UNDERSTANDING
from backend.visualization_catalog import VISUALIZATION_CAPABILITIES, VisualizationCapability


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
        if not concepts:
            return []

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
        return [match.public_dict() for match in matches[:max_items]]

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


VISUALIZATION_PLANNER = VisualizationPlanner()
