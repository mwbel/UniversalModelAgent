from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from backend.config import SETTINGS

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


@dataclass(slots=True)
class MarkdownDocument:
    id: str
    title: str
    category: str
    relative_path: str
    path: str
    size: int
    updated_at: float
    image_count: int


def _stable_id(value: str) -> str:
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]
    stem = Path(value).stem.strip().replace(" ", "-")[:48]
    return f"{stem}-{digest}" if stem else digest


def _clean_category(name: str) -> str:
    return name.strip() or "未分类"


class MarkdownLibraryService:
    def __init__(self, root_dir: str | None = None) -> None:
        self.root_dir = Path(root_dir or SETTINGS.markdown_library_dir).expanduser().resolve()

    def config(self) -> dict[str, Any]:
        return {
            "rootDir": str(self.root_dir),
            "exists": self.root_dir.exists(),
            "mineruBaseUrl": SETTINGS.mineru_base_url,
            "mineruConvertPath": SETTINGS.mineru_convert_path,
        }

    def list_categories(self) -> dict[str, Any]:
        if not self.root_dir.exists():
            return {"ok": False, "error": f"Markdown 书库目录不存在：{self.root_dir}", "items": []}

        categories: list[dict[str, Any]] = []
        for child in sorted(self.root_dir.iterdir(), key=lambda path: path.name):
            if not child.is_dir() or child.name.startswith("."):
                continue
            md_files = list(child.rglob("*.md"))
            image_files = [
                path
                for path in child.rglob("*")
                if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
            ]
            categories.append(
                {
                    "id": _clean_category(child.name),
                    "name": _clean_category(child.name),
                    "path": str(child),
                    "relativePath": child.relative_to(self.root_dir).as_posix(),
                    "documentCount": len(md_files),
                    "imageCount": len(image_files),
                }
            )
        return {"ok": True, "error": None, "rootDir": str(self.root_dir), "items": categories}

    def list_documents(
        self,
        category: str | None = None,
        limit: int = 200,
        offset: int = 0,
    ) -> dict[str, Any]:
        try:
            documents = self._scan_documents(category=category)
        except ValueError as error:
            return {"ok": False, "error": str(error), "items": []}

        total = len(documents)
        selected = documents[offset : offset + limit]
        return {
            "ok": True,
            "error": None,
            "rootDir": str(self.root_dir),
            "total": total,
            "limit": limit,
            "offset": offset,
            "items": [asdict(document) for document in selected],
        }

    def read_documents(
        self,
        category: str | None = None,
        document_ids: list[str] | None = None,
        relative_paths: list[str] | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        documents = self._scan_documents(category=category)
        wanted_ids = set(document_ids or [])
        wanted_paths = {self._normalize_relative_path(path) for path in (relative_paths or [])}

        selected: list[MarkdownDocument] = []
        for document in documents:
            if wanted_ids and document.id not in wanted_ids:
                continue
            if wanted_paths and document.relative_path not in wanted_paths:
                continue
            selected.append(document)
            if limit and len(selected) >= limit:
                break

        payloads: list[dict[str, Any]] = []
        for document in selected:
            text = Path(document.path).read_text(encoding="utf-8", errors="ignore")
            payloads.append(
                {
                    "id": document.id,
                    "filename": Path(document.path).name,
                    "title": document.title,
                    "text": text,
                    "metadata": {
                        "category": document.category,
                        "source_path": document.path,
                        "relative_path": document.relative_path,
                        "image_count": document.image_count,
                    },
                }
            )
        return payloads

    def _scan_documents(self, category: str | None = None) -> list[MarkdownDocument]:
        if not self.root_dir.exists():
            raise ValueError(f"Markdown 书库目录不存在：{self.root_dir}")
        category_dir = self._resolve_category_dir(category)
        search_root = category_dir or self.root_dir

        documents: list[MarkdownDocument] = []
        for path in sorted(search_root.rglob("*.md"), key=lambda item: item.as_posix()):
            if path.name.startswith("."):
                continue
            relative_path = path.relative_to(self.root_dir).as_posix()
            parts = relative_path.split("/")
            category_name = _clean_category(parts[0]) if len(parts) > 1 else "未分类"
            stat = path.stat()
            documents.append(
                MarkdownDocument(
                    id=_stable_id(relative_path),
                    title=path.stem,
                    category=category_name,
                    relative_path=relative_path,
                    path=str(path),
                    size=stat.st_size,
                    updated_at=stat.st_mtime,
                    image_count=self._count_sibling_images(path),
                )
            )
        return documents

    def _resolve_category_dir(self, category: str | None) -> Path | None:
        if not category:
            return None
        normalized = _clean_category(category)
        for child in self.root_dir.iterdir():
            if child.is_dir() and _clean_category(child.name) == normalized:
                return child
        raise ValueError(f"没有找到分类目录：{category}")

    def _normalize_relative_path(self, relative_path: str) -> str:
        target = (self.root_dir / relative_path).resolve()
        if self.root_dir not in target.parents and target != self.root_dir:
            raise ValueError(f"非法路径：{relative_path}")
        return target.relative_to(self.root_dir).as_posix()

    def _count_sibling_images(self, markdown_path: Path) -> int:
        book_dir = markdown_path.parent
        if book_dir.name in {"chapters", "ocr"}:
            book_dir = book_dir.parent
        image_dir = book_dir / "images"
        if not image_dir.exists():
            return 0
        return sum(1 for path in image_dir.rglob("*") if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES)


MARKDOWN_LIBRARY = MarkdownLibraryService()
