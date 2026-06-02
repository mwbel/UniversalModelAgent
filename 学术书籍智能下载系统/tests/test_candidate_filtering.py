#!/usr/bin/env python3
"""测试下载候选过滤逻辑"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database import Database
from main import _get_download_candidates, _candidate_rejection_reason


class TestConfig:
    """测试配置"""

    def get(self, key, default=None):
        values = {
            'validation.min_file_size': 102400,
        }
        return values.get(key, default)


def test_candidate_filtering():
    """过滤预览页、图片和过小文件"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db = Database(str(Path(tmp_dir) / 'books.db'))
        book_id = db.insert_book(
            title='Solar System Dynamics',
            author='Murray & Dermott',
            category='太阳系多体动力学'
        )
        db.update_book_status(book_id, status='found')

        db.insert_search_result(
            book_id=book_id,
            source='Preview Source',
            title='Solar System Dynamics Preview',
            download_url='https://example.org/preview.pdf',
            file_format='pdf',
            file_size='5.0MB',
            score=99.0,
            notes='preview only'
        )
        db.insert_search_result(
            book_id=book_id,
            source='Image Source',
            title='Solar System Dynamics',
            download_url='https://example.org/cover.jpg',
            file_format='jpg',
            file_size='800KB',
            score=95.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Tiny PDF Source',
            title='Solar System Dynamics',
            download_url='https://example.org/tiny.pdf',
            file_format='pdf',
            file_size='50KB',
            score=92.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Good Source',
            title='Solar System Dynamics',
            download_url='https://example.org/fullbook.pdf',
            file_format='pdf',
            file_size='12MB',
            score=88.0
        )

        book = db.get_book(book_id)
        candidates = _get_download_candidates(db, book, TestConfig())

        assert len(candidates) == 1
        assert candidates[0]['source'] == 'Good Source'
        assert candidates[0]['download_url'] == 'https://example.org/fullbook.pdf'
        db.close()

    print('下载候选过滤测试通过')


def test_candidate_rejection_reason():
    """返回明确的过滤原因"""
    config = TestConfig()

    assert '非全文资源' in _candidate_rejection_reason({
        'download_url': 'https://example.org/sample.pdf',
        'title': 'Book Sample',
        'file_format': 'pdf',
        'file_size': '2MB',
        'notes': ''
    }, config)

    assert '不支持的格式' in _candidate_rejection_reason({
        'download_url': 'https://example.org/file.jpg',
        'title': 'Book Cover',
        'file_format': 'jpg',
        'file_size': '2MB',
        'notes': ''
    }, config)

    assert '过小' in _candidate_rejection_reason({
        'download_url': 'https://example.org/tiny.pdf',
        'title': 'Book',
        'file_format': 'pdf',
        'file_size': '80KB',
        'notes': ''
    }, config)

    assert '非全文资源' in _candidate_rejection_reason({
        'download_url': 'https://example.org/numerical-analysis.pdf',
        'title': "Instructor's manual to accompany Numerical analysis",
        'file_format': 'pdf',
        'file_size': '9MB',
        'notes': ''
    }, config)

    print('过滤原因测试通过')


if __name__ == '__main__':
    test_candidate_filtering()
    test_candidate_rejection_reason()
