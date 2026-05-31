# 宇宙模型智能体 MVP

这是基于现有外部 OCR 与多版本 RAG 服务进行集成开发的 MVP 工程骨架。

## 当前已完成

- `backend/server.py`：零依赖 Python HTTP 服务
- `frontend/index.html`：MVP 对话工作台
- `frontend/interactive-visualizations/`：历史可视化展厅与原型页面
- 外部服务接入骨架：
  - MinerU OCR
  - 多版本 RAG

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
- `RAG_BASE_URL`
- `RAG_CHAT_PATH`
- `RAG_VARIANTS`
- `REQUEST_TIMEOUT_SECONDS`

## 当前说明

由于外部服务的真实 API 路径与返回结构还需要进一步对齐，当前后端已经提供统一接入层和本地兜底逻辑。接下来可以继续逐条完成 issue 列表里的：

1. RAG 服务接口对齐
2. OCR 批量转换流程接入
3. 引用结构标准化
4. 问答与可视化联动增强
