"""Excel解析模块"""

import pandas as pd
from pathlib import Path
from typing import List, Dict


class BookParser:
    """书籍清单解析器"""

    def __init__(self, excel_path: str):
        self.excel_path = Path(excel_path)
        if not self.excel_path.exists():
            raise FileNotFoundError(f"Excel文件不存在: {excel_path}")

    def parse(self) -> List[Dict]:
        """解析Excel文件，返回书籍列表"""
        df = pd.read_excel(self.excel_path)

        # 重命名列（根据实际Excel结构）
        df.columns = ['index', 'category', 'subcategory', 'title', 'notes']

        # 数据清洗
        books = []
        current_category = None

        for _, row in df.iterrows():
            # 跳过表头行
            if row['category'] == '方向':
                continue

            # 更新当前分类
            if pd.notna(row['category']) and row['category'] != '':
                current_category = row['category']

            # 提取书籍信息
            title = row['title']
            if pd.isna(title) or title == '':
                continue

            # 解析书名和作者
            book_title, author = self._parse_title_author(str(title))

            books.append({
                'title': book_title,
                'author': author,
                'category': current_category,
                'subcategory': row['subcategory'] if pd.notna(row['subcategory']) else None,
                'notes': row['notes'] if pd.notna(row['notes']) else None
            })

        return books

    def _parse_title_author(self, title_str: str) -> tuple:
        """从标题字符串中解析书名和作者"""
        # 常见格式: "Book Title, Author Name"
        if ',' in title_str:
            parts = title_str.split(',', 1)
            return parts[0].strip(), parts[1].strip()

        # 格式: "Book Title (Author)"
        if '(' in title_str and ')' in title_str:
            title = title_str[:title_str.index('(')].strip()
            author = title_str[title_str.index('(')+1:title_str.index(')')].strip()
            return title, author

        # 无作者信息
        return title_str.strip(), None

    def get_statistics(self, books: List[Dict]) -> Dict:
        """获取书籍统计信息"""
        total = len(books)
        categories = {}

        for book in books:
            cat = book.get('category', 'Unknown')
            categories[cat] = categories.get(cat, 0) + 1

        return {
            'total': total,
            'categories': categories,
            'has_author': sum(1 for b in books if b.get('author'))
        }
