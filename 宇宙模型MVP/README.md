# 宇宙模型

这是一个本地优先的宇宙模型智能体工作区，内置 OCR 接入位、本地 RAG 策略和天文学 A2UI 可视化。

## 版本目录

当前已经冻结并拆分出两个版本：

- `versions/宇宙模型-v0.1`：当前已实现智能体版本，命名为 `宇宙模型 v0.1`
- `versions/宇宙模型-v0.2`：基于 `v0.1` 创建的新版本起点，默认端口与 `v0.1` 错开

两个版本共用根目录 `.env`、`.local_rag`，并继续共用 `UnivModel/RAG` 与 `UnivModel/行星运动模型` 下的图文资料、星历和模型文件。

启动 `v0.2`：

```bash
./start_v0.2.sh
```

也可以分开启动：

```bash
./start_v0.2_backend.sh
./start_v0.2_frontend.sh
```

默认访问地址：

- v0.2 版本首页：`http://127.0.0.1:5174/?home=1`
- v0.2 智能体工作台：`http://127.0.0.1:5174/`
- v0.2 后端：`http://127.0.0.1:8788/`

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

如果你当前使用的是静态前端 `frontend/`，推荐直接使用下面这套脚本。它会自动避开已占用端口，并把实际后端地址写入前端运行时配置，不需要再手改 JS：

```bash
cd "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP"
./start_static_stack.sh
```

这个脚本会保持运行来守护前后端服务。使用时保持终端窗口打开；需要停止时，在该终端按 `Ctrl+C`。

如果想分别启动，也可以：

```bash
./start_backend.sh
./start_backend.sh
```

脚本会把实际地址和端口写到：

- `.run-logs/static-backend.env`
- `.run-logs/static-frontend.env`

其中最常用的是：

- `BACKEND_URL`
- `BACKEND_PORT`
- `FRONTEND_URL`
- `FRONTEND_PORT`

如果要同时启动后端和 React 前端：

```bash
cd "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP" && ./start_all.sh
```

脚本会优先使用默认端口，并在端口被其他进程占用时自动顺延寻找可用端口：

- 后端：`http://127.0.0.1:8787/`
- 前端：`http://127.0.0.1:5173/`
- OCR 校正测试台：`http://127.0.0.1:5173/?ocr=1`

如果端口发生变化，以脚本输出的实际地址为准；同时也会写入：

- `.run-logs/backend.env`
- `.run-logs/frontend.env`

手动指定端口：

```bash
APP_PORT=8800 FRONTEND_PORT=5200 ./start_all.sh
```

如果希望端口被占用时直接失败，而不是自动换端口：

```bash
STRICT_PORTS=1 ./start_all.sh
```

如果启动失败，脚本会把最近日志打印出来，同时把完整日志写到：

- `.run-logs/backend.log`
- `.run-logs/frontend.log`

## 可配置环境变量

- `APP_HOST`
- `APP_PORT`
- `FRONTEND_HOST`
- `FRONTEND_PORT`
- `PORT_SEARCH_LIMIT`：默认 `80`，表示端口被占用时向后搜索的范围
- `STRICT_PORTS`：设为 `1` 时禁用自动换端口
- `MINERU_BASE_URL`：MinerU 服务地址，默认 `https://mineryou.cpolar.top`
- `MINERU_CONVERT_PATH`：MinerU 转换接口路径，默认 `/api/convert`
- `MARKDOWN_LIBRARY_DIR`：已转换 Markdown 资料库根目录，默认 `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605-仅留md 和图片`
- `RAG_CHAT_PATH`
- `RAG_VARIANTS`
- `REQUEST_TIMEOUT_SECONDS`
- `YUNWU_API_BASE_URL`：云雾 API 地址
- `YUNWU_API_KEY`：云雾 API 密钥
- `YUNWU_GPT55_MODEL`：云雾侧使用的 GPT 5.5 模型名，默认 `gpt-5.5`
- `YUNWU_CHAT_PATH`：云雾 OpenAI-compatible chat 路径，默认 `/v1/chat/completions`
- `OCR_CORRECTION_PROVIDER`：`openai-compatible`、`yunwu-openai` 或 `gemini`
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

## 数学书籍 PDF 到 RAG Markdown

根目录新增了一条离线批处理流水线，用于把已有 MinerU 输出修复成适合 RAG 入库的 Markdown：

```text
原始 PDF
-> MinerU markdown/json/layout/page images
-> 高风险数学 block 检测
-> 按 bbox 裁剪页面原图
-> Mathpix 重新识别高风险区域
-> 替换 block 并保留 metadata
-> final.md / chunks.jsonl / audit_report.json
```

运行前设置 Mathpix 凭据：

```bash
python3 -m pip install -r requirements.txt
export MATHPIX_APP_ID="your_app_id"
export MATHPIX_APP_KEY="your_app_key"
```

执行：

```bash
python main.py \
  --pdf input/book.pdf \
  --mineru-output output/mineru_book \
  --page-images output/mineru_book/images \
  --out output/rag_book
```

可选配置在 `config.yaml`，包括 Mathpix API 地址、缓存目录、裁剪 padding、chunk size 和 metadata 注释开关。所有 Mathpix 请求都会按图片 hash 写入本地缓存，默认缓存目录是输出目录下的 `.mathpix_cache`；重复运行时命中缓存不会再次计费。

输出文件：

- `final.md`：RAG 友好的 Markdown，公式使用 `$...$` / `$$...$$`，每个 block 带 HTML metadata 注释。
- `chunks.jsonl`：按 chapter / section / theorem / proof / example / equation / table 友好的边界切分，尽量不截断公式、表格和证明。
- `audit_report.json`：记录替换、失败和低置信度 block，包含 `page`、`bbox`、`original_text`、`new_text`、`reason`、`ocr_engine`。
- `run_manifest.json`：记录本次运行输入、输出、统计和配置快照。

如果 Mathpix 失败，流程不会中断；对应 block 会保留 MinerU 原结果，并在 metadata 与审计报告中标记为 `confidence: low`。

批量处理已有 MinerU 书库：

```bash
python scripts/batch_mathpix_fix_books.py \
  --root "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605" \
  --out "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/mathpix_rag_outputs" \
  --dry-run
```

集中缺少 Mathpix 修复所需文件的书籍目录：

```bash
python scripts/batch_mathpix_fix_books.py \
  --root "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605" \
  --out "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/mathpix_rag_outputs" \
  --collect-missing-only
```

确认 `MATHPIX_APP_ID` 和 `MATHPIX_APP_KEY` 后，正式批量修复：

```bash
python scripts/batch_mathpix_fix_books.py \
  --root "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605" \
  --out "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/mathpix_rag_outputs" \
  --skip-existing \
  --continue-on-error
```

批处理脚本会自动遍历可用书籍下的 `auto` / `ocr` / `hybrid_auto` chunk，逐个调用 `main.py`，并在每本书输出目录中合并生成：

- `book_final.md`
- `book_chunks.jsonl`
- `book_audit_report.json`

建议第一次正式调用时加 `--limit-books 1 --limit-chunks 1` 做小规模计费验证。

也可以只测试指定书籍目录，并限制每个 chunk 最多送给 Mathpix 的高风险块数：

```bash
python scripts/batch_mathpix_fix_books.py \
  --root "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/宇宙模型资料202605" \
  --book-dir "/path/to/one/book-folder" \
  --out "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/RAG/mathpix_rag_outputs_test" \
  --limit-chunks 1 \
  --max-mathpix-blocks 3 \
  --continue-on-error
```

对于当前这批 MinerU chunk，如果 `images/` 只有内嵌图而不是整页图，脚本会优先使用 chunk 目录中的 `*_origin.pdf` 自动渲染整页图片，再按 `page_idx + bbox` 裁剪。

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

如果使用云雾 API 调用 GPT 5.5 做 OCR 校正：

```bash
export OCR_CORRECTION_PROVIDER=yunwu-openai
export YUNWU_API_BASE_URL="https://<your-yunwu-endpoint>"
export YUNWU_API_KEY="..."
export YUNWU_GPT55_MODEL="gpt-5.5"
export YUNWU_CHAT_PATH="/v1/chat/completions"
```

也可以在请求体里显式指定：

```bash
curl -s "http://127.0.0.1:8787/api/ocr/correct" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "yunwu-openai",
    "markdown": "| 变量 | 公式 |\n|---|---|\n| w | $2 7$ |",
    "pageImages": [
      {
        "pageNumber": 1,
        "image": "data:image/png;base64,..."
      }
    ]
  }'
```

## 当前说明

当前 RAG 已改为本地内置模式，不再依赖外部 cpolar manyRAG 服务。接下来可以继续逐条完成 issue 列表里的：

1. RAG 服务接口对齐
2. OCR 批量转换流程接入
3. 引用结构标准化
4. 问答与可视化联动增强

当前前端已支持在侧边栏切换上述 3 种 RAG 方案；上传文档后会直接写入本地知识库，再由当前 Python 服务完成检索与问答。

## 模型测试台

启动后可访问：

- `http://127.0.0.1:8787/model-tester.html`

这个页面用于测试 OpenAI-compatible 模型服务，支持从下拉框选择模型、刷新模型列表、填写 Base URL、临时输入 API key、设置 `temperature` 和 `max_tokens`，并查看延迟、token 用量和原始响应。

推荐用环境变量配置默认服务，避免把密钥写进前端文件：

```bash
export MODEL_TESTER_BASE_URL="https://api.example.com"
export MODEL_TESTER_API_KEY="..."
export MODEL_TESTER_MODELS_PATH="/v1/models"
export MODEL_TESTER_CHAT_PATH="/v1/chat/completions"
```

如果模型服务没有开放模型列表接口，页面会使用内置默认列表：

```text
qwen3.6-27b:latest
batiai/qwen3.6-27b:q4
medgemma:1.5-4b
gemma4:e4b
gemma2:27b
qwen2.5:14b
nomic-embed-text:latest
llama3:latest
```

交互式可视化生成遵循 `edu-viz-core-main` 的 A2UI 思路：先在 `backend/visualization_catalog.py` 声明 capability，再由 `backend/services/visualization_planner.py` 输出 A2UI-compatible render instruction。当前前端仍保留 iframe fallback，但返回结构已经包含 `componentId`、`initialProps`、`propsSchema`、`events` 和 `feedbackContract`，方便后续替换为真正的 A2UI renderer。

具体改造路线见：

- [docs/a2ui-dialog-generation-plan.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/a2ui-dialog-generation-plan.md)
- [docs/edu-viz-core-reuse-plan.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/edu-viz-core-reuse-plan.md)

后续界面和 A2UI 运行时优先复用 `edu-viz-core-main` 的 React/Vite 前端壳、`A2UISetup`、`StreamSplitter`、Gallery 和插件组件注册思路；当前原生 `frontend/` 短期保留为 fallback。
