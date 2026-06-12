# 宇宙模型智能体 MVP

这是一个本地优先的宇宙模型智能体 MVP，内置 OCR 接入位与 3 种可切换的本地 RAG 策略。

## 当前已完成

- `backend/server.py`：零依赖 Python HTTP 服务
- `frontend/index.html`：MVP 对话工作台
- `frontend/interactive-visualizations/`：历史可视化展厅与原型页面
- A2UI-compatible 可视化规划：
  - 能力注册表
  - planner 匹配
  - `a2uiInstruction` 输出
  - iframe fallback 渲染
- 外部服务接入骨架：
  - MinerU OCR
- 已内置首批 RAG 策略目录：
  - `Naive RAG`
  - `Hybrid RAG`
  - `Parent-Document RAG`
- 本地知识库能力：
  - 文档上传
  - 知识库列表
  - 本地检索与回答

## 本地运行

```bash
cd /Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP
python3 -m backend.server
```

启动后访问：

- `http://127.0.0.1:8787/`

如果要同时启动后端和 React 前端：

```bash
cd "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP" && ./start_all.sh
```

脚本会同时拉起：

- 后端：`http://127.0.0.1:8787/`
- 前端：`http://127.0.0.1:5173/`

如果启动失败，脚本会把最近日志打印出来，同时把完整日志写到：

- `.run-logs/backend.log`
- `.run-logs/frontend.log`

## 可配置环境变量

- `APP_HOST`
- `APP_PORT`
- `MINERU_BASE_URL`：MinerU 服务地址，默认 `https://mineryou.cpolar.top`
- `MINERU_CONVERT_PATH`：MinerU 转换接口路径，默认 `/api/convert`
- `MARKDOWN_LIBRARY_DIR`：已转换 Markdown 资料库根目录，默认 `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605-仅留md 和图片`
- `RAG_CHAT_PATH`
- `RAG_VARIANTS`
- `REQUEST_TIMEOUT_SECONDS`
- `OCR_CORRECTION_PROVIDER`：`openai-compatible` 或 `gemini`
- `OCR_CORRECTION_BASE_URL`：校正模型 API 地址；默认复用 `LLM_BASE_URL`
- `OCR_CORRECTION_API_KEY`：校正模型密钥；默认复用 `LLM_API_KEY`
- `OCR_CORRECTION_MODEL`：校正模型名；默认复用 `LLM_MODEL`
- `OCR_CORRECTION_PATH`：OpenAI-compatible 模式下的接口路径，默认 `/v1/chat/completions`
- `OCR_CORRECTION_MAX_CANDIDATES`：每次最多送给模型校正的高风险 Markdown 块数
- `OCR_CORRECTION_MAX_OUTPUT_TOKENS`

## OCR 自动校正流程

MinerU 仍负责普通页面的粗识别，后端会自动挑出高风险块，再把这些块和页面截图交给多模态模型校正，适合处理表格公式、上标、跨多行分块矩阵和伪代码。

详细设计与使用说明见：

- [docs/ocr-markdown-correction-pipeline.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/ocr-markdown-correction-pipeline.md)

当前模块边界：

- `backend/services/mineru_client.py`：只负责调用校园网服务器上的 MinerU 服务。
- `backend/services/ocr_correction.py`：只负责检测和校正 MinerU 容易识别错的 Markdown 块。
- `backend/services/markdown_library.py`：只负责扫描本地分类 Markdown 书库。
- `backend/services/rag_client.py`：只负责本地知识库摄入、检索和回答。
- `backend/server.py`：只负责把 HTTP API 编排到上述服务。

推荐环境配置：

```bash
export MINERU_BASE_URL="https://mineryou.cpolar.top"
export MINERU_CONVERT_PATH="/api/convert"
export MARKDOWN_LIBRARY_DIR="/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605-仅留md 和图片"
```

查看当前配置：

```bash
curl -s "http://127.0.0.1:8787/api/library/config"
```

列出本地 Markdown 分类：

```bash
curl -s "http://127.0.0.1:8787/api/library/categories"
```

列出某个分类下的 Markdown 文档：

```bash
curl -s "http://127.0.0.1:8787/api/library/documents?category=切比雪夫多项式插值md&limit=20"
```

先预览某个分类将摄入哪些文档，不真正写入 RAG：

```bash
curl -s "http://127.0.0.1:8787/api/library/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "dryRun": true,
    "category": "切比雪夫多项式插值md",
    "kbId": "chebyshev"
  }'
```

把某个分类摄入本地 RAG：

```bash
curl -s "http://127.0.0.1:8787/api/library/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "category": "切比雪夫多项式插值md",
    "kbId": "chebyshev",
    "replace": true
  }'
```

只摄入指定 Markdown 文件：

```bash
curl -s "http://127.0.0.1:8787/api/library/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "relativePaths": [
      "切比雪夫多项式插值md/Chebyshev polynomials (Theodore J. Rivlin) (z-library.sk, 1lib.sk, z-lib.sk)/Chebyshev polynomials (Theodore J. Rivlin) (z-library.sk, 1lib.sk, z-lib.sk)_完整.md"
    ],
    "kbId": "chebyshev",
    "replace": false
  }'
```

先只检测候选块，不调用模型：

```bash
curl -s "http://127.0.0.1:8787/api/ocr/correct" \
  -H "Content-Type: application/json" \
  -d '{"dryRun":true,"markdown":"| 变量 | 公式 |\n|---|---|\n| w | $2 7$ |"}'
```

实际校正已有 Markdown：

```bash
curl -s "http://127.0.0.1:8787/api/ocr/correct" \
  -H "Content-Type: application/json" \
  -d '{
    "markdown": "| 变量 | 公式 |\n|---|---|\n| w | $2 7$ |",
    "pageImages": [
      {
        "pageNumber": 1,
        "image": "data:image/png;base64,..."
      }
    ]
  }'
```

也可以把 MinerU 转换和校正串起来：

```bash
curl -s "http://127.0.0.1:8787/api/ocr/convert-and-correct" \
  -H "Content-Type: application/json" \
  -d '{
    "fileUrl": "https://example.com/book.pdf",
    "pageImages": [
      {
        "pageNumber": 1,
        "image": "data:image/png;base64,..."
      }
    ]
  }'
```

如果使用 Gemini 原生接口：

```bash
export OCR_CORRECTION_PROVIDER=gemini
export OCR_CORRECTION_API_KEY="..."
export OCR_CORRECTION_MODEL="gemini-..."
```

如果使用 GPT、DeepSeek 兼容网关或其他 OpenAI-compatible 多模态接口：

```bash
export OCR_CORRECTION_PROVIDER=openai-compatible
export OCR_CORRECTION_BASE_URL="https://api.example.com"
export OCR_CORRECTION_API_KEY="..."
export OCR_CORRECTION_MODEL="..."
```

## 当前说明

当前 RAG 已改为本地内置模式，不再依赖外部 cpolar manyRAG 服务。接下来可以继续逐条完成 issue 列表里的：

1. RAG 服务接口对齐
2. OCR 批量转换流程接入
3. 引用结构标准化
4. 问答与可视化联动增强

当前前端已支持在侧边栏切换上述 3 种 RAG 方案；上传文档后会直接写入本地知识库，再由当前 Python 服务完成检索与问答。

交互式可视化生成遵循 `edu-viz-core-main` 的 A2UI 思路：先在 `backend/visualization_catalog.py` 声明 capability，再由 `backend/services/visualization_planner.py` 输出 A2UI-compatible render instruction。当前前端仍保留 iframe fallback，但返回结构已经包含 `componentId`、`initialProps`、`propsSchema`、`events` 和 `feedbackContract`，方便后续替换为真正的 A2UI renderer。

具体改造路线见：

- [docs/a2ui-dialog-generation-plan.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/a2ui-dialog-generation-plan.md)
- [docs/edu-viz-core-reuse-plan.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/edu-viz-core-reuse-plan.md)

后续界面和 A2UI 运行时优先复用 `edu-viz-core-main` 的 React/Vite 前端壳、`A2UISetup`、`StreamSplitter`、Gallery 和插件组件注册思路；当前原生 `frontend/` 短期保留为 fallback。
