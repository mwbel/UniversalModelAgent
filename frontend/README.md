# 宇宙模型智能体 - 前端项目

这是宇宙模型智能体的前端应用，采用 React + TypeScript + Vite 构建。

## 项目结构

```
frontend/
├── src/
│   ├── components/          # React 组件
│   │   ├── Sidebar.tsx      # 左侧导航栏
│   │   ├── ChatArea.tsx     # 中间对话区
│   │   └── VisualizationPanel.tsx  # 右侧可视化面板
│   ├── styles/              # 样式文件
│   │   └── global.css       # 全局样式
│   ├── App.tsx              # 主应用组件
│   └── main.tsx             # 应用入口
├── index.html               # HTML 模板
├── package.json             # 项目依赖
├── tsconfig.json            # TypeScript 配置
└── vite.config.ts           # Vite 配置

```

## 功能特性

### 三栏布局设计
参考 NotebookLM 的布局风格：

1. **左侧导航栏 (Sidebar)**
   - 新建对话按钮
   - 导航菜单（对话、场景、知识库、历史）
   - 最近对话列表
   - 设置按钮

2. **中间对话区 (ChatArea)**
   - AI 对话界面
   - 消息列表展示
   - 输入框和发送按钮
   - 对话历史管理

3. **右侧可视化面板 (VisualizationPanel)**
   - 3D 场景选择器
   - 可视化画布区域
   - 场景信息展示
   - 交互控制按钮

### 响应式设计
- 桌面端：完整三栏布局
- 平板端：自适应布局调整
- 移动端：简化导航，垂直堆叠布局

## 快速开始

### 安装依赖
```bash
cd frontend
npm install
```

### 启动开发服务器
```bash
npm run dev
```

应用将在 http://localhost:3000 启动

### 构建生产版本
```bash
npm run build
```

### 预览生产构建
```bash
npm run preview
```

## 技术栈

- **React 18** - UI 框架
- **TypeScript** - 类型安全
- **Vite** - 构建工具
- **CSS3** - 样式设计

## 下一步开发计划

1. 集成 Three.js 实现 3D 可视化
2. 连接后端 API 实现真实对话功能
3. 实现 WebSocket 实时通信
4. 添加状态管理（Redux/Zustand）
5. 实现 AI 与可视化联动
6. 添加更多交互功能

## 开发规范

- 使用 TypeScript 严格模式
- 组件采用函数式组件 + Hooks
- CSS 采用模块化设计
- 遵循 React 最佳实践

---

**版本**: v0.1.0
**创建日期**: 2026-04-03
