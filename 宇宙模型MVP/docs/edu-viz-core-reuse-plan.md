# 复用 edu-viz-core 框架与界面规划

## 结论

当前项目的前端是原生 HTML / CSS / JS，已经能完成本地 RAG、三种策略切换和 iframe fallback 可视化，但它不是 A2UI 应用框架。

如果目标是“尽量复用 `edu-viz-core-main` 的框架和界面”，推荐不要继续在现有原生页面上叠功能，而是采用渐进式迁移：

```text
当前 Python 本地后端继续保留
-> 新增 React + Vite 前端壳
-> 复用 edu-viz-core 的 AppShell / A2UISetup / StreamSplitter / BottomInput / Gallery 思路
-> 本项目只负责 astronomy RAG、capability registry、天文 A2UI 组件
```

这样能同时复用：

- A2UI 消息协议
- A2UI 渲染运行时
- 插件 / capability 思路
- 对话界面结构
- Gallery 调试方式
- `The Illuminated Mind` 风格系统

## 可直接参考或迁移的 edu-viz-core 文件

### A2UI 运行时

来源：

- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/A2UISetup.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/StreamSplitter.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/CatalogRegistry.ts`

本项目目标路径：

- `frontend-react/src/a2ui-engine/A2UISetup.tsx`
- `frontend-react/src/a2ui-engine/StreamSplitter.ts`
- `frontend-react/src/a2ui-engine/CatalogRegistry.ts`

适配点：

- 先不接 edu-viz 的插件接口，改成本地 `astronomy-core` 组件注册表。
- 保留 `surfaceUpdate`、`dataModelUpdate`、`beginRendering` 的解析方式。
- 保留 `remapSurfaceId`，避免多条回答的可视化互相覆盖。

### 对话流

来源：

- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/services/chatService.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/hooks/useChat.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/store/chatStore.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/backend/app/services/streaming.py`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/backend/app/orchestrator/a2ui_builder.py`

本项目适配方式：

- 后端新增 `/api/chat/stream`，兼容 edu-viz 的 SSE event 格式。
- 普通文本输出为 `{type: "text", content: "..."}`
- A2UI 输出为 `{type: "a2ui", line: "..."}`
- 结束输出为 `{type: "done"}`
- 保留当前 `/api/chat` 给旧前端作为 fallback。

### 界面壳

来源：

- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/AppShell.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/Layout/TopNav.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/Layout/LeftSidebar.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/Layout/RightSidebar.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/Welcome/BottomInput.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/components/Welcome/WelcomeScreen.tsx`

本项目适配方式：

- `TopNav`：改成宇宙模型智能体标题和本地服务状态。
- `LeftSidebar`：替换为知识库上传、RAG 策略、会话列表。
- `RightSidebar`：替换为 RAG 检索证据、A2UI capability 信息、组件交互状态。
- `BottomInput`：保留 edu-viz 的底部输入体验，但加入文件上传入口和 RAG strategy selector。
- `WelcomeScreen`：改成天文学问题入口，而不是项目驱动学习入口。

### Gallery

来源：

- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/gallery/`

本项目目标：

- `frontend-react/src/gallery/`

用途：

- 预览 `astronomy-core.ecliptic-lunar-path`
- 预览 `astronomy-core.eclipse-geometry`
- 预览 `astronomy-core.retrograde-motion`
- 预览 `astronomy-core.kepler-third-law`

访问方式保持类似：

```text
http://127.0.0.1:5173/?gallery=1
```

## 本项目需要保留的模块

这些模块是本项目已经形成的核心，不建议丢掉：

- `backend/services/rag_client.py`
- `backend/rag_catalog.py`
- `backend/services/chat_service.py`
- `backend/visualization_catalog.py`
- `backend/services/visualization_planner.py`
- `.local_rag/store.json`
- `frontend/interactive-visualizations/legacy/`

迁移时，新 React 前端调用这些 API，而不是重写本地 RAG。

## 推荐目录结构

```text
backend/
  services/
    a2ui_builder.py
    a2ui_orchestrator.py
    rag_client.py
    visualization_planner.py
  server.py

frontend/                       # 旧原生前端，短期保留
frontend-react/                 # 新 React/A2UI 前端
  src/
    a2ui-engine/
    astronomy-components/
    components/
    gallery/
    services/
    store/
```

## 分阶段实施

### Phase 1：建立 React/A2UI 前端壳

目标：

- 新增 `frontend-react`
- 复用 edu-viz 的设计系统和页面壳
- 页面能访问当前后端 `/api/health`、`/api/rag/strategies`、`/api/rag/kbs`

验收：

- `npm run dev` 能启动新前端。
- 页面外观接近 edu-viz-core。
- 左侧能看到本地知识库和 RAG 策略。

### Phase 2：接入 SSE + A2UI 消息

目标：

- 后端新增 `/api/chat/stream`
- 前端复用 `StreamSplitter` 和 `useChat` 模式
- 文本和 A2UI JSONL 分流

验收：

- 普通回答流式显示。
- A2UI 行进入 renderer，而不是显示成文字。

### Phase 3：实现第一个天文 A2UI 组件

目标：

- 实现 `astronomy-core.ecliptic-lunar-path`
- 用它替代“黄道 / 白道文字假图”

验收：

- 用户问“请可视化展示黄道和白道”
- 页面渲染真实组件
- 可以调整月球位置、显示交点、观察 5.145 度倾角

### Phase 4：Gallery 和调试

目标：

- 复用 edu-viz Gallery 结构
- 每个 astronomy component 都有预览数据
- planner 命中结果能跳到 Gallery 调试

验收：

- `?gallery=1` 能查看所有天文组件。
- 每个组件能单独调 props。

### Phase 5：插件化

目标：

- 把 `astronomy-core` 从硬编码 registry 升级为插件 manifest。
- 后续可加入数学、历算、星历对照等插件。

验收：

- 新增组件只需注册 capability 和组件导出。
- planner 不需要硬编码 if/else。

## 技术取舍

推荐先复制框架思想和关键源码结构，不建议第一步就完整合并两个仓库。

原因：

- 本项目后端是轻量 `http.server`，edu-viz 后端是 FastAPI。
- 本项目已有本地 RAG 和文件上传逻辑。
- 完整迁移 FastAPI + React + 插件系统会扩大改动面。
- 先做 `frontend-react + /api/chat/stream`，风险最小，也最接近目标。

## 最近一步建议

下一步直接做 Phase 1：

1. 新增 `frontend-react`
2. 复制并改造 edu-viz 的 `AppShell`、`BottomInput`、`A2UISetup`、`StreamSplitter`
3. 接当前后端 API
4. 保留旧 `frontend/` 作为 fallback

完成 Phase 1 后，再做 `astronomy-core.ecliptic-lunar-path`，真正解决“文字假图”的问题。
