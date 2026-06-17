from __future__ import annotations

import json
import re
from typing import Any

from math_rag_pipeline.latex_validator import fix_basic_latex_wrappers


def render_blocks_to_markdown(blocks: list[dict[str, Any]], attach_metadata: bool = True) -> str:
    rendered: list[str] = []
    for block in sorted(blocks, key=lambda item: item.get("order", 0)):
        text = str(block.get("text") or "").strip()
        if not text:
            continue
        text = normalize_equation_format(text, str(block.get("block_type") or "text"))
        text = normalize_table_format(text)
        if attach_metadata:
            rendered.append(attach_metadata_comments(block))
        rendered.append(text)
    return "\n\n".join(part for part in rendered if part.strip()) + "\n"


def normalize_equation_format(text: str, block_type: str = "text") -> str:
    normalized = fix_basic_latex_wrappers(text, block_type)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = re.sub(r"(?<!\$)\$\s*\n", "$", normalized)
    normalized = re.sub(r"\n\s*\$(?!\$)", "$", normalized)
    return normalized.strip()


def normalize_table_format(text: str) -> str:
    if re.search(r"<\s*/?\s*table\b", text, flags=re.IGNORECASE):
        return text.strip()
    lines = [line.rstrip() for line in text.strip().splitlines()]
    table_lines = [line for line in lines if "|" in line]
    if len(table_lines) < 2:
        return text.strip()

    first_index = lines.index(table_lines[0])
    if len(lines) > first_index + 1 and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[first_index + 1]):
        return "\n".join(lines).strip()

    column_count = max(line.count("|") for line in table_lines)
    if column_count <= 0:
        return text.strip()
    separator = "|" + "|".join([" --- "] * column_count) + "|"
    return "\n".join([lines[0], separator, *lines[1:]]).strip()


def attach_metadata_comments(block: dict[str, Any]) -> str:
    metadata = {
        "source_file": block.get("source_file"),
        "page": block.get("page"),
        "chapter": block.get("chapter"),
        "section": block.get("section"),
        "block_id": block.get("block_id"),
        "block_type": block.get("block_type"),
        "bbox": block.get("bbox"),
        "ocr_engine": block.get("ocr_engine", "mineru"),
        "confidence": block.get("confidence", "medium"),
    }
    return f"<!-- block_metadata: {json.dumps(metadata, ensure_ascii=False, sort_keys=True)} -->"
