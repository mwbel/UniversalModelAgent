"""搜索引擎模块 - 多源书籍搜索"""

import re
import time
import random
import requests
import xml.etree.ElementTree as ET
from typing import List, Dict
from urllib.parse import quote
from bs4 import BeautifulSoup


class SearchResult:
    """搜索结果类"""

    def __init__(self, title: str, author: str = None, download_url: str = None,
                 source: str = None, file_format: str = None, file_size: str = None,
                 is_open_access: bool = False, notes: str = None):
        self.title = title
        self.author = author
        self.download_url = download_url
        self.source = source
        self.file_format = file_format
        self.file_size = file_size
        self.is_open_access = is_open_access
        self.notes = notes
        self.score = 0.0

    def __repr__(self):
        return f"<SearchResult: {self.title} ({self.source})>"


class BaseSearcher:
    """搜索器基类"""

    def __init__(self, config):
        self.config = config
        self.user_agents = config.get('user_agents', [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        ])
        self.delay = 3

    def get_headers(self) -> Dict:
        """获取随机请求头"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """搜索书籍（子类实现）"""
        raise NotImplementedError

    def _delay(self):
        """请求延迟"""
        time.sleep(self.delay + random.uniform(0, 1))

    def _get_source_config(self, source_name: str) -> Dict:
        """获取指定搜索源配置"""
        for source in self.config.get('search_sources', []):
            if source.get('name') == source_name:
                return source
        return {}


class ArxivSearcher(BaseSearcher):
    """arXiv开放资源搜索器"""

    def __init__(self, config):
        super().__init__(config)
        source_config = self._get_source_config('arXiv')
        self.api_url = source_config.get('base_url', 'https://export.arxiv.org/api/query')
        self.delay = source_config.get('delay', 3)
        self.max_results = source_config.get('max_results', 5)

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """通过arXiv API搜索开放PDF"""
        results = []

        try:
            queries = self._build_queries(title, author)
            seen_urls = set()

            for query in queries:
                print(f"  [arXiv] 搜索: {query}")
                response = requests.get(
                    self.api_url,
                    params={
                        'search_query': query,
                        'start': 0,
                        'max_results': self.max_results,
                        'sortBy': 'relevance',
                        'sortOrder': 'descending',
                    },
                    headers=self.get_headers(),
                    timeout=30
                )

                if response.status_code != 200:
                    print(f"  [arXiv] 请求失败: {response.status_code}")
                    continue

                for result in self._parse_feed(response.text):
                    if result.download_url in seen_urls:
                        continue
                    seen_urls.add(result.download_url)
                    results.append(result)

                if results:
                    break

            print(f"  [arXiv] 找到 {len(results)} 个开放PDF")

        except Exception as e:
            print(f"  [arXiv] 搜索出错: {e}")

        self._delay()
        return results

    def _build_queries(self, title: str, author: str = None) -> List[str]:
        """构建arXiv查询语句"""
        safe_title = self._escape_query_value(title)
        queries = []

        author_terms = self._author_terms(author)
        if author_terms:
            queries.append(f'ti:"{safe_title}" AND au:"{author_terms[0]}"')

        queries.append(f'ti:"{safe_title}"')
        queries.append(f'all:"{safe_title}"')
        return queries

    def _parse_feed(self, xml_text: str) -> List[SearchResult]:
        """解析arXiv Atom Feed"""
        results = []
        namespaces = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom',
        }
        root = ET.fromstring(xml_text)

        for entry in root.findall('atom:entry', namespaces):
            title = self._clean_text(entry.findtext('atom:title', default='', namespaces=namespaces))
            if not title:
                continue

            authors = []
            for author in entry.findall('atom:author', namespaces):
                name = author.findtext('atom:name', default='', namespaces=namespaces)
                if name:
                    authors.append(self._clean_text(name))

            abs_url = entry.findtext('atom:id', default='', namespaces=namespaces)
            pdf_url = self._extract_pdf_url(entry, namespaces, abs_url)
            if not pdf_url:
                continue

            published = entry.findtext('atom:published', default='', namespaces=namespaces)
            category = self._extract_primary_category(entry, namespaces)
            notes = 'arXiv开放获取论文'
            if published:
                notes += f"; 发布: {published[:10]}"
            if category:
                notes += f"; 分类: {category}"

            results.append(SearchResult(
                title=title,
                author=', '.join(authors) if authors else None,
                download_url=pdf_url,
                source='arXiv',
                file_format='pdf',
                file_size=None,
                is_open_access=True,
                notes=notes
            ))

        return results

    def _extract_pdf_url(self, entry, namespaces: Dict, abs_url: str) -> str:
        """提取arXiv PDF链接"""
        for link in entry.findall('atom:link', namespaces):
            link_type = link.attrib.get('type', '')
            link_title = link.attrib.get('title', '')
            href = link.attrib.get('href', '')
            if href and (link_type == 'application/pdf' or link_title == 'pdf'):
                return href.replace('http://', 'https://', 1)

        if abs_url and '/abs/' in abs_url:
            return abs_url.replace('http://', 'https://', 1).replace('/abs/', '/pdf/')
        return ''

    def _extract_primary_category(self, entry, namespaces: Dict) -> str:
        """提取arXiv主分类"""
        primary = entry.find('arxiv:primary_category', namespaces)
        if primary is not None:
            return primary.attrib.get('term', '')
        return ''

    def _author_terms(self, author: str = None) -> List[str]:
        """提取适合arXiv作者查询的作者关键词"""
        if not author:
            return []

        parts = re.split(r'\s*(?:,|&|;|\band\b)\s*', author)
        terms = []
        for part in parts:
            words = [word for word in re.split(r'\s+', part.strip()) if len(word) > 1]
            if words:
                terms.append(self._escape_query_value(words[-1]))
        return terms

    def _escape_query_value(self, value: str) -> str:
        """清理arXiv查询值中的引号"""
        return (value or '').replace('"', ' ').strip()

    def _clean_text(self, value: str) -> str:
        """清理Atom文本中的多余空白"""
        return ' '.join((value or '').split())


class InternetArchiveSearcher(BaseSearcher):
    """Internet Archive开放馆藏搜索器"""

    def __init__(self, config):
        super().__init__(config)
        source_config = self._get_source_config('Internet Archive')
        self.search_url = source_config.get(
            'base_url',
            'https://archive.org/advancedsearch.php'
        )
        self.metadata_url = source_config.get(
            'metadata_url',
            'https://archive.org/metadata'
        )
        self.delay = source_config.get('delay', 3)
        self.max_results = source_config.get('max_results', 5)

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """搜索Internet Archive可下载文本资源"""
        results = []

        try:
            queries = self._build_queries(title, author)
            seen_urls = set()

            for query in queries:
                print(f"  [Internet Archive] 搜索: {query}")
                response = requests.get(
                    self.search_url,
                    params={
                        'q': query,
                        'fl[]': [
                            'identifier', 'title', 'creator', 'year',
                            'downloads', 'publicdate'
                        ],
                        'rows': self.max_results,
                        'page': 1,
                        'output': 'json',
                    },
                    headers=self.get_headers(),
                    timeout=30
                )

                if response.status_code != 200:
                    print(f"  [Internet Archive] 请求失败: {response.status_code}")
                    continue

                docs = response.json().get('response', {}).get('docs', [])
                for doc in docs:
                    result = self._build_result_from_doc(doc)
                    if not result or result.download_url in seen_urls:
                        continue
                    seen_urls.add(result.download_url)
                    results.append(result)

                if results:
                    break

            print(f"  [Internet Archive] 找到 {len(results)} 个可下载资源")

        except Exception as e:
            print(f"  [Internet Archive] 搜索出错: {e}")

        self._delay()
        return results

    def _build_queries(self, title: str, author: str = None) -> List[str]:
        """构建Internet Archive查询语句"""
        safe_title = self._escape_query_value(title)
        queries = []

        if author:
            author_terms = self._author_terms(author)
            if author_terms:
                queries.append(
                    f'title:("{safe_title}") AND creator:("{author_terms[0]}") '
                    f'AND mediatype:(texts)'
                )

        queries.append(f'title:("{safe_title}") AND mediatype:(texts)')
        queries.append(f'("{safe_title}") AND mediatype:(texts)')
        return queries

    def _build_result_from_doc(self, doc: Dict) -> SearchResult:
        """将搜索结果条目转换为可下载候选"""
        identifier = doc.get('identifier')
        if not identifier:
            return None

        file_info = self._best_downloadable_file(identifier)
        if not file_info:
            return None

        title = self._coerce_text(doc.get('title')) or identifier
        creator = self._coerce_text(doc.get('creator'))
        year = self._coerce_text(doc.get('year'))
        downloads = self._coerce_text(doc.get('downloads'))
        publicdate = self._coerce_text(doc.get('publicdate'))

        notes = f"Internet Archive馆藏: {identifier}"
        if year:
            notes += f"; 年份: {year}"
        if downloads:
            notes += f"; 下载量: {downloads}"
        if publicdate:
            notes += f"; 入库: {publicdate[:10]}"

        return SearchResult(
            title=title,
            author=creator,
            download_url=self._download_url(identifier, file_info['name']),
            source='Internet Archive',
            file_format=file_info['file_format'],
            file_size=file_info.get('size'),
            is_open_access=True,
            notes=notes
        )

    def _best_downloadable_file(self, identifier: str) -> Dict:
        """从metadata中选择最适合下载的文件"""
        response = requests.get(
            f"{self.metadata_url}/{quote(identifier, safe='')}",
            headers=self.get_headers(),
            timeout=30
        )

        if response.status_code != 200:
            return {}

        files = response.json().get('files', [])
        candidates = []
        for file_info in files:
            file_format = self._detect_file_format(file_info)
            if not file_format:
                continue
            candidates.append({
                'name': file_info.get('name'),
                'file_format': file_format,
                'size': self._format_size(file_info.get('size')),
                'rank': self._format_rank(file_info, file_format),
            })

        if not candidates:
            return {}

        candidates.sort(key=lambda item: item['rank'], reverse=True)
        return candidates[0]

    def _detect_file_format(self, file_info: Dict) -> str:
        """识别可下载文件格式"""
        name = (file_info.get('name') or '').lower()
        file_format = (file_info.get('format') or '').lower()

        if name.endswith('.pdf') and 'encrypted' not in name:
            return 'pdf'
        if name.endswith('.epub'):
            return 'epub'
        if name.endswith('.djvu'):
            return 'djvu'
        if 'text pdf' in file_format or file_format == 'pdf':
            return 'pdf'
        if 'epub' in file_format:
            return 'epub'
        if 'djvu' in file_format:
            return 'djvu'
        return ''

    def _format_rank(self, file_info: Dict, file_format: str) -> int:
        """按可读性和格式偏好给文件排序"""
        name = (file_info.get('name') or '').lower()
        rank = {'pdf': 30, 'epub': 20, 'djvu': 10}.get(file_format, 0)
        if '_text.pdf' in name or file_info.get('format') == 'Text PDF':
            rank += 10
        if 'encrypted' in name:
            rank -= 50
        return rank

    def _download_url(self, identifier: str, filename: str) -> str:
        """构建archive.org文件下载链接"""
        return (
            f"https://archive.org/download/{quote(identifier, safe='')}/"
            f"{quote(filename or '', safe='')}"
        )

    def _format_size(self, size_value) -> str:
        """格式化Internet Archive文件大小"""
        try:
            size = int(size_value)
        except (TypeError, ValueError):
            return None

        units = ['B', 'KB', 'MB', 'GB']
        value = float(size)
        for unit in units:
            if value < 1024 or unit == units[-1]:
                return f"{value:.1f}{unit}"
            value /= 1024

    def _coerce_text(self, value) -> str:
        """将API字段转换为字符串"""
        if value is None:
            return ''
        if isinstance(value, list):
            return ', '.join(str(item) for item in value if item is not None)
        return str(value)

    def _escape_query_value(self, value: str) -> str:
        """清理Internet Archive查询值中的引号"""
        return (value or '').replace('"', ' ').strip()

    def _author_terms(self, author: str = None) -> List[str]:
        """提取作者查询关键词"""
        if not author:
            return []

        terms = []
        for part in re.split(r'\s*(?:,|&|;|\band\b)\s*', author):
            cleaned = self._escape_query_value(part)
            if cleaned:
                terms.append(cleaned)
        return terms


class LibgenSearcher(BaseSearcher):
    """Library Genesis 搜索器"""

    def __init__(self, config):
        super().__init__(config)
        self.base_url = "http://libgen.rs"
        self.search_url = f"{self.base_url}/search.php"

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """搜索Library Genesis"""
        results = []

        try:
            # 构建搜索查询
            query = title
            if author:
                query = f"{title} {author}"

            params = {
                'req': query,
                'lg_topic': 'libgen',
                'open': 0,
                'view': 'simple',
                'res': 25,
                'phrase': 1,
                'column': 'def'
            }

            print(f"  [Libgen] 搜索: {query}")
            response = requests.get(
                self.search_url,
                params=params,
                headers=self.get_headers(),
                timeout=30
            )

            if response.status_code != 200:
                print(f"  [Libgen] 请求失败: {response.status_code}")
                return results

            soup = BeautifulSoup(response.text, 'html.parser')

            # 解析搜索结果表格
            table = soup.find('table', {'class': 'c'})
            if not table:
                print(f"  [Libgen] 未找到结果")
                return results

            rows = table.find_all('tr')[1:]  # 跳过表头

            for row in rows[:5]:  # 只取前5个结果
                cols = row.find_all('td')
                if len(cols) < 10:
                    continue

                # 提取信息
                book_title = cols[2].get_text(strip=True)
                book_author = cols[1].get_text(strip=True)
                file_format = cols[8].get_text(strip=True).lower()
                file_size = cols[7].get_text(strip=True)

                # 提取下载链接
                download_links = cols[9].find_all('a')
                download_url = None
                if download_links:
                    download_url = download_links[0].get('href')
                    if download_url and not download_url.startswith('http'):
                        download_url = self.base_url + download_url

                result = SearchResult(
                    title=book_title,
                    author=book_author,
                    download_url=download_url,
                    source="Library Genesis",
                    file_format=file_format,
                    file_size=file_size
                )

                results.append(result)

            print(f"  [Libgen] 找到 {len(results)} 个结果")

        except Exception as e:
            print(f"  [Libgen] 搜索出错: {e}")

        self._delay()
        return results


class GoogleScholarSearcher(BaseSearcher):
    """Google Scholar 搜索器（仅搜索开放PDF）"""

    def __init__(self, config):
        super().__init__(config)
        self.base_url = "https://scholar.google.com"
        self.delay = 5  # Google需要更长延迟

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """搜索Google Scholar"""
        results = []

        try:
            # 构建搜索查询
            query = f'"{title}"'
            if author:
                query += f' author:"{author}"'

            params = {
                'q': query,
                'hl': 'en',
                'as_sdt': '0,5'
            }

            print(f"  [Scholar] 搜索: {query}")
            response = requests.get(
                f"{self.base_url}/scholar",
                params=params,
                headers=self.get_headers(),
                timeout=30
            )

            if response.status_code != 200:
                print(f"  [Scholar] 请求失败: {response.status_code}")
                return results

            soup = BeautifulSoup(response.text, 'html.parser')

            # 查找搜索结果
            articles = soup.find_all('div', {'class': 'gs_r gs_or gs_scl'})

            for article in articles[:3]:  # 只取前3个结果
                # 提取标题
                title_tag = article.find('h3', {'class': 'gs_rt'})
                if not title_tag:
                    continue

                book_title = title_tag.get_text(strip=True)

                # 查找PDF链接
                pdf_link = article.find('div', {'class': 'gs_or_ggsm'})
                download_url = None

                if pdf_link:
                    link_tag = pdf_link.find('a')
                    if link_tag and '[PDF]' in link_tag.get_text():
                        download_url = link_tag.get('href')

                if download_url:
                    result = SearchResult(
                        title=book_title,
                        download_url=download_url,
                        source="Google Scholar",
                        file_format="pdf",
                        is_open_access=True,
                        notes="Google Scholar开放PDF链接"
                    )
                    results.append(result)

            print(f"  [Scholar] 找到 {len(results)} 个开放PDF")

        except Exception as e:
            print(f"  [Scholar] 搜索出错: {e}")

        self._delay()
        return results


class SearchEngine:
    """搜索引擎管理器"""

    def __init__(self, config):
        self.config = config
        self.searchers = []

        # 初始化搜索器
        search_sources = sorted(
            config.get('search_sources', []),
            key=lambda item: item.get('priority', 999)
        )
        for source in search_sources:
            if not source.get('enabled', True):
                continue

            source_name = source.get('name')
            if source_name == 'arXiv':
                self.searchers.append(ArxivSearcher(config))
            elif source_name == 'Internet Archive':
                self.searchers.append(InternetArchiveSearcher(config))
            elif source_name == 'Library Genesis':
                self.searchers.append(LibgenSearcher(config))
            elif source_name == 'Google Scholar':
                self.searchers.append(GoogleScholarSearcher(config))

    def search(self, title: str, author: str = None) -> List[SearchResult]:
        """多源搜索"""
        all_results = []

        print(f"\n搜索: {title}")
        if author:
            print(f"作者: {author}")

        for searcher in self.searchers:
            try:
                results = searcher.search(title, author)
                all_results.extend(results)
            except Exception as e:
                print(f"  搜索器错误: {e}")

        # 评分和排序
        scored_results = self._score_results(all_results, title, author)

        return scored_results

    def _score_results(self, results: List[SearchResult],
                      target_title: str, target_author: str = None) -> List[SearchResult]:
        """对搜索结果评分"""
        for result in results:
            score = 0.0

            # 标题相似度（40分）
            title_sim = self._similarity(result.title.lower(), target_title.lower())
            score += title_sim * 40

            # 作者匹配（30分）
            if target_author and result.author:
                author_sim = self._author_similarity(result.author, target_author)
                score += author_sim * 30
            elif not target_author:
                score += 15  # 无作者要求时给一半分

            # 文件格式（20分）
            file_format = (result.file_format or '').lower()
            if file_format == 'pdf':
                score += 20
            elif file_format in ['epub', 'djvu']:
                score += 10

            # 开放获取优先（8分）
            if getattr(result, 'is_open_access', False):
                score += 8

            # 来源可信度（10分）
            if result.source == 'arXiv':
                score += 10
            elif result.source == 'Internet Archive':
                score += 10
            elif result.source == 'Google Scholar':
                score += 9
            elif result.source == 'Library Genesis':
                score += 6

            result.score = score

        # 按分数排序
        results.sort(key=lambda x: x.score, reverse=True)
        return results

    def _similarity(self, s1: str, s2: str) -> float:
        """计算字符串相似度（简单版本）"""
        s1_words = set(s1.split())
        s2_words = set(s2.split())

        if not s1_words or not s2_words:
            return 0.0

        intersection = s1_words & s2_words
        union = s1_words | s2_words

        return len(intersection) / len(union)

    def _author_similarity(self, result_author: str, target_author: str) -> float:
        """计算作者相似度，优先匹配姓氏和包含关系"""
        result_norm = self._normalize_text(result_author)
        target_norm = self._normalize_text(target_author)

        if not result_norm or not target_norm:
            return 0.0

        if target_norm in result_norm or result_norm in target_norm:
            return 1.0

        result_words = set(result_norm.split())
        target_terms = self._author_terms(target_norm)
        if target_terms:
            matched = result_words & set(target_terms)
            coverage = len(matched) / len(target_terms)
        else:
            coverage = 0.0

        return max(coverage, self._similarity(result_norm, target_norm))

    def _author_terms(self, author: str) -> List[str]:
        """提取作者姓氏/关键名词"""
        terms = []
        for part in re.split(r'\s*(?:,|&|;|\band\b)\s*', author):
            words = [
                word for word in part.strip().split()
                if len(word) > 1 and word not in {'and'}
            ]
            if words:
                terms.append(words[-1])
        return terms

    def _normalize_text(self, value: str) -> str:
        """规范化比较文本"""
        value = (value or '').lower()
        value = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', ' ', value)
        return ' '.join(value.split())
