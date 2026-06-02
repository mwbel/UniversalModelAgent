#!/usr/bin/env python3
"""测试Internet Archive搜索器解析逻辑"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import searcher as searcher_module
from searcher import InternetArchiveSearcher, SearchEngine


class TestConfig:
    """测试配置"""

    def get(self, key, default=None):
        values = {
            'search_sources': [
                {
                    'name': 'Internet Archive',
                    'enabled': True,
                    'priority': 1,
                    'base_url': 'https://archive.org/advancedsearch.php',
                    'metadata_url': 'https://archive.org/metadata',
                    'delay': 0,
                    'max_results': 5,
                }
            ],
            'user_agents': ['test-agent'],
        }
        return values.get(key, default)


class FakeResponse:
    """伪造requests响应"""

    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    def json(self):
        return self.payload


SEARCH_PAYLOAD = {
    'response': {
        'docs': [
            {
                'identifier': 'solar-system-dynamics',
                'title': 'Solar System Dynamics',
                'creator': ['Carl D. Murray', 'Stanley F. Dermott'],
                'year': '1999',
                'downloads': 1234,
                'publicdate': '2020-01-02T00:00:00Z',
            }
        ]
    }
}


METADATA_PAYLOAD = {
    'files': [
        {
            'name': 'solar-system-dynamics.epub',
            'format': 'EPUB',
            'size': '2097152',
        },
        {
            'name': 'solar-system-dynamics_text.pdf',
            'format': 'Text PDF',
            'size': '10485760',
        },
        {
            'name': 'solar-system-dynamics_encrypted.pdf',
            'format': 'PDF',
            'size': '10485760',
        },
    ]
}


def test_internet_archive_searcher():
    """测试Internet Archive搜索器返回开放馆藏候选"""
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
            if url.startswith('https://archive.org/metadata/'):
                return FakeResponse(METADATA_PAYLOAD)
            return FakeResponse(SEARCH_PAYLOAD)

        searcher_module.requests.get = fake_get

        ia = InternetArchiveSearcher(TestConfig())
        ia._delay = lambda: None
        results = ia.search('Solar System Dynamics', 'Murray & Dermott')

        assert len(results) == 1
        result = results[0]
        assert result.source == 'Internet Archive'
        assert result.title == 'Solar System Dynamics'
        assert result.file_format == 'pdf'
        assert result.file_size == '10.0MB'
        assert result.is_open_access
        assert result.download_url == (
            'https://archive.org/download/solar-system-dynamics/'
            'solar-system-dynamics_text.pdf'
        )
        assert 'Carl D. Murray' in result.author
        assert '年份: 1999' in result.notes
        assert calls[0]['params']['q'] == (
            'title:("Solar System Dynamics") AND creator:("Murray") '
            'AND mediatype:(texts)'
        )
        assert calls[1]['url'] == 'https://archive.org/metadata/solar-system-dynamics'

        engine = SearchEngine(TestConfig())
        scored = engine._score_results(results, 'Solar System Dynamics', 'Murray')
        assert scored[0].score > 75

    finally:
        searcher_module.requests.get = original_get

    print('Internet Archive搜索器测试通过')


if __name__ == '__main__':
    test_internet_archive_searcher()
