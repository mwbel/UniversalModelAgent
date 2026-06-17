from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class AuditRecorder:
    def __init__(self) -> None:
        self.replaced_blocks: list[dict[str, Any]] = []
        self.failed_mathpix_calls: list[dict[str, Any]] = []
        self.low_confidence_blocks: list[dict[str, Any]] = []

    def summary(self) -> dict[str, Any]:
        return {
            "replaced_count": len(self.replaced_blocks),
            "failed_mathpix_count": len(self.failed_mathpix_calls),
            "low_confidence_count": len(self.low_confidence_blocks),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": self.summary(),
            "replaced_blocks": self.replaced_blocks,
            "failed_mathpix_calls": self.failed_mathpix_calls,
            "low_confidence_blocks": self.low_confidence_blocks,
        }


def record_replaced_blocks(
    audit: AuditRecorder,
    original_block: dict[str, Any],
    new_block: dict[str, Any],
    reason: str | list[str],
) -> None:
    audit.replaced_blocks.append(
        {
            "page": original_block.get("page"),
            "bbox": original_block.get("bbox"),
            "block_id": original_block.get("block_id"),
            "block_type": original_block.get("block_type"),
            "original_text": original_block.get("text"),
            "new_text": new_block.get("text"),
            "reason": reason,
            "ocr_engine": new_block.get("ocr_engine", "mathpix"),
            "confidence": new_block.get("confidence"),
        }
    )


def record_failed_mathpix_calls(
    audit: AuditRecorder,
    block: dict[str, Any],
    error: str,
    reason: str | list[str] | None = None,
) -> None:
    audit.failed_mathpix_calls.append(
        {
            "page": block.get("page"),
            "bbox": block.get("bbox"),
            "block_id": block.get("block_id"),
            "block_type": block.get("block_type"),
            "original_text": block.get("text"),
            "new_text": block.get("text"),
            "reason": reason or block.get("risk_reasons", []),
            "ocr_engine": "mineru",
            "confidence": "low",
            "error": error,
        }
    )


def record_low_confidence_blocks(audit: AuditRecorder, block: dict[str, Any], reason: str | list[str]) -> None:
    audit.low_confidence_blocks.append(
        {
            "page": block.get("page"),
            "bbox": block.get("bbox"),
            "block_id": block.get("block_id"),
            "block_type": block.get("block_type"),
            "original_text": block.get("text"),
            "new_text": block.get("text"),
            "reason": reason,
            "ocr_engine": block.get("ocr_engine", "mineru"),
            "confidence": block.get("confidence", "low"),
        }
    )


def write_audit_report(audit: AuditRecorder, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(audit.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
