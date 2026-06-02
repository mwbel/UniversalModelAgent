from __future__ import annotations

from typing import Any


DEFAULT_RAG_STRATEGIES: list[dict[str, Any]] = [
    {
        "id": "naive",
        "label": "Naive RAG",
        "summary": "单路向量检索后直接生成，适合快速问答与基线验证。",
        "workflow": "linear",
        "stage": "基础型",
        "aliases": ["naive", "naive_rag"],
    },
    {
        "id": "hybrid",
        "label": "Hybrid RAG",
        "summary": "结合关键词检索和向量检索，再统一排序后生成答案。",
        "workflow": "parallel",
        "stage": "基础型",
        "aliases": ["hybrid", "hybrid_rag"],
    },
    {
        "id": "parent_document",
        "label": "Parent-Document RAG",
        "summary": "先命中文档块，再回溯父文档补全上下文，适合较长材料。",
        "workflow": "two_stage",
        "stage": "基础型",
        "aliases": [
            "parent_document",
            "parent_document_rag",
            "parent-document",
            "parent-document-rag",
            "parent",
        ],
    },
]


def normalize_strategy_key(value: str | None) -> str:
    return (
        str(value or "")
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def _build_alias_map(strategies: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    alias_map: dict[str, dict[str, Any]] = {}
    for strategy in strategies:
        for alias in strategy.get("aliases", []):
            alias_map[normalize_strategy_key(alias)] = strategy
        alias_map[normalize_strategy_key(strategy.get("id"))] = strategy
    return alias_map


def _normalize_remote_strategy(item: Any) -> dict[str, Any] | None:
    if isinstance(item, str):
        remote_id = item.strip()
        if not remote_id:
            return None
        return {"id": remote_id, "label": remote_id, "summary": "", "workflow": ""}

    if not isinstance(item, dict):
        return None

    remote_id = str(item.get("id") or item.get("name") or item.get("strategy") or "").strip()
    if not remote_id:
        return None

    return {
        "id": remote_id,
        "label": str(item.get("label") or item.get("title") or remote_id),
        "summary": str(item.get("summary") or item.get("description") or ""),
        "workflow": str(item.get("workflow") or item.get("topology") or ""),
        "raw": item,
    }


def build_strategy_catalog(remote_items: list[Any]) -> list[dict[str, Any]]:
    alias_map = _build_alias_map(DEFAULT_RAG_STRATEGIES)
    merged: dict[str, dict[str, Any]] = {
        strategy["id"]: {
            "id": strategy["id"],
            "label": strategy["label"],
            "summary": strategy["summary"],
            "workflow": strategy["workflow"],
            "stage": strategy["stage"],
            "available": False,
            "remoteId": strategy["id"],
        }
        for strategy in DEFAULT_RAG_STRATEGIES
    }

    extras: list[dict[str, Any]] = []
    for item in remote_items:
        normalized = _normalize_remote_strategy(item)
        if not normalized:
            continue

        remote_id = normalized["id"]
        matched = alias_map.get(normalize_strategy_key(remote_id))
        if matched:
            merged_item = merged[matched["id"]]
            merged_item["available"] = True
            merged_item["remoteId"] = remote_id
            if normalized["summary"]:
                merged_item["summary"] = normalized["summary"]
            if normalized["workflow"]:
                merged_item["workflow"] = normalized["workflow"]
            continue

        extras.append(
            {
                "id": remote_id,
                "label": normalized["label"],
                "summary": normalized["summary"] or "远端 manyRAG 返回的策略。",
                "workflow": normalized["workflow"] or "custom",
                "stage": "扩展型",
                "available": True,
                "remoteId": remote_id,
            }
        )

    return list(merged.values()) + extras


def resolve_strategy_id(requested_variant: str | None, remote_items: list[Any]) -> str:
    requested_key = normalize_strategy_key(requested_variant)
    if not requested_key:
        return DEFAULT_RAG_STRATEGIES[0]["id"]

    alias_map = _build_alias_map(DEFAULT_RAG_STRATEGIES)
    matched = alias_map.get(requested_key)
    if not matched:
        return str(requested_variant)

    for item in remote_items:
        normalized = _normalize_remote_strategy(item)
        if not normalized:
            continue
        remote_id = normalized["id"]
        if normalize_strategy_key(remote_id) in {
            normalize_strategy_key(alias) for alias in matched.get("aliases", [])
        } | {matched["id"]}:
            return remote_id

    return matched["id"]
