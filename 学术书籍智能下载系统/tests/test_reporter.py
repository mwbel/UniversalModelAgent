#!/usr/bin/env python3
"""测试报告生成模块"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database import Database
from reporter import ReportGenerator


class TestConfig:
    """测试配置"""

    def __init__(self, log_dir: str):
        self.log_dir = log_dir

    def get(self, key, default=None):
        values = {
            'paths.log_dir': self.log_dir,
        }
        return values.get(key, default)


def test_reporter():
    """测试Markdown和CSV报告生成"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        db = Database(str(tmp_path / 'books.db'))

        book_id = db.insert_book(
            title='Solar System Dynamics',
            author='Murray & Dermott',
            category='太阳系多体动力学',
            notes='测试书目'
        )
        db.update_book_status(
            book_id,
            status='completed',
            download_url='https://example.org/book.pdf',
            file_path=str(tmp_path / 'book.pdf')
        )
        db.log_download_attempt(book_id, source='test', status='completed')

        generator = ReportGenerator(TestConfig(str(tmp_path / 'logs')), db)
        md_path = Path(generator.generate(report_format='md'))
        csv_path = Path(generator.generate(report_format='csv'))

        assert md_path.exists()
        assert csv_path.exists()
        assert 'Solar System Dynamics' in md_path.read_text(encoding='utf-8')
        assert 'Solar System Dynamics' in csv_path.read_text(encoding='utf-8-sig')

        db.close()

    print('报告生成测试通过')


if __name__ == '__main__':
    test_reporter()
