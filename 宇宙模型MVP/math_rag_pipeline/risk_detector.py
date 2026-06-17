from __future__ import annotations

import re
from typing import Any


HIGH_RISK_TYPES = {
    "table",
    "equation",
    "formula",
    "inline_formula",
    "interline_equation",
    "matrix",
    "align",
    "cases",
    "array",
    "tabular",
}

MATH_SYMBOL_RE = re.compile(r"[∑∫∂≤≥αβγδλμπΩ∞≈≠×÷]|\\(?:sum|int|partial|leq|geq|alpha|beta|lambda)\b")
LATEX_WRAPPED_RE = re.compile(r"(\$[^$]+\$|\\\([^)]*\\\)|\\\[[\s\S]*?\\\]|\\begin\{[^}]+})")


def is_high_risk_block(block: dict[str, Any]) -> tuple[bool, list[str]]:
    """Return whether a normalized block should be re-OCRed by Mathpix."""

    text = str(block.get("text") or "")
    block_type = str(block.get("block_type") or "").lower()
    reasons: list[str] = []

    if block_type in HIGH_RISK_TYPES:
        reasons.append(f"block_type:{block_type}")
    if detect_lost_subscripts(text):
        reasons.append("possible_lost_subscript")
    if detect_math_text_without_latex(text):
        reasons.append("math_symbols_without_latex")
    if detect_matrix_like_text(text):
        reasons.append("matrix_like_text")
    if _has_complex_latex_environment(text):
        reasons.append("complex_latex_environment")
    if _has_table_with_math(text):
        reasons.append("table_with_math")
    if text.count("$") % 2 == 1:
        reasons.append("unbalanced_inline_math")

    return bool(reasons), reasons


def detect_lost_subscripts(text: str) -> bool:
    """Detect A11/A12/xij/lambda1 style strings likely missing subscript markup."""

    compact = re.sub(r"\s+", "", text)
    patterns = [
        r"\b[A-Z]\d{2,}\b",
        r"\b[a-z]\d{2,}\b",
        r"\b[A-Za-z]+(?:ij|ji|mn|nm|kl|lk)\b",
        r"\b(?:lambda|alpha|beta|gamma|theta|mu)\d+\b",
        r"\b[αβγθλμ]\d+\b",
        r"\b[A-Za-z]\(\d{1,2}\)\b",
    ]
    return any(re.search(pattern, compact, flags=re.IGNORECASE) for pattern in patterns)


def detect_math_text_without_latex(text: str) -> bool:
    """Detect Unicode math symbols in plain text that are not already inside LaTeX delimiters."""

    stripped = _strip_latex_segments(text)
    if not MATH_SYMBOL_RE.search(stripped):
        return False
    if re.search(r"[=+*/^_<>≤≥≈≠]|∑|∫|∂", stripped):
        return True
    return bool(re.search(r"(\d\s*[αβγδλμ]|[αβγδλμ]\s*\d|[A-Za-z]\s*[≤≥=])", stripped))


def detect_matrix_like_text(text: str) -> bool:
    lowered = text.lower()
    if any(token in lowered for token in ("matrix", "pmatrix", "bmatrix", "vmatrix", "cases", "array", "tabular", "align")):
        return True
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    row_like = 0
    for line in lines:
        numeric_or_symbol_cells = re.split(r"\s{2,}|\t|&|\|", line)
        cells = [cell for cell in numeric_or_symbol_cells if cell.strip()]
        if len(cells) >= 3 and sum(bool(re.search(r"[A-Za-z0-9αβλ+\-*/=]", cell)) for cell in cells) >= 3:
            row_like += 1
    return row_like >= 2


def _strip_latex_segments(text: str) -> str:
    return LATEX_WRAPPED_RE.sub(" ", text)


def _has_complex_latex_environment(text: str) -> bool:
    return bool(re.search(r"\\begin\{(align|cases|array|matrix|pmatrix|bmatrix|tabular)\*?\}", text))


def _has_table_with_math(text: str) -> bool:
    has_table = bool(re.search(r"<\s*/?\s*table\b", text, re.IGNORECASE)) or sum(1 for line in text.splitlines() if "|" in line) >= 2
    return has_table and bool(re.search(r"[$_^=∑∫∂≤≥αβλ]|\\frac|\\sum|\\int", text))
