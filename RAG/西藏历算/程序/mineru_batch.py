#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import subprocess
import http.client
import json
import mimetypes
import os
import re
import shutil
import ssl
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import zipfile
from http.cookies import SimpleCookie
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_BASE_URL = "https://mineryou.cpolar.top"
STATE_FILENAME = ".mineru_batch_state.json"
TMP_DIRNAME = ".mineru_batch_tmp"
SKIP_DIR_NAMES = {"hybrid_auto", "done", "__MACOSX", TMP_DIRNAME, "chunks", "merged", "auto"}
SKIP_FILE_SUFFIXES = ("_origin.pdf", "_layout.pdf", "_span.pdf")
SUPPORTED_EXTENSIONS = {".pdf", ".epub", ".djvu"}
CHAPTER_HEADING_RE = re.compile(
    r"^\s{0,3}(?:#{1,6}\s*)?(?P<title>(?:第[0-9零一二三四五六七八九十百千万〇两IVXLCDMivxlcdm]+章\b.*)|(?:chapter\s+[0-9ivxlcdm]+\b.*))\s*$",
    re.IGNORECASE,
)
TOC_LIKE_HEADING_RE = re.compile(r"[.．。…·]{2,}.*\(\d+\)\s*$")
TRAILING_PAGE_RE = re.compile(r"[\(\（]\d+[\)\）]\s*$")
IMAGE_LINK_RE = re.compile(
    r"!\[([^\]]*)\]\((.+?\.(?:png|jpg|jpeg|gif|webp|bmp|svg))(?:\s+\"[^\"]*\")?\)",
    re.IGNORECASE,
)


@dataclass
class ProcessResult:
    pdf_path: Path
    status: str
    message: str


class MinerUClient:
    def __init__(self, base_url: str, timeout: float = 60.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._parsed = urllib.parse.urlparse(self.base_url)
        self.cookies: dict[str, str] = {}
        if self._parsed.scheme not in {"http", "https"}:
            raise ValueError(f"Unsupported URL scheme: {self._parsed.scheme}")

    def _connection(self) -> http.client.HTTPConnection:
        port = self._parsed.port
        host = self._parsed.hostname
        if not host:
            raise ValueError(f"Invalid base URL: {self.base_url}")
        if self._parsed.scheme == "https":
            return http.client.HTTPSConnection(host, port, timeout=self.timeout, context=ssl.create_default_context())
        return http.client.HTTPConnection(host, port, timeout=self.timeout)

    def _endpoint(self, path: str) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            parsed = urllib.parse.urlparse(path)
            return parsed.path + (f"?{parsed.query}" if parsed.query else "")
        base_path = self._parsed.path.rstrip("/")
        suffix = path if path.startswith("/") else f"/{path}"
        return f"{base_path}{suffix}" or "/"

    def _cookie_header(self) -> str | None:
        if not self.cookies:
            return None
        return "; ".join(f"{key}={value}" for key, value in self.cookies.items())

    def _update_cookies(self, response: http.client.HTTPResponse) -> None:
        raw_headers = response.msg.get_all("Set-Cookie", [])
        for raw in raw_headers:
            parsed = SimpleCookie()
            parsed.load(raw)
            for key, morsel in parsed.items():
                self.cookies[key] = morsel.value

    def _request(self, method: str, path: str, *, headers: dict[str, str] | None = None, body: bytes | None = None) -> tuple[http.client.HTTPResponse, bytes]:
        conn = self._connection()
        request_headers = dict(headers or {})
        cookie_header = self._cookie_header()
        if cookie_header:
            request_headers["Cookie"] = cookie_header
        try:
            conn.request(method, self._endpoint(path), body=body, headers=request_headers)
            response = conn.getresponse()
            payload = response.read()
            self._update_cookies(response)
        finally:
            conn.close()
        return response, payload

    def _json_request(self, method: str, path: str, *, headers: dict[str, str] | None = None, body: bytes | None = None) -> dict[str, Any]:
        response, payload = self._request(method, path, headers=headers, body=body)
        text = payload.decode("utf-8", errors="replace")
        if response.status >= 400:
            try:
                data = json.loads(text)
                message = data.get("detail") or data.get("message") or data.get("error") or text
            except json.JSONDecodeError:
                message = text or response.reason
            raise RuntimeError(f"{response.status} {response.reason}: {message}")

        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSON response from {path}: {text[:300]}") from exc

    def authenticate(self, username: str, password: str, *, register: bool = False) -> dict[str, Any]:
        endpoint = "/auth/register" if register else "/auth/login"
        payload = json.dumps({"username": username, "password": password}).encode("utf-8")
        return self._json_request("POST", endpoint, headers={"Content-Type": "application/json"}, body=payload)

    def submit_pdf(self, pdf_path: Path) -> dict[str, Any]:
        boundary = f"----MinerUBoundary{uuid.uuid4().hex}"
        mime_type = mimetypes.guess_type(pdf_path.name)[0] or "application/pdf"
        filename = pdf_path.name
        header = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
            f"Content-Type: {mime_type}\r\n\r\n"
        ).encode("utf-8")
        footer = f"\r\n--{boundary}--\r\n".encode("utf-8")

        conn = self._connection()
        cookie_header = self._cookie_header()
        try:
            conn.putrequest("POST", self._endpoint("/jobs/pdf"))
            conn.putheader("Content-Type", f"multipart/form-data; boundary={boundary}")
            conn.putheader("Content-Length", str(len(header) + pdf_path.stat().st_size + len(footer)))
            if cookie_header:
                conn.putheader("Cookie", cookie_header)
            conn.endheaders()
            conn.send(header)
            with pdf_path.open("rb") as handle:
                while True:
                    chunk = handle.read(1024 * 1024)
                    if not chunk:
                        break
                    conn.send(chunk)
            conn.send(footer)
            response = conn.getresponse()
            payload = response.read()
            self._update_cookies(response)
        finally:
            conn.close()

        text = payload.decode("utf-8", errors="replace")
        if response.status >= 400:
            try:
                data = json.loads(text)
                message = data.get("message") or data.get("error") or text
            except json.JSONDecodeError:
                message = text or response.reason
            raise RuntimeError(f"{response.status} {response.reason}: {message}")

        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid job response: {text[:300]}") from exc

    def get_job(self, task_id: str) -> dict[str, Any]:
        return self._json_request("GET", f"/jobs/{task_id}")

    def download(self, url: str, destination: Path) -> None:
        resolved = urllib.parse.urljoin(f"{self.base_url}/", url)
        request = urllib.request.Request(resolved, method="GET")
        cookie_header = self._cookie_header()
        if cookie_header:
            request.add_header("Cookie", cookie_header)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                with destination.open("wb") as handle:
                    shutil.copyfileobj(response, handle)
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Download failed: {exc}") from exc


class StateStore:
    def __init__(self, state_path: Path) -> None:
        self.state_path = state_path
        self.data = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.state_path.exists():
            return {"files": {}}
        try:
            return json.loads(self.state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"files": {}}

    def save(self) -> None:
        self.state_path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")

    def record(self, pdf_path: Path, status: str, message: str, *, task_id: str | None = None) -> None:
        files = self.data.setdefault("files", {})
        files[str(pdf_path)] = {
            "status": status,
            "message": message,
            "task_id": task_id,
            "updated_at": int(time.time()),
        }
        self.save()


def log(message: str) -> None:
    print(message, flush=True)


def find_source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if path.name.endswith(SKIP_FILE_SUFFIXES):
            continue
        files.append(path)
    return sorted(files)


def find_result_dirs(root: Path) -> list[Path]:
    result_dirs: set[Path] = set()
    for path in root.rglob("*.md"):
        if path.parent.name == "hybrid_auto":
            result_dirs.add(path.parent.parent)
        elif path.parent.name == "merged" and path.name.endswith("_完整.md"):
            result_dirs.add(path.parent.parent)
    return sorted(result_dirs)


def target_dir_for(source_path: Path) -> Path:
    return source_path.parent / source_path.stem


def result_markers_for(source_path: Path) -> list[Path]:
    target_dir = target_dir_for(source_path)
    return [
        target_dir / "hybrid_auto" / f"{source_path.stem}.md",
        target_dir / "merged" / "parse_manifest.json",
        target_dir / "merged",
        target_dir / "pandoc_epub" / f"{source_path.stem}.md",
    ]


def has_existing_result(source_path: Path) -> bool:
    return any(marker.exists() for marker in result_markers_for(source_path))


def first_existing_marker(source_path: Path) -> Path | None:
    for marker in result_markers_for(source_path):
        if marker.exists():
            return marker
    return None


def safe_rmtree(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|]+', "_", name).strip().strip(".")
    return cleaned or "untitled"


def is_toc_like_heading(title: str) -> bool:
    compact = title.replace(" ", "")
    return bool(TOC_LIKE_HEADING_RE.search(compact) or TRAILING_PAGE_RE.search(compact))


def find_chapter_breaks(lines: list[str]) -> list[tuple[int, str]]:
    breaks: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = CHAPTER_HEADING_RE.match(line)
        if not match:
            continue
        title = match.group("title").strip()
        if is_toc_like_heading(title):
            continue
        breaks.append((index, title))
    return breaks


def chapter_output_dir(markdown_path: Path) -> Path:
    if markdown_path.parent.name == "merged" and markdown_path.stem.endswith("_完整"):
        return markdown_path.parent / f"{markdown_path.stem[:-3]}_chapters"
    return markdown_path.parent / f"{markdown_path.stem}_chapters"


def write_chapters_index(markdown_path: Path, output_dir: Path, chapter_files: list[Path]) -> None:
    relative_source = os_path_rel(markdown_path, output_dir)
    lines = [
        "# Chapters Index",
        "",
        f"- Source Markdown: [{markdown_path.name}]({relative_source})",
        f"- Chapter Count: {len(chapter_files)}",
        "",
        "## Chapters",
        "",
    ]

    for index, chapter_file in enumerate(chapter_files, start=1):
        title = chapter_file.stem.split("_", 1)[1] if "_" in chapter_file.stem else chapter_file.stem
        relative_chapter = os_path_rel(chapter_file, output_dir)
        lines.append(f"{index}. [{title}]({relative_chapter})")

    lines.append("")
    (output_dir / "chapters_index.md").write_text("\n".join(lines), encoding="utf-8")


def os_path_rel(path: Path, start: Path) -> str:
    return str(path.relative_to(start) if path.is_relative_to(start) else Path(os.path.relpath(path, start))).replace("\\", "/")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def collect_merged_image_links(markdown_path: Path, merged_dir: Path, copied: dict[Path, str]) -> int:
    if not markdown_path.exists():
        return 0

    original = markdown_path.read_text(encoding="utf-8", errors="ignore")
    changed = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        alt_text = match.group(1)
        raw_target = normalize_link_target(match.group(2))
        if raw_target.startswith(("http://", "https://", "data:")):
            return match.group(0)

        source_path = (markdown_path.parent / raw_target).resolve()
        if not source_path.exists() or "images" not in source_path.parts:
            return match.group(0)

        copied.setdefault(source_path, source_path.name)
        if markdown_path.parent == merged_dir:
            new_target = f"images/{source_path.name}"
        else:
            new_target = f"../images/{source_path.name}"
        changed += 1
        return f"![{alt_text}]({new_target})"

    updated = IMAGE_LINK_RE.sub(replace, original)
    if updated != original:
        markdown_path.write_text(updated, encoding="utf-8")
    return changed


def materialize_merged_images(merged_dir: Path) -> tuple[int, int]:
    if not merged_dir.exists():
        return 0, 0

    copied: dict[Path, str] = {}
    rewritten = 0
    markdown_files = sorted(merged_dir.glob("*_完整.md"))
    for chapter_dir in sorted(path for path in merged_dir.iterdir() if path.is_dir() and path.name.endswith("_chapters")):
        markdown_files.extend(sorted(path for path in chapter_dir.glob("*.md") if path.name != "chapters_index.md"))

    for markdown_path in markdown_files:
        rewritten += collect_merged_image_links(markdown_path, merged_dir, copied)

    if not copied:
        return rewritten, 0

    images_dir = merged_dir / "images"
    images_dir.mkdir(exist_ok=True)
    copied_count = 0
    for source_path, filename in copied.items():
        destination_path = images_dir / filename
        if not destination_path.exists():
            shutil.copy2(source_path, destination_path)
            copied_count += 1
    return rewritten, copied_count


def split_markdown_into_chapters(markdown_path: Path) -> int:
    if not markdown_path.exists():
        return 0

    text = markdown_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    breaks = find_chapter_breaks(lines)
    output_dir = chapter_output_dir(markdown_path)

    if output_dir.exists():
        safe_rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sections: list[tuple[str, list[str]]] = []
    if not breaks:
        sections.append(("完整文档", lines))
    else:
        first_index = breaks[0][0]
        preface = lines[:first_index]
        if any(line.strip() for line in preface):
            sections.append(("前置内容", preface))

        for i, (start_index, title) in enumerate(breaks):
            end_index = breaks[i + 1][0] if i + 1 < len(breaks) else len(lines)
            section_lines = lines[start_index:end_index]
            if any(line.strip() for line in section_lines):
                sections.append((title, section_lines))

    for index, (title, section_lines) in enumerate(sections, start=1):
        filename = f"{index:03d}_{sanitize_filename(title)[:80]}.md"
        body = "\n".join(section_lines).strip() + "\n"
        (output_dir / filename).write_text(body, encoding="utf-8")

    chapter_files = sorted(output_dir.glob("*.md"))
    write_chapters_index(markdown_path, output_dir, chapter_files)
    return len(sections)


def update_parse_manifest(result_dir: Path, chapter_count: int) -> None:
    manifest_path = result_dir / "merged" / "parse_manifest.json"
    merged_dir = result_dir / "merged"
    if not manifest_path.exists() or not merged_dir.exists():
        return

    complete_markdowns = sorted(merged_dir.glob("*_完整.md"))
    if not complete_markdowns:
        return

    markdown_path = complete_markdowns[0]
    chapters_dir = chapter_output_dir(markdown_path)
    chapter_files = sorted(chapters_dir.glob("*.md"))
    if not chapter_files:
        return

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    if not isinstance(data, list) or not data:
        return

    chapter_items = []
    for index, chapter_file in enumerate(chapter_files, start=1):
        chapter_items.append(
            {
                "index": index,
                "title": chapter_file.stem.split("_", 1)[1] if "_" in chapter_file.stem else chapter_file.stem,
                "markdown": str(chapter_file.relative_to(result_dir)).replace("\\", "/"),
            }
        )

    if isinstance(data[0], dict):
        data[0]["chapters"] = chapter_items
        data[0]["chapter_count"] = chapter_count
        manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def split_result_markdowns(result_dir: Path) -> list[str]:
    messages: list[str] = []

    hybrid_md = result_dir / "hybrid_auto" / f"{result_dir.name}.md"
    if hybrid_md.exists():
        count = split_markdown_into_chapters(hybrid_md)
        messages.append(f"hybrid_auto 拆成 {count} 个章节文件")

    merged_dir = result_dir / "merged"
    if merged_dir.exists():
        complete_markdowns = sorted(merged_dir.glob("*_完整.md"))
        for markdown_path in complete_markdowns:
            count = split_markdown_into_chapters(markdown_path)
            update_parse_manifest(result_dir, count)
            messages.append(f"{markdown_path.name} 拆成 {count} 个章节文件")
        rewritten, copied = materialize_merged_images(merged_dir)
        if rewritten or copied:
            messages.append(f"merged 图片已整理：重写 {rewritten} 处，复制 {copied} 张")

    pandoc_dir = result_dir / "pandoc_epub"
    if pandoc_dir.exists():
        direct_markdowns = sorted(pandoc_dir.glob("*.md"))
        for markdown_path in direct_markdowns:
            if markdown_path.name == "chapters_index.md":
                continue
            count = split_markdown_into_chapters(markdown_path)
            messages.append(f"{markdown_path.name} 拆成 {count} 个章节文件")

    return messages


def process_existing_result_dir(result_dir: Path) -> ProcessResult:
    split_messages = split_result_markdowns(result_dir)
    if split_messages:
        return ProcessResult(result_dir, "completed", f"已拆章: {result_dir}；{'；'.join(split_messages)}")
    return ProcessResult(result_dir, "skipped", f"未找到可拆章的主 Markdown: {result_dir}")


def convert_epub_to_markdown(epub_path: Path, *, force: bool, dry_run: bool) -> ProcessResult:
    result_dir = target_dir_for(epub_path)
    output_dir = result_dir / "pandoc_epub"
    output_md = output_dir / f"{epub_path.stem}.md"
    existing_marker = first_existing_marker(epub_path)

    if existing_marker and not force:
        split_messages = split_result_markdowns(result_dir)
        suffix = f"；{'；'.join(split_messages)}" if split_messages else ""
        return ProcessResult(epub_path, "skipped", f"已有结果，跳过: {existing_marker}{suffix}")

    if dry_run:
        return ProcessResult(epub_path, "dry-run", f"将用 pandoc 处理并输出到: {output_md}")

    output_dir.mkdir(parents=True, exist_ok=True)
    command = ["pandoc", str(epub_path), "-t", "gfm", "-o", str(output_md)]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        split_messages = split_result_markdowns(result_dir)
        suffix = f"；{'；'.join(split_messages)}" if split_messages else ""
        return ProcessResult(epub_path, "completed", f"完成: {output_md}{suffix}")
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or exc.stdout.strip() or "pandoc 转换失败"
        return ProcessResult(epub_path, "failed", message)


def process_djvu(djvu_path: Path, *, dry_run: bool) -> ProcessResult:
    if dry_run:
        return ProcessResult(djvu_path, "dry-run", "检测到 DJVU，目前本机未安装可用转换器，执行时会跳过")
    return ProcessResult(djvu_path, "failed", "DJVU 暂不支持：本机未找到 ddjvu/djvutopdf 等转换工具")


def extract_zip_to_target(zip_path: Path, pdf_path: Path, *, force: bool) -> Path:
    target_dir = target_dir_for(pdf_path)
    parent_dir = pdf_path.parent

    with tempfile.TemporaryDirectory(prefix="mineru_extract_", dir=str(parent_dir)) as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        with zipfile.ZipFile(zip_path) as archive:
            archive.extractall(temp_dir)

        extracted_entries = [entry for entry in temp_dir.iterdir() if entry.name != "__MACOSX"]
        if target_dir.exists():
            if not force:
                raise RuntimeError(f"Target directory already exists: {target_dir}")
            safe_rmtree(target_dir)

        if len(extracted_entries) == 1 and extracted_entries[0].is_dir():
            extracted_root = extracted_entries[0]
            if extracted_root.name == target_dir.name:
                extracted_root.rename(target_dir)
                return target_dir

            target_dir.mkdir(parents=True, exist_ok=True)
            for child in extracted_root.iterdir():
                shutil.move(str(child), str(target_dir / child.name))
            return target_dir

        target_dir.mkdir(parents=True, exist_ok=True)
        for entry in extracted_entries:
            destination = target_dir / entry.name
            if destination.exists():
                if destination.is_dir():
                    safe_rmtree(destination)
                else:
                    destination.unlink()
            shutil.move(str(entry), str(destination))
        return target_dir


def poll_until_complete(client: MinerUClient, task_id: str, *, interval: float) -> dict[str, Any]:
    while True:
        job = client.get_job(task_id)
        status = str(job.get("status", "unknown"))
        progress = job.get("progress", 0)
        message = str(job.get("message", ""))
        current_file = str(job.get("current_file") or "")
        suffix = f" | {current_file}" if current_file else ""
        log(f"    [{status:9}] {progress:>3}% {message}{suffix}")

        if status == "completed":
            return job
        if status == "failed":
            raise RuntimeError(str(job.get("error") or job.get("message") or "MinerU job failed"))
        time.sleep(interval)


def process_pdf(
    client: MinerUClient,
    pdf_path: Path,
    state: StateStore,
    *,
    interval: float,
    force: bool,
    keep_zip: bool,
    dry_run: bool,
) -> ProcessResult:
    result_dir = target_dir_for(pdf_path)
    existing_marker = first_existing_marker(pdf_path)

    if existing_marker and not force:
        split_messages = split_result_markdowns(result_dir)
        suffix = f"；{'；'.join(split_messages)}" if split_messages else ""
        return ProcessResult(pdf_path, "skipped", f"已有结果，跳过: {existing_marker}{suffix}")

    if dry_run:
        return ProcessResult(pdf_path, "dry-run", f"将处理并输出到: {result_dir}")

    tmp_dir = pdf_path.parent / TMP_DIRNAME
    tmp_dir.mkdir(exist_ok=True)
    zip_path = tmp_dir / f"{pdf_path.stem}.zip"

    try:
        log(f"  上传: {pdf_path.name}")
        state.record(pdf_path, "uploading", "正在上传")
        job = client.submit_pdf(pdf_path)
        task_id = str(job["task_id"])
        state.record(pdf_path, "running", "任务已创建", task_id=task_id)
        log(f"  任务: {task_id}")

        final_job = poll_until_complete(client, task_id, interval=interval)
        download_url = final_job.get("download_url")
        if not download_url:
            raise RuntimeError("任务完成后未返回 download_url")

        log("  下载 ZIP")
        client.download(str(download_url), zip_path)

        log("  解压结果")
        extract_zip_to_target(zip_path, pdf_path, force=force)
        split_messages = split_result_markdowns(result_dir)
        state.record(pdf_path, "completed", f"完成: {result_dir}", task_id=task_id)
        suffix = f"；{'；'.join(split_messages)}" if split_messages else ""
        return ProcessResult(pdf_path, "completed", f"完成: {result_dir}{suffix}")
    except Exception as exc:
        state.record(pdf_path, "failed", str(exc))
        return ProcessResult(pdf_path, "failed", str(exc))
    finally:
        if zip_path.exists() and not keep_zip:
            zip_path.unlink()
        if tmp_dir.exists() and not any(tmp_dir.iterdir()):
            tmp_dir.rmdir()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="批量调用 MinerU 服务，把 PDF 逐个转成 Markdown 结果目录。")
    parser.add_argument("--root", default=".", help="递归扫描 PDF 的根目录，默认当前目录")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="MinerU 服务地址")
    parser.add_argument("--username", default=os.environ.get("MINERU_USERNAME", ""), help="MinerU 用户名，也可用环境变量 MINERU_USERNAME")
    parser.add_argument("--password", default=os.environ.get("MINERU_PASSWORD", ""), help="MinerU 密码，也可用环境变量 MINERU_PASSWORD")
    parser.add_argument("--register", action="store_true", help="如果账号不存在，则先注册再登录")
    parser.add_argument("--interval", type=float, default=2.0, help="轮询任务状态的间隔秒数")
    parser.add_argument("--timeout", type=float, default=120.0, help="HTTP 超时秒数")
    parser.add_argument("--limit", type=int, default=0, help="最多处理多少本，0 表示不限制")
    parser.add_argument("--match", default="", help="只处理路径中包含该文本的 PDF")
    parser.add_argument("--force", action="store_true", help="即使已有结果目录，也重新下载并覆盖")
    parser.add_argument("--keep-zip", action="store_true", help="保留下载到临时目录的 ZIP 文件")
    parser.add_argument("--dry-run", action="store_true", help="只列出将要处理的 PDF，不真正上传")
    parser.add_argument("--split-existing-results", action="store_true", help="不上传 PDF，只对现有解析结果补拆章节")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        log(f"根目录不存在: {root}")
        return 1

    state = StateStore(root / STATE_FILENAME)
    client = MinerUClient(args.base_url, timeout=args.timeout)

    results: list[ProcessResult] = []
    log(f"根目录: {root}")

    if args.split_existing_results:
        result_dirs = find_result_dirs(root)
        if args.match:
            result_dirs = [path for path in result_dirs if args.match in str(path)]
        if args.limit > 0:
            result_dirs = result_dirs[: args.limit]
        if not result_dirs:
            log("没有找到可拆章的解析结果目录。")
            return 0

        log(f"待拆章结果目录数量: {len(result_dirs)}")
        for index, result_dir in enumerate(result_dirs, start=1):
            log("")
            log(f"[{index}/{len(result_dirs)}] {result_dir}")
            result = process_existing_result_dir(result_dir)
            results.append(result)
            log(f"  结果: {result.status} | {result.message}")
    else:
        files = find_source_files(root)
        if args.match:
            files = [path for path in files if args.match in str(path)]
        if args.limit > 0:
            files = files[: args.limit]

        if not files:
            log("没有找到可处理的源文件。")
            return 0

        need_auth = (not args.dry_run) and any(path.suffix.lower() == ".pdf" for path in files)
        if need_auth:
            if not args.username or not args.password:
                log("存在 PDF 需要走 MinerU 服务，但未提供账号密码。请使用 --username/--password 或环境变量 MINERU_USERNAME/MINERU_PASSWORD。")
                return 1
            auth_data = client.authenticate(args.username, args.password, register=args.register)
            user = auth_data.get("user", {})
            log(f"已登录用户: {user.get('username', args.username)}")

        log(f"服务地址: {args.base_url}")
        log(f"待处理源文件数量: {len(files)}")

        for index, source_path in enumerate(files, start=1):
            log("")
            log(f"[{index}/{len(files)}] {source_path}")
            suffix = source_path.suffix.lower()
            if suffix == ".pdf":
                result = process_pdf(
                    client,
                    source_path,
                    state,
                    interval=args.interval,
                    force=args.force,
                    keep_zip=args.keep_zip,
                    dry_run=args.dry_run,
                )
            elif suffix == ".epub":
                result = convert_epub_to_markdown(source_path, force=args.force, dry_run=args.dry_run)
            elif suffix == ".djvu":
                result = process_djvu(source_path, dry_run=args.dry_run)
            else:
                result = ProcessResult(source_path, "skipped", f"暂不支持的格式: {suffix}")
            results.append(result)
            log(f"  结果: {result.status} | {result.message}")

    completed = sum(1 for item in results if item.status == "completed")
    skipped = sum(1 for item in results if item.status == "skipped")
    failed = sum(1 for item in results if item.status == "failed")
    dry_run = sum(1 for item in results if item.status == "dry-run")

    log("")
    log("处理结束")
    log(f"  完成: {completed}")
    log(f"  跳过: {skipped}")
    log(f"  失败: {failed}")
    log(f"  预演: {dry_run}")

    if failed:
        log("")
        log("失败列表:")
        for item in results:
            if item.status == "failed":
                log(f"  - {item.pdf_path}: {item.message}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
