from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


MARKDOWN_SUFFIXES = {".md", ".markdown"}
LAYOUT_NAME_HINTS = ("layout", "middle", "content", "blocks", "model")
BLOCK_TEXT_KEYS = ("text", "content", "markdown", "md", "html", "latex")
BLOCK_TYPE_KEYS = ("type", "block_type", "category", "label", "kind")
BBOX_KEYS = ("bbox", "box", "poly", "polygon", "position")
PAGE_KEYS = ("page", "page_no", "page_num", "page_number", "pageIndex", "page_id", "page_idx")
CHILD_KEYS = ("blocks", "children", "items", "spans", "lines", "sub_blocks", "layout", "pages")


def load_mineru_markdown(mineru_output: str | Path) -> dict[str, Any]:
    """Return the most likely MinerU Markdown file content and its path."""

    root = Path(mineru_output)
    if root.is_file() and root.suffix.lower() in MARKDOWN_SUFFIXES:
        return {"path": str(root), "text": root.read_text(encoding="utf-8")}

    candidates = sorted(
        (p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in MARKDOWN_SUFFIXES),
        key=lambda p: (0 if "auto" in p.parts else 1, -p.stat().st_size, len(p.parts)),
    )
    if not candidates:
        return {"path": None, "text": ""}

    path = candidates[0]
    return {"path": str(path), "text": path.read_text(encoding="utf-8")}


def load_mineru_layout_json(mineru_output: str | Path) -> list[dict[str, Any]]:
    """Load MinerU JSON/layout files using a schema-tolerant strategy."""

    root = Path(mineru_output)
    files: list[Path]
    if root.is_file() and root.suffix.lower() == ".json":
        files = [root]
    else:
        files = sorted(
            p
            for p in root.rglob("*")
            if p.is_file()
            and p.suffix.lower() == ".json"
            and any(hint in p.name.lower() for hint in LAYOUT_NAME_HINTS)
        )
        if not files:
            files = sorted(p for p in root.rglob("*.json") if p.is_file())

    payloads: list[dict[str, Any]] = []
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        payloads.append({"path": str(path), "data": data})
    return payloads


def normalize_blocks(
    markdown: str | dict[str, Any],
    layout_json: list[dict[str, Any]] | dict[str, Any] | None = None,
    source_file: str | None = None,
) -> list[dict[str, Any]]:
    """Normalize heterogeneous MinerU output into ordered block dictionaries."""

    markdown_text = markdown.get("text", "") if isinstance(markdown, dict) else str(markdown or "")
    markdown_path = markdown.get("path") if isinstance(markdown, dict) else None
    raw_blocks = _extract_layout_blocks(layout_json)

    if raw_blocks:
        blocks = [_normalize_layout_block(item, index, source_file, markdown_path) for index, item in enumerate(raw_blocks)]
        return _fill_missing_text_from_markdown(blocks, markdown_text)

    return _blocks_from_markdown(markdown_text, source_file, markdown_path)


def _extract_layout_blocks(layout_json: list[dict[str, Any]] | dict[str, Any] | None) -> list[dict[str, Any]]:
    if not layout_json:
        return []

    payloads = layout_json if isinstance(layout_json, list) else [{"path": None, "data": layout_json}]
    found: list[dict[str, Any]] = []
    for payload in payloads:
        data = payload.get("data", payload)
        path = payload.get("path")
        _walk_for_blocks(data, found, path, inherited_page=None)
    return found


def _walk_for_blocks(node: Any, found: list[dict[str, Any]], path: str | None, inherited_page: int | None) -> None:
    if isinstance(node, dict):
        page = _coerce_page(_first_value(node, PAGE_KEYS), inherited_page)
        has_text = any(isinstance(node.get(key), str) and node.get(key).strip() for key in BLOCK_TEXT_KEYS)
        has_bbox = any(key in node for key in BBOX_KEYS)
        has_type = any(key in node for key in BLOCK_TYPE_KEYS)
        if (has_text or has_bbox) and has_type:
            item = dict(node)
            item["_layout_path"] = path
            if page is not None:
                item["_page"] = page
            found.append(item)
            return
        for key in CHILD_KEYS:
            child = node.get(key)
            if child is not None:
                _walk_for_blocks(child, found, path, page)
    elif isinstance(node, list):
        for child in node:
            _walk_for_blocks(child, found, path, inherited_page)


def _normalize_layout_block(
    item: dict[str, Any],
    index: int,
    source_file: str | None,
    markdown_path: str | None,
) -> dict[str, Any]:
    block_type = str(_first_value(item, BLOCK_TYPE_KEYS) or "text").lower()
    text = str(_first_value(item, BLOCK_TEXT_KEYS) or "").strip()
    bbox = _normalize_bbox(_first_value(item, BBOX_KEYS))
    page = _coerce_layout_page(item)
    return {
        "source_file": source_file,
        "mineru_markdown": markdown_path,
        "page": page,
        "chapter": None,
        "section": None,
        "block_id": str(item.get("id") or item.get("block_id") or f"block-{index:06d}"),
        "block_type": block_type,
        "bbox": bbox,
        "text": text,
        "raw": item,
        "ocr_engine": "mineru",
        "confidence": "medium" if text else "low",
        "risk_reasons": [],
        "order": index,
    }


def _fill_missing_text_from_markdown(blocks: list[dict[str, Any]], markdown_text: str) -> list[dict[str, Any]]:
    fallback_blocks = _split_markdown_blocks(markdown_text)
    fallback_index = 0
    current_chapter: str | None = None
    current_section: str | None = None
    for block in blocks:
        if not block.get("text") and fallback_index < len(fallback_blocks):
            block["text"] = fallback_blocks[fallback_index]
            fallback_index += 1
        chapter, section = _heading_context(str(block.get("text") or ""), current_chapter, current_section)
        current_chapter, current_section = chapter, section
        block["chapter"] = chapter
        block["section"] = section
    return blocks


def _blocks_from_markdown(markdown_text: str, source_file: str | None, markdown_path: str | None) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    chapter: str | None = None
    section: str | None = None
    for index, text in enumerate(_split_markdown_blocks(markdown_text)):
        block_type = _guess_block_type(text)
        chapter, section = _heading_context(text, chapter, section)
        blocks.append(
            {
                "source_file": source_file,
                "mineru_markdown": markdown_path,
                "page": _guess_page_from_text(text),
                "chapter": chapter,
                "section": section,
                "block_id": f"block-{index:06d}",
                "block_type": block_type,
                "bbox": None,
                "text": text.strip(),
                "raw": {},
                "ocr_engine": "mineru",
                "confidence": "medium",
                "risk_reasons": [],
                "order": index,
            }
        )
    return blocks


def _split_markdown_blocks(markdown_text: str) -> list[str]:
    return [match.group(0).strip() for match in re.finditer(r"\S(?:.*?)(?=\n{2,}\S|\Z)", markdown_text, flags=re.DOTALL)]


def _guess_block_type(text: str) -> str:
    stripped = text.strip()
    lowered = stripped.lower()
    if stripped.startswith("#"):
        return "heading"
    if "$$" in stripped or "\\[" in stripped or "\\begin{" in stripped:
        return "equation"
    if re.search(r"<\s*/?\s*table\b", stripped, flags=re.IGNORECASE):
        return "table"
    if sum(1 for line in stripped.splitlines() if "|" in line) >= 2:
        return "table"
    if any(word in lowered for word in ("theorem", "proof", "lemma", "example", "定理", "证明", "例")):
        return "math_text"
    return "text"


def _heading_context(text: str, chapter: str | None, section: str | None) -> tuple[str | None, str | None]:
    first = text.strip().splitlines()[0] if text.strip() else ""
    match = re.match(r"^(#{1,6})\s+(.+)$", first)
    if not match:
        return chapter, section
    level = len(match.group(1))
    title = match.group(2).strip()
    if level <= 1 or re.search(r"(chapter|第.+章)", title, flags=re.IGNORECASE):
        return title, None
    return chapter, title


def _guess_page_from_text(text: str) -> int | None:
    match = re.search(r"(?:page|页码|第)\s*[:：]?\s*(\d{1,5})", text, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def _first_value(item: dict[str, Any], keys: tuple[str, ...]) -> Any:
    for key in keys:
        if key in item and item[key] is not None:
            return item[key]
    return None


def _coerce_page(value: Any, fallback: int | None) -> int | None:
    if value is None:
        return fallback
    if isinstance(value, int):
        return value if value >= 1 else value + 1
    try:
        number = int(str(value))
    except ValueError:
        return fallback
    return number if number >= 1 else number + 1


def _coerce_layout_page(item: dict[str, Any]) -> int | None:
    if "page_idx" in item and item["page_idx"] is not None:
        try:
            return int(item["page_idx"]) + 1
        except (TypeError, ValueError):
            pass
    return _coerce_page(_first_value(item, ("_page", *PAGE_KEYS)), None)


def _normalize_bbox(value: Any) -> list[float] | None:
    if value is None:
        return None
    if isinstance(value, dict):
        if all(key in value for key in ("x0", "y0", "x1", "y1")):
            return [float(value["x0"]), float(value["y0"]), float(value["x1"]), float(value["y1"])]
        if all(key in value for key in ("x", "y", "w", "h")):
            x, y, w, h = float(value["x"]), float(value["y"]), float(value["w"]), float(value["h"])
            return [x, y, x + w, y + h]
    if isinstance(value, list):
        flat: list[float] = []
        for item in value:
            if isinstance(item, list):
                flat.extend(float(v) for v in item[:2])
            else:
                try:
                    flat.append(float(item))
                except (TypeError, ValueError):
                    pass
        if len(flat) == 4:
            x0, y0, x1, y1 = flat
            if x1 < x0 or y1 < y0:
                return [x0, y0, x0 + x1, y0 + y1]
            return [x0, y0, x1, y1]
        if len(flat) >= 8:
            xs = flat[0::2]
            ys = flat[1::2]
            return [min(xs), min(ys), max(xs), max(ys)]
    return None
