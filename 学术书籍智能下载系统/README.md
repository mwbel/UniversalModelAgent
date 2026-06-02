# 学术书籍智能下载系统

一个智能化的学术书籍批量下载工具，支持多源搜索、自动下载和分类管理。

## 功能特性

- ✅ Excel书籍清单解析
- ✅ SQLite数据库管理
- ✅ 多源智能搜索（arXiv、Internet Archive、Google Scholar、Library Genesis等）
- ✅ 搜索候选结果持久化
- ✅ 并发下载管理
- ✅ 断点续传
- ✅ 文件验证
- ✅ 自动分类归档
- ✅ 详细下载报告

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置系统

编辑 `config.yaml` 文件，设置：
- Excel文件路径
- 下载目录
- 搜索源优先级
- 并发下载数等

### 3. 初始化系统

```bash
# 导入书籍清单到数据库
python main.py --init
```

### 4. 开始下载

```bash
# 搜索书籍资源
python main.py --search

# 开始下载
python main.py --download

# 查看统计
python main.py --stats
```

## 项目结构

```
学术书籍智能下载系统/
├── main.py                 # 主程序入口
├── config.yaml             # 配置文件
├── requirements.txt        # 依赖列表
├── src/                    # 源代码
│   ├── __init__.py
│   ├── config.py          # 配置管理
│   ├── database.py        # 数据库操作
│   ├── parser.py          # Excel解析
│   ├── searcher.py        # 搜索引擎
│   ├── downloader.py      # 下载管理
│   ├── validator.py       # 文件验证
│   └── reporter.py        # 报告生成
├── tests/                  # 测试文件
├── data/                   # 数据库文件
├── downloads/              # 下载目录
└── logs/                   # 日志文件
```

## 当前状态

**版本**: 0.6.2-alpha  
**开发进度**: 86%  
**状态**: 核心流程已闭环，网络连接需要优化

### 已实现功能
- ✅ Excel书籍清单解析（95本书已导入）
- ✅ SQLite数据库管理
- ✅ 多源智能搜索（arXiv、Internet Archive、Google Scholar、Library Genesis）
- ✅ 搜索候选结果管理
- ✅ 下载管理器
- ✅ 候选资源自动回退下载
- ✅ 搜索结果过滤
- ✅ 文件验证（PDF/EPUB/DJVU基础检查）
- ✅ 下载报告生成（Excel/CSV/Markdown）
- ✅ CLI命令行界面
- ✅ 进度显示和统计

### 待完成功能
- ⚠️ 网络连接优化（代理、镜像站）
- 🔄 更多开放获取搜索源（Crossref/OpenAlex、机构仓储）
- 🔄 错误恢复机制
- 🔄 并发下载与断点续传增强

详见 [开发日志.md](./开发日志.md)

## 常用命令

```bash
# 验证已下载文件
python main.py --validate

# 生成Excel报告
python main.py --report --report-format xlsx

# 生成Markdown报告
python main.py --report --report-format md

# 查看所有书籍的搜索候选概览
python main.py --candidates

# 查看指定书籍的搜索候选详情
python main.py --candidates --book-id 1

# 同步每个分类 wrong/ 目录中的人工判错文件
python main.py --sync-wrong
```

`--download` 现在会自动按候选评分顺序尝试多个下载链接；单个链接失败或文件验证失败时，会继续切换到下一个候选。

下载前还会过滤明显不是全文资源的候选，例如预览页、封面图、图片文件和过小的伪全文文件。

`--sync-wrong` 会把 `downloads/**/wrong/*` 视为人工确认的误下载真值源。匹配到的书籍会统一改为 `failed`，清空 `file_path` 和 `download_url`，并删除当前错误候选链接；wrong 目录里的文件本身不会被删除。

## 合规说明

本工具仅用于个人学习研究目的，优先使用合法开放资源：
- arXiv.org
- Internet Archive
- Google Scholar开放PDF
- 大学机构仓储
- 作者个人网站

请遵守版权法律，不要用于商业传播。

## 许可证

MIT License

## 作者

Claude - 2026
