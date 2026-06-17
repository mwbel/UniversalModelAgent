from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}
MARKDOWN_SUFFIXES = {".md", ".markdown"}
ARTIFACT_DIR_NAMES = {"chunks", "merged", "images", "auto", "ocr", "hybrid_auto"}
IGNORED_DIR_NAMES = {"_missing_mathpix_required_files"}


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    project_root = Path(args.project_root).resolve()
    out_root = Path(args.out).resolve()
    missing_dir = Path(args.missing_dir).resolve() if args.missing_dir else root / "_missing_mathpix_required_files"

    books = [scan_one_book(Path(path).resolve()) for path in args.book_dir] if args.book_dir else scan_books(root)
    collect_missing_books(books, missing_dir, mode=args.missing_mode)

    ready_books = [book for book in books if book["status"] == "ready"]
    if args.limit_books:
        ready_books = ready_books[: args.limit_books]

    report: dict[str, Any] = {
        "root": str(root),
        "out": str(out_root),
        "missing_dir": str(missing_dir),
        "summary": dict(Counter(book["status"] for book in books)),
        "ready_books": len(ready_books),
        "missing_books": [book_summary(book) for book in books if book["status"] != "ready"],
        "processed": [],
        "skipped": [],
        "failed": [],
    }

    if args.collect_missing_only:
        write_json(out_root / "batch_report.json", report)
        print(json.dumps({"missing_dir": str(missing_dir), "summary": report["summary"]}, ensure_ascii=False))
        return 0

    if args.dry_run:
        report["dry_run_chunks"] = dry_run_plan(ready_books, args.limit_chunks)
        write_json(out_root / "batch_report.json", report)
        print(json.dumps({"dry_run": True, "books": len(ready_books), "chunks": sum(len(item["chunks"]) for item in report["dry_run_chunks"])}, ensure_ascii=False))
        return 0

    if not os.environ.get("MATHPIX_APP_ID") or not os.environ.get("MATHPIX_APP_KEY"):
        raise SystemExit("MATHPIX_APP_ID and MATHPIX_APP_KEY must be set before running the batch.")

    out_root.mkdir(parents=True, exist_ok=True)
    for book in ready_books:
        book_out = out_root / safe_name(book["path"])
        book_out.mkdir(parents=True, exist_ok=True)
        chunks = discover_processable_chunks(Path(book["path"]))
        if args.limit_chunks:
            chunks = chunks[: args.limit_chunks]

        chunk_reports: list[dict[str, Any]] = []
        for chunk_dir in chunks:
            chunk_out = book_out / safe_name(chunk_label(chunk_dir))
            final_md = chunk_out / "final.md"
            if args.skip_existing and final_md.exists():
                chunk_reports.append({"chunk": str(chunk_dir), "out": str(chunk_out), "status": "skipped_existing"})
                continue

            command = [
                sys.executable,
                str(project_root / "main.py"),
                "--pdf",
                infer_pdf_path(Path(book["path"])),
                "--mineru-output",
                str(chunk_dir),
                "--page-images",
                str(chunk_dir / "images"),
                "--out",
                str(chunk_out),
            ]
            if args.config:
                command.extend(["--config", str(Path(args.config).resolve())])
            if args.max_mathpix_blocks:
                command.extend(["--max-mathpix-blocks", str(args.max_mathpix_blocks)])

            completed = subprocess.run(command, cwd=project_root, text=True, capture_output=True)
            chunk_report = {
                "chunk": str(chunk_dir),
                "out": str(chunk_out),
                "status": "ok" if completed.returncode == 0 else "failed",
                "stdout": completed.stdout.strip(),
                "stderr": completed.stderr.strip(),
                "returncode": completed.returncode,
            }
            chunk_reports.append(chunk_report)
            if completed.returncode != 0:
                report["failed"].append(chunk_report)
                if not args.continue_on_error:
                    write_json(out_root / "batch_report.json", report)
                    raise SystemExit(completed.returncode)

        merge_book_outputs(book_out, chunk_reports, Path(book["path"]))
        report["processed"].append({"book": book["path"], "out": str(book_out), "chunks": chunk_reports})
        write_json(out_root / "batch_report.json", report)

    print(json.dumps({"processed_books": len(report["processed"]), "failed_chunks": len(report["failed"]), "out": str(out_root)}, ensure_ascii=False))
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch Mathpix repair for MinerU book chunk directories.")
    parser.add_argument("--root", required=True, help="Root folder containing book folders.")
    parser.add_argument("--book-dir", action="append", default=[], help="Specific book folder to process. Can be repeated.")
    parser.add_argument("--out", required=True, help="Output folder for repaired books.")
    parser.add_argument("--project-root", default=Path(__file__).resolve().parents[1], help="Project root that contains main.py.")
    parser.add_argument("--config", default=None, help="Optional config.yaml path passed to main.py.")
    parser.add_argument("--missing-dir", default=None, help="Unified folder for books missing required files.")
    parser.add_argument("--missing-mode", choices=["symlink", "copy"], default="symlink", help="How to collect missing books.")
    parser.add_argument("--collect-missing-only", action="store_true", help="Only collect missing books and write a report.")
    parser.add_argument("--dry-run", action="store_true", help="Preview processable chunks without calling Mathpix.")
    parser.add_argument("--skip-existing", action="store_true", help="Skip chunk outputs that already have final.md.")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue processing after a chunk failure.")
    parser.add_argument("--limit-books", type=int, default=0, help="Process at most N ready books.")
    parser.add_argument("--limit-chunks", type=int, default=0, help="Process at most N chunks per book.")
    parser.add_argument("--max-mathpix-blocks", type=int, default=0, help="Maximum high-risk blocks to send to Mathpix per chunk.")
    return parser.parse_args()


def scan_books(root: Path) -> list[dict[str, Any]]:
    records: dict[Path, dict[str, Any]] = defaultdict(
        lambda: {
            "path": "",
            "md": 0,
            "json": 0,
            "images": 0,
            "pdf": 0,
            "bbox_json": 0,
            "md_examples": [],
            "json_examples": [],
            "image_examples": [],
            "bbox_examples": [],
        }
    )

    for path in root.rglob("*"):
        if not path.is_file() or path.name == ".DS_Store":
            continue
        if any(part in IGNORED_DIR_NAMES for part in path.relative_to(root).parts):
            continue
        book_dir = book_dir_for(root, path)
        record = records[book_dir]
        record["path"] = str(book_dir)
        suffix = path.suffix.lower()
        if suffix in MARKDOWN_SUFFIXES:
            record["md"] += 1
            add_example(record, "md_examples", path)
        elif suffix == ".json":
            record["json"] += 1
            add_example(record, "json_examples", path)
            if json_has_bbox(path):
                record["bbox_json"] += 1
                add_example(record, "bbox_examples", path)
        elif suffix in IMAGE_SUFFIXES:
            record["images"] += 1
            add_example(record, "image_examples", path)
        elif suffix == ".pdf":
            record["pdf"] += 1

    books: list[dict[str, Any]] = []
    for book_dir, record in records.items():
        if not any(record[key] for key in ("md", "json", "images", "pdf")):
            continue
        record["path"] = str(book_dir)
        record["status"] = classify(record)
        books.append(record)
    books.sort(key=lambda item: item["path"])
    return books


def scan_one_book(book_dir: Path) -> dict[str, Any]:
    record: dict[str, Any] = {
        "path": str(book_dir),
        "md": 0,
        "json": 0,
        "images": 0,
        "pdf": 0,
        "bbox_json": 0,
        "md_examples": [],
        "json_examples": [],
        "image_examples": [],
        "bbox_examples": [],
    }
    for path in book_dir.rglob("*"):
        if not path.is_file() or path.name == ".DS_Store":
            continue
        if any(part in IGNORED_DIR_NAMES for part in path.relative_to(book_dir).parts):
            continue
        suffix = path.suffix.lower()
        if suffix in MARKDOWN_SUFFIXES:
            record["md"] += 1
            add_example(record, "md_examples", path)
        elif suffix == ".json":
            record["json"] += 1
            add_example(record, "json_examples", path)
            if json_has_bbox(path):
                record["bbox_json"] += 1
                add_example(record, "bbox_examples", path)
        elif suffix in IMAGE_SUFFIXES:
            record["images"] += 1
            add_example(record, "image_examples", path)
        elif suffix == ".pdf":
            record["pdf"] += 1
    record["status"] = classify(record)
    return record


def book_dir_for(root: Path, path: Path) -> Path:
    rel = path.relative_to(root)
    parts = rel.parts
    for index, part in enumerate(parts):
        if part in ARTIFACT_DIR_NAMES and index > 0:
            return root.joinpath(*parts[:index])
    if len(parts) >= 2:
        return root / parts[0] / parts[1]
    return path.parent


def classify(record: dict[str, Any]) -> str:
    if record["md"] and record["json"] and record["images"] and record["bbox_json"]:
        return "ready"
    if record["md"] and record["json"] and record["bbox_json"] and not record["images"]:
        return "missing_images"
    if record["md"] and record["images"] and not record["bbox_json"]:
        return "missing_bbox_json"
    if record["md"] and not record["json"]:
        return "md_only_or_no_json"
    if record["json"] and record["bbox_json"] and not record["md"]:
        return "bbox_json_no_md"
    return "incomplete"


def discover_processable_chunks(book_dir: Path) -> list[Path]:
    chunks: list[Path] = []
    for candidate in book_dir.rglob("*"):
        if not candidate.is_dir() or candidate.name not in {"auto", "ocr", "hybrid_auto"}:
            continue
        if not (candidate / "images").is_dir():
            continue
        has_md = any(path.suffix.lower() in MARKDOWN_SUFFIXES for path in candidate.iterdir() if path.is_file())
        json_files = [path for path in candidate.iterdir() if path.is_file() and path.suffix.lower() == ".json"]
        if has_md and json_files and any(json_has_bbox(path) for path in json_files):
            chunks.append(candidate)
    chunks.sort()
    return chunks


def collect_missing_books(books: list[dict[str, Any]], missing_dir: Path, mode: str) -> None:
    missing = [book for book in books if book["status"] != "ready"]
    missing_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for book in missing:
        source = Path(book["path"])
        target = missing_dir / f"{book['status']}__{safe_name(str(source))}"
        if not source.is_dir():
            manifest.append(book_summary(book) | {"link_or_copy": None, "note": "source is not a directory"})
            continue
        if target.exists() or target.is_symlink():
            pass
        elif mode == "symlink":
            target.symlink_to(source, target_is_directory=True)
        else:
            import shutil

            shutil.copytree(source, target)
        manifest.append(book_summary(book) | {"link_or_copy": str(target)})
    write_json(missing_dir / "missing_mathpix_required_files.json", manifest)


def dry_run_plan(books: list[dict[str, Any]], limit_chunks: int) -> list[dict[str, Any]]:
    plan = []
    for book in books:
        chunks = discover_processable_chunks(Path(book["path"]))
        if limit_chunks:
            chunks = chunks[:limit_chunks]
        plan.append({"book": book["path"], "chunks": [str(chunk) for chunk in chunks]})
    return plan


def merge_book_outputs(book_out: Path, chunk_reports: list[dict[str, Any]], book_dir: Path) -> None:
    final_parts: list[str] = []
    merged_chunks: list[dict[str, Any]] = []
    merged_audits: list[dict[str, Any]] = []

    for index, item in enumerate(chunk_reports):
        chunk_out = Path(item["out"])
        final_md = chunk_out / "final.md"
        if final_md.exists():
            final_parts.append(f"<!-- source_chunk: {json.dumps(item['chunk'], ensure_ascii=False)} -->\n\n")
            final_parts.append(final_md.read_text(encoding="utf-8").strip())
            final_parts.append("\n")

        chunks_jsonl = chunk_out / "chunks.jsonl"
        if chunks_jsonl.exists():
            for line in chunks_jsonl.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                chunk = json.loads(line)
                chunk["id"] = f"book-{index:04d}-{chunk.get('id', 'chunk')}"
                chunk.setdefault("metadata", {})
                chunk["metadata"]["source_chunk_dir"] = item["chunk"]
                merged_chunks.append(chunk)

        audit_path = chunk_out / "audit_report.json"
        if audit_path.exists():
            merged_audits.append({"source_chunk_dir": item["chunk"], "audit": json.loads(audit_path.read_text(encoding="utf-8"))})

    (book_out / "book_final.md").write_text("\n\n".join(part for part in final_parts if part.strip()) + "\n", encoding="utf-8")
    with (book_out / "book_chunks.jsonl").open("w", encoding="utf-8") as handle:
        for chunk in merged_chunks:
            handle.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    write_json(
        book_out / "book_audit_report.json",
        {
            "book_dir": str(book_dir),
            "chunk_count": len(chunk_reports),
            "merged_chunk_count": len(merged_chunks),
            "chunk_audits": merged_audits,
        },
    )


def json_has_bbox(path: Path) -> bool:
    try:
        if path.stat().st_size > 80_000_000:
            return False
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    return contains_bbox(data, [0])


def contains_bbox(value: Any, counter: list[int]) -> bool:
    counter[0] += 1
    if counter[0] > 200_000:
        return False
    if isinstance(value, dict):
        if any(key in value for key in ("bbox", "box", "poly", "polygon")):
            return True
        return any(contains_bbox(child, counter) for child in value.values())
    if isinstance(value, list):
        return any(contains_bbox(child, counter) for child in value)
    return False


def infer_pdf_path(book_dir: Path) -> str:
    pdfs = sorted(book_dir.rglob("*.pdf"))
    if pdfs:
        return str(pdfs[0])
    return str(book_dir)


def chunk_label(chunk_dir: Path) -> str:
    parent = chunk_dir.parent.name
    return f"{parent}_{chunk_dir.name}"


def safe_name(value: str | Path) -> str:
    text = str(value)
    name = Path(text).name or text
    name = re.sub(r"[\\/:*?\"<>|]+", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return f"{name[:90]}__{digest}"


def add_example(record: dict[str, Any], key: str, path: Path) -> None:
    if len(record[key]) < 3:
        record[key].append(str(path))


def book_summary(book: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": book["status"],
        "book": book["path"],
        "md": book["md"],
        "json": book["json"],
        "images": book["images"],
        "bbox_json": book["bbox_json"],
        "md_examples": book["md_examples"][:2],
        "json_examples": book["json_examples"][:2],
        "image_examples": book["image_examples"][:2],
        "bbox_examples": book["bbox_examples"][:2],
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
