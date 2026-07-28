from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from backend.config import SETTINGS


PATCH_STATUSES = {"draft", "accepted", "rejected", "noop", "conflict"}
PATCH_SOURCES = {"mathpix", "human", "auto_normalizer"}
BOOK_STATUSES = {"uploaded", "in_review", "completed", "archived"}
BOOK_ROLES = {"owner", "marker", "editor", "viewer"}


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _json_loads(value: str | None, fallback: Any) -> Any:
    if not value:
        return fallback
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return fallback


def _slug(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "-", value.strip()).strip("-")
    return cleaned[:120] or fallback


def _parse_data_url(value: str) -> tuple[str, bytes] | None:
    match = re.match(r"^data:([^;,]+);base64,(.+)$", value, flags=re.DOTALL)
    if not match:
        return None
    return match.group(1), base64.b64decode(match.group(2))


def _file_bytes(file_item: dict[str, Any]) -> tuple[str, bytes]:
    data_url = str(file_item.get("dataUrl") or "")
    parsed = _parse_data_url(data_url)
    if parsed:
        return parsed
    if "base64" in file_item:
        mime_type = str(file_item.get("mimeType") or "application/octet-stream")
        return mime_type, base64.b64decode(str(file_item.get("base64") or ""))
    if "json" in file_item:
        return "application/json", _json_dumps(file_item.get("json")).encode("utf-8")
    text = str(file_item.get("text") or "")
    mime_type = str(file_item.get("mimeType") or "text/plain; charset=utf-8")
    return mime_type, text.encode("utf-8")


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


@dataclass(frozen=True)
class StoredObject:
    key: str
    url: str
    size_bytes: int
    checksum: str
    mime_type: str


class LocalObjectStorage:
    def __init__(self, root_dir: str, public_base_url: str = "") -> None:
        self.root_dir = Path(root_dir)
        self.public_base_url = public_base_url.rstrip("/")

    def put_bytes(self, key: str, content: bytes, mime_type: str) -> StoredObject:
        safe_key = self._safe_key(key)
        path = self.root_dir / safe_key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        if self.public_base_url:
            url = f"{self.public_base_url}/{safe_key}"
        else:
            url = f"local://ocr-workbench/{safe_key}"
        return StoredObject(
            key=safe_key,
            url=url,
            size_bytes=len(content),
            checksum=_sha256(content),
            mime_type=mime_type,
        )

    def read_text(self, key: str) -> str:
        return (self.root_dir / self._safe_key(key)).read_text(encoding="utf-8")

    @staticmethod
    def _safe_key(key: str) -> str:
        parts = [part for part in str(key).replace("\\", "/").split("/") if part and part not in {".", ".."}]
        if not parts:
            raise ValueError("Missing storage key")
        return "/".join(parts)


class OcrWorkbenchRepository:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _init_schema(self) -> None:
        with self.connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT,
                    created_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS books (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    owner_user_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    page_count INTEGER,
                    current_page INTEGER,
                    current_block_key TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS book_users (
                    book_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    created_by TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    PRIMARY KEY (book_id, user_id),
                    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS book_files (
                    id TEXT PRIMARY KEY,
                    book_id TEXT NOT NULL,
                    file_type TEXT NOT NULL,
                    storage_key TEXT NOT NULL,
                    url TEXT NOT NULL,
                    name TEXT NOT NULL,
                    relative_path TEXT,
                    mime_type TEXT NOT NULL,
                    size_bytes INTEGER NOT NULL,
                    checksum TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS ocr_patches (
                    id TEXT PRIMARY KEY,
                    book_id TEXT NOT NULL,
                    page_no INTEGER,
                    block_key TEXT NOT NULL,
                    status TEXT NOT NULL,
                    source TEXT NOT NULL,
                    old_hash TEXT,
                    old_text TEXT,
                    new_text TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    created_by TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    revision INTEGER NOT NULL DEFAULT 1,
                    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
                );
                CREATE TABLE IF NOT EXISTS exports (
                    id TEXT PRIMARY KEY,
                    book_id TEXT NOT NULL,
                    export_type TEXT NOT NULL,
                    storage_key TEXT NOT NULL,
                    url TEXT NOT NULL,
                    size_bytes INTEGER NOT NULL,
                    checksum TEXT NOT NULL,
                    created_by TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL,
                    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
                );
                CREATE INDEX IF NOT EXISTS idx_books_owner ON books(owner_user_id);
                CREATE INDEX IF NOT EXISTS idx_book_users_book ON book_users(book_id);
                CREATE INDEX IF NOT EXISTS idx_book_users_user ON book_users(user_id);
                CREATE INDEX IF NOT EXISTS idx_files_book ON book_files(book_id);
                CREATE INDEX IF NOT EXISTS idx_patches_book ON ocr_patches(book_id);
                CREATE INDEX IF NOT EXISTS idx_patches_block_status ON ocr_patches(book_id, block_key, status);
                CREATE INDEX IF NOT EXISTS idx_exports_book ON exports(book_id);
                """
            )
            columns = {row["name"] for row in conn.execute("PRAGMA table_info(book_files)").fetchall()}
            if "relative_path" not in columns:
                conn.execute("ALTER TABLE book_files ADD COLUMN relative_path TEXT")


class OcrWorkbenchService:
    def __init__(self) -> None:
        self.storage = LocalObjectStorage(
            SETTINGS.ocr_workbench_storage_dir,
            SETTINGS.ocr_workbench_public_base_url,
        )
        self.repo = OcrWorkbenchRepository(SETTINGS.ocr_workbench_db_path)

    def config(self) -> dict[str, Any]:
        return {
            "ok": True,
            "storageDriver": SETTINGS.ocr_workbench_storage_driver,
            "storageMode": "local-object-store",
            "dbPath": SETTINGS.ocr_workbench_db_path,
            "ossConfigured": bool(SETTINGS.oss_endpoint and SETTINGS.oss_bucket),
            "ossBucket": SETTINGS.oss_bucket,
            "ossEndpoint": SETTINGS.oss_endpoint,
        }

    def create_book(self, payload: dict[str, Any]) -> dict[str, Any]:
        title = str(payload.get("title") or "").strip()
        owner_user_id = str(payload.get("ownerUserId") or payload.get("owner_user_id") or "local-owner").strip()
        owner_name = str(payload.get("ownerName") or owner_user_id).strip() or owner_user_id
        collaborators_payload = payload.get("collaborators")
        files = payload.get("files")
        if not title:
            return {"ok": False, "error": "Missing title"}
        if not isinstance(files, list) or not files:
            return {"ok": False, "error": "Missing files"}

        now = _now_iso()
        book_id = str(payload.get("bookId") or uuid.uuid4())
        page_count = self._optional_int(payload.get("pageCount"))
        status = str(payload.get("status") or "uploaded")
        if status not in BOOK_STATUSES:
            return {"ok": False, "error": f"Unsupported book status: {status}"}

        saved_files: list[dict[str, Any]] = []
        try:
            with self.repo.connect() as conn:
                conn.execute(
                    "INSERT OR IGNORE INTO users(id, name, email, created_at) VALUES(?, ?, ?, ?)",
                    (owner_user_id, owner_name, str(payload.get("ownerEmail") or ""), now),
                )
                conn.execute(
                    """
                    INSERT INTO books(id, title, owner_user_id, status, page_count, current_page, current_block_key, created_at, updated_at)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (book_id, title, owner_user_id, status, page_count, 1, "", now, now),
                )
                conn.execute(
                    "INSERT OR REPLACE INTO book_users(book_id, user_id, role, created_by, created_at) VALUES(?, ?, 'owner', ?, ?)",
                    (book_id, owner_user_id, owner_user_id, now),
                )
                for collaborator in self._normalize_book_users(collaborators_payload, owner_user_id):
                    conn.execute(
                        "INSERT OR REPLACE INTO book_users(book_id, user_id, role, created_by, created_at) VALUES(?, ?, ?, ?, ?)",
                        (book_id, collaborator["user_id"], collaborator["role"], owner_user_id, now),
                    )
                for index, file_item in enumerate(files):
                    if not isinstance(file_item, dict):
                        raise ValueError("Invalid file item")
                    saved = self._store_book_file(book_id, file_item, index, now)
                    conn.execute(
                        """
                        INSERT INTO book_files(id, book_id, file_type, storage_key, url, name, relative_path, mime_type, size_bytes, checksum, created_at)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            saved["id"],
                            book_id,
                            saved["fileType"],
                            saved["storageKey"],
                            saved["url"],
                            saved["name"],
                            saved["relativePath"],
                            saved["mimeType"],
                            saved["sizeBytes"],
                            saved["checksum"],
                            now,
                        ),
                    )
                    saved_files.append(saved)
        except sqlite3.IntegrityError as error:
            return {"ok": False, "error": f"Book create failed: {error}"}
        except Exception as error:  # noqa: BLE001
            return {"ok": False, "error": str(error)}

        return {"ok": True, "book": self.get_book(book_id).get("book"), "files": saved_files}

    def list_books(self, owner_user_id: str | None = None) -> dict[str, Any]:
        where = ""
        params: tuple[Any, ...] = ()
        if owner_user_id:
            where = "WHERE owner_user_id = ?"
            params = (owner_user_id,)
        with self.repo.connect() as conn:
            rows = conn.execute(
                f"SELECT * FROM books {where} ORDER BY updated_at DESC, created_at DESC",
                params,
            ).fetchall()
        return {"ok": True, "books": [self._book_dict(row) for row in rows]}

    def get_book(self, book_id: str) -> dict[str, Any]:
        with self.repo.connect() as conn:
            book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
            if not book:
                return {"ok": False, "error": "Book not found"}
            files = conn.execute("SELECT * FROM book_files WHERE book_id = ? ORDER BY created_at, file_type", (book_id,)).fetchall()
            exports = conn.execute("SELECT * FROM exports WHERE book_id = ? ORDER BY created_at DESC", (book_id,)).fetchall()
            participants = conn.execute(
                "SELECT user_id, role, created_by, created_at FROM book_users WHERE book_id = ? ORDER BY created_at, user_id",
                (book_id,),
            ).fetchall()
            normalized_participants = [self._participant_dict(row) for row in participants]
        book_payload = self._book_dict(book)
        book_payload["participants"] = normalized_participants
        return {
            "ok": True,
            "book": book_payload,
            "files": [self._file_dict(row) for row in files],
            "exports": [self._export_dict(row) for row in exports],
            "participants": normalized_participants,
        }

    def get_state(self, book_id: str) -> dict[str, Any]:
        book_result = self.get_book(book_id)
        if not book_result.get("ok"):
            return book_result
        patches = self.list_patches(book_id)
        if not patches.get("ok"):
            return patches
        book = book_result["book"]
        return {
            "ok": True,
            "book": {
                **book,
                "participants": book_result.get("participants", []),
            },
            "files": book_result["files"],
            "exports": book_result["exports"],
            "ocrPatches": patches["patches"],
        }

    def add_book_files(self, book_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        created_by = str(payload.get("createdBy") or payload.get("ownerUserId") or "").strip()
        files = payload.get("files")
        if not created_by:
            return {"ok": False, "error": "Missing createdBy"}
        if not isinstance(files, list) or not files:
            return {"ok": False, "error": "Missing files"}
        write_permission = self._require_access(
            book_id=book_id,
            user_id=created_by,
            allowed={"owner", "marker", "editor"},
        )
        if not write_permission.get("ok"):
            return write_permission
        now = _now_iso()
        saved_files: list[dict[str, Any]] = []
        try:
            with self.repo.connect() as conn:
                for index, file_item in enumerate(files):
                    if not isinstance(file_item, dict):
                        raise ValueError("Invalid file item")
                    saved = self._store_book_file(book_id, file_item, index, now)
                    conn.execute(
                        """
                        INSERT INTO book_files(id, book_id, file_type, storage_key, url, name, relative_path, mime_type, size_bytes, checksum, created_at)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            saved["id"],
                            book_id,
                            saved["fileType"],
                            saved["storageKey"],
                            saved["url"],
                            saved["name"],
                            saved["relativePath"],
                            saved["mimeType"],
                            saved["sizeBytes"],
                            saved["checksum"],
                            now,
                        ),
                    )
                    saved_files.append(saved)
                conn.execute("UPDATE books SET updated_at = ? WHERE id = ?", (now, book_id))
        except Exception as error:  # noqa: BLE001
            return {"ok": False, "error": str(error)}
        return {"ok": True, "files": saved_files}

    def save_patch(self, book_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        status = str(payload.get("status") or "draft")
        source = str(payload.get("source") or "")
        block_key = str(payload.get("blockKey") or payload.get("blockId") or "").strip()
        created_by = str(payload.get("createdBy") or payload.get("updatedBy") or "").strip()
        if status not in PATCH_STATUSES:
            return {"ok": False, "error": f"Unsupported patch status: {status}"}
        if source not in PATCH_SOURCES:
            return {"ok": False, "error": f"Unsupported patch source: {source}"}
        if not block_key:
            return {"ok": False, "error": "Missing blockKey"}
        if not created_by:
            return {"ok": False, "error": "Missing createdBy"}
        if status in {"accepted", "rejected", "noop", "conflict"}:
            patch_permission = self._require_access(
                book_id=book_id,
                user_id=created_by,
                allowed={"owner", "editor"},
            )
        else:
            patch_permission = self._require_access(
                book_id=book_id,
                user_id=created_by,
                allowed={"owner", "marker", "editor"},
            )
        if not patch_permission.get("ok"):
            return patch_permission

        now = _now_iso()
        patch_id = str(payload.get("patchId") or payload.get("id") or uuid.uuid4())
        page_no = self._optional_int(payload.get("pageNo") or payload.get("page_no"))
        metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
        old_text = str(payload.get("oldText") or "")
        new_text = str(payload.get("newText") or "")
        old_hash = str(payload.get("oldHash") or "")
        if not old_hash and old_text:
            old_hash = _sha256(old_text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8"))

        with self.repo.connect() as conn:
            if status == "accepted":
                conn.execute(
                    """
                    UPDATE ocr_patches
                    SET status = 'rejected', updated_at = ?, revision = revision + 1
                    WHERE book_id = ? AND block_key = ? AND status = 'accepted' AND id != ?
                    """,
                    (now, book_id, block_key, patch_id),
                )
            conn.execute(
                """
                INSERT INTO ocr_patches(
                    id, book_id, page_no, block_key, status, source, old_hash, old_text, new_text,
                    metadata_json, created_by, created_at, updated_at, revision
                )
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
                ON CONFLICT(id) DO UPDATE SET
                    page_no = excluded.page_no,
                    block_key = excluded.block_key,
                    status = excluded.status,
                    source = excluded.source,
                    old_hash = excluded.old_hash,
                    old_text = excluded.old_text,
                    new_text = excluded.new_text,
                    metadata_json = excluded.metadata_json,
                    updated_at = excluded.updated_at,
                    revision = ocr_patches.revision + 1
                """,
                (
                    patch_id,
                    book_id,
                    page_no,
                    block_key,
                    status,
                    source,
                    old_hash,
                    old_text,
                    new_text,
                    _json_dumps(metadata),
                    created_by,
                    now,
                    now,
                ),
            )
            conn.execute("UPDATE books SET updated_at = ? WHERE id = ?", (now, book_id))
        return {"ok": True, "patch": self.get_patch(book_id, patch_id).get("patch")}

    def update_patch_status(self, book_id: str, patch_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        status = str(payload.get("status") or "")
        updated_by = str(payload.get("updatedBy") or payload.get("createdBy") or "").strip()
        if status not in PATCH_STATUSES:
            return {"ok": False, "error": f"Unsupported patch status: {status}"}
        if not updated_by:
            return {"ok": False, "error": "Missing updatedBy"}
        review_permission = self._require_access(book_id=book_id, user_id=updated_by, allowed={"owner", "editor"})
        if not review_permission.get("ok"):
            return review_permission
        existing = self.get_patch(book_id, patch_id)
        if not existing.get("ok"):
            return existing
        now = _now_iso()
        block_key = existing["patch"]["blockKey"]
        with self.repo.connect() as conn:
            if status == "accepted":
                conn.execute(
                    """
                    UPDATE ocr_patches
                    SET status = 'rejected', updated_at = ?, revision = revision + 1
                    WHERE book_id = ? AND block_key = ? AND status = 'accepted' AND id != ?
                    """,
                    (now, book_id, block_key, patch_id),
                )
            conn.execute(
                "UPDATE ocr_patches SET status = ?, updated_at = ?, revision = revision + 1 WHERE book_id = ? AND id = ?",
                (status, now, book_id, patch_id),
            )
            conn.execute("UPDATE books SET updated_at = ? WHERE id = ?", (now, book_id))
        return {"ok": True, "patch": self.get_patch(book_id, patch_id).get("patch")}

    def list_patches(self, book_id: str) -> dict[str, Any]:
        with self.repo.connect() as conn:
            exists = conn.execute("SELECT id FROM books WHERE id = ?", (book_id,)).fetchone()
            if not exists:
                return {"ok": False, "error": "Book not found"}
            rows = conn.execute(
                "SELECT * FROM ocr_patches WHERE book_id = ? ORDER BY page_no, block_key, updated_at",
                (book_id,),
            ).fetchall()
        return {"ok": True, "patches": [self._patch_dict(row) for row in rows]}

    def get_patch(self, book_id: str, patch_id: str) -> dict[str, Any]:
        with self.repo.connect() as conn:
            row = conn.execute("SELECT * FROM ocr_patches WHERE book_id = ? AND id = ?", (book_id, patch_id)).fetchone()
        if not row:
            return {"ok": False, "error": "Patch not found"}
        return {"ok": True, "patch": self._patch_dict(row)}

    def create_accepted_export(self, book_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        created_by = str(payload.get("createdBy") or "").strip()
        markdown = str(payload.get("markdown") or "")
        if not created_by:
            return {"ok": False, "error": "Missing createdBy"}
        if not markdown:
            return {"ok": False, "error": "Missing markdown"}
        export_permission = self._require_access(book_id=book_id, user_id=created_by, allowed={"owner", "editor"})
        if not export_permission.get("ok"):
            return export_permission

        now = _now_iso()
        export_id = str(uuid.uuid4())
        content = markdown.encode("utf-8")
        stored = self.storage.put_bytes(
            f"books/{book_id}/outputs/accepted-corrected-{now.replace(':', '').replace('-', '')}.md",
            content,
            "text/markdown; charset=utf-8",
        )
        metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
        with self.repo.connect() as conn:
            conn.execute(
                """
                INSERT INTO exports(id, book_id, export_type, storage_key, url, size_bytes, checksum, created_by, created_at, metadata_json)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    export_id,
                    book_id,
                    "accepted_markdown",
                    stored.key,
                    stored.url,
                    stored.size_bytes,
                    stored.checksum,
                    created_by,
                    now,
                    _json_dumps(metadata),
                ),
            )
            conn.execute("UPDATE books SET updated_at = ? WHERE id = ?", (now, book_id))
        return {
            "ok": True,
            "export": {
                "id": export_id,
                "bookId": book_id,
                "type": "accepted_markdown",
                "storageKey": stored.key,
                "url": stored.url,
                "sizeBytes": stored.size_bytes,
                "checksum": stored.checksum,
                "createdBy": created_by,
                "createdAt": now,
                "metadata": metadata,
            },
        }

    def upsert_book_user(self, book_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        actor_user_id = str(
            payload.get("actorUserId")
            or payload.get("updatedBy")
            or payload.get("createdBy")
            or ""
        ).strip()
        user_id = str(payload.get("userId") or "").strip()
        role = self._normalize_role(str(payload.get("role") or ""))
        if not actor_user_id:
            return {"ok": False, "error": "Missing actorUserId"}
        if not user_id:
            return {"ok": False, "error": "Missing userId"}
        if role not in BOOK_ROLES:
            return {"ok": False, "error": f"Unsupported role: {role}"}

        actor_check = self._require_access(book_id=book_id, user_id=actor_user_id, allowed={"owner"})
        if not actor_check.get("ok"):
            return actor_check
        now = _now_iso()
        with self.repo.connect() as conn:
            conn.execute(
                """
                INSERT INTO book_users(book_id, user_id, role, created_by, created_at)
                VALUES(?, ?, ?, ?, ?)
                ON CONFLICT(book_id, user_id) DO UPDATE SET
                    role = excluded.role,
                    created_by = excluded.created_by,
                    created_at = excluded.created_at
                """,
                (book_id, user_id, role, actor_user_id, now),
            )
        return {
            "ok": True,
            "participant": {
                "userId": user_id,
                "role": role,
                "createdBy": actor_user_id,
                "createdAt": now,
            },
        }

    def list_book_users(self, book_id: str) -> dict[str, Any]:
        with self.repo.connect() as conn:
            exists = conn.execute("SELECT id FROM books WHERE id = ?", (book_id,)).fetchone()
            if not exists:
                return {"ok": False, "error": "Book not found"}
            rows = conn.execute(
                "SELECT user_id, role, created_by, created_at FROM book_users WHERE book_id = ? ORDER BY created_at, user_id",
                (book_id,),
            ).fetchall()
        return {
            "ok": True,
            "bookId": book_id,
            "users": [self._participant_dict(row) for row in rows],
        }

    def _store_book_file(self, book_id: str, file_item: dict[str, Any], index: int, now: str) -> dict[str, Any]:
        file_type = str(file_item.get("fileType") or file_item.get("type") or "asset").strip()
        name = _slug(str(file_item.get("name") or f"{file_type}-{index}"), f"{file_type}-{index}")
        relative_path = self._safe_relative_path(
            str(
                file_item.get("relativePath")
                or file_item.get("webkitRelativePath")
                or file_item.get("path")
                or name
            )
        )
        mime_type, content = _file_bytes(file_item)
        stored = self.storage.put_bytes(f"books/{book_id}/source/{file_type}/{relative_path}", content, mime_type)
        return {
            "id": str(uuid.uuid4()),
            "bookId": book_id,
            "fileType": file_type,
            "name": name,
            "relativePath": relative_path,
            "mimeType": stored.mime_type,
            "storageKey": stored.key,
            "url": stored.url,
            "sizeBytes": stored.size_bytes,
            "checksum": stored.checksum,
            "createdAt": now,
        }

    def _require_owner(self, book_id: str, user_id: str) -> dict[str, Any]:
        with self.repo.connect() as conn:
            book = conn.execute("SELECT owner_user_id FROM books WHERE id = ?", (book_id,)).fetchone()
        if not book:
            return {"ok": False, "error": "Book not found"}
        if book["owner_user_id"] != user_id:
            return {"ok": False, "error": "Only the book owner can edit this book", "code": "not_book_owner"}
        return {"ok": True}

    def _require_access(self, book_id: str, user_id: str, allowed: set[str]) -> dict[str, Any]:
        if not user_id:
            return {"ok": False, "error": "Missing user id", "code": "missing_user"}
        with self.repo.connect() as conn:
            book = conn.execute("SELECT owner_user_id FROM books WHERE id = ?", (book_id,)).fetchone()
            if not book:
                return {"ok": False, "error": "Book not found"}
            owner_user_id = str(book["owner_user_id"] or "")
            if user_id == owner_user_id:
                return {"ok": True, "role": "owner"}
            participant = conn.execute(
                "SELECT role FROM book_users WHERE book_id = ? AND user_id = ?",
                (book_id, user_id),
            ).fetchone()
            if participant and self._normalize_role(participant["role"]) in allowed:
                return {"ok": True, "role": self._normalize_role(participant["role"])}
            return {
                "ok": False,
                "error": "Only authorized collaborators can edit this book",
                "code": "not_book_member",
            }

    @staticmethod
    def _optional_int(value: Any) -> int | None:
        if value in {None, ""}:
            return None
        return int(value)

    @staticmethod
    def _safe_relative_path(value: str) -> str:
        parts = [
            _slug(part, "item")
            for part in str(value).replace("\\", "/").split("/")
            if part and part not in {".", ".."}
        ]
        if not parts:
            return "item"
        return "/".join(parts)

    @staticmethod
    def _book_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "title": row["title"],
            "ownerUserId": row["owner_user_id"],
            "status": row["status"],
            "pageCount": row["page_count"],
            "currentPage": row["current_page"],
            "currentBlockKey": row["current_block_key"],
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
        }

    @staticmethod
    def _file_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "bookId": row["book_id"],
            "fileType": row["file_type"],
            "storageKey": row["storage_key"],
            "url": row["url"],
            "name": row["name"],
            "relativePath": row["relative_path"] or row["name"],
            "mimeType": row["mime_type"],
            "sizeBytes": row["size_bytes"],
            "checksum": row["checksum"],
            "createdAt": row["created_at"],
        }

    @staticmethod
    def _patch_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "patchId": row["id"],
            "bookId": row["book_id"],
            "pageNo": row["page_no"],
            "blockKey": row["block_key"],
            "blockId": row["block_key"],
            "status": row["status"],
            "source": row["source"],
            "oldHash": row["old_hash"],
            "oldText": row["old_text"],
            "newText": row["new_text"],
            "metadata": _json_loads(row["metadata_json"], {}),
            "createdBy": row["created_by"],
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
            "revision": row["revision"],
        }

    @staticmethod
    def _participant_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "userId": row["user_id"],
            "role": row["role"],
            "createdBy": row["created_by"],
            "createdAt": row["created_at"],
        }

    @staticmethod
    def _normalize_role(role: str) -> str:
        value = str(role or "").strip().lower()
        return value if value in BOOK_ROLES else "viewer"

    @staticmethod
    def _normalize_book_users(
        collaborators_payload: Any,
        owner_user_id: str,
    ) -> list[dict[str, str]]:
        if not isinstance(collaborators_payload, list):
            return []
        normalized: list[dict[str, str]] = []
        for item in collaborators_payload:
            if isinstance(item, str):
                user_id = item.strip()
                role = "viewer"
            elif isinstance(item, dict):
                user_id = str(item.get("userId") or item.get("user_id") or "").strip()
                role = OcrWorkbenchService._normalize_role(str(item.get("role") or ""))
            else:
                continue
            if not user_id:
                continue
            if user_id == owner_user_id:
                role = "owner"
            normalized.append({"user_id": user_id, "role": role})
        return normalized

    @staticmethod
    def _export_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "bookId": row["book_id"],
            "type": row["export_type"],
            "storageKey": row["storage_key"],
            "url": row["url"],
            "sizeBytes": row["size_bytes"],
            "checksum": row["checksum"],
            "createdBy": row["created_by"],
            "createdAt": row["created_at"],
            "metadata": _json_loads(row["metadata_json"], {}),
        }


OCR_WORKBENCH_SERVICE = OcrWorkbenchService()
