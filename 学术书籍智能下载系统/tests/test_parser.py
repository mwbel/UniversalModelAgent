"""测试Excel解析模块"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from parser import BookParser


def test_parser():
    """测试解析器"""
    excel_file = "行星运行轨道理论的相关书籍(1).xlsx"

    print(f"测试解析: {excel_file}")
    parser = BookParser(excel_file)

    books = parser.parse()
    print(f"\n解析结果: 共 {len(books)} 本书")

    # 显示前5本书
    print("\n前5本书:")
    for i, book in enumerate(books[:5], 1):
        print(f"\n{i}. {book['title']}")
        print(f"   作者: {book['author']}")
        print(f"   分类: {book['category']}")
        if book['notes']:
            print(f"   备注: {book['notes'][:50]}...")

    # 统计信息
    stats = parser.get_statistics(books)
    print(f"\n统计信息:")
    print(f"  总数: {stats['total']}")
    print(f"  有作者: {stats['has_author']}")
    print(f"\n分类分布:")
    for cat, count in stats['categories'].items():
        if cat:
            print(f"  - {cat}: {count}")


if __name__ == '__main__':
    test_parser()
