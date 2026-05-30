# 基于 A2UI 的抽象概念交互式可视化设计方案

## 1. 目标

参考 [GreanEnderman/edu-viz-core](https://github.com/GreanEnderman/edu-viz-core) 的实现思路，为“宇宙模型智能体”设计一套适合**抽象概念教学**的交互式可视化体系。

这里的“抽象概念”不是单纯展示静态结论，而是帮助用户理解：

- 看不见但决定现象的结构
- 变量之间的约束关系
- 尺度变化带来的认知跳跃
- 多坐标系、多参考系下同一对象的不同表现
- 时间演化、因果链、阈值效应

在天文学场景里，典型包括：

- 月食 / 日食为什么发生
- 逆行为什么只是视运动
- 开普勒定律如何从轨道运动中体现
- 红移如何对应波长拉伸
- 黄道 / 赤道 / 地平坐标如何互相转换
- 引力势、轨道能量、共振关系如何影响行星系统

---

## 2. 从 `edu-viz-core` 提炼出的核心模式

### 2.1 它的重点不是“某个前端页”，而是“Agent 到 UI 的渲染链路”

从 [README.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/README.md:31)、[A2UISetup.tsx](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend-v1/src/a2ui-engine/A2UISetup.tsx:1)、[CatalogRegistry.ts](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/frontend-v1/src/a2ui-engine/CatalogRegistry.ts:1) 可以看出，这个项目最值得借鉴的是：

1. LLM 不只输出文本，还输出 A2UI 消息。
2. 前端不是硬编码某个页面，而是通过 `Catalog + Renderer` 动态渲染组件。
3. 用户对组件的操作会回传给 Agent，形成闭环。
4. 学科能力通过插件注册，而不是把所有可视化直接写死在主应用里。

这非常适合你的项目，因为“宇宙模型智能体”本质上也是：

- 问答驱动
- 概念解释驱动
- 需要在恰当时机插入可视化
- 后续还会增加很多不同类型的天文学组件

### 2.2 组件能力是通过 `capabilities` 明确暴露给模型的

从示例插件清单，如：

- [chemistry-orbital-3d/manifest.json](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/plugins/chemistry-orbital-3d/manifest.json:1)
- [genetics-volcano/manifest.json](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/plugins/genetics-volcano/manifest.json:1)

可以总结出一套非常适合你复用的约束：

- 每个组件都要有清晰的 `component_id`
- 每个组件都要有 `props_schema`
- 要写清楚 `a2ui_hint`
- 要区分：
  - `expresses`：这个组件能表达什么
  - `cannot_express`：这个组件不能表达什么
  - `educational_use`：它在教学上为什么有价值

这点对“抽象概念可视化”尤其重要，因为很多误用都来自：

- 模型不知道什么时候该调用某个组件
- 模型不知道这个组件的边界
- 模型试图用一个组件解释不适合的问题

### 2.3 现成 A2UI 组件适合做“外壳”，专业可视化组件适合做“核心画布”

从 [components.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/vendor/A2UI-main/docs/reference/components.md:1) 看，A2UI 标准组件非常适合承担：

- 布局：`Row`、`Column`、`List`
- 文本：`Text`
- 控件：`Button`、`TextField`、`Checkbox`
- 说明信息、提示区、参数面板

但真正的“抽象概念可视化内核”仍然应该是自定义组件，例如：

- 3D 场景
- 坐标系变换器
- 时间推演器
- 参数敏感性分析器
- 因果链动画器

结论是：

**A2UI 用来编排教学界面，自定义组件用来承载学科可视化本体。**

---

## 3. 适合“抽象概念”的 A2UI 组件设计原则

### 3.1 不直接“给答案”，而是让用户操纵变量

抽象概念最怕做成 PPT 式演示。

所以每个组件都应该尽量让用户做这几类动作：

- 改一个参数，看结果怎么变
- 切换一个参考系，看图像怎么变
- 比较两个状态，找出差异
- 推进时间，观察轨迹演化
- 选一个观测点，理解“视角”如何改变现象

### 3.2 一次只承载一个核心认知任务

建议每个组件只围绕一个“认知动作”设计：

- `理解遮挡关系`
- `理解相对运动`
- `理解坐标转换`
- `理解尺度层级`
- `理解能量与轨道形态关系`

不要试图把“月食、逆行、轨道共振、黄赤交角、红移”全部塞进同一个组件里。

### 3.3 组件内部自带常用控件，Agent 只传初始状态

这一点和 `edu-viz-core` 的示例插件风格一致。

例如：

- Agent 只传 `mode = lunar_eclipse`
- 组件内部自己带：
  - 时间滑块
  - 视角切换
  - 轨迹显隐
  - 标注开关

这样可以减少：

- A2UI 消息复杂度
- Agent 控件编排负担
- 前端动态拼装错误

---

## 4. 适用于宇宙模型智能体的 A2UI 组件分层

建议把组件分成 4 层。

### 4.1 第一层：概念外壳组件

这些组件主要用 A2UI 标准组件组合即可。

#### `ConceptNarrativeCard`

用途：

- 展示一句核心定义
- 展示一个误区提醒
- 展示“建议你接下来操作哪个可视化”

适合承载：

- “月食不是每次满月都会发生”
- “逆行不是行星真的倒退”

#### `ConceptComparePanel`

用途：

- 左右对照两个模型 / 两个视角 / 两个时刻

适合承载：

- 地心视角 vs 日心视角
- VSOP vs DE440
- 黄道坐标 vs 赤道坐标

#### `GuidedStepPanel`

用途：

- 把复杂概念拆成 3-5 个教学步骤

适合承载：

- “先看三体几何关系，再看影锥，再看观测结果”

### 4.2 第二层：参数实验组件

这类组件是抽象概念教学的核心。

#### `ParameterWorkbench`

用途：

- 左侧参数
- 中间主画布
- 右侧当前状态解释

适合承载：

- 轨道半长轴 / 偏心率 / 倾角变化
- 观测者纬度 / 日期 / 时间变化

#### `StateTransitionExplorer`

用途：

- 展示同一系统在不同时间点的状态变化

适合承载：

- 月相变化
- 食分变化
- 逆行发生前后

#### `MultiScaleZoomScene`

用途：

- 从宏观到微观逐层缩放

适合承载：

- 宇宙尺度 -> 星系群 -> 银河系 -> 太阳系
- 太阳系 -> 地月系统 -> 地球影锥

### 4.3 第三层：抽象关系组件

这类组件最适合“解释本质”。

#### `CausalFlowMap`

用途：

- 用图结构把“条件 -> 机制 -> 现象”串起来

适合承载：

- 月食：
  - 满月
  - 轨道交点附近
  - 地球在中间
  - 月球进入地影

#### `ReferenceFrameSwitcher`

用途：

- 切换参考系
- 同步更新同一对象的表现

适合承载：

- 地心 / 日心
- 惯性系 / 旋转系
- 赤道 / 黄道 / 地平坐标

#### `ConstraintSurfaceExplorer`

用途：

- 展示“哪些状态允许、哪些状态不允许”

适合承载：

- 可见食区
- 轨道共振窗口
- 稳定轨道参数区间

### 4.4 第四层：学科专属高复杂组件

这类组件建议做成插件能力。

#### `EclipseGeometryLab`

解释：

- 日食 / 月食 / 半影 / 本影 / 食甚

建议交互：

- 时间拖动
- 俯视 / 侧视切换
- 地影 / 月影显隐
- 黄白交点标注

#### `RetrogradeMotionLab`

解释：

- 逆行作为视运动的成因

建议交互：

- 地心 / 日心切换
- 恒星背景显隐
- 轨迹尾迹
- 会合点高亮

#### `CoordinateTransformLab`

解释：

- 黄道坐标、赤道坐标、地平坐标的关系

建议交互：

- 日期 / 时刻 / 纬度输入
- 三球联动
- 同一点在三坐标系中的位置同步标注

#### `RedshiftSpectrumLab`

解释：

- 波长拉伸、谱线位移、宇宙学红移

建议交互：

- 红移值调节
- 谱线对齐
- 速度 / 距离近似展示

#### `OrbitalResonanceLab`

解释：

- 共振、会合周期、轨道锁定

建议交互：

- 公转比调节
- 角位置追踪
- 相位图

---

## 5. 面向宇宙模型智能体的首批组件清单

建议第一批只做 6 个，覆盖“天文学抽象概念”最常见的解释任务。

### P0

1. `EclipseGeometryLab`
2. `RetrogradeMotionLab`
3. `CoordinateTransformLab`
4. `LunarPhaseWorkbench`

### P1

5. `RedshiftSpectrumLab`
6. `KeplerLawWorkbench`

原因：

- 这 6 个组件足以覆盖大量问答入口
- 都很适合“参数可操纵”的抽象概念教学
- 其中 4 个还能和你现有的行星运动 / 天球项目直接复用

---

## 6. 推荐的 A2UI 插件组织方式

参考 [plugin-development-guide.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/docs/plugin-development-guide.md:1)，建议你不要把所有可视化塞进主前端，而是做成“宿主负责运行时，插件负责学科能力”的模式。

建议目录：

```text
plugins/astronomy-abstract-concepts/
├── manifest.json
├── src/
│   ├── index.ts
│   ├── EclipseGeometryLab.tsx
│   ├── RetrogradeMotionLab.tsx
│   ├── CoordinateTransformLab.tsx
│   ├── LunarPhaseWorkbench.tsx
│   ├── RedshiftSpectrumLab.tsx
│   └── KeplerLawWorkbench.tsx
├── backend/
│   ├── __init__.py
│   ├── orbital_service.py
│   ├── coordinate_service.py
│   └── schemas.py
└── knowledge/
    └── astronomy_concepts.db
```

### 宿主负责

- A2UI Runtime
- Catalog 注册
- 聊天流中的 A2UI 消息渲染
- 用户操作回传
- 统一会话状态

### 插件负责

- 抽象概念组件
- 参数 schema
- 教学提示词
- 必要的天文计算桥接

---

## 7. 推荐的 capability 设计模板

建议你的 `manifest.json` 里，单个组件能力尽量写成类似下面这种风格：

```json
{
  "component_id": "EclipseGeometryLab",
  "name": "日食月食几何实验室",
  "tags": ["月食", "日食", "地影", "本影", "半影", "黄白交点"],
  "props_schema": {
    "mode": {
      "type": "string",
      "default": "lunar",
      "description": "演示模式：lunar 或 solar"
    },
    "timeISO": {
      "type": "string",
      "default": "",
      "description": "初始时刻，ISO 时间字符串"
    },
    "showShadowCone": {
      "type": "boolean",
      "default": true,
      "description": "是否显示本影和半影锥"
    },
    "viewMode": {
      "type": "string",
      "default": "side",
      "description": "视角模式：top 或 side"
    }
  },
  "a2ui_hint": "用于解释月食或日食形成条件。组件内部自带时间拖动、视角切换和影锥显隐，不需要额外生成控件。适合回答“为什么会发生月食”“为什么不是每次满月都有月食”这类问题。",
  "expresses": [
    "太阳地球月球的遮挡几何关系",
    "本影、半影和食分变化",
    "黄白交点与食发生条件"
  ],
  "educational_use": "帮助用户把文字解释转换成空间几何直觉。",
  "cannot_express": [
    "完整高精度观测预报",
    "地方时刻的精确观测条件"
  ]
}
```

关键原则：

- Agent 只传“初始状态”
- 组件内部自带“教学期望内的控件”
- `cannot_express` 一定要写

---

## 8. 推荐的消息与交互链路

参考 [data-flow.md](/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/edu-viz-core-main/vendor/A2UI-main/docs/concepts/data-flow.md:1)，你的链路建议是：

```text
用户提问
→ 问答 Orchestrator 判断是否需要可视化
→ 选择 capability
→ 生成 A2UI surface + component + initial props
→ 前端 Renderer 渲染
→ 用户拖动/点击/切换参数
→ onAction / data update 回传后端
→ Agent 根据用户操作继续解释
```

最重要的不是“把图画出来”，而是：

**把用户的操作重新纳入对话上下文。**

例如：

- 用户把 `viewMode` 从 `top` 切到 `side`
- 用户打开了 `showShadowCone`
- 用户把时间拖到月球进入本影的时刻

这时 Agent 后续回答可以说：

> 你现在看到的是侧视图。当地球影锥完全覆盖月球时，就会进入月全食阶段。

这才是 A2UI 相比普通 iframe 页面真正有价值的地方。

---

## 9. 与你当前宇宙模型智能体的结合方式

你现在已有：

- 问答前端工作台
- manyRAG / MinerU 接入
- 已做好的多张天文学前端页
- `solar_system_app.py`、`heliocentric_celestial_app.py` 这类较成熟的交互原型

建议不要一开始把这些原型全部重写。

更现实的路线是：

### 第一步：页面级能力封装

先把现有成熟页面抽象成 capability：

- `SolarSystemCompareScene`
- `HeliocentricCelestialScene`
- `EclipseGeometryLab`

哪怕底层暂时仍然复用现有 Streamlit / Plotly 逻辑，也先把“何时调用、传什么参数、解释什么概念”定义清楚。

### 第二步：把“页面”重构成插件组件

从最值得频繁调用的组件开始重写成 React + A2UI。

优先顺序建议：

1. `EclipseGeometryLab`
2. `RetrogradeMotionLab`
3. `CoordinateTransformLab`

### 第三步：形成“问答 + 可视化 + 操作反馈”的闭环

当用户问：

- “为什么会发生月食？”
- “逆行到底是不是倒着走？”
- “黄道坐标和赤道坐标有什么区别？”

系统不只是给文字答案，而是：

1. 给一句短解释
2. 自动插入一个 A2UI 组件
3. 引导用户做一步操作
4. 根据操作结果继续讲解

---

## 10. 首批开发建议

### Sprint 1

- 定义 `astronomy-abstract-concepts` 插件边界
- 写 `manifest.json`
- 先做 `EclipseGeometryLab`
- 在宿主里打通一条 A2UI 调用链

### Sprint 2

- 做 `RetrogradeMotionLab`
- 做 `CoordinateTransformLab`
- 增加 Gallery 示例

### Sprint 3

- 加入“用户交互回传后的二次讲解”
- 加入“同一问题推荐多个可视化”的编排逻辑
- 开始接入你现有 DE440 / VSOP 计算服务

---

## 11. 最终建议

如果只保留一句话，我建议是：

**不要把“抽象概念可视化”理解成一组页面，而要把它设计成一组可被 Agent 选择、可被用户操纵、可把操作结果回流给教学对话的 A2UI 能力。**

这正是 `edu-viz-core` 给你的最大启发。

对“宇宙模型智能体”来说，最自然的目标形态不是“一个可视化展厅”，而是：

> 用户在提问，Agent 在判断，A2UI 在生成界面，用户在操作，系统再继续解释。

这会让你的产品从“有很多天文学页面”升级成“真正会教学的宇宙概念交互系统”。
