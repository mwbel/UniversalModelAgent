from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any

from math_rag_pipeline.audit import (
    AuditRecorder,
    record_failed_mathpix_calls,
    record_low_confidence_blocks,
    record_replaced_blocks,
    write_audit_report,
)
from math_rag_pipeline.chunker import split_markdown_for_rag, write_chunks_jsonl
from math_rag_pipeline.config import load_config
from math_rag_pipeline.image_cropper import crop_block_image
from math_rag_pipeline.mathpix_client import call_mathpix_image
from math_rag_pipeline.mineru_loader import load_mineru_layout_json, load_mineru_markdown, normalize_blocks
from math_rag_pipeline.rag_formatter import render_blocks_to_markdown
from math_rag_pipeline.replacer import replace_block_with_mathpix_result
from math_rag_pipeline.risk_detector import is_high_risk_block


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    _install_runtime_config(config)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    configured_cache_dir = Path(str(config["mathpix"].get("cache_dir", ".mathpix_cache")))
    cache_dir = configured_cache_dir if configured_cache_dir.is_absolute() else out_dir / configured_cache_dir
    cache_dir.mkdir(parents=True, exist_ok=True)
    config["mathpix"]["cache_dir"] = str(cache_dir)

    markdown = load_mineru_markdown(args.mineru_output)
    layout_json = load_mineru_layout_json(args.mineru_output)
    blocks = normalize_blocks(markdown, layout_json, source_file=str(Path(args.pdf)))
    page_images = _index_page_images(args.page_images)
    audit = AuditRecorder()
    processed_blocks: list[dict[str, Any]] = []
    mathpix_attempts = 0

    crop_dir = out_dir / str(config["crop"].get("output_dir", "crops"))
    crop_dir.mkdir(parents=True, exist_ok=True)
    rendered_page_images = _render_origin_pdf_pages(args.mineru_output, out_dir / "_page_images")
    if rendered_page_images:
        page_images = rendered_page_images

    for block in blocks:
        high_risk, reasons = is_high_risk_block(block)
        block["risk_reasons"] = reasons
        if not high_risk:
            block["confidence"] = block.get("confidence") or "medium"
            processed_blocks.append(block)
            continue

        if args.max_mathpix_blocks and mathpix_attempts >= args.max_mathpix_blocks:
            block["mathpix_skipped"] = "max_mathpix_blocks_reached"
            processed_blocks.append(block)
            continue

        page_image = _page_image_for_block(block, page_images)
        if not page_image or not block.get("bbox"):
            block["confidence"] = "low"
            reason = "missing_page_image_or_bbox"
            record_failed_mathpix_calls(audit, block, reason, reasons)
            record_low_confidence_blocks(audit, block, reason)
            processed_blocks.append(block)
            continue

        try:
            crop_path = crop_block_image(page_image, block["bbox"], padding=int(config["crop"].get("padding", 8)))
            stable_crop_path = crop_dir / Path(crop_path).name
            if Path(crop_path) != stable_crop_path:
                shutil.copy2(crop_path, stable_crop_path)
                crop_path = str(stable_crop_path)
        except Exception as exc:
            block["confidence"] = "low"
            record_failed_mathpix_calls(audit, block, f"crop_failed:{exc}", reasons)
            record_low_confidence_blocks(audit, block, "crop_failed")
            processed_blocks.append(block)
            continue

        mathpix_attempts += 1
        mathpix_result = call_mathpix_image(crop_path, mode=_mode_for_block(block))
        new_block = replace_block_with_mathpix_result(block, mathpix_result)
        if mathpix_result.get("ok") and new_block.get("ocr_engine") == "mathpix":
            record_replaced_blocks(audit, block, new_block, reasons)
        else:
            record_failed_mathpix_calls(audit, block, str(mathpix_result.get("error") or new_block.get("mathpix_error")), reasons)
            record_low_confidence_blocks(audit, new_block, reasons)
        processed_blocks.append(new_block)

    final_md = render_blocks_to_markdown(
        processed_blocks,
        attach_metadata=bool(config["markdown"].get("attach_metadata_comments", True)),
    )
    (out_dir / "final.md").write_text(final_md, encoding="utf-8")

    chunk_cfg = config["chunking"]
    chunks = split_markdown_for_rag(
        final_md,
        metadata={"source_file": str(Path(args.pdf)), "mineru_output": str(Path(args.mineru_output))},
        chunk_size=int(chunk_cfg.get("chunk_size_tokens", 1200)),
        chunk_overlap=int(chunk_cfg.get("chunk_overlap_tokens", 150)),
    )
    write_chunks_jsonl(chunks, out_dir / "chunks.jsonl")
    write_audit_report(audit, out_dir / "audit_report.json")
    _write_run_manifest(out_dir, args, config, blocks, processed_blocks, chunks, audit)

    print(json.dumps({"out": str(out_dir), "blocks": len(blocks), "chunks": len(chunks), **audit.summary()}, ensure_ascii=False))
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert MinerU math-book output to RAG Markdown with Mathpix repair.")
    parser.add_argument("--pdf", required=True, help="Original source PDF path.")
    parser.add_argument("--mineru-output", required=True, help="MinerU output directory.")
    parser.add_argument("--page-images", required=True, help="Directory containing MinerU page images.")
    parser.add_argument("--out", required=True, help="Output directory for final.md, chunks.jsonl, audit_report.json.")
    parser.add_argument("--config", default="config.yaml", help="Pipeline config path.")
    parser.add_argument("--max-mathpix-blocks", type=int, default=0, help="Maximum high-risk blocks to send to Mathpix. 0 means unlimited.")
    return parser.parse_args()


def _install_runtime_config(config: dict[str, Any]) -> None:
    import math_rag_pipeline.mathpix_client as mathpix_client

    mathpix_client.CONFIG = config


def _index_page_images(page_images_dir: str | Path) -> dict[int, str]:
    root = Path(page_images_dir)
    images = sorted(
        p
        for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}
    )
    indexed: dict[int, str] = {}
    for order, path in enumerate(images, start=1):
        page = _extract_page_number(path.name) or order
        indexed.setdefault(page, str(path))
    return indexed


def _render_origin_pdf_pages(mineru_output: str | Path, output_dir: str | Path) -> dict[int, str]:
    root = Path(mineru_output)
    pdfs = sorted(root.glob("*_origin.pdf")) if root.is_dir() else []
    if not pdfs:
        return {}
    pdf_path = pdfs[0]
    output = Path(output_dir) / pdf_path.stem
    output.mkdir(parents=True, exist_ok=True)
    try:
        import fitz  # type: ignore
    except ModuleNotFoundError:
        return {}

    doc = fitz.open(pdf_path)
    rendered: dict[int, str] = {}
    for index, page in enumerate(doc, start=1):
        target = output / f"page_{index:04d}.png"
        if not target.exists():
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            pix.save(target)
        rendered[index] = str(target)
    doc.close()
    return rendered


def _extract_page_number(name: str) -> int | None:
    matches = re.findall(r"(?<!\d)(\d{1,5})(?!\d)", name)
    if not matches:
        return None
    return int(matches[-1])


def _page_image_for_block(block: dict[str, Any], page_images: dict[int, str]) -> str | None:
    if not page_images:
        return None
    page = block.get("page")
    if isinstance(page, int) and page in page_images:
        return page_images[page]
    if isinstance(page, str) and page.isdigit() and int(page) in page_images:
        return page_images[int(page)]
    return page_images[min(page_images)]


def _mode_for_block(block: dict[str, Any]) -> str:
    block_type = str(block.get("block_type") or "").lower()
    if block_type in {"table", "tabular"}:
        return "html"
    return "latex"


def _write_run_manifest(
    out_dir: Path,
    args: argparse.Namespace,
    config: dict[str, Any],
    original_blocks: list[dict[str, Any]],
    processed_blocks: list[dict[str, Any]],
    chunks: list[dict[str, Any]],
    audit: AuditRecorder,
) -> None:
    manifest = {
        "pdf": args.pdf,
        "mineru_output": args.mineru_output,
        "page_images": args.page_images,
        "outputs": {
            "final_md": str(out_dir / "final.md"),
            "chunks_jsonl": str(out_dir / "chunks.jsonl"),
            "audit_report": str(out_dir / "audit_report.json"),
        },
        "counts": {
            "original_blocks": len(original_blocks),
            "processed_blocks": len(processed_blocks),
            "chunks": len(chunks),
            **audit.summary(),
        },
        "config": config,
    }
    (out_dir / "run_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
