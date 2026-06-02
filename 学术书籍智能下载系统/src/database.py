"""数据库操作模块"""

import sqlite3
import hashlib
from pathlib import Path
from typing import List, Dict, Optional


class Database:
    """数据库管理类"""

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None
        self._init_database()

    def _init_database(self):
        """初始化数据库"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        """创建数据表"""
        cursor = self.conn.cursor()

        # 书籍表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                category TEXT,
                notes TEXT,
                status TEXT DEFAULT 'pending',
                download_url TEXT,
                file_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 下载日志表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS download_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                source TEXT,
                status TEXT,
                error_message TEXT,
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)

        # 搜索候选结果表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                result_key TEXT NOT NULL,
                source TEXT,
                title TEXT NOT NULL,
                author TEXT,
                download_url TEXT,
                file_format TEXT,
                file_size TEXT,
                score REAL DEFAULT 0,
                is_open_access INTEGER DEFAULT 0,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (book_id) REFERENCES books(id),
                UNIQUE (book_id, result_key)
            )
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_search_results_book_score
            ON search_results (book_id, score DESC)
        """)

        self.conn.commit()

    def insert_book(self, title: str, author: str = None,
                   category: str = None, notes: str = None) -> int:
        """插入书籍记录"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, category, notes)
            VALUES (?, ?, ?, ?)
        """, (title, author, category, notes))
        self.conn.commit()
        return cursor.lastrowid

    def update_book_status(self, book_id: int, status: str,
                          download_url: str = None, file_path: str = None):
        """更新书籍状态"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE books
            SET status = ?,
                download_url = COALESCE(?, download_url),
                file_path = COALESCE(?, file_path),
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (status, download_url, file_path, book_id))
        self.conn.commit()

    def replace_book_download_state(self, book_id: int, status: str,
                                    download_url: str = None,
                                    file_path: str = None):
        """显式替换书籍下载状态和文件信息，可用于清空错误记录"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE books
            SET status = ?,
                download_url = ?,
                file_path = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (status, download_url, file_path, book_id))
        self.conn.commit()

    def get_book(self, book_id: int) -> Optional[Dict]:
        """获取书籍信息"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_all_books(self, status: str = None) -> List[Dict]:
        """获取所有书籍"""
        cursor = self.conn.cursor()
        if status:
            cursor.execute("SELECT * FROM books WHERE status = ? ORDER BY id", (status,))
        else:
            cursor.execute("SELECT * FROM books ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]

    def log_download_attempt(self, book_id: int, source: str,
                            status: str, error_message: str = None):
        """记录下载尝试"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO download_logs (book_id, source, status, error_message)
            VALUES (?, ?, ?, ?)
        """, (book_id, source, status, error_message))
        self.conn.commit()

    def clear_search_results(self, book_id: int):
        """清空指定书籍的旧搜索候选"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM search_results WHERE book_id = ?", (book_id,))
        self.conn.commit()

    def delete_search_result_by_url(self, book_id: int, download_url: str):
        """删除指定书籍中某个错误下载链接对应的候选结果"""
        if not download_url:
            return
        cursor = self.conn.cursor()
        cursor.execute("""
            DELETE FROM search_results
            WHERE book_id = ?
              AND download_url = ?
        """, (book_id, download_url))
        self.conn.commit()

    def insert_search_result(self, book_id: int, source: str, title: str,
                             author: str = None, download_url: str = None,
                             file_format: str = None, file_size: str = None,
                             score: float = 0.0, is_open_access: bool = False,
                             notes: str = None) -> int:
        """保存搜索候选结果"""
        result_key = self._make_result_key(source, title, download_url)
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO search_results (
                book_id, result_key, source, title, author, download_url,
                file_format, file_size, score, is_open_access, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(book_id, result_key) DO UPDATE SET
                source = excluded.source,
                title = excluded.title,
                author = excluded.author,
                download_url = excluded.download_url,
                file_format = excluded.file_format,
                file_size = excluded.file_size,
                score = excluded.score,
                is_open_access = excluded.is_open_access,
                notes = excluded.notes,
                updated_at = CURRENT_TIMESTAMP
        """, (
            book_id, result_key, source, title, author, download_url,
            file_format, file_size, score, 1 if is_open_access else 0, notes
        ))
        self.conn.commit()
        return cursor.lastrowid

    def get_search_results(self, book_id: int = None,
                           only_downloadable: bool = False) -> List[Dict]:
        """获取搜索候选结果"""
        cursor = self.conn.cursor()
        clauses = []
        params = []

        if book_id is not None:
            clauses.append("sr.book_id = ?")
            params.append(book_id)

        if only_downloadable:
            clauses.append("sr.download_url IS NOT NULL")
            clauses.append("sr.download_url != ''")

        where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        cursor.execute(f"""
            SELECT
                sr.*,
                b.title AS book_title,
                b.author AS book_author,
                b.category AS book_category
            FROM search_results sr
            JOIN books b ON b.id = sr.book_id
            {where_sql}
            ORDER BY sr.book_id, sr.score DESC, sr.id
        """, params)
        return [dict(row) for row in cursor.fetchall()]

    def get_best_search_result(self, book_id: int) -> Optional[Dict]:
        """获取指定书籍评分最高且可下载的候选结果"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT *
            FROM search_results
            WHERE book_id = ?
              AND download_url IS NOT NULL
              AND download_url != ''
            ORDER BY score DESC, id
            LIMIT 1
        """, (book_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_statistics(self) -> Dict:
        """获取统计信息"""
        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) as total FROM books")
        total = cursor.fetchone()['total']

        cursor.execute("SELECT COUNT(*) as total_candidates FROM search_results")
        total_candidates = cursor.fetchone()['total_candidates']

        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM books
            GROUP BY status
        """)
        status_counts = {row['status']: row['count'] for row in cursor.fetchall()}

        completed = status_counts.get('completed', 0)

        return {
            'total': total,
            'completed': completed,
            'failed': status_counts.get('failed', 0),
            'pending': status_counts.get('pending', 0),
            'found': status_counts.get('found', 0),
            'validation_failed': status_counts.get('validation_failed', 0),
            'total_candidates': total_candidates,
            'status_counts': status_counts,
            'success_rate': f"{(completed/total*100):.1f}%" if total > 0 else "0%"
        }

    def get_report_rows(self) -> List[Dict]:
        """获取报告所需的书籍和最近日志信息"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.author,
                b.category,
                b.notes,
                b.status,
                b.download_url,
                b.file_path,
                b.created_at,
                b.updated_at,
                l.source AS latest_source,
                l.status AS latest_log_status,
                l.error_message AS latest_error,
                l.attempt_time AS latest_attempt_time,
                (
                    SELECT COUNT(*)
                    FROM search_results sr
                    WHERE sr.book_id = b.id
                ) AS candidate_count,
                (
                    SELECT MAX(score)
                    FROM search_results sr
                    WHERE sr.book_id = b.id
                ) AS best_candidate_score
            FROM books b
            LEFT JOIN download_logs l ON l.id = (
                SELECT id
                FROM download_logs
                WHERE book_id = b.id
                ORDER BY attempt_time DESC, id DESC
                LIMIT 1
            )
            ORDER BY b.id
        """)
        return [dict(row) for row in cursor.fetchall()]

    def get_download_logs(self, book_id: int = None) -> List[Dict]:
        """获取下载/搜索日志"""
        cursor = self.conn.cursor()
        if book_id is None:
            cursor.execute("""
                SELECT * FROM download_logs
                ORDER BY attempt_time DESC, id DESC
            """)
        else:
            cursor.execute("""
                SELECT * FROM download_logs
                WHERE book_id = ?
                ORDER BY attempt_time DESC, id DESC
            """, (book_id,))
        return [dict(row) for row in cursor.fetchall()]

    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()

    def _make_result_key(self, source: str, title: str, download_url: str = None) -> str:
        """生成搜索结果去重键"""
        raw_key = '|'.join([
            (source or '').strip().lower(),
            (download_url or '').strip().lower(),
            (title or '').strip().lower(),
        ])
        return hashlib.sha1(raw_key.encode('utf-8')).hexdigest()
