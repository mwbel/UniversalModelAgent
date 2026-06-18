const RUNTIME_CONFIG = window.__UMA_RUNTIME_CONFIG__ || {};
const API_BASE =
  RUNTIME_CONFIG.apiBaseUrl ||
  RUNTIME_CONFIG.backendUrl ||
  (window.location.protocol === "file:" || window.location.port !== "8787"
    ? "http://127.0.0.1:8787"
    : "");

const state = {
  pdfFile: null,
  pdfDataUrl: "",
  pdfPageCount: 0,
  currentPage: 1,
  pageCache: new Map(),
  mineruInfo: null,
  mineruFileName: "",
  mathpixCache: new Map(),
  busy: false,
};

const els = {};

function apiUrl(path) {
  return `${API_BASE}${path}`;
}

function bindElements() {
  [
    "pdfInput",
    "mineruInput",
    "pickPdfButton",
    "pickMineruButton",
    "mathpixButton",
    "clearButton",
    "fileName",
    "fileMeta",
    "pageList",
    "statusBadge",
    "prevPageButton",
    "nextPageButton",
    "pageInput",
    "pageCountLabel",
  ].forEach((id) => {
    els[id] = document.getElementById(id);
  });
}

function initialize() {
  bindElements();
  els.pickPdfButton.addEventListener("click", () => els.pdfInput.click());
  els.pickMineruButton.addEventListener("click", () => els.mineruInput.click());
  els.pdfInput.addEventListener("change", handlePdfChange);
  els.mineruInput.addEventListener("change", handleMineruChange);
  els.mathpixButton.addEventListener("click", recognizeCurrentPageWithMathpix);
  els.clearButton.addEventListener("click", resetPage);
  els.prevPageButton.addEventListener("click", () => goToPage(state.currentPage - 1));
  els.nextPageButton.addEventListener("click", () => goToPage(state.currentPage + 1));
  els.pageInput.addEventListener("change", () => goToPage(Number(els.pageInput.value || 1)));
  window.addEventListener("mathjax-ready", () => typesetMath(els.pageList));
}

async function handlePdfChange() {
  const file = els.pdfInput.files?.[0] || null;
  if (!file) {
    return;
  }
  state.pdfFile = file;
  state.pdfDataUrl = await readFileAsDataUrl(file);
  state.pageCache.clear();
  state.mathpixCache.clear();
  state.currentPage = 1;
  els.fileName.textContent = file.name;
  els.fileMeta.textContent = `${file.type || "unknown"} · ${formatBytes(file.size)} · 正在读取页数`;
  setStatus("Preparing", "busy");

  try {
    const preview = await loadPagePreview(1);
    state.pdfPageCount = preview.pageCount || preview.pages?.length || 1;
    els.fileMeta.textContent = `${file.type || "unknown"} · ${formatBytes(file.size)} · ${state.pdfPageCount} 页`;
    updatePager();
    await renderCurrentPage();
    setStatus("Ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    els.pageList.innerHTML = `<div class="empty-state">${escapeHtml(error.message)}</div>`;
  }
}

async function handleMineruChange() {
  const file = els.mineruInput.files?.[0] || null;
  if (!file) {
    return;
  }
  setStatus("MinerU", "busy");
  try {
    const text = await readFileAsText(file);
    const data = JSON.parse(text);
    const pdfInfo = Array.isArray(data.pdf_info) ? data.pdf_info : [];
    if (!pdfInfo.length) {
      throw new Error("这个 JSON 没有找到 pdf_info，可能不是 MinerU middle.json。");
    }
    state.mineruInfo = data;
    state.mineruFileName = file.name;
    if (!state.pdfPageCount) {
      state.pdfPageCount = pdfInfo.length;
    }
    updatePager();
    await renderCurrentPage();
    setStatus("Ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    state.mineruInfo = null;
    renderCurrentPage();
  }
}

function resetPage() {
  state.pdfFile = null;
  state.pdfDataUrl = "";
  state.pdfPageCount = 0;
  state.currentPage = 1;
  state.pageCache.clear();
  state.mineruInfo = null;
  state.mineruFileName = "";
  state.mathpixCache.clear();
  state.busy = false;
  els.pdfInput.value = "";
  els.mineruInput.value = "";
  els.fileName.textContent = "未选择原书 PDF";
  els.fileMeta.textContent = "中栏读取已有 MinerU 整书识别结果；右栏按当前页懒加载 Mathpix。";
  els.pageList.innerHTML = '<div class="empty-state">选择原书 PDF，再选择对应的 MinerU `_middle.json`。Mathpix 会按当前页识别并缓存。</div>';
  updatePager();
  setStatus("Ready", "ok");
}

async function goToPage(pageNumber) {
  const total = state.pdfPageCount || getMineruPageCount() || 1;
  const nextPage = Math.max(1, Math.min(pageNumber, total));
  if (nextPage === state.currentPage && state.pageCache.has(nextPage)) {
    return;
  }
  state.currentPage = nextPage;
  updatePager();
  await renderCurrentPage();
}

async function renderCurrentPage() {
  if (!state.pdfDataUrl && !state.mineruInfo) {
    return;
  }
  els.pageList.innerHTML = "";
  const row = document.createElement("article");
  row.className = "page-row";
  const page = await ensureCurrentPagePreview();
  row.append(renderImageCard(page), renderMineruCard(), renderMathpixCard(page));
  els.pageList.append(row);
  typesetMath(row);
}

async function ensureCurrentPagePreview() {
  if (state.pageCache.has(state.currentPage)) {
    return state.pageCache.get(state.currentPage);
  }
  if (!state.pdfDataUrl) {
    return {
      pageNumber: state.currentPage,
      width: "-",
      height: "-",
      image: "",
      mimeType: "image/png",
    };
  }
  setStatus("Page", "busy");
  const preview = await loadPagePreview(state.currentPage);
  const page = preview.pages?.[0];
  if (!page) {
    throw new Error(`没有渲染出第 ${state.currentPage} 页。`);
  }
  state.pdfPageCount = preview.pageCount || state.pdfPageCount || 1;
  state.pageCache.set(state.currentPage, page);
  updatePager();
  setStatus("Ready", "ok");
  return page;
}

async function loadPagePreview(pageNumber) {
  const response = await postJson("/api/ocr/preview-pages", {
    name: state.pdfFile?.name || "book.pdf",
    mimeType: state.pdfFile?.type || "application/pdf",
    dataUrl: state.pdfDataUrl,
    pageNumber,
    maxPages: 1,
    zoom: 1.8,
  });
  if (!response.ok) {
    throw new Error(response.error || "PDF 页面渲染失败");
  }
  return response;
}

function renderImageCard(page) {
  const card = document.createElement("section");
  card.className = "preview-card";
  const imageHtml = page.image
    ? `<img src="${page.image}" alt="第 ${page.pageNumber} 页 OCR 截图">`
    : `<div class="empty-inline">尚未选择 PDF。</div>`;
  card.innerHTML = `
    <div class="card-head">
      <strong>第 ${state.currentPage} 页</strong>
      <span>${page.width || "-"} × ${page.height || "-"}</span>
    </div>
    <div class="page-image-wrap">${imageHtml}</div>
  `;
  return card;
}

function renderMineruCard() {
  const card = document.createElement("section");
  card.className = "preview-card";
  const markdown = mineruMarkdownForPage(state.currentPage);
  const source = state.mineruFileName ? `来自 ${state.mineruFileName}` : "未选择 middle.json";
  card.innerHTML = `
    <div class="card-head">
      <div>
        <strong>MinerU</strong>
        <span>${escapeHtml(source)}</span>
      </div>
      <button class="text-button" type="button" ${markdown ? "" : "disabled"}>复制</button>
    </div>
    <div class="render-body markdown-body ${markdown ? "" : "is-loading"}">
      ${markdown ? renderMarkdownHtml(normalizeMathMarkdown(markdown)) : "选择 MinerU `_middle.json` 后显示当前页结果。"}
    </div>
  `;
  card.querySelector("button").addEventListener("click", async () => {
    await copyButtonText(card.querySelector("button"), markdown);
  });
  return card;
}

function renderMathpixCard(page) {
  const card = document.createElement("section");
  card.className = "preview-card";
  const cached = state.mathpixCache.get(state.currentPage);
  const markdown = cached?.editText || cached?.markdown || "";
  const error = cached?.error || "";
  const previewId = `mathpix-preview-${state.currentPage}`;
  const editorId = `mathpix-editor-${state.currentPage}`;
  card.innerHTML = `
    <div class="card-head">
      <div>
        <strong>Mathpix</strong>
        <span>${cached?.latencyMs ? `${cached.latencyMs} ms` : cached ? "已缓存" : "未识别"}</span>
      </div>
      <button class="text-button" type="button" ${markdown ? "" : "disabled"}>复制</button>
    </div>
    ${renderMathpixBody({ markdown, error, editorId, previewId })}
  `;
  card.querySelector("button").addEventListener("click", async () => {
    const latest = state.mathpixCache.get(state.currentPage);
    await copyButtonText(card.querySelector("button"), latest?.editText || latest?.markdown || markdown);
  });
  const editor = card.querySelector(`#${editorId}`);
  const preview = card.querySelector(`#${previewId}`);
  if (editor && preview) {
    card.querySelectorAll("[data-mathpix-tab]").forEach((button) => {
      button.addEventListener("click", () => {
        const target = button.dataset.mathpixTab;
        card.querySelectorAll("[data-mathpix-tab]").forEach((tabButton) => {
          tabButton.classList.toggle("is-active", tabButton.dataset.mathpixTab === target);
        });
        card.querySelectorAll("[data-mathpix-panel]").forEach((panel) => {
          panel.classList.toggle("is-active", panel.dataset.mathpixPanel === target);
        });
        if (target === "preview") {
          typesetMath(preview);
        }
      });
    });
    editor.addEventListener("input", () => {
      const nextText = editor.value;
      const current = state.mathpixCache.get(state.currentPage) || {};
      state.mathpixCache.set(state.currentPage, { ...current, markdown: current.markdown || nextText, editText: nextText });
      preview.innerHTML = renderMarkdownHtml(normalizeMathMarkdown(nextText));
      typesetMath(preview);
    });
  }
  return card;
}

function renderMathpixBody({ markdown, error, editorId, previewId }) {
  if (error) {
    return `<div class="render-body markdown-body is-error">${escapeHtml(error)}</div>`;
  }
  if (!markdown) {
    return `<div class="render-body markdown-body is-loading">点击“识别当前页 Mathpix”后生成右栏结果。</div>`;
  }
  return `
    <div class="mathpix-workbench">
      <div class="mathpix-tabs" role="tablist" aria-label="Mathpix result view">
        <button class="mathpix-tab is-active" type="button" data-mathpix-tab="source">Markdown</button>
        <button class="mathpix-tab" type="button" data-mathpix-tab="preview">预览</button>
      </div>
      <div class="mathpix-tab-panel is-active" data-mathpix-panel="source">
        <textarea id="${editorId}" class="markdown-editor" spellcheck="false">${escapeHtml(markdown)}</textarea>
      </div>
      <div class="mathpix-tab-panel" data-mathpix-panel="preview">
        <div id="${previewId}" class="render-body markdown-body live-preview">
          ${renderMarkdownHtml(normalizeMathMarkdown(markdown))}
        </div>
      </div>
    </div>
  `;
}

async function recognizeCurrentPageWithMathpix() {
  if (state.busy || !state.pdfDataUrl) {
    return;
  }
  state.busy = true;
  els.mathpixButton.disabled = true;
  setStatus("Mathpix", "busy");
  try {
    const page = await ensureCurrentPagePreview();
    const upload = await postJson("/api/model-tester/upload", {
      name: `page-${state.currentPage}.png`,
      kind: "image",
      mimeType: page.mimeType || "image/png",
      size: estimateDataUrlBytes(page.image),
      dataUrl: page.image,
    });
    if (!upload.ok) {
      throw new Error(upload.error || "图片上传失败");
    }
    const data = await postJson("/api/model-tester/image-to-markdown", {
      attachmentIds: [upload.id],
      prompt: "请将图片中的内容转为 markdown 格式",
      model: "mathpix:mathpix-text",
      models: ["mathpix:mathpix-text"],
      allowFallback: false,
      temperature: 0.3,
    });
    if (!data.ok) {
      throw new Error(data.error || "Mathpix 请求失败");
    }
    const markdown = data.markdown || data.answer || "";
    if (!markdown) {
      throw new Error("Mathpix 响应为空");
    }
    state.mathpixCache.set(state.currentPage, { markdown, editText: markdown, latencyMs: data.latencyMs || null });
    setStatus("Ready", "ok");
  } catch (error) {
    state.mathpixCache.set(state.currentPage, { error: error.message });
    setStatus("Error", "error");
  } finally {
    state.busy = false;
    updatePager();
    await renderCurrentPage();
  }
}

function mineruMarkdownForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  if (!page) {
    return "";
  }
  const blocks = Array.isArray(page.para_blocks) ? page.para_blocks : [];
  return blocks.map(blockToMarkdown).filter(Boolean).join("\n\n");
}

function blockToMarkdown(block) {
  if (!block || typeof block !== "object") {
    return "";
  }
  if (Array.isArray(block.blocks) && !block.lines) {
    const nested = block.blocks.map(blockToMarkdown).filter(Boolean).join("\n\n");
    if (block.type === "code" && nested) {
      return fencedCode(nested);
    }
    return nested;
  }
  if (block.type === "interline_equation") {
    const content = collectBlockText(block, { displayMath: true }).trim();
    return content ? `$$\n${content.replace(/^\$\$|\$\$$/g, "").trim()}\n$$` : "";
  }
  if (block.type === "table") {
    const html = firstSpanValue(block, "html");
    if (html) {
      return htmlTableToMarkdown(html);
    }
  }
  if (block.type === "image") {
    const imagePath = firstSpanValue(block, "image_path");
    return imagePath ? `![image](${imagePath})` : "";
  }
  if (block.type === "code") {
    return fencedCode(collectBlockText(block).trim());
  }
  const text = collectBlockText(block).trim();
  if (!text) {
    return "";
  }
  if (block.type === "title") {
    return `### ${text}`;
  }
  if (block.type === "list") {
    return text
      .split("\n")
      .map((line) => (line.trim() ? `- ${line.trim()}` : ""))
      .join("\n");
  }
  return text;
}

function collectBlockText(block, options = {}) {
  const chunks = [];
  if (Array.isArray(block.lines)) {
    block.lines.forEach((line) => {
      const lineText = (line.spans || []).map((span) => spanToMarkdown(span, options)).join("");
      if (lineText.trim()) {
        chunks.push(lineText.trim());
      }
    });
  }
  if (Array.isArray(block.blocks)) {
    block.blocks.forEach((nested) => {
      const text = collectBlockText(nested, options);
      if (text.trim()) {
        chunks.push(text.trim());
      }
    });
  }
  return chunks.join("\n");
}

function spanToMarkdown(span, options = {}) {
  if (!span || typeof span !== "object") {
    return "";
  }
  if (span.html) {
    return htmlTableToMarkdown(span.html);
  }
  const content = String(span.content || "");
  if (!content && span.image_path) {
    return `![image](${span.image_path})`;
  }
  if (span.type === "inline_equation") {
    return `$${content}$`;
  }
  if (span.type === "interline_equation") {
    return options.displayMath ? content : `$$\n${content}\n$$`;
  }
  return content;
}

function firstSpanValue(block, key) {
  if (Array.isArray(block.lines)) {
    for (const line of block.lines) {
      for (const span of line.spans || []) {
        if (span?.[key]) {
          return span[key];
        }
      }
    }
  }
  if (Array.isArray(block.blocks)) {
    for (const nested of block.blocks) {
      const value = firstSpanValue(nested, key);
      if (value) {
        return value;
      }
    }
  }
  return "";
}

function htmlTableToMarkdown(html) {
  const doc = new DOMParser().parseFromString(String(html || ""), "text/html");
  const rows = Array.from(doc.querySelectorAll("tr")).map((row) =>
    Array.from(row.querySelectorAll("th,td")).map((cell) => cell.textContent.trim().replace(/\s+/g, " "))
  );
  if (!rows.length) {
    return "";
  }
  const width = Math.max(...rows.map((row) => row.length), 1);
  const normalized = rows.map((row) => row.concat(Array(Math.max(0, width - row.length)).fill("")));
  return [
    `| ${normalized[0].join(" | ")} |`,
    `| ${Array(width).fill("---").join(" | ")} |`,
    ...normalized.slice(1).map((row) => `| ${row.join(" | ")} |`),
  ].join("\n");
}

function fencedCode(text) {
  return `\`\`\`\n${text}\n\`\`\``;
}

function getMineruPageCount() {
  return state.mineruInfo?.pdf_info?.length || 0;
}

function updatePager() {
  const total = state.pdfPageCount || getMineruPageCount();
  const hasPages = total > 0;
  els.pageInput.disabled = !hasPages;
  els.prevPageButton.disabled = !hasPages || state.currentPage <= 1;
  els.nextPageButton.disabled = !hasPages || state.currentPage >= total;
  els.mathpixButton.disabled = !state.pdfDataUrl || state.busy;
  els.pageInput.max = hasPages ? String(total) : "";
  els.pageInput.value = String(state.currentPage);
  els.pageCountLabel.textContent = `/ ${hasPages ? total : "-"}`;
}

async function copyButtonText(button, text) {
  if (!text) {
    return;
  }
  await navigator.clipboard.writeText(text);
  button.textContent = "已复制";
  window.setTimeout(() => {
    button.textContent = "复制";
  }, 1200);
}

async function postJson(path, body) {
  const response = await fetch(apiUrl(path), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  return response.json();
}

function readFileAsDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(new Error("读取文件失败"));
    reader.readAsDataURL(file);
  });
}

function readFileAsText(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(new Error("读取文件失败"));
    reader.readAsText(file);
  });
}

function formatBytes(bytes) {
  if (!bytes) {
    return "0 B";
  }
  const units = ["B", "KB", "MB", "GB"];
  let size = bytes;
  let unit = 0;
  while (size >= 1024 && unit < units.length - 1) {
    size /= 1024;
    unit += 1;
  }
  return `${size.toFixed(size >= 10 || unit === 0 ? 0 : 1)} ${units[unit]}`;
}

function estimateDataUrlBytes(dataUrl) {
  const base64 = String(dataUrl || "").split(",", 2)[1] || "";
  return Math.round((base64.length * 3) / 4);
}

function setStatus(text, tone) {
  els.statusBadge.textContent = text;
  els.statusBadge.className = `status-badge ${tone === "busy" ? "is-busy" : tone === "error" ? "is-error" : ""}`;
}

function stripMarkdownFence(text) {
  const stripped = String(text || "").trim();
  const match = stripped.match(/^```(?:markdown|md)?\s*([\s\S]*?)\s*```$/i);
  return match ? match[1].trim() : stripped;
}

function normalizeMathMarkdown(text) {
  const inlineMathPattern = /\b([A-Za-z]\s*=\s*[-+]?(?:[A-Za-z]+|\d+(?:\.\d+)?)(?:\s*\^\s*(?:\{[^}\n]+\}|[A-Za-z0-9()+-]+))?)(?=$|[\s,.;:|)\]])/g;
  return String(text || "")
    .split("\n")
    .map((line) => {
      if (!line.includes("|")) {
        return wrapInlineMathOutsideMathSpans(line, inlineMathPattern);
      }
      const cells = splitMarkdownTableRow(line);
      if (cells.length < 2) {
        return wrapInlineMathOutsideMathSpans(line, inlineMathPattern);
      }
      return `| ${cells
        .map((cell) => {
          const trimmed = cell.trim();
          if (!trimmed || /^:?-{3,}:?$/.test(trimmed)) {
            return trimmed;
          }
          return wrapInlineMathOutsideMathSpans(trimmed, inlineMathPattern);
        })
        .join(" | ")} |`;
    })
    .join("\n");
}

function wrapInlineMathOutsideMathSpans(text, inlineMathPattern) {
  const mathSpanPattern = /(\$\$[\s\S]*?\$\$|\$[^$\n]*?\$)/g;
  return text
    .split(mathSpanPattern)
    .map((part) => {
      if (!part || /^(\$\$[\s\S]*?\$\$|\$[^$\n]*?\$)$/.test(part)) {
        return part;
      }
      return part.replace(inlineMathPattern, (match) => `$${match}$`);
    })
    .join("");
}

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function splitMarkdownTableRow(line) {
  const trimmed = line.trim();
  const body = trimOuterTablePipes(trimmed);
  const cells = [];
  let cell = "";
  let mathDelimiter = "";

  for (let index = 0; index < body.length; index += 1) {
    const char = body[index];
    const previous = body[index - 1] || "";
    if (char === "$" && previous !== "\\") {
      const delimiter = body[index + 1] === "$" ? "$$" : "$";
      if (!mathDelimiter) {
        mathDelimiter = delimiter;
      } else if (mathDelimiter === delimiter) {
        mathDelimiter = "";
      }
      cell += delimiter;
      if (delimiter === "$$") {
        index += 1;
      }
      continue;
    }
    if (char === "|" && !mathDelimiter) {
      cells.push(cell.trim());
      cell = "";
      continue;
    }
    cell += char;
  }
  cells.push(cell.trim());
  return cells;
}

function trimOuterTablePipes(line) {
  let start = 0;
  let end = line.length;
  if (line[start] === "|") {
    start += 1;
  }
  if (line[end - 1] === "|" && line[end - 2] !== "\\") {
    end -= 1;
  }
  return line.slice(start, end);
}

function isMarkdownTableSeparator(line) {
  const cells = splitMarkdownTableRow(line);
  return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
}

function isMarkdownTableStart(lines, index) {
  return (
    typeof lines[index] === "string" &&
    typeof lines[index + 1] === "string" &&
    lines[index].trim().startsWith("|") &&
    lines[index + 1].trim().startsWith("|") &&
    isMarkdownTableSeparator(lines[index + 1])
  );
}

function isCodeFenceStart(line) {
  return /^```/.test(String(line || "").trim());
}

function renderCodeBlock(lines) {
  const opener = lines[0].trim();
  const language = opener.replace(/^```/, "").trim();
  const body = lines.slice(1, -1).join("\n");
  const languageClass = language ? ` class="language-${escapeHtml(language)}"` : "";
  return `<pre><code${languageClass}>${escapeHtml(body)}</code></pre>`;
}

function renderAlgorithmBlock(lines) {
  let indent = 0;
  const formatted = lines
    .map(cleanAlgorithmLine)
    .filter((line, index, arr) => line || (arr[index - 1] && arr[index + 1]))
    .map((line) => {
      if (!line) {
        return "";
      }
      if (/^end\b/i.test(line)) {
        indent = Math.max(0, indent - 1);
      }
      const rendered = `${"  ".repeat(indent)}${line}`;
      if (/^for\b/i.test(line)) {
        indent += 1;
      }
      return rendered;
    })
    .join("\n")
    .trim();
  return `<pre class="algorithm-block"><code>${escapeHtml(formatted)}</code></pre>`;
}

function renderMarkdownTable(lines) {
  const header = splitMarkdownTableRow(lines[0]);
  const bodyRows = lines.slice(2).map(splitMarkdownTableRow);
  const width = Math.max(header.length, ...bodyRows.map((row) => row.length), 1);
  const normalizeRow = (row) => row.concat(Array(Math.max(0, width - row.length)).fill(""));
  const headHtml = normalizeRow(header)
    .map((cell) => `<th>${escapeHtml(cell)}</th>`)
    .join("");
  const bodyHtml = bodyRows
    .map((row) => `<tr>${normalizeRow(row).map((cell) => `<td>${escapeHtml(cell)}</td>`).join("")}</tr>`)
    .join("");
  return `<div class="markdown-table-wrap"><table><thead><tr>${headHtml}</tr></thead><tbody>${bodyHtml}</tbody></table></div>`;
}

function renderParagraph(lines) {
  const text = lines.join("\n").trim();
  if (!text) {
    return "";
  }
  return `<p>${escapeHtml(text).replace(/\n/g, "<br>")}</p>`;
}

function renderHeading(line) {
  const match = String(line || "").match(/^(#{1,6})\s+(.+)$/);
  if (!match) {
    return "";
  }
  const level = Math.min(match[1].length, 4);
  return `<h${level}>${escapeHtml(match[2].trim())}</h${level}>`;
}

function renderList(lines) {
  const items = lines
    .map((line) => line.replace(/^\s*[-*+]\s+/, "").trim())
    .filter(Boolean)
    .map((item) => `<li>${escapeHtml(item)}</li>`)
    .join("");
  return items ? `<ul>${items}</ul>` : "";
}

function renderBlockquote(lines) {
  const text = lines.map((line) => line.replace(/^\s*>\s?/, "")).join("\n");
  return `<blockquote>${renderMarkdownHtml(text)}</blockquote>`;
}

function isAlgorithmLine(line) {
  const trimmed = String(line || "").trim();
  return (
    /^for\b/i.test(trimmed) ||
    /^end\b/i.test(trimmed) ||
    /^\$[^$].*?\$$/.test(trimmed) ||
    /^[A-Za-z]\s*=/.test(trimmed)
  );
}

function cleanAlgorithmLine(line) {
  return String(line || "")
    .trim()
    .replace(/^\$\$?\s*/, "")
    .replace(/\s*\$\$?$/, "")
    .replace(/\\sqrt\{\}\{([^}]+)\}/g, "\\sqrt{$1}")
    .replace(/\s+/g, " ");
}

function collectAlgorithmBlock(lines, startIndex) {
  const blockLines = [];
  let index = startIndex;
  let sawEnd = false;

  while (index < lines.length) {
    const line = lines[index];
    const trimmed = String(line || "").trim();
    if (!trimmed) {
      const nextLine = nextNonEmptyLine(lines, index + 1);
      if (sawEnd && nextLine && !/^for\b/i.test(nextLine.trim())) {
        break;
      }
      blockLines.push("");
      index += 1;
      continue;
    }
    if (blockLines.length && sawEnd && !isAlgorithmLine(line)) {
      break;
    }
    if (!isAlgorithmLine(line)) {
      break;
    }
    blockLines.push(line);
    if (/^end\b/i.test(trimmed)) {
      sawEnd = true;
    }
    index += 1;
  }

  return { blockLines, nextIndex: index };
}

function nextNonEmptyLine(lines, startIndex) {
  for (let index = startIndex; index < lines.length; index += 1) {
    if (String(lines[index] || "").trim()) {
      return lines[index];
    }
  }
  return "";
}

function renderMarkdownHtml(markdown) {
  const lines = String(markdown || "").replace(/\r\n?/g, "\n").split("\n");
  const parts = [];
  let index = 0;

  while (index < lines.length) {
    if (!lines[index].trim()) {
      index += 1;
      continue;
    }

    if (/^(#{1,6})\s+/.test(lines[index].trim())) {
      parts.push(renderHeading(lines[index].trim()));
      index += 1;
      continue;
    }

    if (isCodeFenceStart(lines[index])) {
      const codeLines = [lines[index]];
      index += 1;
      while (index < lines.length && !isCodeFenceStart(lines[index])) {
        codeLines.push(lines[index]);
        index += 1;
      }
      if (index < lines.length) {
        codeLines.push(lines[index]);
        index += 1;
      } else {
        codeLines.push("```");
      }
      parts.push(renderCodeBlock(codeLines));
      continue;
    }

    if (/^for\b/i.test(lines[index].trim())) {
      const { blockLines, nextIndex } = collectAlgorithmBlock(lines, index);
      if (blockLines.some((line) => /^end\b/i.test(String(line || "").trim()))) {
        parts.push(renderAlgorithmBlock(blockLines));
        index = nextIndex;
        continue;
      }
    }

    if (isMarkdownTableStart(lines, index)) {
      const tableLines = [lines[index], lines[index + 1]];
      index += 2;
      while (index < lines.length && lines[index].trim().startsWith("|")) {
        tableLines.push(lines[index]);
        index += 1;
      }
      parts.push(renderMarkdownTable(tableLines));
      continue;
    }

    if (/^\s*[-*+]\s+/.test(lines[index])) {
      const listLines = [];
      while (index < lines.length && /^\s*[-*+]\s+/.test(lines[index])) {
        listLines.push(lines[index]);
        index += 1;
      }
      parts.push(renderList(listLines));
      continue;
    }

    if (/^\s*>\s?/.test(lines[index])) {
      const quoteLines = [];
      while (index < lines.length && /^\s*>\s?/.test(lines[index])) {
        quoteLines.push(lines[index]);
        index += 1;
      }
      parts.push(renderBlockquote(quoteLines));
      continue;
    }

    const paragraphLines = [];
    while (
      index < lines.length &&
      lines[index].trim() &&
      !/^(#{1,6})\s+/.test(lines[index].trim()) &&
      !/^\s*[-*+]\s+/.test(lines[index]) &&
      !/^\s*>\s?/.test(lines[index]) &&
      !isMarkdownTableStart(lines, index) &&
      !isCodeFenceStart(lines[index])
    ) {
      paragraphLines.push(lines[index]);
      index += 1;
    }
    parts.push(renderParagraph(paragraphLines));
  }

  return parts.join("");
}

function typesetMath(root) {
  if (!root || !window.MathJax?.typesetPromise) {
    return;
  }
  window.MathJax.typesetPromise([root]).catch(() => {});
}

initialize();
