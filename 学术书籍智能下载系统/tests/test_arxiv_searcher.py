#!/usr/bin/env python3
"""测试arXiv搜索器解析逻辑"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import searcher as searcher_module
from searcher import ArxivSearcher, SearchEngine


class TestConfig:
    """测试配置"""

    def get(self, key, default=None):
        values = {
            'search_sources': [
                {
                    'name': 'arXiv',
                    'enabled': True,
                    'priority': 1,
                    'base_url': 'https://export.arxiv.org/api/query',
                    'delay': 0,
                    'max_results': 5,
                }
            ],
            'user_agents': ['test-agent'],
        }
        return values.get(key, default)


class FakeResponse:
    """伪造requests响应"""

    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


ARXIV_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/astro-ph/0601234v1</id>
    <updated>2006-01-12T00:00:00Z</updated>
    <published>2006-01-12T00:00:00Z</published>
    <title>Solar System Dynamics and Resonances</title>
    <summary>Open paper summary.</summary>
    <author>
      <name>Jane Murray</name>
    </author>
    <author>
      <name>John Dermott</name>
    </author>
    <arxiv:primary_category term="astro-ph"/>
    <link href="http://arxiv.org/abs/astro-ph/0601234v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/astro-ph/0601234v1" rel="related" type="application/pdf"/>
  </entry>
</feed>
"""


def test_arxiv_searcher():
    """测试arXiv搜索器返回开放PDF候选"""
    original_get = searcher_module.requests.get
    try:
        calls = []

        def fake_get(url, params=None, headers=None, timeout=None):
            calls.append({
                'url': url,
                'params': params,
                'headers': headers,
                'timeout': timeout,
            })
            return FakeResponse(ARXIV_FEED)

        searcher_module.requests.get = fake_get

        arxiv = ArxivSearcher(TestConfig())
        arxiv._delay = lambda: None
        results = arxiv.search('Solar System Dynamics', 'Murray & Dermott')

        assert len(results) == 1
        result = results[0]
        assert result.source == 'arXiv'
        assert result.file_format == 'pdf'
        assert result.is_open_access
        assert result.download_url.startswith('https://arxiv.org/pdf/')
        assert 'Jane Murray' in result.author
        assert 'astro-ph' in result.notes
        assert calls[0]['params']['search_query'] == 'ti:"Solar System Dynamics" AND au:"Murray"'

        engine = SearchEngine(TestConfig())
        scored = engine._score_results(results, 'Solar System Dynamics', 'Murray')
        assert scored[0].score > 70

    finally:
        searcher_module.requests.get = original_get

    print('arXiv搜索器测试通过')


if __name__ == '__main__':
    test_arxiv_searcher()
