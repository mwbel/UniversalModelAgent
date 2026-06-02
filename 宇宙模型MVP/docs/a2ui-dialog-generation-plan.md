# A2UI 对话式可视化生成规划

## 背景判断

当前对话里出现的“黄道与白道示意图”只是大模型用 Markdown 和字符画生成的文字说明，不是真正的交互式可视化。它不能被用户拖动、播放、改变参数，也没有状态回传，因此不符合 A2UI 的目标。

参考 `edu-viz-core-main` 后，本项目应该把“请用可视化方式展示”改造成一条明确链路：

```text
用户问题
-> 本地 RAG 检索
-> Visualizer 判断是否需要可视化
-> 选择 capability
-> 生成 A2UI v0.8 JSONL
-> 前端 A2UI renderer 渲染真实组件
-> 用户交互事件回流到对话上下文
```

## edu-viz-core-main 的关键做法

参考文件：

- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/backend/app/orchestrator/a2ui_builder.py`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/backend/app/orchestrator/prompt_builder.py`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/backend/app/services/streaming.py`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/StreamSplitter.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/hooks/useChat.ts`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/A2UISetup.tsx`
- `/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend/src/a2ui-engine/CatalogRegistry.ts`

核心模式：

1. A2UI v0.8 消息不是普通 JSON 对象，而是 JSONL，每行一个消息。
2. 消息类型是顶层键：`surfaceUpdate`、`dataModelUpdate`、`beginRendering`、`deleteSurface`。
3. 后端 SSE 把普通文本包装成 `{type: "text"}`，把 A2UI 行包装成 `{type: "a2ui", line: "..."}`。
4. 前端流式拆分 SSE，遇到 A2UI 行就交给 `useA2UI().processMessages()`。
5. 每条回答中的 A2UI surface 要分配独立 `surfaceId`，避免多个组件互相覆盖。
6. 插件组件通过 manifest / registry 注册，LLM 只选择组件并传初始 props，不负责写前端代码。

## 本项目当前差距

当前已经有：

- `backend/visualization_catalog.py`：可视化 capability registry
- `backend/services/visualization_planner.py`：根据问题选择可视化能力
- `frontend/app.js`：用 iframe 卡片展示旧可视化页面
- `a2uiInstruction`：已经开始输出 component / props / events / fallback

还缺：

- 真实 A2UI JSONL 生成器
- SSE streaming 协议
- 前端 A2UI runtime / renderer
- 天文学插件组件注册
- 用户操作事件回流

## 目标架构

### 后端

新增 A2UI 编排层：

```text
backend/services/a2ui_builder.py
backend/services/a2ui_orchestrator.py
backend/services/visualization_planner.py
backend/server.py
```

职责：

- `a2ui_builder.py`：生成 A2UI v0.8 JSONL 消息。
- `a2ui_orchestrator.py`：把 planner 输出的 `a2uiInstruction` 转成 `surfaceUpdate -> dataModelUpdate -> beginRendering`。
- `visualization_planner.py`：只负责选 capability，不直接拼 UI。
- `server.py`：新增 streaming chat endpoint，输出 text 和 a2ui SSE events。

### 前端

新增 A2UI 运行层：

```text
frontend/a2ui/
frontend/a2ui/A2UIRuntime.js
frontend/a2ui/StreamSplitter.js
frontend/a2ui/components/
frontend/a2ui/components/EclipticLunarPath.js
frontend/a2ui/components/EclipseGeometry.js
frontend/a2ui/components/RetrogradeMotion.js
```

职责：

- 解析 SSE。
- 将 A2UI JSONL 转成渲染状态。
- 根据 `componentId` 找到本地组件。
- 渲染真实交互组件。
- 将组件事件发回后端或写入当前对话上下文。

## 第一批真实 A2UI 组件

### 1. `astronomy-core.ecliptic-lunar-path`

用于替代当前“黄道/白道文字示意图”。

表达内容：

- 黄道平面
- 白道倾角
- 约 5 度夹角
- 升交点 / 降交点
- 月球沿白道运动
- 交点附近更容易发生日月食

初始 props：

```json
{
  "inclinationDeg": 5.145,
  "showNodes": true,
  "showLabels": true,
  "moonPositionDeg": 35,
  "animate": false
}
```

事件：

```text
moonPositionChanged
nodeSelected
inclinationToggled
```

### 2. `astronomy-core.eclipse-geometry`

用于日食、月食、月相相关问题。

### 3. `astronomy-core.retrograde-motion`

用于行星逆行、地心视角、日心视角切换。

### 4. `astronomy-core.kepler-third-law`

用于半长轴、周期、`T² ∝ a³` 参数探索。

## A2UI JSONL 示例

用户问：“请以可视化方式展示黄道和白道的关系。”

后端不应该返回字符画，而应该输出：

```json
{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"astronomy-core.ecliptic-lunar-path":{"inclinationDeg":5.145,"showNodes":true,"showLabels":true,"moonPositionDeg":35,"animate":false}}}]}}
{"beginRendering":{"surfaceId":"main","root":"root"}}
```

如果需要数据模型：

```json
{"dataModelUpdate":{"surfaceId":"main","contents":[{"key":"inclinationDeg","valueNumber":5.145},{"key":"showNodes","valueBoolean":true}]}}
```

## 大模型的职责边界

大模型可以做：

- 判断是否需要可视化
- 解释为什么选择某个可视化
- 根据用户问题给出初始参数
- 根据用户交互后的状态继续解释

大模型不应该做：

- 用字符画冒充可视化
- 随机编造不存在的组件
- 直接生成前端代码
- 绕过 capability registry 自行拼 UI

## 推荐实现路线

### Phase 1：确定性 A2UI 生成

目标：不依赖 LLM 生成 A2UI JSON，先由后端 planner 确定性生成。

任务：

1. 新增 `backend/services/a2ui_builder.py`。
2. 新增 `backend/services/a2ui_orchestrator.py`。
3. 为 `ecliptic-lunar-path` 注册 capability。
4. 当前 `/api/chat` 返回 `a2uiMessages` 字段，先不做 SSE。
5. 前端根据 `a2uiMessages` 渲染真实组件。

验收：

- 用户问“请可视化展示黄道和白道”，页面出现真实交互组件。
- 回答中不再出现字符画或 Markdown 假图。

### Phase 2：前端 A2UI runtime

目标：让前端具备类似 edu-viz-core 的 A2UI 渲染管线。

任务：

1. 实现 `StreamSplitter`。
2. 实现 `A2UIRuntime`。
3. 实现本地 component registry。
4. 注册 `astronomy-core.ecliptic-lunar-path`。
5. 对话消息中显示 A2UI surface，而不是 iframe fallback。

验收：

- `surfaceUpdate` 和 `beginRendering` 能被前端解析并渲染。
- 多条回答中的 surface 互不覆盖。

### Phase 3：SSE 流式对话

目标：对齐 edu-viz-core 的 text + a2ui 混合流。

任务：

1. 新增 `/api/chat/stream`。
2. 后端把文本输出为 `{type: "text"}` SSE event。
3. 后端把 A2UI JSONL 输出为 `{type: "a2ui", line: "..."}` SSE event。
4. 前端边接收边渲染文字和组件。

验收：

- 文本回答先出现。
- 随后组件自动插入到对应位置。
- 对话继续流式输出。

### Phase 4：LLM 辅助参数化

目标：让 LLM 参与选择参数，但不直接生成任意 UI。

任务：

1. Prompt 中提供 capability table。
2. LLM 输出受控结构，例如 `visualization_request`。
3. 后端校验 `componentId` 和 `propsSchema`。
4. 校验通过后由 `a2ui_orchestrator` 生成 A2UI JSONL。

验收：

- LLM 只能选择已注册组件。
- props 不符合 schema 时自动修正或降级。

### Phase 5：交互事件回流

目标：让用户操作组件后，对话能继续解释。

任务：

1. 组件触发 `moonPositionChanged` 等事件。
2. 前端将事件发送到 `/api/a2ui/events`。
3. 后端把事件写入会话上下文。
4. 用户追问时，RAG + LLM 可以引用当前组件状态。

验收：

- 用户拖动月球位置后追问“这里为什么不会发生月食？”
- 系统能基于当前角度、交点距离继续解释。

## 当前最小闭环建议

先做 `astronomy-core.ecliptic-lunar-path`。

原因：

- 它正好对应当前截图里的失败场景。
- 组件逻辑不复杂。
- 教学价值明确。
- 能快速证明“真正 A2UI 可视化”与“文字假图”的差别。

最小闭环只需要：

1. `capability`
2. `a2ui_builder`
3. 一个前端 JS 组件
4. 对话消息中的 A2UI render block

## 风险与取舍

- 直接引入完整 React + `@a2ui/react` 会比当前原生 HTML 项目重很多，建议先做轻量 A2UI-compatible runtime。
- 旧 iframe 可视化不要立刻删除，先作为 fallback。
- LLM 生成 A2UI JSONL 的能力不稳定，早期应由后端确定性生成。
- 真正插件化可以稍后做，先把 astronomy core 组件注册表跑通。
