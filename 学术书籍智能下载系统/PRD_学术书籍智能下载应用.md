# PRD：学术书籍智能下载应用

## 1. 项目概述

### 1.1 项目背景
用户拥有一份包含约95本行星运行轨道理论相关学术书籍的Excel清单，需要批量获取这些书籍的电子版。手动逐本搜索和下载效率低下，需要一个智能化的自动下载系统。

### 1.2 项目目标
开发一个智能应用/智能体，能够：
- 自动解析Excel书籍清单
- 智能搜索并定位书籍电子版资源
- 自动下载或提供下载链接
- 管理下载进度和结果

### 1.3 核心价值
- 节省时间：自动化批量处理，减少90%以上的人工操作
- 提高成功率：多源搜索策略，提升资源获取成功率
- 合规性：优先使用合法渠道，记录资源来源

## 2. 功能需求

### 2.1 核心功能

#### 2.1.1 书籍清单解析
- 支持读取Excel文件（.xlsx格式）
- 提取关键信息：
  - 书名（中英文）
  - 作者
  - 出版社
  - 分类标签
  - 备注信息
- 数据清洗和标准化

#### 2.1.2 智能搜索引擎
多渠道搜索策略（按优先级）：

**合法渠道（优先）：**
1. 开放获取资源
   - arXiv.org
   - ResearchGate
   - Google Scholar（开放PDF）
   - 大学机构仓储
   - 作者个人网站

2. 图书馆资源
   - Library Genesis（学术镜像）
   - Z-Library
   - Anna's Archive
   - Sci-Hub（论文）

3. 商业平台试读
   - Google Books预览
   - Amazon试读章节
   - Springer/Elsevier样章

**搜索策略：**
- 多关键词组合：书名+作者+ISBN
- 模糊匹配：处理不同版本、年份
- 语言识别：中英文书籍分别处理

#### 2.1.3 资源验证
- 文件格式验证（PDF/EPUB/DJVU）
- 文件完整性检查
- 内容匹配度验证（书名、作者、页数）
- 文件大小合理性判断

#### 2.1.4 下载管理
- 断点续传
- 并发下载控制（避免IP封禁）
- 下载速度限制
- 失败重试机制（最多3次）
- 下载进度实时显示

#### 2.1.5 结果管理
- 按分类自动归档（太阳系动力学、广义相对论等）
- 统一命名规范：`[分类]书名_作者.pdf`
- 生成下载报告：
  - 成功下载列表
  - 失败列表（含原因）
  - 部分成功列表（试读版）

### 2.2 辅助功能

#### 2.2.1 用户交互
- Web界面或命令行界面
- 实时进度展示
- 手动干预选项（选择下载源）
- 暂停/继续/取消功能

#### 2.2.2 智能推荐
- 当找不到完整版时，推荐替代资源：
  - 相同作者其他版本
  - 相似主题书籍
  - 论文集/章节

#### 2.2.3 元数据管理
- 自动提取书籍元数据
- 生成书目管理文件（BibTeX格式）
- 与Zotero/Mendeley集成

## 3. 技术方案

### 3.1 技术栈

**后端：**
- Python 3.10+
- 框架：FastAPI（API服务）或Streamlit（快速原型）
- 异步处理：asyncio + aiohttp

**核心库：**
- `pandas`：Excel解析
- `openpyxl`：Excel读写
- `requests` / `aiohttp`：HTTP请求
- `BeautifulSoup4` / `lxml`：网页解析
- `selenium` / `playwright`：动态网页处理
- `PyPDF2` / `pdfplumber`：PDF验证
- `tqdm`：进度条

**AI能力：**
- LLM API（Claude/GPT）：智能搜索策略、内容匹配
- 向量数据库（可选）：书籍相似度匹配

### 3.2 系统架构

```
┌─────────────────┐
│  用户界面层      │  Web UI / CLI
└────────┬────────┘
         │
┌────────▼────────┐
│  控制层          │  任务调度、进度管理
└────────┬────────┘
         │
┌────────▼────────┐
│  业务逻辑层      │
│  ├─ 解析模块    │  Excel → 结构化数据
│  ├─ 搜索模块    │  多源智能搜索
│  ├─ 验证模块    │  资源验证
│  ├─ 下载模块    │  并发下载管理
│  └─ 归档模块    │  文件整理
└────────┬────────┘
         │
┌────────▼────────┐
│  数据访问层      │
│  ├─ 文件系统    │
│  ├─ 数据库      │  SQLite（任务状态）
│  └─ 外部API     │  搜索引擎、下载源
└─────────────────┘
```

### 3.3 核心算法

#### 3.3.1 智能搜索算法
```python
def intelligent_search(book_info):
    """
    多阶段搜索策略
    """
    # 阶段1：精确匹配（书名+作者+ISBN）
    result = exact_search(book_info)
    if result: return result
    
    # 阶段2：模糊匹配（书名+作者）
    result = fuzzy_search(book_info)
    if result: return result
    
    # 阶段3：LLM辅助搜索（理解备注信息）
    result = llm_assisted_search(book_info)
    if result: return result
    
    # 阶段4：推荐替代资源
    return recommend_alternatives(book_info)
```

#### 3.3.2 资源评分算法
```python
def score_resource(resource, book_info):
    """
    对搜索到的资源进行评分
    """
    score = 0
    # 标题匹配度（40分）
    score += title_similarity(resource.title, book_info.title) * 40
    # 作者匹配度（30分）
    score += author_match(resource.author, book_info.author) * 30
    # 文件质量（20分）
    score += file_quality_score(resource) * 20
    # 来源可信度（10分）
    score += source_credibility(resource.source) * 10
    return score
```

### 3.4 数据库设计

**books表：**
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    category TEXT,
    notes TEXT,
    status TEXT,  -- pending/searching/downloading/completed/failed
    download_url TEXT,
    file_path TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

**download_logs表：**
```sql
CREATE TABLE download_logs (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    attempt_time TIMESTAMP,
    source TEXT,
    status TEXT,
    error_message TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

## 4. 合规性与风险

### 4.1 法律合规
- **优先使用合法渠道**：开放获取、图书馆授权资源
- **尊重版权**：
  - 仅用于个人学习研究
  - 不进行商业传播
  - 标注资源来源
- **用户协议**：明确告知用户版权责任

### 4.2 技术风险
- **IP封禁**：
  - 限制请求频率（每个源间隔3-5秒）
  - 使用代理池轮换
  - User-Agent随机化
- **资源失效**：定期更新搜索源列表
- **文件安全**：病毒扫描、恶意代码检测

### 4.3 隐私保护
- 本地运行，不上传用户数据
- 可选的匿名统计（改进搜索算法）

## 5. 实施计划

### 5.1 开发阶段（4周）

**Week 1：基础框架**
- Excel解析模块
- 数据库设计与实现
- 基础UI框架

**Week 2：搜索引擎**
- 实现3-5个主要搜索源
- 搜索结果评分算法
- LLM集成（可选）

**Week 3：下载管理**
- 并发下载引擎
- 断点续传
- 文件验证

**Week 4：优化与测试**
- 错误处理
- 性能优化
- 用户测试

### 5.2 MVP功能（最小可行产品）
1. Excel解析
2. 2-3个主要搜索源（Library Genesis + Google Scholar）
3. 基础下载功能
4. 简单的CLI界面
5. 下载报告生成

### 5.3 后续迭代
- Web界面
- 更多搜索源
- AI智能推荐
- 书目管理集成
- 多语言支持

## 6. 成功指标

### 6.1 功能指标
- 书籍识别准确率 > 90%
- 资源获取成功率 > 70%（完整版）
- 下载成功率 > 95%（已找到资源）

### 6.2 性能指标
- 单本书籍搜索时间 < 30秒
- 并发下载数：3-5个
- 系统稳定性：连续运行24小时无崩溃

### 6.3 用户体验
- 操作简单：3步完成配置
- 进度透明：实时显示当前状态
- 结果清晰：详细的成功/失败报告

## 7. 项目交付物

1. **源代码**：完整的Python项目
2. **使用文档**：
   - 安装指南
   - 使用教程
   - 配置说明
3. **下载报告**：Excel格式，包含：
   - 书籍清单
   - 下载状态
   - 文件路径
   - 失败原因
4. **书籍文件**：按分类整理的PDF文件

## 8. 预算与资源

### 8.1 开发成本
- 开发时间：4周（1人）
- LLM API费用：约$20-50（可选）
- 服务器/代理费用：$0（本地运行）

### 8.2 运行成本
- 存储空间：约10-20GB（95本书）
- 网络流量：约10-20GB
- 电力成本：可忽略

## 9. 附录

### 9.1 书籍清单统计
- 总数：95本
- 主要分类：
  - 太阳系多体动力学：7本
  - 广义相对论：7本
  - 月球物理：6本
  - 地球物理：9本
  - 数值积分：7本
  - 观测数据拟合：9本
  - 其他：50本

### 9.2 参考资源
- Library Genesis: http://libgen.rs
- Anna's Archive: https://annas-archive.org
- arXiv: https://arxiv.org
- Google Scholar: https://scholar.google.com

---

**文档版本**：v1.0  
**创建日期**：2026-04-23  
**作者**：Claude  
**状态**：待审核
