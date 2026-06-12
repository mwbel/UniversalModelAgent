from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class ConceptMatch:
    concept_id: str
    label: str
    confidence: float
    evidence: list[str]

    def public_dict(self) -> dict[str, object]:
        return {
            "conceptId": self.concept_id,
            "label": self.label,
            "confidence": round(self.confidence, 3),
            "evidence": self.evidence,
        }


class QuestionUnderstandingService:
    def __init__(self) -> None:
        self.concept_rules: list[tuple[str, str, list[str]]] = [
            (
                "ecliptic_lunar_path",
                "黄道白道与交点几何",
                [
                    "黄道",
                    "白道",
                    "升交点",
                    "降交点",
                    "黄白交点",
                    "黄道和白道",
                    "白道和黄道",
                    "ecliptic",
                    "lunar orbit",
                    "lunar path",
                    "ascending node",
                    "descending node",
                ],
            ),
            (
                "eclipse_geometry",
                "食现象与月相几何",
                ["月食", "日食", "月相", "lunar eclipse", "solar eclipse", "moon phase"],
            ),
            (
                "retrograde_motion",
                "行星逆行与视运动",
                ["逆行", "视运动", "retrograde", "apparent motion"],
            ),
            (
                "geocentric_daily_motion",
                "地心天球周日视运动",
                [
                    "周日视运动",
                    "日周运动",
                    "地心模型",
                    "地心天球",
                    "天球",
                    "七政",
                    "七大行星",
                    "恒星背景",
                    "diurnal motion",
                    "geocentric",
                    "celestial sphere",
                    "daily apparent motion",
                ],
            ),
            (
                "kepler_third_law",
                "开普勒第三定律",
                [
                    "开普勒第三定律",
                    "开普勒三定律",
                    "开普勒三大定律",
                    "kepler",
                    "周期",
                    "半长轴",
                    "长半轴",
                    "t²",
                    "a³",
                    "t^2",
                    "a^3",
                ],
            ),
            (
                "ephemeris_compare",
                "星历模型对照",
                ["vsop", "de440", "星历", "行星位置", "精度对照", "ephemeris"],
            ),
            (
                "solar_system_structure",
                "太阳系轨道结构",
                ["太阳系", "轨道", "solar system", "orbit", "行星系统"],
            ),
        ]

    def analyze(self, question: str, answer: str = "") -> list[ConceptMatch]:
        text = f"{question}\n{answer}".strip().lower()
        if not text:
            return []

        matches: list[ConceptMatch] = []
        for concept_id, label, patterns in self.concept_rules:
            confidence = 0.0
            evidence: list[str] = []
            for pattern in patterns:
                if re.search(re.escape(pattern.lower()), text):
                    confidence += 1.0 if len(pattern) <= 4 else 1.4
                    evidence.append(pattern)

            if concept_id == "kepler_third_law":
                if ("第三定律" in text or "third law" in text) and ("开普勒" in text or "kepler" in text):
                    confidence += 2.2
                    evidence.append("开普勒+第三定律")
                if ("三大定律" in text or "三定律" in text) and ("开普勒" in text or "kepler" in text):
                    confidence += 2.0
                    evidence.append("开普勒+三大定律")
                if ("周期" in text or "period" in text) and ("半长轴" in text or "长半轴" in text or "semi-major" in text):
                    confidence += 1.8
                    evidence.append("周期-半长轴关系")

            if concept_id == "ephemeris_compare":
                if ("vsop" in text and "de440" in text) or ("模型" in text and "对照" in text):
                    confidence += 2.0
                    evidence.append("模型对照")

            if concept_id == "retrograde_motion":
                if ("为什么" in text or "how" in text or "why" in text) and evidence:
                    confidence += 0.3
                if "逆行" not in text and "retrograde" not in text:
                    confidence *= 0.35

            if concept_id == "geocentric_daily_motion":
                if ("地心" in text or "geocentric" in text) and evidence:
                    confidence += 1.8
                    evidence.append("地心参考系")
                if ("周日" in text or "日周" in text or "diurnal" in text or "daily apparent" in text) and evidence:
                    confidence += 2.2
                    evidence.append("周日视运动")
                if ("3d" in text or "三维" in text or "可视化" in text or "演示" in text) and evidence:
                    confidence += 0.8
                    evidence.append("3D可视化意图")

            if concept_id == "ecliptic_lunar_path":
                if ("可视化" in text or "展示" in text or "关系" in text) and evidence:
                    confidence += 1.2
                    evidence.append("黄白二道关系展示")
                if ("交点" in text or "node" in text) and evidence:
                    confidence += 0.8
                    evidence.append("交点说明")

            if confidence > 0:
                matches.append(
                    ConceptMatch(
                        concept_id=concept_id,
                        label=label,
                        confidence=confidence,
                        evidence=evidence,
                    )
                )

        matches.sort(key=lambda item: item.confidence, reverse=True)
        return matches


QUESTION_UNDERSTANDING = QuestionUnderstandingService()
