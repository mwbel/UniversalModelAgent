#!/usr/bin/env python3
"""测试搜索候选结果持久化"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database import Database


def test_candidates():
    """测试候选结果保存、排序和清理"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db = Database(str(Path(tmp_dir) / 'books.db'))
        book_id = db.insert_book(
            title='Solar System Dynamics',
            author='Murray & Dermott',
            category='太阳系多体动力学',
        )

        db.insert_search_result(
            book_id=book_id,
            source='Google Scholar',
            title='Solar System Dynamics',
            author='Murray and Dermott',
            download_url='https://example.org/open.pdf',
            file_format='pdf',
            file_size='12 MB',
            score=92.5,
            is_open_access=True,
            notes='开放PDF'
        )
        db.insert_search_result(
            book_id=book_id,
            source='Library Genesis',
            title='Solar System Dynamics',
            author='Murray & Dermott',
            download_url='https://example.org/libgen.pdf',
            file_format='pdf',
            file_size='10 MB',
            score=88.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Google Scholar',
            title='Solar System Dynamics',
            author='Murray and Dermott',
            download_url='https://example.org/open.pdf',
            file_format='pdf',
            file_size='12 MB',
            score=95.0,
            is_open_access=True,
            notes='更新评分'
        )

        results = db.get_search_results(book_id)
        assert len(results) == 2
        assert results[0]['score'] == 95.0
        assert results[0]['is_open_access'] == 1

        best = db.get_best_search_result(book_id)
        assert best['download_url'] == 'https://example.org/open.pdf'

        stats = db.get_statistics()
        assert stats['total_candidates'] == 2

        db.clear_search_results(book_id)
        assert db.get_search_results(book_id) == []
        db.close()

    print('搜索候选结果测试通过')


if __name__ == '__main__':
    test_candidates()
