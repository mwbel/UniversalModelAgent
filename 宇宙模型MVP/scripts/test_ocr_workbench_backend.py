#!/usr/bin/env python3
from __future__ import annotations

import base64
import importlib
import os
import sys
import tempfile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


def data_url(mime: str, text: str) -> str:
    encoded = base64.b64encode(text.encode("utf-8")).decode("ascii")
    return f"data:{mime};base64,{encoded}"


with tempfile.TemporaryDirectory() as tmp_dir:
    os.environ["OCR_WORKBENCH_DB_PATH"] = os.path.join(tmp_dir, "workbench.sqlite3")
    os.environ["OCR_WORKBENCH_STORAGE_DIR"] = os.path.join(tmp_dir, "objects")
    os.environ["OCR_WORKBENCH_PUBLIC_BASE_URL"] = ""

    service_module = importlib.import_module("backend.services.ocr_workbench")
    service = service_module.OcrWorkbenchService()

    created = service.create_book(
        {
            "title": "Test Book",
            "ownerUserId": "owner-1",
            "pageCount": 2,
            "files": [
                {
                    "fileType": "middle_json",
                    "name": "book_middle.json",
                    "dataUrl": data_url("application/json", '{"pdf_info": []}'),
                },
                {
                    "fileType": "content_list",
                    "name": "content_list.json",
                    "relativePath": "chunks/part_0001_pages_0001-0070/auto/content_list.json",
                    "json": [{"page_idx": 0, "text": "A"}],
                },
            ],
        }
    )
    assert created["ok"], created
    book_id = created["book"]["id"]
    assert created["book"]["ownerUserId"] == "owner-1"
    assert len(created["files"]) == 2
    assert created["files"][0]["storageKey"].startswith(f"books/{book_id}/source/")
    assert created["files"][1]["relativePath"] == "chunks/part_0001_pages_0001-0070/auto/content_list.json"
    assert created["files"][1]["storageKey"].endswith("/chunks/part_0001_pages_0001-0070/auto/content_list.json")

    added_files = service.add_book_files(
        book_id,
        {
            "createdBy": "owner-1",
            "files": [
                {
                    "fileType": "asset",
                    "name": "note.txt",
                    "text": "late file",
                }
            ],
        },
    )
    assert added_files["ok"], added_files
    assert added_files["files"][0]["storageKey"].startswith(f"books/{book_id}/source/asset/")
    assert added_files["files"][0]["relativePath"] == "note.txt"

    restored_book = service.get_book(book_id)
    assert restored_book["ok"], restored_book
    restored_paths = [file["relativePath"] for file in restored_book["files"]]
    assert "chunks/part_0001_pages_0001-0070/auto/content_list.json" in restored_paths, restored_paths

    listed = service.list_books(owner_user_id="owner-1")
    assert listed["ok"], listed
    assert [book["id"] for book in listed["books"]] == [book_id]

    draft = service.save_patch(
        book_id,
        {
            "patchId": "patch-1",
            "blockKey": "p1:b1",
            "pageNo": 1,
            "status": "draft",
            "source": "human",
            "oldText": "E=mc2",
            "newText": "E = mc^2",
            "createdBy": "owner-1",
            "metadata": {"reason": "manual"},
        },
    )
    assert draft["ok"], draft
    assert draft["patch"]["status"] == "draft"

    denied = service.save_patch(
        book_id,
        {
            "patchId": "patch-denied",
            "blockKey": "p1:b2",
            "status": "draft",
            "source": "human",
            "newText": "no",
            "createdBy": "other-user",
        },
    )
    assert not denied["ok"], denied
    assert denied["code"] == "not_book_member"

    accepted = service.update_patch_status(book_id, "patch-1", {"status": "accepted", "updatedBy": "owner-1"})
    assert accepted["ok"], accepted
    assert accepted["patch"]["status"] == "accepted"

    replacement = service.save_patch(
        book_id,
        {
            "patchId": "patch-2",
            "blockKey": "p1:b1",
            "pageNo": 1,
            "status": "accepted",
            "source": "human",
            "oldText": "E=mc2",
            "newText": "E = mc^{2}",
            "createdBy": "owner-1",
        },
    )
    assert replacement["ok"], replacement
    patches = service.list_patches(book_id)
    assert patches["ok"], patches
    statuses = {patch["patchId"]: patch["status"] for patch in patches["patches"]}
    assert statuses["patch-1"] == "rejected", statuses
    assert statuses["patch-2"] == "accepted", statuses

    state = service.get_state(book_id)
    assert state["ok"], state
    assert len(state["ocrPatches"]) == 2

    exported = service.create_accepted_export(
        book_id,
        {
            "createdBy": "owner-1",
            "markdown": "# Accepted\n\nE = mc^{2}\n",
            "metadata": {"acceptedPatchCount": 1},
        },
    )
    assert exported["ok"], exported
    assert exported["export"]["storageKey"].startswith(f"books/{book_id}/outputs/")

print("ocr workbench backend tests ok")
