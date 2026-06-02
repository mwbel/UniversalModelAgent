"""下载管理模块"""

import os
import time
import requests
from pathlib import Path
from typing import Optional
from tqdm import tqdm
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode


class Downloader:
    """下载管理器"""

    def __init__(self, config):
        self.config = config
        self.download_dir = Path(config.download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = config.timeout
        self.retry_times = config.retry_times
        self.retry_delay = config.get('download.retry_delay', 2)
        self.chunk_size = config.get('download.chunk_size', 8192)
        self.user_agents = config.get('user_agents', ['Mozilla/5.0'])
        self.session = requests.Session()

    def download(self, url: str, filename: str, category: str = None) -> Optional[str]:
        """下载文件"""
        if not url:
            print("  ✗ 下载失败: 缺少下载链接")
            return None

        try:
            # 创建分类目录
            if category:
                save_dir = self.download_dir / self._sanitize_filename(category)
            else:
                save_dir = self.download_dir / "未分类"

            save_dir.mkdir(parents=True, exist_ok=True)

            # 完整文件路径
            file_path = save_dir / self._sanitize_filename(filename)

            # 检查文件是否已存在
            if file_path.exists():
                print(f"  文件已存在: {file_path.name}")
                return str(file_path)

            for attempt in range(1, self.retry_times + 1):
                print(f"  下载: {filename} (尝试 {attempt}/{self.retry_times})")

                try:
                    total_size = 0
                    temp_path = file_path.with_suffix(file_path.suffix + '.part')

                    for request_url, headers in self._build_request_variants(url):
                        if temp_path.exists():
                            temp_path.unlink()

                        with self.session.get(
                            request_url,
                            stream=True,
                            timeout=self.timeout,
                            headers=headers,
                            allow_redirects=True
                        ) as response:
                            if response.status_code != 200:
                                raise requests.HTTPError(f"HTTP {response.status_code}")

                            total_size = int(response.headers.get('content-length', 0))

                            with open(temp_path, 'wb') as f, tqdm(
                                total=total_size,
                                unit='B',
                                unit_scale=True,
                                desc=f"  {filename[:30]}"
                            ) as pbar:
                                for chunk in response.iter_content(chunk_size=self.chunk_size):
                                    if chunk:
                                        f.write(chunk)
                                        pbar.update(len(chunk))

                        temp_path.replace(file_path)
                        print(f"  ✓ 下载完成: {file_path}")
                        return str(file_path)

                except Exception as e:
                    temp_path = file_path.with_suffix(file_path.suffix + '.part')
                    if temp_path.exists():
                        temp_path.unlink()

                    if attempt >= self.retry_times:
                        print(f"  ✗ 下载失败: {e}")
                        return None

                    print(f"  下载重试: {e}")
                    time.sleep(self.retry_delay)

        except Exception as e:
            print(f"  ✗ 下载失败: {e}")
            return None

    def _base_headers(self) -> dict:
        """构建基础请求头"""
        user_agent = self.user_agents[0] if self.user_agents else 'Mozilla/5.0'
        return {
            'User-Agent': user_agent,
            'Accept': 'application/pdf,application/epub+zip,application/octet-stream,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8',
            'Connection': 'close',
        }

    def _build_request_variants(self, url: str) -> list:
        """为容易失败的源站构建多种请求方式"""
        variants = []
        seen = set()

        def add_variant(request_url: str, extra_headers: dict = None):
            headers = self._base_headers()
            if extra_headers:
                headers.update(extra_headers)
            key = (request_url, tuple(sorted(headers.items())))
            if key not in seen:
                seen.add(key)
                variants.append((request_url, headers))

        add_variant(url)

        parsed = urlparse(url)
        host = parsed.netloc.lower()

        if 'archive.org' in host:
            identifier = self._extract_archive_identifier(parsed.path)
            details_url = f'https://archive.org/details/{identifier}' if identifier else 'https://archive.org/'
            add_variant(url, {
                'Referer': details_url,
                'Origin': 'https://archive.org',
            })
            add_variant(self._append_query_flag(url, 'download', '1'), {
                'Referer': details_url,
                'Origin': 'https://archive.org',
            })

        if 'researchgate.net' in host:
            publication_url = url.split('/links/', 1)[0] if '/links/' in url else 'https://www.researchgate.net/'
            add_variant(url, {
                'Referer': publication_url,
                'Origin': 'https://www.researchgate.net',
            })

        return variants

    def _append_query_flag(self, url: str, key: str, value: str) -> str:
        """在下载链接上追加查询参数"""
        parsed = urlparse(url)
        query = dict(parse_qsl(parsed.query, keep_blank_values=True))
        query[key] = value
        return urlunparse(parsed._replace(query=urlencode(query)))

    def _extract_archive_identifier(self, path: str) -> str:
        """从 archive.org 下载路径中提取馆藏标识"""
        parts = [segment for segment in path.split('/') if segment]
        if len(parts) >= 2 and parts[0] == 'download':
            return parts[1]
        return ''

    def _sanitize_filename(self, filename: str) -> str:
        """清理文件名中的非法字符"""
        # 移除或替换非法字符
        illegal_chars = '<>:"/\\|?*'
        for char in illegal_chars:
            filename = filename.replace(char, '_')

        # 限制长度
        max_length = self.config.get('naming.max_filename_length', 200)
        if len(filename) > max_length:
            name, ext = os.path.splitext(filename)
            filename = name[:max_length-len(ext)] + ext

        return filename
