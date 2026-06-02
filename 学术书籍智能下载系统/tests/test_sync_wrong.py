#!/usr/bin/env python3
"""测试 wrong 目录同步逻辑"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database import Database
from main import sync_wrong_files


class TestConfig:
    """测试配置"""

    def __init__(self, download_dir):
        self.download_dir = str(download_dir)

    def get(self, key, default=None):
        return default


def test_sync_wrong_files():
    """wrong 目录中的人工判错文件应回写到数据库"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        download_dir = tmp_path / 'downloads'
        wrong_dir = download_dir / '分类A' / 'wrong'
        wrong_dir.mkdir(parents=True, exist_ok=True)

        db = Database(str(tmp_path / 'books.db'))

        # 即使有备用候选，也应该从 completed 统一回到 failed
        book_a = db.insert_book(
            title='Solar System Dynamics',
            author='Murray & Dermott',
            category='分类A'
        )
        db.insert_search_result(
            book_id=book_a,
            source='Wrong Source',
            title='Solar System Dynamics',
            author='Murray & Dermott',
            download_url='https://wrong.example/file.pdf',
            file_format='pdf',
            score=95.0
        )
        db.insert_search_result(
            book_id=book_a,
            source='Backup Source',
            title='Solar System Dynamics',
            author='Murray & Dermott',
            download_url='https://backup.example/file.pdf',
            file_format='pdf',
            score=85.0
        )
        db.replace_book_download_state(
            book_a,
            status='completed',
            download_url='https://wrong.example/file.pdf',
            file_path='downloads/分类A/Solar System Dynamics_Murray & Dermott.pdf'
        )
        (wrong_dir / 'Solar System Dynamics_Murray & Dermott.pdf').write_bytes(b'wrong')

        # 没有备用候选的书，也应该统一回到 failed
        book_b = db.insert_book(
            title='Parallel Computing',
            author='Quinn',
            category='分类A'
        )
        db.insert_search_result(
            book_id=book_b,
            source='Only Source',
            title='Parallel Computing',
            author='Quinn',
            download_url='https://only.example/file.pdf',
            file_format='pdf',
            score=90.0
        )
        db.replace_book_download_state(
            book_b,
            status='completed',
            download_url='https://only.example/file.pdf',
            file_path='downloads/分类A/Parallel Computing_Quinn.pdf'
        )
        (wrong_dir / 'Parallel Computing_Quinn.pdf').write_bytes(b'wrong')

        # found 状态且被人工补充了 wrong 文件名，也应匹配并统一改为 failed
        book_c = db.insert_book(
            title='Symplectic Geometry',
            author='Abraham & Marsden',
            category='分类A'
        )
        db.insert_search_result(
            book_id=book_c,
            source='Wrong Found Source',
            title='Symplectic Geometry',
            author='Abraham & Marsden',
            download_url='https://found-wrong.example/file.pdf',
            file_format='pdf',
            score=88.0
        )
        db.insert_search_result(
            book_id=book_c,
            source='Backup Found Source',
            title='Symplectic Geometry',
            author='Abraham & Marsden',
            download_url='https://found-backup.example/file.pdf',
            file_format='pdf',
            score=83.0
        )
        db.update_book_status(
            book_c,
            status='found',
            download_url='https://found-wrong.example/file.pdf'
        )
        (
            wrong_dir
            / 'Symplectic Geometry_Abraham & Marsden-是论文不是书且作者不同.pdf'
        ).write_bytes(b'wrong')

        sync_wrong_files(TestConfig(download_dir), db)

        updated_a = db.get_book(book_a)
        assert updated_a['status'] == 'failed'
        assert updated_a['download_url'] is None
        assert updated_a['file_path'] is None

        candidates_a = db.get_search_results(book_id=book_a, only_downloadable=True)
        assert [item['download_url'] for item in candidates_a] == ['https://backup.example/file.pdf']

        updated_b = db.get_book(book_b)
        assert updated_b['status'] == 'failed'
        assert updated_b['download_url'] is None
        assert updated_b['file_path'] is None

        candidates_b = db.get_search_results(book_id=book_b, only_downloadable=True)
        assert candidates_b == []

        updated_c = db.get_book(book_c)
        assert updated_c['status'] == 'failed'
        assert updated_c['download_url'] is None
        assert updated_c['file_path'] is None

        candidates_c = db.get_search_results(book_id=book_c, only_downloadable=True)
        assert [item['download_url'] for item in candidates_c] == [
            'https://found-backup.example/file.pdf'
        ]

        logs = db.get_download_logs()
        assert any(log['status'] == 'wrong_file' for log in logs)
        db.close()

    print('wrong目录同步测试通过')


if __name__ == '__main__':
    test_sync_wrong_files()
