from __future__ import annotations

import re
from copy import deepcopy
from typing import Any

from math_rag_pipeline.latex_validator import fix_basic_latex_wrappers, validate_latex_syntax


def replace_block_with_mathpix_result(block: dict[str, Any], mathpix_result: dict[str, Any]) -> dict[str, Any]:
    """Return a block copy with Mathpix text substituted when available."""

    updated = deepcopy(block)
    if not mathpix_result.get("ok"):
        updated["ocr_engine"] = "mineru"
        updated["confidence"] = "low"
        updated["mathpix_error"] = mathpix_result.get("error", "unknown_error")
        return updated

    new_text = str(mathpix_result.get("text") or "").strip()
    if not new_text:
        updated["ocr_engine"] = "mineru"
        updated["confidence"] = "low"
        updated["mathpix_error"] = "empty_mathpix_text"
        return updated
    if _is_unusable_mathpix_text(new_text, str(block.get("block_type") or "text")):
        updated["ocr_engine"] = "mineru"
        updated["confidence"] = "low"
        updated["mathpix_error"] = "unusable_mathpix_text"
        return updated

    new_text = fix_basic_latex_wrappers(new_text, str(block.get("block_type") or "text"))
    validation = validate_latex_syntax(new_text)
    updated["text"] = new_text
    updated["ocr_engine"] = "mathpix"
    updated["confidence"] = "high" if validation["ok"] else "medium"
    updated["mathpix_raw"] = mathpix_result.get("raw")
    updated["latex_validation"] = validation
    return preserve_context_and_metadata(block, updated)


def preserve_context_and_metadata(original: dict[str, Any], updated: dict[str, Any]) -> dict[str, Any]:
    """Preserve block identity and context metadata after replacement."""

    for key in ("source_file", "page", "chapter", "section", "block_id", "block_type", "bbox", "order"):
        updated[key] = original.get(key)
    updated.setdefault("risk_reasons", original.get("risk_reasons", []))
    return updated


def _is_unusable_mathpix_text(text: str, block_type: str) -> bool:
    compact = text.strip()
    if not compact:
        return True
    lowered = compact.lower()
    if block_type.lower() in {"table", "tabular"}:
        stripped_tags = re.sub(r"<[^>]+>", "", compact).strip()
        if "table" in lowered or "table_tabular" in lowered:
            return not any(char.isalnum() for char in stripped_tags)
    return False
