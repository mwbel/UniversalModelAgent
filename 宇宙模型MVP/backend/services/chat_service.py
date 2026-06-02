from __future__ import annotations

import re
from typing import Any

from backend.services.rag_client import RAG_CLIENT
from backend.services.visualization_planner import VISUALIZATION_PLANNER


def _recommend_visualizations(question: str, answer: str = "") -> list[dict[str, Any]]:
    # Keep visualization routing anchored to the user's request. Retrieved context can mention
    # adjacent concepts and otherwise pull the UI toward the wrong component.
    return VISUALIZATION_PLANNER.plan(question=question)


def _orchestration_steps(
    *,
    question: str,
    rag_result: dict[str, Any],
    visualizations: list[dict[str, Any]],
    service: str,
) -> list[dict[str, Any]]:
    contexts = rag_result.get("contexts") or []
    visual_component_ids = [
        item.get("componentId")
        or ((item.get("a2uiInstruction") or {}).get("componentId"))
        for item in visualizations
    ]
    visual_component_ids = [str(item) for item in visual_component_ids if item]
    wants_visual = any(marker in question for marker in ("可视化", "展示", "画", "图", "演示", "模拟"))

    return [
        {
            "id": "intent",
            "label": "确定任务意图",
            "status": "completed",
            "detail": "可视化问答" if wants_visual or visualizations else "知识库问答",
        },
        {
            "id": "retrieval",
            "label": "检索本地知识库",
            "status": "completed" if contexts else "skipped",
            "detail": f"命中 {len(contexts)} 段上下文" if contexts else "未使用知识库上下文",
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
            "detail": "DeepSeek + RAG" if service == "knowledge" else "本地兜底回答",
        },
        {
            "id": "validation",
            "label": "校验并交给前端渲染",
            "status": "completed" if visualizations else "skipped",
            "detail": "A2UI 指令已生成" if visualizations else "纯文本回答",
        },
    ]


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
            "如果你想直观抓住核心，最适合先看第三定律，因为它最容易通过轨道大小和周期变化建立数量直觉。"
        )
    if "开普勒第三定律" in question:
        return (
            "开普勒第三定律说的是：行星公转周期的平方，与轨道长半轴的立方成正比。"
            "直观理解就是，离太阳越远的行星，轨道越大，运行得也越慢，所以周期会显著变长。"
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

    return (
        "当前知识库还没有切到合适的天文学专题，所以这次先用了本地兜底回答。"
        "你可以继续问天文学基础问题，我会尽量给出直接解释。"
    )


def _is_bad_rag_result(rag_result: dict[str, Any]) -> bool:
    answer = str(rag_result.get("answer") or "").strip()
    if not rag_result.get("ok"):
        return True
    if not answer:
        return True
    if answer in {"我不知道", "我不知道。", "I don't know", "I do not know"}:
        return True

    contexts = rag_result.get("contexts") or []
    if contexts:
        top_score = max(float(item.get("score") or 0.0) for item in contexts)
        joined = " ".join(str(item.get("content") or "") for item in contexts[:3]).lower()
        astronomy_markers = [
            "太阳",
            "月球",
            "月食",
            "日食",
            "行星",
            "轨道",
            "星系",
            "恒星",
            "eclipse",
            "planet",
            "orbit",
            "moon",
            "sun",
            "galaxy",
            "star",
        ]
        if top_score < 0.45 and not any(marker in joined for marker in astronomy_markers):
            return True

    return False


class ChatService:
    def ask(
        self,
        question: str,
        history: list[dict[str, Any]],
        variant: str | None = None,
        kb_id: str | None = None,
    ) -> dict[str, Any]:
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
                "raw": rag_result["raw"],
            }

        answer = _fallback_answer(question)
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
            "service": "assistant",
            "strategy": variant,
            "raw": rag_result.get("raw"),
        }


CHAT_SERVICE = ChatService()
