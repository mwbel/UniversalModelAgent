# 时轮历推算独立仓库迁移设计

## 目标

将现有应用
`时轮历推算/AstroZangli-AI_20260716_220133`
迁移为独立项目仓库，使新仓库根目录直接包含 `backend/`、`frontend/`、`package.json` 等应用文件，不再依赖 `AstroZangli/时轮历推算/` 的多层路径。

## 目标仓库

- 主仓库：`jwcai-sh/shilunli-tuishuan`
- 备份仓库：`mwbel/shilunli-tuishuan`
- 新仓库默认分支：`main`
- Zeabur 部署目录：仓库根目录

## 迁移内容

纳入新仓库：

- `backend/` 与 `frontend/` 全部源代码和测试
- `README.md`、运行指南、依赖清单和锁文件
- `frontend/public/` 中的知识库与可视化资源
- `de421.bsp`，因为 `backend/annual_motion.py` 会从项目根目录读取该星历文件
- 项目级 `.gitignore`，并保留对依赖、构建产物和环境变量的忽略规则

不纳入新仓库：

- `node_modules/`
- `.next/`、`dist/`、`build/` 等构建缓存
- `.env` 及任何本地密钥
- Python 缓存、日志和临时文件

## Git 结构与推送

在应用目录建立独立 Git 历史，父级 `UnivModel` 仓库保留不动。新仓库使用：

- `origin`：`jwcai-sh/shilunli-tuishuan`
- `backup`：`mwbel/shilunli-tuishuan`

迁移时从当前已验证的应用快照创建 `main` 初始提交；旧的 `AstroZangli` 仓库不删除，作为迁移期间的回滚来源。备份仓库使用 `mwbel` 自有凭据，避免用 `jwcai-sh` 的 Fine-grained Token 作为跨账号协作者推送。

## 验证标准

1. 新仓库根目录直接显示 `backend/` 和 `frontend/`。
2. Git 跟踪列表不包含 `node_modules/`、环境文件或构建产物。
3. `de421.bsp` 存在，周年视运动接口可以加载星历。
4. `main` 分支成功推送到 `jwcai-sh` 主仓库，并可单独推送到 `mwbel` 备份仓库。
5. Zeabur 使用仓库根目录构建，不再配置旧的多层根目录。

## 回滚策略

迁移完成并验证部署前，不删除旧仓库、旧分支或现有本地目录。若新仓库推送或部署失败，继续使用旧 `AstroZangli` 仓库，修复新仓库后再切换 Zeabur。
