#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def rewrite_markdown(markdown_path: Path, merged_dir: Path, copied: dict[Path, str]) -> int:
    original = markdown_path.read_text(encoding="utf-8", errors="ignore")
    changed = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        alt_text = match.group(1)
        raw_target = normalize_target(match.group(2))
        if raw_target.startswith(("http://", "https://", "data:")):
            return match.group(0)

        source_path = (markdown_path.parent / raw_target).resolve()
        if not source_path.exists() or "images" not in source_path.parts:
            return match.group(0)

        destination_name = copied.get(source_path)
        if not destination_name:
            destination_name = source_path.name
            copied[source_path] = destination_name

        if markdown_path.parent == merged_dir:
            new_target = f"images/{destination_name}"
        else:
            new_target = f"../images/{destination_name}"
        changed += 1
        return f"![{alt_text}]({new_target})"

    updated = IMAGE_LINK_RE.sub(replace, original)
    if updated != original:
        markdown_path.write_text(updated, encoding="utf-8")
    return changed


def collect_and_copy_images(merged_dir: Path, copied: dict[Path, str]) -> int:
    images_dir = merged_dir / "images"
    images_dir.mkdir(exist_ok=True)
    count = 0
    for source_path, destination_name in copied.items():
        destination_path = images_dir / destination_name
        if not destination_path.exists():
            shutil.copy2(source_path, destination_path)
            count += 1
    return count


def process_merged_dir(merged_dir: Path) -> tuple[int, int]:
    copied: dict[Path, str] = {}
    changed = 0

    md_files = sorted(merged_dir.glob("*_完整.md"))
    chapter_dirs = sorted(path for path in merged_dir.iterdir() if path.is_dir() and path.name.endswith("_chapters"))
    for chapter_dir in chapter_dirs:
        md_files.extend(sorted(path for path in chapter_dir.glob("*.md") if path.name != "chapters_index.md"))

    for markdown_path in md_files:
        changed += rewrite_markdown(markdown_path, merged_dir, copied)

    copied_count = collect_and_copy_images(merged_dir, copied)
    return changed, copied_count


def find_merged_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("merged") if path.is_dir())


def main() -> int:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()
    merged_dirs = find_merged_dirs(root)
    if not merged_dirs:
        print("没有找到 merged 目录。")
        return 0

    total_changed = 0
    total_copied = 0
    processed = 0

    for merged_dir in merged_dirs:
        changed, copied = process_merged_dir(merged_dir)
        if changed or copied:
            processed += 1
            total_changed += changed
            total_copied += copied
            print(f"{merged_dir}")
            print(f"  rewritten_links={changed} copied_images={copied}")

    print("")
    print(f"processed={processed}")
    print(f"rewritten_links={total_changed}")
    print(f"copied_images={total_copied}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
