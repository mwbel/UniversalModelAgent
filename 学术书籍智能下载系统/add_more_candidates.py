#!/usr/bin/env python3
"""添加更多搜索候选结果到数据库"""

import sqlite3

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

print("开始添加更多候选...")

# 1. IAU Resolutions (ID: 18)
print("\n[1] IAU Resolutions on Astronomical Constants & Reference Systems")
add_candidate(db_path, 18,
    "https://arxiv.org/pdf/astro-ph/0602086",
    "arXiv", "IAU Resolutions on Astronomical Reference Systems", 90.0)
add_candidate(db_path, 18,
    "https://aa.usno.navy.mil/publications/docs/Circular_163.pdf",
    "USNO", "USNO Circular 163", 85.0)
update_book_status(db_path, 18, 'found')

# 2. Barnes-Hut Algorithm (ID: 91)
print("\n[2] Barnes-Hut Algorithm")
add_candidate(db_path, 91,
    "https://www.nature.com/articles/324446a0.pdf",
    "Nature", "A hierarchical O(N log N) force-calculation algorithm", 95.0)
update_book_status(db_path, 91, 'found')

# 3. The Moon: Constitution and Structure (ID: 22)
print("\n[3] The Moon: From Interior to Exterior")
add_candidate(db_path, 22,
    "https://www.degruyter.com/document/doi/10.1515/9781501509537-007/pdf",
    "De Gruyter", "The Constitution and Structure of the Lunar Interior", 90.0)
add_candidate(db_path, 22,
    "https://www.researchgate.net/publication/328831585_3_The_Constitution_and_Structure_of_the_Lunar_Interior",
    "ResearchGate", "The Constitution and Structure of the Lunar Interior", 85.0)
update_book_status(db_path, 22, 'found')

# 4. Post-Newtonian Geodesy (ID: 16)
print("\n[4] Post-Newtonian Geodesy and Relativistic Metrology")
add_candidate(db_path, 16,
    "https://arxiv.org/pdf/1510.03131",
    "arXiv", "Post-Newtonian reference-ellipsoid for relativistic geodesy", 85.0)
add_candidate(db_path, 16,
    "https://arxiv.org/pdf/1710.09144",
    "arXiv", "Advanced relativistic VLBI model for geodesy", 80.0)
update_book_status(db_path, 16, 'found')

# 5. Lunar Laser Ranging (ID: 50)
print("\n[5] Lunar Laser Ranging: A Continuing Legacy")
add_candidate(db_path, 50,
    "https://ntrs.nasa.gov/api/citations/20210004132/downloads/Dickey%20et%20al%201994%20LLR%20Science.pdf",
    "NASA", "Lunar Laser Ranging: A Continuing Legacy", 90.0)
update_book_status(db_path, 50, 'found')

# 6. JPL Ephemerides DE430/DE440 (ID: 49)
print("\n[6] JPL Planetary and Lunar Ephemerides DE430 and DE440")
add_candidate(db_path, 49,
    "https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf",
    "JPL", "The Planetary and Lunar Ephemerides DE430 and DE431", 95.0)
update_book_status(db_path, 49, 'found')

print("\n完成！已添加更多候选链接。")
