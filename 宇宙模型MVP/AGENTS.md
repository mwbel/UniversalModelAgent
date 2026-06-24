# AGENTS.md

## 项目目标

本项目是数学、物理、天文学专业书籍 OCR 校对 MVP。

核心链路：

MinerU output
→ 第三栏校正
→ Mathpix / human draft patch
→ accepted patch
→ dry-run preview
→ accepted corrected Markdown download

目标是 MVP 实用闭环，不追求架构洁癖。

## 执行前必须先输出 Preflight Plan

Codex 修改代码前必须先输出：

1. 本次任务目标。
2. 准备修改的文件。
3. 明确不会修改的文件。
4. 是否涉及：
   - `frontend/ocr-compare.js`
   - `state.ocrPatches`
   - DOM / UI buttons
   - browser wrapper
   - Mathpix API
   - export / download logic
5. 准备运行的测试命令。
6. 如果涉及前端，必须给出手动前端冒烟测试步骤。

输出 Preflight Plan 后，除非用户特别说明“需要确认后再执行”或明确要求当前任务先停留在规划阶段，否则无需等待确认，可以直接修改代码。

即使涉及以下内容，也遵循上述默认直接执行规则，但必须在 Preflight Plan 中明确说明：

1. `frontend/ocr-compare.js`
2. `state.ocrPatches`
3. accepted / rejected patch status
4. export / download logic
5. Mathpix API
6. browser wrapper
7. UI buttons / DOM events

只有用户特别说明需要确认时，才必须等待用户明确确认后再改代码。

## MVP 当前优先级

优先顺序：

1. 不替换原正式导出按钮。
2. 保留原正式导出逻辑作为 fallback。
3. 使用 accepted patch dry-run preview。
4. 新增独立 “下载 accepted 校正稿” 按钮。
5. 只有 accepted 校正稿下载稳定后，才考虑替换正式导出。

## 禁止越界修改

除非任务明确要求，否则禁止修改：

1. `backend/services/model_tester.py`
2. `backend/services/ocr_correction.py`
3. `math_rag_pipeline/mineru_loader.py`
4. Mathpix API 调用逻辑
5. 原正式导出逻辑
6. `buildBookMarkdown()`
7. `mineruMarkdownForPage()`
8. 已有 fixtures expected 文件
9. package dependencies
10. 全局项目配置

## Patch 规则

所有校正修改必须进入 `OcrPatch`。

允许状态：

- `draft`
- `accepted`
- `rejected`
- `noop`
- `conflict`

MVP 规则：

1. `draft` 可以变成 `accepted` 或 `rejected`。
2. accepted patches 可以进入 dry-run preview。
3. accepted patches 可以进入独立的 accepted corrected Markdown download。
4. accepted patches 暂时不能静默替换原正式导出。
5. rejected / noop / conflict patches 不进入 accepted corrected Markdown download。

## 每次修改后必须运行

```bash
node scripts/test_ocr_compare_frontend.js
node frontend/ocr-core/tests/test_block_parser.js
node frontend/ocr-core/tests/test_patch_model.js
node frontend/ocr-core/tests/test_patch_merger.js
node frontend/ocr-core/tests/test_mathpix_render_pipeline.js
node frontend/ocr-core/tests/test_render_validator.js
node frontend/ocr-core/tests/test_mathpix_to_target_markdown_adapter.js
node scripts/test_ocr_core_fixtures.js
node frontend/ocr-core/tests/test_math_delimiter_normalizer.js
node -e "const fs=require('fs'); new Function(fs.readFileSync('frontend/ocr-compare.js','utf8')); console.log('ocr frontend ok')"
git diff --check -- frontend/ocr-compare.js scripts/test_ocr_compare_frontend.js
```
