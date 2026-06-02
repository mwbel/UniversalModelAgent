#!/usr/bin/env python3
"""测试下载候选自动回退逻辑"""

import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database import Database
from main import _get_download_candidates, _try_download_candidates


class TestConfig:
    """测试配置"""

    def get(self, key, default=None):
        values = {
            'validation.min_file_size': 102400,
        }
        return values.get(key, default)


class FakeDownloader:
    """伪造下载器"""

    def __init__(self, outcomes):
        self.outcomes = outcomes
        self.calls = []

    def download(self, url, filename, category=None):
        self.calls.append({
            'url': url,
            'filename': filename,
            'category': category,
        })
        return self.outcomes.get(url)


class FakeValidator:
    """伪造验证器"""

    def __init__(self, valid_paths=None, invalid_paths=None):
        self.valid_paths = set(valid_paths or [])
        self.invalid_paths = set(invalid_paths or [])
        self.calls = []

    def validate(self, file_path, expected_title=None, expected_author=None):
        self.calls.append(file_path)
        if file_path in self.invalid_paths:
            return SimpleNamespace(
                is_valid=False,
                errors=['Mock validation failed'],
                warnings=[]
            )
        return SimpleNamespace(
            is_valid=file_path in self.valid_paths,
            errors=[] if file_path in self.valid_paths else ['Unknown mock path'],
            warnings=[]
        )


def test_download_fallback():
    """测试下载失败后自动切换到下一个候选"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db = Database(str(Path(tmp_dir) / 'books.db'))
        book_id = db.insert_book(
            title='Solar System Dynamics',
            author='Murray & Dermott',
            category='太阳系多体动力学'
        )
        db.update_book_status(
            book_id,
            status='found',
            download_url='https://fallback.example/final.pdf'
        )
        db.insert_search_result(
            book_id=book_id,
            source='Broken Source',
            title='Solar System Dynamics',
            download_url='https://broken.example/file.pdf',
            file_format='pdf',
            score=95.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Working Source',
            title='Solar System Dynamics',
            download_url='https://working.example/file.pdf',
            file_format='pdf',
            score=90.0
        )

        book = db.get_book(book_id)
        candidates = _get_download_candidates(db, book, TestConfig())
        assert [item['source'] for item in candidates] == ['Broken Source', 'Working Source', 'book_record']

        downloader = FakeDownloader({
            'https://working.example/file.pdf': '/tmp/mock-success.pdf',
        })
        validator = FakeValidator(valid_paths={'/tmp/mock-success.pdf'})

        success = _try_download_candidates(book, candidates, downloader, validator, db)
        assert success
        assert len(downloader.calls) == 2

        updated = db.get_book(book_id)
        assert updated['status'] == 'completed'
        assert updated['download_url'] == 'https://working.example/file.pdf'
        assert updated['file_path'] == '/tmp/mock-success.pdf'
        db.close()

    print('下载候选回退测试通过')


def test_download_fallback_after_validation_failure():
    """测试校验失败后继续尝试下一个候选"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db = Database(str(Path(tmp_dir) / 'books.db'))
        book_id = db.insert_book(
            title='Celestial Mechanics',
            author='Danby',
            category='太阳系多体动力学'
        )
        db.update_book_status(book_id, status='found')
        db.insert_search_result(
            book_id=book_id,
            source='Invalid PDF Source',
            title='Celestial Mechanics',
            download_url='https://invalid.example/file.pdf',
            file_format='pdf',
            score=88.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Valid EPUB Source',
            title='Celestial Mechanics',
            download_url='https://valid.example/file.epub',
            file_format='epub',
            score=80.0
        )

        book = db.get_book(book_id)
        candidates = _get_download_candidates(db, book, TestConfig())

        downloader = FakeDownloader({
            'https://invalid.example/file.pdf': '/tmp/mock-invalid.pdf',
            'https://valid.example/file.epub': '/tmp/mock-valid.epub',
        })
        validator = FakeValidator(
            valid_paths={'/tmp/mock-valid.epub'},
            invalid_paths={'/tmp/mock-invalid.pdf'}
        )

        success = _try_download_candidates(book, candidates, downloader, validator, db)
        assert success
        assert len(downloader.calls) == 2

        updated = db.get_book(book_id)
        assert updated['status'] == 'completed'
        assert updated['download_url'] == 'https://valid.example/file.epub'
        assert updated['file_path'] == '/tmp/mock-valid.epub'
        db.close()

    print('校验失败后回退测试通过')


def test_invalid_file_removed_before_next_candidate():
    """校验失败后移除坏文件，避免阻塞下一个候选"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db = Database(str(Path(tmp_dir) / 'books.db'))
        book_id = db.insert_book(
            title='Numerical Analysis',
            author='Burden & Faires',
            category='数值分析'
        )
        db.update_book_status(book_id, status='found')
        db.insert_search_result(
            book_id=book_id,
            source='Bad Match',
            title='Numerical Analysis',
            download_url='https://bad.example/file.pdf',
            file_format='pdf',
            score=90.0
        )
        db.insert_search_result(
            book_id=book_id,
            source='Good Match',
            title='Numerical Analysis',
            download_url='https://good.example/file.pdf',
            file_format='pdf',
            score=80.0
        )

        target_path = Path(tmp_dir) / 'Numerical Analysis_Burden & Faires.pdf'

        class RewritingDownloader:
            def __init__(self, path):
                self.path = path
                self.calls = []

            def download(self, url, filename, category=None):
                self.calls.append(url)
                if url == 'https://good.example/file.pdf':
                    assert not self.path.exists()
                self.path.write_bytes(b'%PDF mock content')
                return str(self.path)

        class SequentialValidator:
            def __init__(self, valid_path):
                self.valid_path = valid_path
                self.calls = 0

            def validate(self, file_path, expected_title=None, expected_author=None):
                self.calls += 1
                if self.calls == 1:
                    return SimpleNamespace(
                        is_valid=False,
                        errors=['Mock validation failed'],
                        warnings=[]
                    )
                return SimpleNamespace(
                    is_valid=file_path == self.valid_path,
                    errors=[],
                    warnings=[]
                )

        book = db.get_book(book_id)
        candidates = _get_download_candidates(db, book, TestConfig())
        downloader = RewritingDownloader(target_path)
        validator = SequentialValidator(str(target_path))

        success = _try_download_candidates(book, candidates, downloader, validator, db)
        assert success
        assert downloader.calls == [
            'https://bad.example/file.pdf',
            'https://good.example/file.pdf',
        ]

        updated = db.get_book(book_id)
        assert updated['status'] == 'completed'
        assert updated['file_path'] == str(target_path)
        db.close()

    print('无效文件清理测试通过')


if __name__ == '__main__':
    test_download_fallback()
    test_download_fallback_after_validation_failure()
    test_invalid_file_removed_before_next_candidate()
