#!/usr/bin/env python3
"""测试搜索功能"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from config import Config
from searcher import SearchEngine


def test_search():
    """测试搜索引擎"""
    config_path = Path(__file__).parent.parent / 'config.yaml'
    config = Config(str(config_path))
    engine = SearchEngine(config)

    # 测试搜索
    test_books = [
        ("Solar System Dynamics", "Murray"),
        ("Celestial Mechanics", "Danby"),
        ("天体力学基础", "易照华")
    ]

    for title, author in test_books:
        print("\n" + "="*60)
        results = engine.search(title, author)

        if results:
            print(f"\n找到 {len(results)} 个结果:")
            for i, result in enumerate(results[:3], 1):
                print(f"\n{i}. {result.title}")
                print(f"   作者: {result.author}")
                print(f"   来源: {result.source}")
                print(f"   格式: {result.file_format}")
                print(f"   大小: {result.file_size}")
                print(f"   评分: {result.score:.1f}")
                print(f"   链接: {result.download_url[:80] if result.download_url else 'N/A'}...")
        else:
            print("\n未找到结果")

        print("="*60)


if __name__ == '__main__':
    test_search()
