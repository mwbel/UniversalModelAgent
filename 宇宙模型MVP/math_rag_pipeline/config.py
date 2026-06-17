from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "mathpix": {
        "api_url": "https://api.mathpix.com/v3/text",
        "timeout_seconds": 60,
        "max_retries": 3,
        "retry_sleep_seconds": 3,
        "cache_dir": ".mathpix_cache",
        "formats": ["text", "latex_styled", "data", "html"],
    },
    "crop": {
        "padding": 8,
        "output_dir": "crops",
    },
    "risk": {
        "enabled_block_types": [
            "table",
            "equation",
            "inline_formula",
            "interline_equation",
            "matrix",
            "align",
            "cases",
            "array",
            "tabular",
        ],
        "lost_subscript_patterns": [
            r"\b[A-Za-z]\d{2,}\b",
            r"\b[A-Za-z]+(?:ij|ji|mn|nm|kl|lk)\b",
            r"\blambda\d+\b",
            r"\balpha\d+\b",
            r"\bbeta\d+\b",
        ],
    },
    "chunking": {
        "chunk_size_tokens": 1200,
        "chunk_overlap_tokens": 150,
        "min_chunk_tokens": 250,
    },
    "markdown": {
        "attach_metadata_comments": True,
    },
}


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _load_yaml_or_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return {}
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(text)
        return loaded if isinstance(loaded, dict) else {}
    except ModuleNotFoundError:
        try:
            loaded = json.loads(text)
            return loaded if isinstance(loaded, dict) else {}
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"Cannot parse {path}. Install PyYAML or use JSON-compatible config."
            ) from exc


def load_config(config_path: str | Path = "config.yaml") -> dict[str, Any]:
    """Load config.yaml and merge it with conservative defaults."""

    return _deep_merge(DEFAULT_CONFIG, _load_yaml_or_json(Path(config_path)))
