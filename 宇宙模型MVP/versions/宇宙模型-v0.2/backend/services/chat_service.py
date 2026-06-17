from __future__ import annotations

import re
from typing import Any

import requests

from backend.config import SETTINGS
from backend.services.ephemeris_compare import BODY_IDS, compare_ephemeris, normalize_tolerance_unit
from backend.services.rag_client import RAG_CLIENT
from backend.services.visualization_planner import VISUALIZATION_PLANNER, has_explicit_visualization_intent

PLANET_MOTION_KB_ID = "planet-motion"
PLANET_ALIASES = {
    "水星": "mercury",
    "mercury": "mercury",
    "金星": "venus",
    "venus": "venus",
    "地球": "earth",
    "earth": "earth",
    "火星": "mars",
    "mars": "mars",
    "木星": "jupiter",
    "jupiter": "jupiter",
    "土星": "saturn",
    "saturn": "saturn",
    "天王星": "uranus",
    "uranus": "uranus",
    "海王星": "neptune",
    "neptune": "neptune",
    "月球": "moon",
    "月亮": "moon",
    "moon": "moon",
}
PLANET_MOTION_RAG_MARKERS = [
    "vsop",
    "de440",
    "de模型",
    "de 模型",
    "星历",
    "切比雪夫",
    "chebyshev",
    "误差",
    "精度",
    "截断",
    "插值",
    "行星运动",
    "数值分析",
    "作业",
    "报告",
]
PLANET_COMPUTE_MARKERS = [
    "位置",
    "坐标",
    "速度",
    "距离",
    "查询",
    "计算",
    "差多少",
    "对照",
    "比较",
    "误差",
    "精度",
    "ephemeris",
]


def _recommend_visualizations(question: str, answer: str = "") -> list[dict[str, Any]]:
    # Keep visualization routing anchored to the user's request. Retrieved context can mention
    # adjacent concepts and otherwise pull the UI toward the wrong component.
    return VISUALIZATION_PLANNER.plan(question=question)


def _detect_planet_motion_domain(question: str) -> bool:
    lowered = question.lower()
    return any(marker in lowered or marker in question for marker in PLANET_MOTION_RAG_MARKERS) or any(
        alias.lower() in lowered or alias in question for alias in PLANET_ALIASES
    )


def _detect_compute_intent(question: str) -> bool:
    lowered = question.lower()
    if not any(marker in lowered or marker in question for marker in PLANET_COMPUTE_MARKERS):
        return False
    return any(alias.lower() in lowered or alias in question for alias in PLANET_ALIASES) or any(
        marker in lowered or marker in question for marker in ("vsop", "de440", "星历", "行星运动")
    )


def _extract_bodies(question: str) -> list[str]:
    lowered = question.lower()
    bodies: list[str] = []
    for alias, body in PLANET_ALIASES.items():
        if alias.lower() in lowered or alias in question:
            bodies.append(body)
    return list(dict.fromkeys(body for body in bodies if body in BODY_IDS))


def _extract_date(question: str) -> str | None:
    iso_match = re.search(r"(\d{4})[-/.](\d{1,2})(?:[-/.](\d{1,2}))?", question)
    if iso_match:
        year, month, day = iso_match.groups()
        return f"{int(year):04d}-{int(month):02d}-{int(day or '1'):02d}"

    cn_match = re.search(r"(\d{4})\s*年(?:\s*(\d{1,2})\s*月)?(?:\s*(\d{1,2})\s*[日号])?", question)
    if cn_match:
        year, month, day = cn_match.groups()
        return f"{int(year):04d}-{int(month or '1'):02d}-{int(day or '1'):02d}"

    year_match = re.search(r"\b(1[6-9]\d{2}|2[0-6]\d{2})\b", question)
    if year_match:
        return f"{int(year_match.group(1)):04d}-01-01"
    return None


def _extract_tolerance(question: str) -> tuple[str | None, str | None]:
    lowered = question.lower()
    tolerance_match = re.search(r"(\d+(?:\.\d+)?e[-+]?\d+|10\^[-+]?\d+|10\^\{[-+]?\d+\}|0\.\d+)", lowered)
    tolerance = None
    if tolerance_match:
        tolerance = tolerance_match.group(1).replace("^{", "^").replace("}", "")
    if "km" in lowered or "公里" in question or "千米" in question:
        return tolerance, "km"
    if "au" in lowered or "天文单位" in question:
        return tolerance, "AU"
    return tolerance, "AU" if tolerance else None


def _build_ephemeris_query(question: str) -> dict[str, str | None]:
    bodies = _extract_bodies(question)
    tolerance, tolerance_unit = _extract_tolerance(question)
    return {
        "date": _extract_date(question),
        "bodies": ",".join(bodies) if bodies else None,
        "tolerance": tolerance,
        "tolerance_unit": normalize_tolerance_unit(tolerance_unit),
    }


def _format_number(value: float | int | None, digits: int = 6) -> str:
    if value is None:
        return "-"
    number = float(value)
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    return f"{number:.{digits}f}"


def _summarize_ephemeris(ephemeris: dict[str, Any] | None) -> str:
    if not ephemeris or not ephemeris.get("ok") or not ephemeris.get("items"):
        return ""
    lines = [f"计算时刻：{ephemeris.get('date')}，参考系：日心赤道直角坐标。"]
    for item in (ephemeris.get("items") or [])[:4]:
        if item.get("error"):
            lines.append(f"{item.get('name')}: 计算失败，{item.get('error')}")
            continue
        de440 = item.get("de440") or {}
        vsop = item.get("vsop") or {}
        delta = item.get("delta") or {}
        recommendation = item.get("recommendation") or {}
        lines.append(
            (
                f"{item.get('name')}: DE440 距离 {de440.get('distanceAu')} AU，"
                f"VSOP 距离 {vsop.get('distanceAu')} AU，"
                f"位置差约 {_format_number(delta.get('distanceKm'), 3)} km，"
                f"模型建议 {recommendation.get('model') or 'DE440'}。"
            )
        )
    return "\n".join(lines)


def _fallback_answer(question: str) -> str:
    lowered = question.lower()

    if "月食" in question or "lunar eclipse" in lowered:
        return (
            "月食发生在太阳、地球、月球接近排成一条直线时，地球位于太阳和月球之间，"
            "地球的影子投到月球表面，于是我们看到月面变暗甚至变成红铜色。"
            "只有在满月前后、并且月球靠近黄白交点时，月食才比较可能发生。"
        )
    if "日食" in question or "solar eclipse" in lowered:
        return (
            "日食发生在太阳、月球、地球接近排成一条直线时，月球运行到太阳和地球之间，"
            "挡住了部分或全部太阳光。因为月球本影和半影范围有限，所以只有地球上一部分地区能看到日食。"
        )
    if "开普勒三大定律" in question or "开普勒三定律" in question or "kepler" in lowered:
        return (
            "开普勒三大定律可以这样理解：第一定律说行星绕太阳走的是椭圆轨道，太阳位于一个焦点；"
            "第二定律说行星在相等时间内扫过相等面积，所以近日点更快、远日点更慢；"
            "第三定律说公转周期的平方与轨道长半轴的立方成正比。"
        )
    if "逆行" in question or "retrograde" in lowered:
        return (
            "行星逆行主要是一种视运动现象，不是行星真的突然掉头。"
            "当地球在轨道上追过外行星，或者被内行星从内侧超越时，"
            "从地球视角看，它在恒星背景中的投影会暂时出现反向移动。"
        )
    if "月相" in question or "moon phase" in lowered:
        return (
            "月相变化来自太阳、地球、月球相对位置的改变。"
            "月球本身并不会发光，我们看到的是被太阳照亮的那一部分；随着月球绕地球公转，"
            "从地球看见的受光面比例不断变化，于是出现新月、上弦、满月、下弦等月相。"
        )

    return "这次没有命中需要调用本地知识库或数值模型的专题，我先给出简洁回答：可以继续补充你的问题条件，我会据此细化。"


def _generate_direct_answer(question: str, history: list[dict[str, Any]]) -> tuple[str, dict[str, Any] | None]:
    recent_history = [
        {
            "role": item.get("role", "user"),
            "content": str(item.get("content") or "")[:1200],
        }
        for item in history[-6:]
        if str(item.get("content") or "").strip()
    ]
    if SETTINGS.llm_base_url and SETTINGS.llm_api_key and SETTINGS.llm_model:
        try:
            response = requests.post(
                f"{SETTINGS.llm_base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {SETTINGS.llm_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": SETTINGS.llm_model,
                    "temperature": 0.2,
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "你是一个面向天文学与宇宙模型教学的中文助手。"
                                "默认直接回答用户问题，不要声称查询了知识库。"
                                "如果用户要求可视化，请只给简洁文字解释；"
                                "交互式图形会由 A2UI 组件单独渲染。"
                            ),
                        },
                        *recent_history,
                        {
                            "role": "user",
                            "content": f"{question}\n\n请给出简洁、直接的中文回答。",
                        },
                    ],
                },
                timeout=SETTINGS.request_timeout_seconds,
            )
            response.raise_for_status()
            payload = response.json()
            answer = ((((payload.get("choices") or [{}])[0]).get("message") or {}).get("content") or "").strip()
            if answer:
                return answer, payload.get("usage")
        except Exception:
            pass
    return _fallback_answer(question), None


def _build_computed_answer(
    question: str,
    ephemeris: dict[str, Any] | None,
    rag_contexts: list[dict[str, Any]],
) -> str:
    computed_summary = _summarize_ephemeris(ephemeris)
    if computed_summary:
        if rag_contexts:
            return f"{computed_summary}\n\n依据本地课程材料，DE440 使用切比雪夫插值读取 JPL 数值星历，VSOP 是解析级数近似，适合做模型对照和教学解释。"
        return computed_summary
    if rag_contexts:
        return (
            f"我检索了 `planet-motion` 知识库，最相关材料来自《{rag_contexts[0].get('source')}》。\n\n"
            f"{str(rag_contexts[0].get('content') or '')[:320]}"
        )
    return _fallback_answer(question)


def _is_bad_rag_result(rag_result: dict[str, Any]) -> bool:
    answer = str(rag_result.get("answer") or "").strip()
    if not rag_result.get("ok"):
        return True
    if not answer:
        return True
    if answer in {"我不知道", "我不知道。", "I don't know", "I do not know"}:
        return True
    return False


def _orchestration_steps(
    *,
    question: str,
    rag_result: dict[str, Any],
    visualizations: list[dict[str, Any]],
    service: str,
    computed_ephemeris: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    contexts = rag_result.get("contexts") or []
    visual_component_ids = [
        item.get("componentId") or ((item.get("a2uiInstruction") or {}).get("componentId"))
        for item in visualizations
    ]
    visual_component_ids = [str(item) for item in visual_component_ids if item]
    wants_visual = has_explicit_visualization_intent(question)

    steps = [
        {
            "id": "intent",
            "label": "确定任务意图",
            "status": "completed",
            "detail": "可视化问答" if wants_visual or visualizations else ("计算问答" if computed_ephemeris else ("知识库问答" if service == "knowledge" else "普通问答")),
        },
    ]
    if computed_ephemeris is not None:
        item_count = len(computed_ephemeris.get("items") or []) if isinstance(computed_ephemeris, dict) else 0
        steps.append(
            {
                "id": "calculation",
                "label": "Python 数值计算",
                "status": "completed" if item_count else "skipped",
                "detail": f"完成 {item_count} 个天体 VSOP/DE440 对照" if item_count else "未得到星历结果",
            }
        )
    steps.extend(
        [
            {
                "id": "retrieval",
                "label": "检索本地知识库",
                "status": "completed" if contexts else "skipped",
                "detail": f"命中 {len(contexts)} 段上下文" if contexts else "未使用 RAG",
            },
            {
                "id": "visualizer",
                "label": "匹配 A2UI 能力",
                "status": "completed" if visualizations else "skipped",
                "detail": "、".join(visual_component_ids) if visual_component_ids else "未命中可视化能力",
            },
            {
                "id": "generation",
                "label": "生成文字解释",
                "status": "completed",
                "detail": "Python + DeepSeek + RAG" if computed_ephemeris and contexts else ("DeepSeek + RAG" if service == "knowledge" else ("DeepSeek" if service == "llm" else "本地兜底回答")),
            },
            {
                "id": "validation",
                "label": "校验并交给前端渲染",
                "status": "completed" if visualizations else "skipped",
                "detail": "A2UI 指令已生成" if visualizations else "纯文本回答",
            },
        ]
    )
    return steps


class ChatService:
    def ask(
        self,
        question: str,
        history: list[dict[str, Any]],
        variant: str | None = None,
        kb_id: str | None = None,
        use_rag: bool = False,
    ) -> dict[str, Any]:
        is_planet_motion = _detect_planet_motion_domain(question)
        wants_compute = _detect_compute_intent(question)

        if not use_rag:
            computed_ephemeris = None
            if wants_compute:
                query = _build_ephemeris_query(question)
                computed_ephemeris = compare_ephemeris(
                    date=query["date"],
                    bodies=query["bodies"],
                    tolerance=query["tolerance"],
                    tolerance_unit=query["tolerance_unit"],
                )

            rag_result = {"ok": False, "answer": "", "citations": [], "contexts": [], "raw": None}
            auto_rag_used = False
            if computed_ephemeris:
                rag_result = RAG_CLIENT.ask_auto(
                    question=question,
                    history=history,
                    variant="hybrid",
                    preferred_kb_id=PLANET_MOTION_KB_ID if is_planet_motion else None,
                )
                auto_rag_used = bool(rag_result.get("contexts"))
            else:
                rag_result = RAG_CLIENT.ask_auto(
                    question=question,
                    history=history,
                    variant="hybrid",
                    preferred_kb_id=PLANET_MOTION_KB_ID if is_planet_motion else None,
                )
                auto_rag_used = not _is_bad_rag_result(rag_result)

            if computed_ephemeris:
                answer = _build_computed_answer(question, computed_ephemeris, rag_result.get("contexts") or [])
                usage = None
                service = "knowledge" if auto_rag_used else "assistant"
            elif auto_rag_used:
                answer = rag_result.get("answer") or _build_computed_answer(question, None, rag_result.get("contexts") or [])
                usage = rag_result.get("tokenUsage")
                service = "knowledge"
            else:
                answer, usage = _generate_direct_answer(question, history)
                service = "llm"

            visualizations = _recommend_visualizations(question, answer)
            return {
                "answer": answer,
                "citations": rag_result.get("citations") or [],
                "contexts": rag_result.get("contexts") or [],
                "recommendedVisualizations": visualizations,
                "orchestration": _orchestration_steps(
                    question=question,
                    rag_result=rag_result,
                    visualizations=visualizations,
                    service=service,
                    computed_ephemeris=computed_ephemeris,
                ),
                "service": service,
                "strategy": rag_result.get("strategy"),
                "tokenUsage": usage,
                "computedEphemeris": computed_ephemeris,
                "autoRagUsed": auto_rag_used,
                "raw": rag_result.get("raw"),
            }

        rag_result = RAG_CLIENT.ask(question=question, history=history, variant=variant, kb_id=kb_id)
        if not _is_bad_rag_result(rag_result):
            visualizations = _recommend_visualizations(question, rag_result["answer"])
            return {
                "answer": rag_result["answer"],
                "citations": rag_result["citations"],
                "contexts": rag_result["contexts"],
                "recommendedVisualizations": visualizations,
                "orchestration": _orchestration_steps(
                    question=question,
                    rag_result=rag_result,
                    visualizations=visualizations,
                    service="knowledge",
                ),
                "service": "knowledge",
                "strategy": rag_result.get("strategy") or variant,
                "resolvedStrategy": rag_result.get("resolvedStrategy"),
                "latencyMs": rag_result.get("latencyMs"),
                "tokenUsage": rag_result.get("tokenUsage"),
                "autoRagUsed": False,
                "raw": rag_result["raw"],
            }

        auto_rag_result = RAG_CLIENT.ask_auto(question=question, history=history, variant="hybrid")
        if not _is_bad_rag_result(auto_rag_result):
            visualizations = _recommend_visualizations(question, auto_rag_result["answer"])
            return {
                "answer": auto_rag_result["answer"],
                "citations": auto_rag_result["citations"],
                "contexts": auto_rag_result["contexts"],
                "recommendedVisualizations": visualizations,
                "orchestration": _orchestration_steps(
                    question=question,
                    rag_result=auto_rag_result,
                    visualizations=visualizations,
                    service="knowledge",
                ),
                "service": "knowledge",
                "strategy": auto_rag_result.get("strategy") or "hybrid",
                "resolvedStrategy": auto_rag_result.get("resolvedStrategy"),
                "latencyMs": auto_rag_result.get("latencyMs"),
                "tokenUsage": auto_rag_result.get("tokenUsage"),
                "autoRagUsed": True,
                "raw": auto_rag_result.get("raw"),
            }

        answer, usage = _generate_direct_answer(question, history)
        visualizations = _recommend_visualizations(question, answer)
        return {
            "answer": answer,
            "citations": [],
            "contexts": [],
            "recommendedVisualizations": visualizations,
            "orchestration": _orchestration_steps(
                question=question,
                rag_result=rag_result,
                visualizations=visualizations,
                service="assistant",
            ),
            "service": "llm",
            "strategy": variant,
            "autoRagUsed": False,
            "tokenUsage": usage,
            "raw": rag_result.get("raw"),
        }


CHAT_SERVICE = ChatService()
