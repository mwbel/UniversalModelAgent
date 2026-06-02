#!/usr/bin/env python3
"""测试完整流程：搜索前3本书"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from config import Config
from database import Database
from searcher import SearchEngine


def test_workflow():
    """测试搜索工作流"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    config = Config(str(config_path))

    db_path = Path(__file__).parent.parent / 'data' / 'books.db'
    db = Database(str(db_path))

    # 获取前3本待搜索的书
    books = db.get_all_books(status='pending')[:3]

    print(f"测试搜索前 {len(books)} 本书\n")

    engine = SearchEngine(config)

    for i, book in enumerate(books, 1):
        print(f"\n{'='*60}")
        print(f"[{i}/{len(books)}] {book['title']}")
        if book['author']:
            print(f"作者: {book['author']}")

        try:
            results = engine.search(book['title'], book['author'])

            if results:
                best = results[0]
                print(f"\n✓ 找到资源 (评分: {best.score:.1f})")
                print(f"  标题: {best.title[:60]}")
                print(f"  来源: {best.source}")
                print(f"  格式: {best.file_format}")

                # 更新数据库
                db.update_book_status(
                    book['id'],
                    status='found',
                    download_url=best.download_url
                )
                print(f"  数据库已更新")
            else:
                print(f"\n✗ 未找到资源")

        except Exception as e:
            print(f"\n✗ 错误: {e}")

    print(f"\n{'='*60}")
    print("\n测试完成！")

    # 显示统计
    stats = db.get_statistics()
    print(f"\n统计: 总数={stats['total']}, 已找到资源={db.get_all_books(status='found').__len__()}")

    db.close()


if __name__ == '__main__':
    test_workflow()
