from __future__ import annotations

import re
from typing import Any


ENV_RE = re.compile(r"\\(begin|end)\{([^}]+)\}")


def validate_latex_syntax(text: str) -> dict[str, Any]:
    """Run lightweight LaTeX checks that do not require a TeX runtime."""

    errors: list[str] = []
    if text.count("$") % 2 == 1:
        errors.append("unbalanced_dollar_delimiter")
    unclosed = detect_unclosed_environment(text)
    if unclosed:
        errors.append(f"unclosed_environment:{','.join(unclosed)}")
    if not _balanced_braces(text):
        errors.append("unbalanced_braces")
    return {"ok": not errors, "errors": errors}


def fix_basic_latex_wrappers(text: str, block_type: str = "text") -> str:
    """Normalize common Mathpix/MinerU formula wrapper issues."""

    stripped = text.strip()
    if not stripped:
        return stripped

    stripped = stripped.replace("\\[", "$$").replace("\\]", "$$")
    stripped = stripped.replace("\\(", "$").replace("\\)", "$")
    stripped = re.sub(r"\${3,}", "$$", stripped)

    if _is_display_math_type(block_type) or _looks_like_display_formula(stripped):
        inner = _strip_outer_math_delimiters(stripped)
        return f"$$\n{inner.strip()}\n$$"

    if _looks_like_inline_formula(stripped) and not _has_outer_math_delimiters(stripped):
        return f"${stripped}$"

    return stripped


def detect_unclosed_environment(text: str) -> list[str]:
    stack: list[str] = []
    for match in ENV_RE.finditer(text):
        action, name = match.group(1), match.group(2)
        if action == "begin":
            stack.append(name)
        elif stack and stack[-1] == name:
            stack.pop()
        else:
            return [name]
    return stack


def _balanced_braces(text: str) -> bool:
    depth = 0
    escaped = False
    for char in text:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


def _is_display_math_type(block_type: str) -> bool:
    return block_type.lower() in {
        "equation",
        "interline_equation",
        "display_formula",
        "matrix",
        "align",
        "cases",
        "array",
    }


def _looks_like_display_formula(text: str) -> bool:
    return "\n" in text and bool(re.search(r"\\begin\{|=|\\\\|&", text))


def _looks_like_inline_formula(text: str) -> bool:
    if " " in text.strip() and not re.search(r"[=+\-*/_^\\∑∫∂≤≥αβλ]", text):
        return False
    return bool(re.search(r"[=+\-*/_^\\∑∫∂≤≥αβλ]", text))


def _has_outer_math_delimiters(text: str) -> bool:
    return (text.startswith("$") and text.endswith("$")) or text.startswith("\\begin{")


def _strip_outer_math_delimiters(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("$$") and stripped.endswith("$$"):
        return stripped[2:-2]
    if stripped.startswith("$") and stripped.endswith("$"):
        return stripped[1:-1]
    return stripped
