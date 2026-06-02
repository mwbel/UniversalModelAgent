#!/usr/bin/env python3
"""学术书籍智能下载系统 - 主程序"""

import sys
import argparse
from pathlib import Path

# 添加src目录到路径
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from config import Config
from database import Database
from parser import BookParser
from searcher import SearchEngine
from downloader import Downloader
from validator import FileValidator
from reporter import ReportGenerator

ALLOWED_DOWNLOAD_FORMATS = {'pdf', 'epub', 'djvu'}
BLOCKED_CANDIDATE_KEYWORDS = {
    'preview', 'sample', 'excerpt', 'abstract', 'thumbnail',
    'cover', 'frontmatter', 'table of contents', 'contents',
    'teacher', 'teachers manual', 'instructor', 'instructor manual',
    'solutions manual', 'student solutions', 'computer supplement',
    'software', 'workbook'
}


def _normalize_match_text(value: str) -> str:
    """规范化文件名和书籍名，便于错误文件匹配"""
    import re
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', str(value or '').lower())


def init_system(config: Config) -> tuple:
    """初始化系统"""
    print("正在初始化系统...")

    # 初始化数据库
    db = Database(config.database_path)
    print(f"✓ 数据库已初始化: {config.database_path}")

    return db


def load_books(config: Config, db: Database):
    """加载书籍清单"""
    print(f"\n正在解析书籍清单: {config.excel_file}")

    parser = BookParser(config.excel_file)
    books = parser.parse()

    # 获取统计信息
    stats = parser.get_statistics(books)
    print(f"✓ 共解析到 {stats['total']} 本书籍")
    print(f"  - 包含作者信息: {stats['has_author']} 本")
    print(f"  - 分类数量: {len(stats['categories'])} 个")

    # 显示分类统计
    print("\n分类统计:")
    for category, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        if category:
            print(f"  - {category}: {count} 本")

    # 导入到数据库
    print("\n正在导入数据库...")
    imported = 0
    for book in books:
        try:
            db.insert_book(
                title=book['title'],
                author=book['author'],
                category=book['category'],
                notes=book['notes']
            )
            imported += 1
        except Exception as e:
            print(f"  警告: 导入失败 - {book['title']}: {e}")

    print(f"✓ 成功导入 {imported} 本书籍")


def show_statistics(db: Database):
    """显示统计信息"""
    stats = db.get_statistics()
    print("\n" + "="*50)
    print("系统统计")
    print("="*50)
    print(f"总书籍数: {stats['total']}")
    print(f"已找到资源: {stats['found']}")
    print(f"已完成: {stats['completed']}")
    print(f"失败: {stats['failed']}")
    print(f"验证失败: {stats['validation_failed']}")
    print(f"待处理: {stats['pending']}")
    print(f"搜索候选结果: {stats['total_candidates']}")
    print(f"成功率: {stats['success_rate']}")
    print("="*50)


def search_books(config: Config, db: Database):
    """搜索书籍资源"""
    print("\n开始搜索书籍资源...")

    # 获取待搜索的书籍
    books = db.get_all_books(status='pending')
    if not books:
        print("没有待搜索的书籍")
        return

    print(f"共有 {len(books)} 本书籍待搜索")

    # 初始化搜索引擎
    search_engine = SearchEngine(config)

    # 搜索每本书
    for i, book in enumerate(books, 1):
        print(f"\n[{i}/{len(books)}] {book['title']}")

        try:
            # 搜索
            results = search_engine.search(book['title'], book['author'])
            db.clear_search_results(book['id'])

            if results:
                for result in results:
                    db.insert_search_result(
                        book_id=book['id'],
                        source=result.source,
                        title=result.title,
                        author=result.author,
                        download_url=result.download_url,
                        file_format=result.file_format,
                        file_size=result.file_size,
                        score=result.score,
                        is_open_access=getattr(result, 'is_open_access', False),
                        notes=getattr(result, 'notes', None)
                    )

                # 选择最佳结果
                best_result = next((result for result in results if result.download_url), results[0])
                print(f"  ✓ 找到 {len(results)} 个候选资源 (最佳评分: {best_result.score:.1f})")
                print(f"    来源: {best_result.source}")
                print(f"    格式: {best_result.file_format}")
                if best_result.file_size:
                    print(f"    大小: {best_result.file_size}")

                # 更新数据库
                db.update_book_status(
                    book['id'],
                    status='found',
                    download_url=best_result.download_url
                )
                db.log_download_attempt(
                    book['id'],
                    source=best_result.source,
                    status='found'
                )
            else:
                print(f"  ✗ 未找到资源")
                db.log_download_attempt(
                    book['id'],
                    source='all',
                    status='not_found',
                    error_message='No results found'
                )

        except Exception as e:
            print(f"  ✗ 搜索出错: {e}")
            db.log_download_attempt(
                book['id'],
                source='all',
                status='error',
                error_message=str(e)
            )

    # 显示搜索结果统计
    show_statistics(db)


def show_candidates(db: Database, book_id: int = None):
    """显示搜索候选结果"""
    if book_id is None:
        rows = db.get_report_rows()
        rows = [row for row in rows if row.get('candidate_count')]
        if not rows:
            print("\n暂无搜索候选结果，请先运行 --search")
            return

        print("\n搜索候选概览")
        print("="*80)
        for row in rows:
            score = row.get('best_candidate_score')
            score_text = f"{score:.1f}" if isinstance(score, (int, float)) else "-"
            print(
                f"[{row['id']}] {row['title']} | "
                f"候选: {row['candidate_count']} | 最高评分: {score_text}"
            )
        print("="*80)
        print("查看单本详情: python main.py --candidates --book-id <ID>")
        return

    book = db.get_book(book_id)
    if not book:
        print(f"\n未找到书籍ID: {book_id}")
        return

    results = db.get_search_results(book_id=book_id)
    print("\n" + "="*80)
    print(f"书籍: [{book['id']}] {book['title']}")
    if book.get('author'):
        print(f"作者: {book['author']}")
    print("="*80)

    if not results:
        print("暂无候选结果，请先运行 --search")
        return

    for i, result in enumerate(results, 1):
        access_label = "开放" if result.get('is_open_access') else "待确认"
        score = result.get('score') or 0
        print(f"\n{i}. {result['title']}")
        print(f"   来源: {result.get('source') or '-'} | 评分: {score:.1f} | 访问: {access_label}")
        if result.get('author'):
            print(f"   作者: {result['author']}")
        if result.get('file_format') or result.get('file_size'):
            print(f"   文件: {result.get('file_format') or '-'} / {result.get('file_size') or '-'}")
        if result.get('download_url'):
            print(f"   链接: {result['download_url']}")
        if result.get('notes'):
            print(f"   备注: {result['notes']}")


def _build_download_filename(book: dict, candidate: dict = None) -> str:
    """为下载候选构建文件名"""
    title = book['title']
    author = book.get('author')
    file_format = (candidate or {}).get('file_format') or 'pdf'

    filename = f"{title}"
    if author:
        filename += f"_{author}"
    filename += f".{file_format.lower()}"
    return filename


def _normalize_candidate_text(value: str) -> str:
    """规范化候选文本，便于关键词过滤"""
    return ' '.join(str(value or '').lower().replace('_', ' ').split())


def _parse_candidate_size_bytes(file_size: str) -> int:
    """解析候选文件大小文本"""
    if not file_size:
        return 0

    text = str(file_size).strip().upper().replace(' ', '')
    match = None
    import re
    match = re.match(r'^(\d+(?:\.\d+)?)(B|KB|MB|GB)$', text)
    if not match:
        return 0

    value = float(match.group(1))
    unit = match.group(2)
    factor = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
    }[unit]
    return int(value * factor)


def _candidate_rejection_reason(result: dict, config: Config) -> str:
    """判断候选是否应被过滤，返回过滤原因"""
    download_url = result.get('download_url') or ''
    if not download_url:
        return '缺少下载链接'

    file_format = (result.get('file_format') or '').lower()
    if file_format and file_format not in ALLOWED_DOWNLOAD_FORMATS:
        return f'不支持的格式: {file_format}'

    normalized_url = _normalize_candidate_text(download_url)
    normalized_title = _normalize_candidate_text(result.get('title'))
    normalized_notes = _normalize_candidate_text(result.get('notes'))

    for keyword in BLOCKED_CANDIDATE_KEYWORDS:
        if keyword in normalized_url or keyword in normalized_title or keyword in normalized_notes:
            return f'疑似非全文资源: {keyword}'

    blocked_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.jp2', '.xml')
    if normalized_url.endswith(blocked_extensions):
        return '疑似图片或元数据文件'

    size_bytes = _parse_candidate_size_bytes(result.get('file_size'))
    min_file_size = config.get('validation.min_file_size', 102400)
    if size_bytes and size_bytes < min_file_size:
        return f'候选文件过小: {result.get("file_size")}'

    return ''


def _get_download_candidates(db: Database, book: dict, config: Config) -> list:
    """获取当前书籍的下载候选，优先使用搜索候选表"""
    candidates = []
    seen_urls = set()

    for result in db.get_search_results(book_id=book['id'], only_downloadable=True):
        url = result.get('download_url')
        if not url or url in seen_urls:
            continue
        rejection_reason = _candidate_rejection_reason(result, config)
        if rejection_reason:
            print(
                f"  跳过候选 | 来源: {result.get('source') or '-'} | "
                f"原因: {rejection_reason}"
            )
            continue
        seen_urls.add(url)
        candidates.append({
            'source': result.get('source') or 'search_result',
            'download_url': url,
            'file_format': result.get('file_format') or 'pdf',
            'score': result.get('score') or 0,
            'title': result.get('title') or book['title'],
            'author': result.get('author') or book.get('author'),
            'notes': result.get('notes'),
            'file_size': result.get('file_size'),
        })

    if book.get('download_url') and book['download_url'] not in seen_urls:
        fallback_candidate = {
            'source': 'book_record',
            'download_url': book['download_url'],
            'file_format': 'pdf',
            'score': 0,
            'title': book['title'],
            'author': book.get('author'),
            'notes': '',
            'file_size': None,
        }
        rejection_reason = _candidate_rejection_reason(fallback_candidate, config)
        if not rejection_reason:
            candidates.append(fallback_candidate)
        else:
            print(f"  跳过书籍默认链接 | 原因: {rejection_reason}")

    return candidates


def _find_book_for_wrong_file(db: Database, wrong_path: Path) -> dict | None:
    """根据wrong目录中的文件，尽量匹配到数据库中的书籍记录"""
    wrong_name = wrong_path.name
    wrong_stem = wrong_path.stem
    wrong_norm = _normalize_match_text(wrong_stem)

    books = db.get_all_books()

    # 先按当前数据库记录的文件名精确/前缀匹配
    for book in books:
        file_path = book.get('file_path')
        if not file_path:
            continue
        book_file = Path(file_path)
        if book_file.name == wrong_name:
            return book
        if wrong_stem.startswith(book_file.stem) or book_file.stem.startswith(wrong_stem):
            return book

    # 再用标题和作者做弱匹配，兼容被手动改过名字的wrong文件
    for book in books:
        title_norm = _normalize_match_text(book.get('title'))
        author_norm = _normalize_match_text(book.get('author'))
        if title_norm and title_norm in wrong_norm:
            if not author_norm or author_norm in wrong_norm:
                return book

    return None


def sync_wrong_files(config: Config, db: Database):
    """扫描wrong目录，把人工确认的错文件回写到数据库"""
    print("\n开始同步 wrong 目录中的人工判错文件...")

    download_root = Path(config.download_dir)
    wrong_files = sorted(download_root.glob('**/wrong/*'))
    wrong_files = [path for path in wrong_files if path.is_file()]

    if not wrong_files:
        print("未找到 wrong 目录中的文件")
        return

    print(f"发现 {len(wrong_files)} 个 wrong 文件")
    matched_count = 0
    skipped_count = 0

    for wrong_path in wrong_files:
        print(f"\n检查: {wrong_path}")
        book = _find_book_for_wrong_file(db, wrong_path)
        if not book:
            skipped_count += 1
            print("  ✗ 未匹配到数据库书籍记录")
            continue

        matched_count += 1
        previous_url = book.get('download_url')
        print(f"  关联书籍: [{book['id']}] {book['title']}")

        if previous_url:
            db.delete_search_result_by_url(book['id'], previous_url)

        db.replace_book_download_state(
            book['id'],
            status='failed',
            download_url=None,
            file_path=None
        )
        db.log_download_attempt(
            book['id'],
            source='wrong_folder',
            status='wrong_file',
            error_message=f'人工放入wrong目录: {wrong_path}'
        )
        print("  ✓ 已移除错误记录，状态改为 failed")

    print(f"\n同步完成: 匹配 {matched_count} 本，未匹配 {skipped_count} 个文件")
    show_statistics(db)


def _try_download_candidates(book: dict, candidates: list,
                             downloader: Downloader,
                             validator: FileValidator,
                             db: Database) -> bool:
    """按候选顺序尝试下载并验证"""
    if not candidates:
        db.update_book_status(book['id'], status='failed')
        db.log_download_attempt(
            book['id'],
            source='download',
            status='failed',
            error_message='No downloadable candidates'
        )
        print("  ✗ 没有可下载候选")
        return False

    last_error = None

    for index, candidate in enumerate(candidates, 1):
        source = candidate.get('source') or 'unknown'
        print(
            f"  尝试候选 {index}/{len(candidates)} | "
            f"来源: {source} | 评分: {candidate.get('score', 0):.1f}"
        )

        file_path = downloader.download(
            url=candidate.get('download_url'),
            filename=_build_download_filename(book, candidate),
            category=book.get('category')
        )

        if not file_path:
            last_error = f"Download failed from {source}"
            db.log_download_attempt(
                book['id'],
                source=source,
                status='failed',
                error_message=last_error
            )
            continue

        validation = validator.validate(
            file_path,
            expected_title=book['title'],
            expected_author=book.get('author')
        )

        if validation.is_valid:
            db.update_book_status(
                book['id'],
                status='completed',
                download_url=candidate.get('download_url'),
                file_path=file_path
            )
            db.log_download_attempt(
                book['id'],
                source=source,
                status='completed'
            )
            if validation.warnings:
                print(f"  验证警告: {'; '.join(validation.warnings)}")
            return True

        last_error = '; '.join(validation.errors) or 'Validation failed'
        print(f"  ✗ 文件验证失败: {last_error}")
        try:
            invalid_path = Path(file_path)
            if invalid_path.exists():
                invalid_path.unlink()
                print(f"  已移除无效文件: {invalid_path.name}")
        except OSError as cleanup_error:
            print(f"  警告: 无法移除无效文件: {cleanup_error}")
        db.log_download_attempt(
            book['id'],
            source=source,
            status='validation_failed',
            error_message=last_error
        )

    db.update_book_status(book['id'], status='failed')
    db.log_download_attempt(
        book['id'],
        source='download',
        status='failed',
        error_message=last_error or 'All candidates failed'
    )
    return False


def download_books(config: Config, db: Database):
    """下载书籍"""
    print("\n开始下载书籍...")

    # 获取可重试下载的书籍
    books = [
        book for book in db.get_all_books()
        if book.get('status') in {'found', 'failed', 'validation_failed'}
    ]
    if not books:
        print("没有可下载的书籍（请先运行 --search，或确认存在可重试候选）")
        return

    print(f"共有 {len(books)} 本书籍待下载")

    # 初始化下载器
    downloader = Downloader(config)
    validator = FileValidator(config)

    # 下载每本书
    for i, book in enumerate(books, 1):
        print(f"\n[{i}/{len(books)}] {book['title']}")

        try:
            candidates = _get_download_candidates(db, book, config)
            _try_download_candidates(book, candidates, downloader, validator, db)

        except Exception as e:
            print(f"  ✗ 下载出错: {e}")
            db.update_book_status(book['id'], status='failed')
            db.log_download_attempt(
                book['id'],
                source='download',
                status='error',
                error_message=str(e)
            )

    # 显示下载结果统计
    show_statistics(db)


def validate_books(config: Config, db: Database):
    """验证已下载文件"""
    print("\n开始验证已下载文件...")

    books = [book for book in db.get_all_books() if book.get('file_path')]
    if not books:
        print("没有可验证的文件")
        return

    validator = FileValidator(config)
    valid_count = 0
    invalid_count = 0

    for i, book in enumerate(books, 1):
        print(f"\n[{i}/{len(books)}] {book['title']}")
        result = validator.validate(
            book['file_path'],
            expected_title=book['title'],
            expected_author=book['author']
        )

        if result.is_valid:
            valid_count += 1
            db.update_book_status(book['id'], status='completed', file_path=book['file_path'])
            db.log_download_attempt(book['id'], source='validator', status='completed')
            print(f"  ✓ 验证通过 ({result.file_format}, {validator.human_size(result.file_size)})")
            if result.page_count is not None:
                print(f"    页数: {result.page_count}")
            if result.warnings:
                print(f"    警告: {'; '.join(result.warnings)}")
        else:
            invalid_count += 1
            errors = '; '.join(result.errors)
            db.update_book_status(book['id'], status='validation_failed', file_path=book['file_path'])
            db.log_download_attempt(
                book['id'],
                source='validator',
                status='validation_failed',
                error_message=errors
            )
            print(f"  ✗ 验证失败: {errors}")

    print(f"\n验证完成: 通过 {valid_count} 个，失败 {invalid_count} 个")
    show_statistics(db)


def generate_report(config: Config, db: Database, report_format: str,
                    output_path: str = None):
    """生成下载报告"""
    generator = ReportGenerator(config, db)
    report_path = generator.generate(output_path=output_path, report_format=report_format)
    print(f"\n✓ 报告已生成: {report_path}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='学术书籍智能下载系统',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--init',
        action='store_true',
        help='初始化系统并导入书籍清单'
    )

    parser.add_argument(
        '--stats',
        action='store_true',
        help='显示统计信息'
    )

    parser.add_argument(
        '--search',
        action='store_true',
        help='开始搜索书籍资源'
    )

    parser.add_argument(
        '--download',
        action='store_true',
        help='开始下载书籍'
    )

    parser.add_argument(
        '--validate',
        action='store_true',
        help='验证已下载文件'
    )

    parser.add_argument(
        '--sync-wrong',
        action='store_true',
        help='同步 wrong 目录中的人工判错文件'
    )

    parser.add_argument(
        '--report',
        action='store_true',
        help='生成下载报告'
    )

    parser.add_argument(
        '--candidates',
        action='store_true',
        help='查看搜索候选结果'
    )

    parser.add_argument(
        '--book-id',
        type=int,
        help='指定书籍ID'
    )

    parser.add_argument(
        '--report-format',
        choices=['xlsx', 'csv', 'md'],
        default='xlsx',
        help='报告格式（默认: xlsx）'
    )

    parser.add_argument(
        '--report-output',
        help='报告输出路径'
    )

    args = parser.parse_args()

    # 加载配置
    try:
        config = Config('config.yaml')
    except FileNotFoundError:
        print("错误: 配置文件 config.yaml 不存在")
        return 1

    # 初始化数据库
    db = init_system(config)

    try:
        if args.init:
            # 初始化并导入书籍
            load_books(config, db)
            show_statistics(db)

        elif args.stats:
            # 显示统计信息
            show_statistics(db)

        elif args.search:
            # 搜索书籍资源
            search_books(config, db)

        elif args.download:
            # 下载书籍
            download_books(config, db)

        elif args.validate:
            # 验证已下载文件
            validate_books(config, db)

        elif args.sync_wrong:
            # 同步人工判错文件
            sync_wrong_files(config, db)

        elif args.report:
            # 生成下载报告
            generate_report(config, db, args.report_format, args.report_output)

        elif args.candidates:
            # 查看搜索候选结果
            show_candidates(db, args.book_id)

        else:
            parser.print_help()

    finally:
        db.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())
