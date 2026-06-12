# MinerU Markdown 高风险块校正流程

## 背景

当前 OCR 链路不是让大模型重做整本书 OCR，而是采用分层处理：

```text
PDF / 扫描页
-> MinerU 粗识别
-> 输出 Markdown
-> 系统筛选高风险 Markdown 块
-> 仅把高风险块交给 GPT / Gemini 多模态模型校正
-> 将校正结果按原位置合并回 Markdown
```

这样做的目标是：

- 普通正文仍由 MinerU 负责，控制成本。
- 复杂块由多模态模型兜底，提升公式、表格、矩阵、伪代码的准确率。
- 保留 MinerU 已经正确识别的大部分内容，避免整篇重写带来的额外风险。

## 当前模块边界

当前项目中，这条链路已经拆成几个独立模块：

- `backend/services/mineru_client.py`
  只负责调用远端 MinerU 服务。
- `backend/services/ocr_correction.py`
  只负责高风险块检测、模型校正、结果合并。
- `backend/services/markdown_library.py`
  只负责扫描本地 Markdown 资料库。
- `backend/services/rag_client.py`
  只负责本地知识库的摄入、检索和回答。
- `backend/server.py`
  只负责把 HTTP API 编排到这些服务。

这意味着后续如果我们要：

- 调整高风险筛选规则
- 替换校正模型
- 接入新的本地资料目录
- 新增批量处理任务

都不需要把所有逻辑混在一起改。

## 接口入口

相关接口如下：

- `POST /api/ocr/convert`
  只调用 MinerU 转 Markdown。
- `POST /api/ocr/correct`
  对已有 Markdown 做高风险块检测和校正。
- `POST /api/ocr/convert-and-correct`
  先调 MinerU，再自动校正高风险块。

配置项如下：

```bash
export MINERU_BASE_URL="https://mineryou.cpolar.top"
export MINERU_CONVERT_PATH="/api/convert"

export OCR_CORRECTION_PROVIDER="openai-compatible"
export OCR_CORRECTION_BASE_URL="https://..."
export OCR_CORRECTION_API_KEY="..."
export OCR_CORRECTION_MODEL="..."

# 或者使用 Gemini
export OCR_CORRECTION_PROVIDER="gemini"
export OCR_CORRECTION_API_KEY="..."
export OCR_CORRECTION_MODEL="gemini-..."
```

## 核心流程

### 1. MinerU 粗识别

MinerU 将 PDF 或页面图像转换成 Markdown。这个阶段适合处理：

- 普通段落
- 标题
- 大部分线性正文
- 一部分简单表格

但它容易在以下情况出错：

- 表格中的数学公式
- 上标、下标
- 跨多行分块矩阵
- 伪代码缩进与层级
- 复杂二维排版

### 2. 将 Markdown 切成块

系统不会把整篇 Markdown 一次性交给多模态模型，而是先按“空行分隔的文本块”拆分。

每个块都会记录：

- `block_index`
- `start`
- `end`
- `text`

其中 `start/end` 是原始 Markdown 中的字符位置，用于后续精确替换。

### 3. 高风险块检测

每个 Markdown 块会跑一组启发式规则，生成风险分数和原因列表。

主要规则包括：

- `table_with_math`
  表格中同时出现数学信号，例如 `|`、`$`、`\frac`、`^`、`_`。
- `split_formula_tokens`
  疑似把 `$2^7$` 识别成 `$2 7$`，或者把上下标拆成空格数字。
- `matrix_like_layout`
  疑似矩阵布局，例如 `\begin{matrix}`、`pmatrix`、`bmatrix`，或括号中的多列排版。
- `pseudocode_like_layout`
  疑似伪代码，例如命中 `algorithm`、`input`、`output`、`for`、`while`、`if`、`return`、`算法`、`步骤` 等关键词。
- `unbalanced_math_delimiter`
  数学定界符不平衡，例如 `$` 数量为奇数。
- `latex_command_spacing`
  LaTeX 命令后面出现异常空格。

分数低于阈值的块会被跳过，只保留高风险块。然后按分数降序排序，并截取前 `OCR_CORRECTION_MAX_CANDIDATES` 个候选块。

这一步的核心思想是：

- 只把“最可疑、最值得花钱校正”的块送给模型。
- 不要把整篇 Markdown 全量送给大模型。

### 4. `dryRun` 的含义

`dryRun` 表示“只预演，不真正校正”。

例如：

```json
{
  "dryRun": true,
  "markdown": "...",
  "pageImages": [...]
}
```

它会执行：

- Markdown 切块
- 高风险块打分
- 返回候选块列表

但不会执行：

- 调用 GPT / Gemini
- 修改正文
- 合并回 Markdown

适用场景：

- 调试筛选规则
- 检查哪些块会被送去校正
- 控制成本
- 快速验证数据准备是否正确

### 5. 请求体字段如何理解

#### `markdown`

这是待校正的 Markdown 正文。通常来源有两种：

- MinerU 刚输出的全文 Markdown
- 你本地资料库里已有的 `.md` 文件内容

系统会在这份 Markdown 里切块、打分、替换。

#### `pageImages`

这是页面图像列表。典型结构：

```json
[
  {
    "pageNumber": 12,
    "image": "data:image/png;base64,..."
  }
]
```

含义是：

- `pageNumber`
  这张图对应哪一页。
- `image`
  页面图片本身，通常是 `data URL`。

如果候选块可以匹配到对应页码，系统就把那一页图交给模型；如果匹配不到，就先退回用第一张图。

### 6. 为什么校正模型还要处理图片

这一步不是在“重复 OCR”，而是在补回 Markdown 丢失的二维版面信息。

MinerU 输出的 Markdown 只保留了线性文本，但很多错误恰恰来自版面关系丢失。例如：

- `$2 7$` 到底是 `27` 还是 `$2^7$`
- 一个数字是同一行的相邻字符，还是另一个字符的上标
- 矩阵中的元素是同一行，还是上下两行
- 伪代码的缩进和分支结构是不是被打散了
- 表格中的公式究竟属于哪一列哪一行

这些问题单看文本往往判断不稳，多模态模型必须看原页图，才能恢复：

- 左右位置
- 上下位置
- 缩进
- 行列关系
- 基线关系

所以这里的图片不是可选装饰，而是复杂块校正的关键证据。

## 为什么 OpenAI-compatible 和 Gemini 图片字段不同

业务逻辑相同，差别只在 API 协议格式。

### `openai-compatible`

走 `/v1/chat/completions`，图片放在 `image_url` 字段中。

结构类似：

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "..." },
        { "type": "image_url", "image_url": { "url": "data:image/png;base64,..." } }
      ]
    }
  ]
}
```

### `gemini`

走 `generateContent`，图片放在 `inline_data` 中。

结构类似：

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        { "text": "..." },
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "base64..."
          }
        }
      ]
    }
  ]
}
```

所以不是我们想把逻辑写复杂，而是两家模型接口协议本来就不一样。

## 模型收到的内容

系统不会把整本书直接发给模型，而是“逐块发”。

每个候选块单独发送，内容包括：

- 当前块的原始 Markdown
- 当前块命中的 `reasons`
- 当前页图片
- 强约束系统提示词

提示词的要求是：

- 只修这个块
- 只输出修正后的 Markdown
- 不解释
- 不扩写
- 不编造图片中不存在的内容

这样做有几个好处：

- token 更省
- 输出更稳
- 易于回溯具体哪一块被修了
- 失败时不影响全篇

## 合并回 Markdown

校正完成后，系统不会让模型输出整篇新 Markdown，而是做局部替换。

具体做法：

- 依赖每个候选块的 `start/end`
- 保留候选块前后的原始内容
- 只替换当前块范围内的文本
- 依次拼接，得到新的 `correctedMarkdown`

这样能最大程度保留：

- MinerU 已经识别正确的正文
- 原始标题层级
- 其他非高风险区域的结构

也能避免“大模型把整篇 Markdown 重写一遍”的不稳定问题。

## 失败处理

如果某个候选块调用模型失败：

- 该块会记录到 `errors`
- 其他块继续处理
- 原块内容保持不变

这意味着批量处理整本书时，不会因为单个块失败而整篇报废。

## 推荐使用方式

### 第一步：先跑 `dryRun`

先确认筛出来的候选块是不是你真正想修的内容。

```json
{
  "dryRun": true,
  "markdown": "...",
  "pageImages": [...]
}
```

重点看返回里的：

- `candidates`
- 每个候选块的 `score`
- 每个候选块的 `reasons`

### 第二步：关闭 `dryRun`

当候选块看起来合理后，再真正调用模型校正。

```json
{
  "dryRun": false,
  "markdown": "...",
  "pageImages": [...],
  "provider": "openai-compatible",
  "model": "..."
}
```

### 第三步：批量化

后续建议将这条链路再往前推进一步，做成：

```text
本地 Markdown 书库
-> 自动定位对应书籍目录
-> 自动找到 images/ 页图
-> 自动组装 pageImages
-> 自动调用 /api/ocr/correct
-> 输出 correctedMarkdown
-> 回写到新文件或校正结果目录
```

这样才能真正实现“批量自动处理整本书”。

## 下一步建议

当前链路已经具备基础能力，但如果要更实用，建议继续补三件事：

- 自动从本地资料目录的 `images/` 中构建 `pageImages`
- 自动把校正结果写回到新文件，而不是只留在接口返回里
- 增加“页码到 Markdown 块”的映射规则，提升图像匹配准确率

这样之后就不仅是一个接口，而是一条可以真正批量跑书库的处理流水线。
