#!/usr/bin/env python3
"""测试文件验证模块"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from validator import FileValidator


class TestConfig:
    """测试配置"""

    def get(self, key, default=None):
        values = {
            'validation.min_file_size': 1,
            'validation.max_file_size': 1024 * 1024,
            'validation.allowed_formats': ['pdf', 'epub', 'djvu'],
            'validation.first_page_min_title_similarity': 0.2,
            'validation.first_page_min_author_similarity': 0.2,
        }
        return values.get(key, default)


class StubFirstPageValidator(FileValidator):
    """通过覆写首页文本提取来测试首页匹配逻辑"""

    def __init__(self, config, first_page_text):
        super().__init__(config)
        self._stub_first_page_text = first_page_text

    def _extract_pdf_first_page_text(self, reader) -> str:
        return self._stub_first_page_text


def test_validator():
    """测试PDF验证成功和失败路径"""
    validator = FileValidator(TestConfig())

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        valid_pdf = tmp_path / 'valid.pdf'
        invalid_pdf = tmp_path / 'invalid.pdf'

        from PyPDF2 import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        writer.add_metadata({
            '/Title': 'Solar System Dynamics',
            '/Author': 'Murray',
        })
        with valid_pdf.open('wb') as f:
            writer.write(f)

        invalid_pdf.write_bytes(b'not a pdf')

        valid_result = validator.validate(
            str(valid_pdf),
            expected_title='Solar System Dynamics',
            expected_author='Murray'
        )
        assert valid_result.is_valid
        assert valid_result.file_format == 'pdf'
        assert valid_result.page_count == 1

        invalid_result = validator.validate(str(invalid_pdf))
        assert not invalid_result.is_valid
        assert invalid_result.errors

    print('文件验证测试通过')


def test_first_page_matching():
    """第一页内容明显不符时应判定失败"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        pdf_path = tmp_path / 'sample.pdf'

        from PyPDF2 import PdfWriter

        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with pdf_path.open('wb') as f:
            writer.write(f)

        valid_validator = StubFirstPageValidator(
            TestConfig(),
            '陈国良 并行计算导论 高等教育出版社 并行计算基础与算法'
        )
        valid_result = valid_validator.validate(
            str(pdf_path),
            expected_title='陈国良《并行计算导论》',
            expected_author='陈国良'
        )
        assert valid_result.is_valid
        assert not valid_result.errors

        invalid_validator = StubFirstPageValidator(
            TestConfig(),
            'NASA Contractor Report 3077 Significant Achievements in the Planetary Geology Program'
        )
        invalid_result = invalid_validator.validate(
            str(pdf_path),
            expected_title='Solar System Evolution',
            expected_author='Chambers'
        )
        assert not invalid_result.is_valid
        assert 'PDF第一页内容与目标书名明显不符' in invalid_result.errors

    print('首页内容匹配测试通过')


if __name__ == '__main__':
    test_validator()
    test_first_page_matching()
