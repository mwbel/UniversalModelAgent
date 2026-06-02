"""配置管理模块"""

import yaml
from pathlib import Path
from typing import Dict, Any


class Config:
    """配置管理类"""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")

        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default

        return value

    @property
    def database_path(self) -> str:
        return self.get('database.path', 'data/books.db')

    @property
    def excel_file(self) -> str:
        return self.get('paths.excel_file')

    @property
    def download_dir(self) -> str:
        return self.get('paths.download_dir', 'downloads')

    @property
    def concurrent_downloads(self) -> int:
        return self.get('download.concurrent_downloads', 3)

    @property
    def timeout(self) -> int:
        return self.get('download.timeout', 60)

    @property
    def retry_times(self) -> int:
        return self.get('download.retry_times', 3)
