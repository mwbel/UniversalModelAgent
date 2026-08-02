# 时轮历推算独立仓库迁移 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `AstroZangli-AI_20260716_220133` 的应用内容建立为独立 Git 仓库，并推送到 `jwcai-sh/shilunli-tuishuan` 与 `mwbel/shilunli-tuishuan`。

**Architecture:** 在现有应用目录中建立独立 `.git`，父级 `UnivModel` 仓库保持不变。新仓库根目录直接包含 `backend/`、`frontend/`、`package.json` 和 `de421.bsp`；依赖目录、构建产物和本地密钥由项目级 `.gitignore` 排除。 `origin` 指向 jwcai-sh 主仓库，`backup` 指向 mwbel 备份仓库。

**Tech Stack:** Git, Next.js/TypeScript frontend, Python backend, Skyfield `de421.bsp` ephemeris.

## Global Constraints

- 新仓库根目录必须是应用内容，不保留 `AstroZangli/时轮历推算/` 前缀。
- 必须排除 `node_modules/`、`.next/`、`dist/`、`build/`、`.env`、缓存和日志。
- 必须保留 `de421.bsp`，因为 `backend/annual_motion.py` 从项目根目录读取它。
- 旧 `AstroZangli` 仓库和父级 `UnivModel` 仓库不得删除或重置。
- 主仓库身份使用 `jwcai-sh`；备份仓库身份使用 `mwbel`，不混用跨账号 Fine-grained Token。

---

### Task 1: 建立独立仓库并创建初始提交

**Files:**
- Create: `时轮历推算/AstroZangli-AI_20260716_220133/.git/`（Git 元数据）
- Use: `时轮历推算/AstroZangli-AI_20260716_220133/.gitignore`
- Include: `backend/`、`frontend/`、`README.md`、`运行指南.md`、`package.json`、`package-lock.json`、`de421.bsp`

**Interfaces:**
- Produces: standalone repository rooted at `时轮历推算/AstroZangli-AI_20260716_220133` on branch `main`.

- [ ] **Step 1: Verify source scope before initialization**

```bash
cd "/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/时轮历推算/AstroZangli-AI_20260716_220133"
test -f backend/annual_motion.py
test -f de421.bsp
test -d frontend
test ! -d .git
```

- [ ] **Step 2: Initialize the standalone repository**

```bash
git init -b main
```

- [ ] **Step 3: Stage the project and verify exclusions**

```bash
git add -A
git status --short
git ls-files | rg '(^|/)(node_modules|\\.next|dist|build)(/|$)|(^|/)\\.env($|\\.)' && exit 1 || true
git ls-files de421.bsp
```

Expected: no dependency/build/env paths are listed, and `de421.bsp` is listed.

- [ ] **Step 4: Create the standalone initial commit**

```bash
git commit -m "Initial standalone Shilunli calendar application"
```

- [ ] **Step 5: Verify the new repository root and commit**

```bash
git rev-parse --show-toplevel
git branch --show-current
git log -1 --oneline
```

Expected root: `.../时轮历推算/AstroZangli-AI_20260716_220133`; branch: `main`.

### Task 2: Configure the two GitHub remotes

**Files:**
- Modify: `时轮历推算/AstroZangli-AI_20260716_220133/.git/config`

**Interfaces:**
- Consumes: Task 1 standalone repository and initial commit.
- Produces: `origin` for `jwcai-sh/shilunli-tuishuan`; `backup` for `mwbel/shilunli-tuishuan`.

- [ ] **Step 1: Confirm both empty GitHub repositories exist**

```bash
git ls-remote https://github.com/jwcai-sh/shilunli-tuishuan.git
git ls-remote https://github.com/mwbel/shilunli-tuishuan.git
```

If either command reports that the repository does not exist, create that empty repository in the matching GitHub account before continuing.

- [ ] **Step 2: Configure remotes**

```bash
git remote remove origin 2>/dev/null || true
git remote remove backup 2>/dev/null || true
git remote add origin https://github.com/jwcai-sh/shilunli-tuishuan.git
git remote add backup https://mwbel@github.com/mwbel/shilunli-tuishuan.git
git remote -v
```

- [ ] **Step 3: Configure path-scoped HTTPS credentials**

```bash
git config credential.useHttpPath true
```

This keeps the jwcai-sh and mwbel credentials separate in macOS Keychain.

### Task 3: Push and verify the standalone repositories

**Files:**
- Modify: remote GitHub repositories only

**Interfaces:**
- Consumes: Task 2 remotes and credentials.
- Produces: `main` branch in both new repositories.

- [ ] **Step 1: Push the main repository as jwcai-sh**

```bash
git push -u origin main
```

At the prompt use username `jwcai-sh` and the jwcai-sh Token with access to `jwcai-sh/shilunli-tuishuan`.

- [ ] **Step 2: Push the backup repository as mwbel**

```bash
git push -u backup main
```

At the prompt use username `mwbel` and the mwbel Token with access to `mwbel/shilunli-tuishuan`.

- [ ] **Step 3: Verify both remote branches**

```bash
git ls-remote --heads origin main
git ls-remote --heads backup main
git status --short
```

Expected: both remotes report a `main` reference for the same initial commit, and the working tree is clean.

- [ ] **Step 4: Verify deployment root configuration**

Configure Zeabur to deploy `jwcai-sh/shilunli-tuishuan`, branch `main`, with repository root as the build context. Do not configure the old nested path.

- [ ] **Step 5: Commit any migration-only documentation changes**

```bash
git add README.md 2>/dev/null || true
git diff --cached --check
git commit -m "Document standalone repository layout" 2>/dev/null || true
```

Only create this optional follow-up commit if the root README needs an updated repository/deployment path.
