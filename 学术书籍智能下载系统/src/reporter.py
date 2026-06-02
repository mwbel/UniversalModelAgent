"""报告生成模块"""

import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ReportGenerator:
    """下载结果报告生成器"""

    def __init__(self, config, db):
        self.config = config
        self.db = db
        self.report_dir = Path(config.get('paths.log_dir', 'logs')) / 'reports'
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, output_path: Optional[str] = None,
                 report_format: str = 'xlsx') -> str:
        """生成下载报告"""
        report_format = report_format.lower().lstrip('.')
        rows = [self._format_row(row) for row in self.db.get_report_rows()]
        summary = self._build_summary(rows)
        path = Path(output_path) if output_path else self._default_path(report_format)
        path.parent.mkdir(parents=True, exist_ok=True)

        if report_format == 'xlsx':
            self._write_xlsx(path, rows, summary)
        elif report_format == 'csv':
            self._write_csv(path, rows)
        elif report_format in {'md', 'markdown'}:
            self._write_markdown(path, rows, summary)
        else:
            raise ValueError(f"不支持的报告格式: {report_format}")

        return str(path)

    def _default_path(self, report_format: str) -> Path:
        """生成默认报告路径"""
        suffix = 'md' if report_format == 'markdown' else report_format
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return self.report_dir / f"download_report_{timestamp}.{suffix}"

    def _format_row(self, row: Dict) -> Dict:
        """统一报告字段"""
        status = row.get('status') or 'unknown'
        return {
            'ID': row.get('id'),
            '书名': row.get('title') or '',
            '作者': row.get('author') or '',
            '分类': row.get('category') or '',
            '状态': status,
            '状态说明': self._status_label(status),
            '文件路径': row.get('file_path') or '',
            '下载链接': row.get('download_url') or '',
            '候选数量': row.get('candidate_count') or 0,
            '最高候选评分': row.get('best_candidate_score') or '',
            '最近来源': row.get('latest_source') or '',
            '最近日志状态': row.get('latest_log_status') or '',
            '最近错误': row.get('latest_error') or '',
            '最近尝试时间': row.get('latest_attempt_time') or '',
            '更新时间': row.get('updated_at') or '',
            '备注': row.get('notes') or '',
        }

    def _build_summary(self, rows: List[Dict]) -> List[Dict]:
        """生成汇总信息"""
        total = len(rows)
        status_counts = {}
        category_counts = {}

        for row in rows:
            status = row['状态']
            category = row['分类'] or '未分类'
            status_counts[status] = status_counts.get(status, 0) + 1
            category_counts[category] = category_counts.get(category, 0) + 1

        summary = [
            {'指标': '总书籍数', '数量': total, '说明': ''},
            {
                '指标': '下载完成',
                '数量': status_counts.get('completed', 0),
                '说明': self._rate(status_counts.get('completed', 0), total),
            },
            {
                '指标': '已找到资源',
                '数量': status_counts.get('found', 0),
                '说明': self._rate(status_counts.get('found', 0), total),
            },
            {
                '指标': '待处理',
                '数量': status_counts.get('pending', 0),
                '说明': self._rate(status_counts.get('pending', 0), total),
            },
            {
                '指标': '失败',
                '数量': status_counts.get('failed', 0),
                '说明': self._rate(status_counts.get('failed', 0), total),
            },
            {
                '指标': '验证失败',
                '数量': status_counts.get('validation_failed', 0),
                '说明': self._rate(status_counts.get('validation_failed', 0), total),
            },
        ]

        for category, count in sorted(category_counts.items(), key=lambda item: item[1], reverse=True):
            summary.append({
                '指标': f"分类: {category}",
                '数量': count,
                '说明': self._rate(count, total),
            })

        return summary

    def _write_xlsx(self, path: Path, rows: List[Dict], summary: List[Dict]):
        """写入Excel报告"""
        import pandas as pd

        with pd.ExcelWriter(path, engine='openpyxl') as writer:
            pd.DataFrame(rows).to_excel(writer, index=False, sheet_name='明细')
            pd.DataFrame(summary).to_excel(writer, index=False, sheet_name='汇总')

            detail_sheet = writer.sheets['明细']
            summary_sheet = writer.sheets['汇总']
            self._autosize_columns(detail_sheet)
            self._autosize_columns(summary_sheet)

    def _write_csv(self, path: Path, rows: List[Dict]):
        """写入CSV报告"""
        fieldnames = list(rows[0].keys()) if rows else []
        with path.open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def _write_markdown(self, path: Path, rows: List[Dict], summary: List[Dict]):
        """写入Markdown报告"""
        lines = [
            '# 下载报告',
            '',
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            '',
            '## 汇总',
            '',
            '| 指标 | 数量 | 说明 |',
            '| --- | ---: | --- |',
        ]

        for row in summary:
            lines.append(f"| {row['指标']} | {row['数量']} | {row['说明']} |")

        lines.extend([
            '',
            '## 明细',
            '',
            '| ID | 书名 | 作者 | 分类 | 状态 | 文件路径 | 最近错误 |',
            '| ---: | --- | --- | --- | --- | --- | --- |',
        ])

        for row in rows:
            lines.append(
                f"| {row['ID']} | {self._escape_md(row['书名'])} | "
                f"{self._escape_md(row['作者'])} | {self._escape_md(row['分类'])} | "
                f"{self._escape_md(row['状态说明'])} | {self._escape_md(row['文件路径'])} | "
                f"{self._escape_md(row['最近错误'])} |"
            )

        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    def _autosize_columns(self, sheet):
        """按内容粗略调整Excel列宽"""
        for column_cells in sheet.columns:
            values = [str(cell.value) for cell in column_cells if cell.value is not None]
            if not values:
                continue
            width = min(max(len(value) for value in values) + 2, 60)
            sheet.column_dimensions[column_cells[0].column_letter].width = width

    def _status_label(self, status: str) -> str:
        """状态中文说明"""
        labels = {
            'pending': '待搜索',
            'found': '已找到资源',
            'completed': '已完成',
            'failed': '失败',
            'validation_failed': '验证失败',
        }
        return labels.get(status, status)

    def _rate(self, value: int, total: int) -> str:
        """百分比字符串"""
        if total <= 0:
            return '0.0%'
        return f"{value / total * 100:.1f}%"

    def _escape_md(self, value: str) -> str:
        """转义Markdown表格内容"""
        return str(value).replace('|', '\\|').replace('\n', ' ')
