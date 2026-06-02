#!/usr/bin/env python3
"""手动添加搜索候选结果到数据库"""

import sqlite3
import sys

def add_candidate(db_path, book_id, url, source, title, score=80.0):
    """添加候选下载链接"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 检查候选是否已存在
    cursor.execute("""
        SELECT id FROM search_results
        WHERE book_id = ? AND download_url = ?
    """, (book_id, url))

    if cursor.fetchone():
        print(f"  候选已存在: {url}")
        conn.close()
        return False

    # 生成result_key
    result_key = f"{book_id}_{source}_{hash(url) % 1000000}"

    # 插入新候选
    cursor.execute("""
        INSERT INTO search_results
        (book_id, result_key, title, download_url, source, file_format, score, created_at)
        VALUES (?, ?, ?, ?, ?, 'pdf', ?, datetime('now'))
    """, (book_id, result_key, title, url, source, score))

    conn.commit()
    conn.close()
    print(f"  ✓ 已添加候选: {url}")
    return True

def update_book_status(db_path, book_id, status='found'):
    """更新书籍状态"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books SET status = ?, updated_at = datetime('now')
        WHERE id = ?
    """, (status, book_id))

    conn.commit()
    conn.close()

# 数据库路径
db_path = "data/books.db"

print("开始添加手动候选...")

# 1. Symplectic Geometric Algorithms for Hamiltonian Systems (ID: 81)
print("\n[1] Symplectic Geometric Algorithms for Hamiltonian Systems")
add_candidate(db_path, 81,
    "http://link.springer.com/content/pdf/10.1007/978-3-642-01777-3.pdf",
    "Springer", "Symplectic Geometric Algorithms for Hamiltonian Systems", 90.0)
update_book_status(db_path, 81, 'found')

# 2. Solving Ordinary Differential Equations II (ID: 79)
print("\n[2] Solving Ordinary Differential Equations II")
add_candidate(db_path, 79,
    "https://archive.org/download/solvingordinaryd0002hair/solvingordinaryd0002hair.pdf",
    "Internet Archive", "Solving Ordinary Differential Equations II", 85.0)
add_candidate(db_path, 79,
    "https://www.researchgate.net/publication/200175470_Solving_Ordinary_Differential_Equations_II_Stiff_and_Differential-Algebraic_Problems",
    "ResearchGate", "Solving Ordinary Differential Equations II", 80.0)
update_book_status(db_path, 79, 'found')

# 3. Geometric Numerical Integration (ID: 80)
print("\n[3] Geometric Numerical Integration")
add_candidate(db_path, 80,
    "https://link.springer.com/content/pdf/10.1007/3-540-30666-8.pdf",
    "Springer", "Geometric Numerical Integration", 90.0)
update_book_status(db_path, 80, 'found')

# 4. Data Reduction and Error Analysis (ID: 46)
print("\n[4] Data Analysis for Physical Applications")
add_candidate(db_path, 46,
    "https://archive.org/download/datareductionerr0000bevi/datareductionerr0000bevi.pdf",
    "Internet Archive", "Data Reduction and Error Analysis", 85.0)
update_book_status(db_path, 46, 'found')

# 5. Rounding Errors in Algebraic Processes - Wilkinson (ID: 60)
print("\n[5] Computer Arithmetic and Error Analysis")
add_candidate(db_path, 60,
    "https://archive.org/download/roundingerrorsin0000wilk/roundingerrorsin0000wilk.pdf",
    "Internet Archive", "Rounding Errors in Algebraic Processes", 85.0)
update_book_status(db_path, 60, 'found')

# 6. Approximation Theory and Practice (ID: 70)
print("\n[6] Approximation Theory and Practice")
add_candidate(db_path, 70,
    "https://epubs.siam.org/doi/pdf/10.1137/1.9781611975949",
    "SIAM", "Approximation Theory and Practice", 90.0)
update_book_status(db_path, 70, 'found')

# 7. Fundamentals of Astrometry (ID: 73)
print("\n[7] Fundamentals of Astrometry")
add_candidate(db_path, 73,
    "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDE20FEB13247F87C50718D41CDC6A83/9780521642163c1_p1-10_CBO.pdf",
    "Cambridge", "Fundamentals of Astrometry", 85.0)
update_book_status(db_path, 73, 'found')

print("\n完成！已添加候选链接。")
