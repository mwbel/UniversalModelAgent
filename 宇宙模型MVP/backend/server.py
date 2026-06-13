from __future__ import annotations

import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from backend.catalog import VISUALIZATIONS
from backend.config import SETTINGS
from backend.services.chat_service import CHAT_SERVICE
from backend.services.ephemeris_compare import compare_ephemeris
from backend.services.mineru_client import MINERU_CLIENT
from backend.services.markdown_library import MARKDOWN_LIBRARY
from backend.services.model_tester import MODEL_TESTER_SERVICE
from backend.services.ocr_correction import OCR_CORRECTION_SERVICE
from backend.services.rag_client import RAG_CLIENT
from backend.services.visualization_planner import VISUALIZATION_PLANNER

ROOT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT_DIR / "frontend"


class AppHandler(BaseHTTPRequestHandler):
    server_version = "UniverseModelHTTP/0.1"

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(HTTPStatus.NO_CONTENT)
        self._send_cors_headers()
        self.end_headers()

    def do_HEAD(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
          self.send_response(HTTPStatus.OK)
          self._send_cors_headers()
          self.end_headers()
          return
        self._serve_static(parsed.path, head_only=True)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        if parsed.path == "/api/health":
            self._send_json(
                {
                    "ok": True,
                    "appName": SETTINGS.app_name,
                    "mineruBaseUrl": SETTINGS.mineru_base_url,
                    "ragBaseUrl": SETTINGS.rag_base_url,
                }
            )
            return
        if parsed.path == "/api/config":
            self._send_json(SETTINGS.public_dict())
            return
        if parsed.path == "/api/model-tester/config":
            self._send_json(MODEL_TESTER_SERVICE.config())
            return
        if parsed.path == "/api/library/config":
            self._send_json({"ok": True, **MARKDOWN_LIBRARY.config()})
            return
        if parsed.path == "/api/library/categories":
            self._send_json(MARKDOWN_LIBRARY.list_categories())
            return
        if parsed.path == "/api/library/documents":
            category = (query.get("category") or [None])[0]
            limit = int((query.get("limit") or ["200"])[0])
            offset = int((query.get("offset") or ["0"])[0])
            self._send_json(MARKDOWN_LIBRARY.list_documents(category=category, limit=limit, offset=offset))
            return
        if parsed.path == "/api/visualizations":
            self._send_json({"items": VISUALIZATIONS})
            return
        if parsed.path == "/api/visualizations/plan":
            question = (query.get("question") or [""])[0]
            self._send_json({"items": VISUALIZATION_PLANNER.plan(question=question)})
            return
        if parsed.path == "/api/rag/strategies":
            self._send_json(RAG_CLIENT.get_strategies())
            return
        if parsed.path == "/api/rag/kbs":
            self._send_json(RAG_CLIENT.get_knowledge_bases())
            return
        if parsed.path == "/api/ephemeris/compare":
            include_orbits = ((query.get("includeOrbits") or ["0"])[0]).lower() in {"1", "true", "yes"}
            self._send_json(
                compare_ephemeris(
                    date=(query.get("date") or [None])[0],
                    bodies=(query.get("bodies") or [None])[0],
                    tolerance=(query.get("tolerance") or [None])[0],
                    tolerance_unit=(query.get("toleranceUnit") or [None])[0],
                    include_orbits=include_orbits,
                )
            )
            return
        self._serve_static(parsed.path)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/rag/upload":
            raw_body = self._read_body()
            content_type = self.headers.get("Content-Type", "")
            self._send_json(RAG_CLIENT.upload_document(raw_body, content_type))
            return

        payload = self._read_json()
        if parsed.path == "/api/chat":
            result = CHAT_SERVICE.ask(
                question=str(payload.get("question", "")).strip(),
                history=payload.get("history", []),
                variant=payload.get("ragVariant"),
                kb_id=payload.get("kbId"),
                use_rag=bool(payload.get("useRag")),
            )
            self._send_json(result)
            return
        if parsed.path == "/api/model-tester/models":
            self._send_json(MODEL_TESTER_SERVICE.list_models(payload))
            return
        if parsed.path == "/api/model-tester/upload":
            self._send_json(MODEL_TESTER_SERVICE.upload_attachment(payload))
            return
        if parsed.path == "/api/model-tester/chat":
            self._send_json(MODEL_TESTER_SERVICE.chat(payload))
            return
        if parsed.path == "/api/ocr/convert":
            self._send_json(MINERU_CLIENT.convert_markdown(payload))
            return
        if parsed.path == "/api/ocr/correct":
            self._send_json(OCR_CORRECTION_SERVICE.correct_markdown(payload))
            return
        if parsed.path == "/api/ocr/convert-and-correct":
            self._send_json(OCR_CORRECTION_SERVICE.convert_and_correct(payload))
            return
        if parsed.path == "/api/library/ingest":
            try:
                documents = MARKDOWN_LIBRARY.read_documents(
                    category=payload.get("category"),
                    document_ids=payload.get("documentIds") if isinstance(payload.get("documentIds"), list) else None,
                    relative_paths=payload.get("relativePaths") if isinstance(payload.get("relativePaths"), list) else None,
                    limit=int(payload["limit"]) if payload.get("limit") else None,
                )
            except ValueError as error:
                self._send_json({"ok": False, "error": str(error)})
                return
            if payload.get("dryRun"):
                self._send_json(
                    {
                        "ok": True,
                        "dryRun": True,
                        "kbId": payload.get("kbId") or SETTINGS.default_kb_id,
                        "documents": len(documents),
                        "items": [
                            {
                                "id": item.get("id"),
                                "filename": item.get("filename"),
                                "metadata": item.get("metadata"),
                                "chars": len(str(item.get("text") or "")),
                            }
                            for item in documents[:20]
                        ],
                    }
                )
                return
            self._send_json(
                RAG_CLIENT.ingest_markdown_documents(
                    kb_id=str(payload.get("kbId") or SETTINGS.default_kb_id),
                    documents=documents,
                    replace=payload.get("replace", True) is not False,
                )
            )
            return
        self._send_json({"ok": False, "error": "Not found"}, status=HTTPStatus.NOT_FOUND)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return

    def _read_json(self) -> dict:
        raw = self._read_body().decode("utf-8")
        if not raw.strip():
            return {}
        return json.loads(raw)

    def _read_body(self) -> bytes:
        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length <= 0:
            return b""
        return self.rfile.read(content_length)

    def _send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(body)

    def _send_cors_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def _serve_static(self, path: str, head_only: bool = False) -> None:
        relative_path = "index.html" if path in {"", "/"} else path.lstrip("/")
        file_path = (FRONTEND_DIR / relative_path).resolve()
        if FRONTEND_DIR not in file_path.parents and file_path != FRONTEND_DIR:
            self._send_json({"ok": False, "error": "Forbidden"}, status=HTTPStatus.FORBIDDEN)
            return
        if file_path.is_dir():
            file_path = file_path / "index.html"
        if not file_path.exists():
            self._send_json({"ok": False, "error": "Not found"}, status=HTTPStatus.NOT_FOUND)
            return

        content = file_path.read_bytes()
        content_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if not head_only:
            self.wfile.write(content)


def run() -> None:
    server = ThreadingHTTPServer((SETTINGS.host, SETTINGS.port), AppHandler)
    print(f"Universe Model Agent server running at http://{SETTINGS.host}:{SETTINGS.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
