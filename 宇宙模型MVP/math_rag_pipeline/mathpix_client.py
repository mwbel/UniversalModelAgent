from __future__ import annotations

import base64
import hashlib
import http.client
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from math_rag_pipeline.config import load_config


CONFIG = load_config()


def call_mathpix_image(image_path: str | Path, mode: str = "latex") -> dict[str, Any]:
    """Call Mathpix for one image crop, using a mandatory local cache."""

    image_path = Path(image_path)
    cached = cache_result_by_image_hash(image_path, mode=mode)
    if cached.get("hit"):
        return cached["result"]

    app_id = os.environ.get("MATHPIX_APP_ID")
    app_key = os.environ.get("MATHPIX_APP_KEY")
    if not app_id or not app_key:
        return {
            "ok": False,
            "error": "MATHPIX_APP_ID and MATHPIX_APP_KEY must be set",
            "cached": False,
        }

    payload = _build_payload(image_path, mode)
    headers = {
        "Content-Type": "application/json",
        "app_id": app_id,
        "app_key": app_key,
    }
    api_url = str(CONFIG["mathpix"]["api_url"])
    timeout = int(CONFIG["mathpix"].get("timeout_seconds", 60))
    max_retries = int(CONFIG["mathpix"].get("max_retries", 3))

    last_error = ""
    for attempt in range(max_retries):
        request = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
                result = {"ok": True, "cached": False, "raw": data, "text": _extract_mathpix_text(data, mode)}
                _write_cache(image_path, mode, result)
                return result
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            last_error = f"HTTP {exc.code}: {body}"
            if exc.code in {429, 500, 502, 503, 504} and attempt < max_retries - 1:
                handle_rate_limit(attempt)
                continue
            break
        except (urllib.error.URLError, TimeoutError, ConnectionError, http.client.RemoteDisconnected, json.JSONDecodeError) as exc:
            last_error = str(exc)
            if attempt < max_retries - 1:
                handle_rate_limit(attempt)
                continue
            break

    result = {"ok": False, "cached": False, "error": last_error or "Mathpix request failed"}
    _write_cache(image_path, mode, result)
    return result


def handle_rate_limit(attempt: int = 0) -> None:
    base_sleep = float(CONFIG["mathpix"].get("retry_sleep_seconds", 3))
    time.sleep(base_sleep * (2**attempt))


def cache_result_by_image_hash(image_path: str | Path, mode: str = "latex") -> dict[str, Any]:
    cache_path = _cache_path(Path(image_path), mode)
    if not cache_path.exists():
        return {"hit": False, "path": str(cache_path)}
    try:
        return {"hit": True, "path": str(cache_path), "result": json.loads(cache_path.read_text(encoding="utf-8"))}
    except json.JSONDecodeError:
        return {"hit": False, "path": str(cache_path)}


def _build_payload(image_path: Path, mode: str) -> dict[str, Any]:
    image_base64 = base64.b64encode(image_path.read_bytes()).decode("ascii")
    formats = CONFIG["mathpix"].get("formats") or ["text", "latex_styled", "data", "html"]
    return {
        "src": f"data:image/{image_path.suffix.lstrip('.').lower() or 'png'};base64,{image_base64}",
        "formats": formats,
        "ocr": ["math", "text"],
        "skip_recrop": True,
        "math_inline_delimiters": ["$", "$"],
        "math_display_delimiters": ["$$", "$$"],
        "rm_spaces": mode == "latex",
    }


def _extract_mathpix_text(data: dict[str, Any], mode: str) -> str:
    if mode == "html" and isinstance(data.get("html"), str):
        return data["html"].strip()
    if isinstance(data.get("latex_styled"), str) and data["latex_styled"].strip():
        return data["latex_styled"].strip()
    if isinstance(data.get("text"), str):
        return data["text"].strip()
    return ""


def _cache_path(image_path: Path, mode: str) -> Path:
    digest = hashlib.sha256(image_path.read_bytes()).hexdigest()
    cache_dir = Path(os.environ.get("MATHPIX_CACHE_DIR") or str(CONFIG["mathpix"].get("cache_dir", ".mathpix_cache")))
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / f"{digest}.{mode}.json"


def _write_cache(image_path: Path, mode: str, result: dict[str, Any]) -> None:
    _cache_path(image_path, mode).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
