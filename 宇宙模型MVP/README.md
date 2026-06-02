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

## 可配置环境变量

- `APP_HOST`
- `APP_PORT`
- `MINERU_BASE_URL`
- `MINERU_CONVERT_PATH`
- `RAG_CHAT_PATH`
- `RAG_VARIANTS`
- `REQUEST_TIMEOUT_SECONDS`

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
