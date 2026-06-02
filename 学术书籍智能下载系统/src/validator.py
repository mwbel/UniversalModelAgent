"""文件验证模块"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
import re
import zipfile


@dataclass
class ValidationResult:
    """单个文件的验证结果"""

    file_path: str
    is_valid: bool
    file_format: Optional[str] = None
    file_size: int = 0
    page_count: Optional[int] = None
    first_page_text: str = ''
    metadata: Dict[str, str] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """转换为普通字典，便于报告导出"""
        return {
            'file_path': self.file_path,
            'is_valid': self.is_valid,
            'file_format': self.file_format,
            'file_size': self.file_size,
            'page_count': self.page_count,
            'first_page_text': self.first_page_text,
            'metadata': self.metadata,
            'warnings': '; '.join(self.warnings),
            'errors': '; '.join(self.errors),
        }


class FileValidator:
    """下载文件验证器"""

    def __init__(self, config):
        self.config = config
        self.min_file_size = config.get('validation.min_file_size', 102400)
        self.max_file_size = config.get('validation.max_file_size', 524288000)
        self.allowed_formats = {
            fmt.lower().lstrip('.')
            for fmt in config.get('validation.allowed_formats', ['pdf', 'epub', 'djvu'])
        }
        self.first_page_min_title_similarity = config.get(
            'validation.first_page_min_title_similarity',
            0.2
        )
        self.first_page_min_author_similarity = config.get(
            'validation.first_page_min_author_similarity',
            0.2
        )

    def validate(self, file_path: str, expected_title: str = None,
                 expected_author: str = None) -> ValidationResult:
        """验证单个文件"""
        path = Path(file_path) if file_path else None
        result = ValidationResult(
            file_path=str(path) if path else '',
            is_valid=False
        )

        if not path:
            result.errors.append('文件路径为空')
            return result

        if not path.exists():
            result.errors.append('文件不存在')
            return result

        if not path.is_file():
            result.errors.append('路径不是文件')
            return result

        result.file_format = path.suffix.lower().lstrip('.')
        result.file_size = path.stat().st_size

        self._validate_size(result)
        self._validate_format(result)

        if result.file_format == 'pdf':
            self._validate_pdf(path, result, expected_title, expected_author)
        elif result.file_format == 'epub':
            self._validate_epub(path, result)
        elif result.file_format == 'djvu':
            self._validate_djvu(path, result)

        result.is_valid = not result.errors
        return result

    def _validate_size(self, result: ValidationResult):
        """验证文件大小"""
        if result.file_size <= 0:
            result.errors.append('文件为空')
        elif result.file_size < self.min_file_size:
            result.errors.append(
                f"文件过小 ({self.human_size(result.file_size)} < {self.human_size(self.min_file_size)})"
            )
        elif result.file_size > self.max_file_size:
            result.errors.append(
                f"文件过大 ({self.human_size(result.file_size)} > {self.human_size(self.max_file_size)})"
            )

    def _validate_format(self, result: ValidationResult):
        """验证文件扩展名"""
        if not result.file_format:
            result.errors.append('文件缺少扩展名')
        elif result.file_format not in self.allowed_formats:
            result.errors.append(f"不支持的文件格式: {result.file_format}")

    def _validate_pdf(self, path: Path, result: ValidationResult,
                      expected_title: str = None, expected_author: str = None):
        """验证PDF可读性和基础元数据"""
        try:
            with path.open('rb') as f:
                header = f.read(5)
            if header != b'%PDF-':
                result.errors.append('PDF文件头无效')
                return
        except OSError as exc:
            result.errors.append(f"PDF文件读取失败: {exc}")
            return

        try:
            from PyPDF2 import PdfReader

            reader = PdfReader(str(path), strict=False)
            result.page_count = len(reader.pages)
            if result.page_count == 0:
                result.errors.append('PDF没有可读取页面')

            metadata = reader.metadata or {}
            result.metadata = {
                str(key).lstrip('/'): str(value)
                for key, value in metadata.items()
                if value is not None
            }

            self._check_metadata_match(result, expected_title, expected_author)
            self._check_first_page_match(reader, result, expected_title, expected_author)
        except Exception as exc:
            result.errors.append(f"PDF解析失败: {exc}")

    def _check_first_page_match(self, reader, result: ValidationResult,
                                expected_title: str = None,
                                expected_author: str = None):
        """检查PDF第一页文本与目标书名/作者是否匹配"""
        first_page_text = self._extract_pdf_first_page_text(reader)
        result.first_page_text = first_page_text[:2000]

        if not first_page_text:
            result.warnings.append('PDF第一页无法提取文本')
            return

        if expected_title:
            title_similarity = self._best_text_similarity(first_page_text, expected_title)
            if title_similarity < self.first_page_min_title_similarity:
                result.errors.append('PDF第一页内容与目标书名明显不符')

        if expected_author:
            author_similarity = self._best_text_similarity(first_page_text, expected_author)
            if author_similarity < self.first_page_min_author_similarity:
                result.warnings.append('PDF第一页内容与目标作者匹配度较低')

    def _extract_pdf_first_page_text(self, reader) -> str:
        """提取PDF第一页文本"""
        if not reader.pages:
            return ''
        try:
            text = reader.pages[0].extract_text() or ''
        except Exception:
            return ''
        return ' '.join(text.split())

    def _validate_epub(self, path: Path, result: ValidationResult):
        """验证EPUB容器结构"""
        if not zipfile.is_zipfile(path):
            result.errors.append('EPUB不是有效的ZIP容器')
            return

        try:
            with zipfile.ZipFile(path) as zf:
                names = set(zf.namelist())
                if 'mimetype' not in names:
                    result.warnings.append('EPUB缺少mimetype文件')
                if 'META-INF/container.xml' not in names:
                    result.errors.append('EPUB缺少META-INF/container.xml')
        except zipfile.BadZipFile as exc:
            result.errors.append(f"EPUB解析失败: {exc}")

    def _validate_djvu(self, path: Path, result: ValidationResult):
        """验证DJVU文件头"""
        try:
            with path.open('rb') as f:
                header = f.read(12)
            if b'DJVU' not in header.upper() and not header.startswith(b'AT&T'):
                result.warnings.append('DJVU文件头无法确认')
        except OSError as exc:
            result.errors.append(f"DJVU文件读取失败: {exc}")

    def _check_metadata_match(self, result: ValidationResult,
                              expected_title: str = None,
                              expected_author: str = None):
        """用PDF元数据进行弱匹配，避免误删可用文件"""
        metadata_title = result.metadata.get('Title') or result.metadata.get('title')
        metadata_author = result.metadata.get('Author') or result.metadata.get('author')

        if expected_title and metadata_title:
            if self._similarity(metadata_title, expected_title) < 0.2:
                result.warnings.append('PDF标题元数据与书名匹配度较低')
        elif expected_title:
            result.warnings.append('PDF缺少标题元数据')

        if expected_author and metadata_author:
            if self._similarity(metadata_author, expected_author) < 0.2:
                result.warnings.append('PDF作者元数据与目标作者匹配度较低')
        elif expected_author:
            result.warnings.append('PDF缺少作者元数据')

    def _similarity(self, left: str, right: str) -> float:
        """计算简单词集相似度"""
        left_words = set(self._normalize(left).split())
        right_words = set(self._normalize(right).split())
        if not left_words or not right_words:
            return 0.0
        return len(left_words & right_words) / len(left_words | right_words)

    def _best_text_similarity(self, text: str, query: str) -> float:
        """用全文与滑窗片段做匹配，降低长文档首段噪声的影响"""
        normalized_text = self._normalize(text)
        normalized_query = self._normalize(query)
        if not normalized_text or not normalized_query:
            return 0.0

        best = self._similarity(normalized_text, normalized_query)
        tokens = normalized_text.split()
        query_len = max(1, len(normalized_query.split()))
        window = max(query_len * 3, 12)

        for start in range(0, len(tokens), max(1, query_len)):
            chunk = ' '.join(tokens[start:start + window])
            if not chunk:
                continue
            best = max(best, self._similarity(chunk, normalized_query))
            if best >= 1.0:
                return best

        return best

    def _normalize(self, value: str) -> str:
        """规范化比较字符串"""
        value = value.lower()
        value = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', ' ', value)
        return ' '.join(value.split())

    def human_size(self, size: int) -> str:
        """格式化文件大小"""
        units = ['B', 'KB', 'MB', 'GB']
        value = float(size)
        for unit in units:
            if value < 1024 or unit == units[-1]:
                return f"{value:.1f}{unit}"
            value /= 1024
