# New Thread Start Prompt - OCR Compare

请接手当前 Codex 线程的 OCR 校对模块工作。你不能依赖上一线程的聊天记忆，请先读取并遵守：

```text
/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/AGENTS.md
/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP/docs/thread-handoff-ocr-compare-2026-06-19.md
```

工作目录：

```bash
/Users/Min369/Documents/同步空间/Manju/AIProjects/UnivModel/宇宙模型MVP
```

当前任务不是从头开发，而是接管并稳定已有 OCR Compare 功能。重点文件：

```text
frontend/ocr-compare.html
frontend/ocr-compare.js
frontend/ocr-compare.css
scripts/show_memory.sh
docs/thread-handoff-ocr-compare-2026-06-19.md
```

当前产品目标：

1. 左栏显示原书 PDF 当前页截图。
2. 中栏显示 MinerU 整书 Markdown 在当前页范围内的 Typora-like 渲染结果。
3. 右栏显示高风险 MinerU 块，支持按块调用 Mathpix 校正、查看源码、编辑 Mathpix Markdown，并应用到校正稿。
4. 可选第四栏或右栏 tab 显示整页 Mathpix 参考稿；Mathpix 是付费高精度参考，不替代 MinerU 全书初稿。
5. 导出校正稿时必须使用 applied correction，而不是未应用的 Mathpix draft。

请先复现和验证，不要直接堆补丁。

必须优先验证的已知失败点：

1. MinerU 单行 display math 不能渲染成源码。例如：

```md
$$\widehat {f}(x) = \left\{ \begin{array}{ll}0, & 0 \leq x < 1, \\ 1, & x \geq 1. \end{array} \right.$$
```

2. Mathpix 破碎 aligned 环境必须规范化并正确渲染。例如：

```md
$$\begin{aligned}
$$
\sqrt { x } & \leq ...
$$
$$
& = ...
$$
\end{aligned}$$
```

应该变为：

```md
$$
\begin{aligned}
\sqrt { x } & \leq ...
& = ...
\end{aligned}
$$
```

3. 第三栏默认展开行为：

```text
页面首次加载时展开当前页第一个高风险块，便于检查。
调用 Mathpix 校正后，只展开当前被校正的块。
其他块默认折叠。
```

4. 布局：

```text
如果四栏太挤，优先改成三栏 + 右栏 tab：
- 块级校对
- 整页 Mathpix
```

5. 数据流必须严格区分：

```text
MinerU source -> rendered middle column
Mathpix draft -> editable reference
Applied correction -> exportable corrected Markdown
```

当前已知相关函数/状态：

```text
renderMarkdownHtml()
isDisplayMathStart()
collectDisplayMathBlock()
renderDisplayMathBlock()
prepareMathpixMarkdown()
repairBrokenDisplayMathDelimiters()
removeDanglingSingleDollarLines()
normalizeSingleLineDisplayMath()
reviewExpanded
reviewInitializedPages
ensureDefaultReviewExpansion()
expandOnlyReviewBlock()
renderReviewItem()
mathpixBlockDrafts
```

验证命令：

```bash
node -e "const fs=require('fs'); new Function(fs.readFileSync('frontend/ocr-compare.js','utf8')); console.log('ocr frontend ok')"
python3 -m py_compile backend/*.py backend/services/*.py
```

Codex 自身上下文窗口用量显示已配置：

```toml
show-context-window-usage = true

[features]
memories = true

[memories]
generate_memories = true
use_memories = true
```

如果 UI 中仍看不到 context window usage，需要重启 Codex，或手动打开：

```text
Settings -> General -> Composer -> Show context window usage
```

注意：仓库整体 `git status` 很大，因为 UnivModel 上级项目有大量无关 RAG/data 变动。不要清理、重置或提交无关文件。只处理 OCR Compare 相关文件。
