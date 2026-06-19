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
  mineruOverrides: new Map(),
  mineruBlockOverrides: new Map(),
  mathpixBlockDrafts: new Map(),
  riskByPage: new Map(),
  mathpixCache: new Map(),
  reviewExpanded: new Set(),
  reviewInitializedPages: new Set(),
  busy: false,
};

const els = {};
const COLUMN_WIDTHS_KEY = "uma-ocr-compare-column-ratios-v6";
const LEGACY_COLUMN_WIDTHS_KEYS = [
  "uma-ocr-compare-column-widths",
  "uma-ocr-compare-column-fractions-v2",
  "uma-ocr-compare-column-fractions-v3",
  "uma-ocr-compare-column-ratios-v4",
  "uma-ocr-compare-column-ratios-v5",
];

let ocrCoreNormalizeMathDelimiters = null;
let ocrCoreNormalizerLoadStarted = false;
let ocrCoreNormalizerWarningShown = false;

function getOcrCoreNormalizeMathDelimiters() {
  if (ocrCoreNormalizeMathDelimiters) {
    return ocrCoreNormalizeMathDelimiters;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/normalization/mathDelimiterNormalizer");
      if (typeof module?.normalizeMathDelimiters === "function") {
        ocrCoreNormalizeMathDelimiters = module.normalizeMathDelimiters;
        return ocrCoreNormalizeMathDelimiters;
      }
    } catch (error) {
      warnOcrCoreNormalizer("无法通过 require 加载 mathDelimiterNormalizer。", error);
    }
  }
  const browserModule = globalThis?.OcrCoreMathDelimiterNormalizer;
  if (typeof browserModule?.normalizeMathDelimiters === "function") {
    ocrCoreNormalizeMathDelimiters = browserModule.normalizeMathDelimiters;
    return ocrCoreNormalizeMathDelimiters;
  }
  loadOcrCoreNormalizerForBrowser();
  return null;
}

function loadOcrCoreNormalizerForBrowser() {
  if (ocrCoreNormalizerLoadStarted || typeof document === "undefined" || typeof document.createElement !== "function") {
    return;
  }
  ocrCoreNormalizerLoadStarted = true;
  const script = document.createElement("script");
  script.src = "./ocr-core/normalization/mathDelimiterNormalizer.browser.js";
  script.async = false;
  script.dataset.ocrCore = "math-delimiter-normalizer";
  script.addEventListener("error", () => {
    warnOcrCoreNormalizer("浏览器兼容入口 mathDelimiterNormalizer.browser.js 加载失败。");
  });
  (document.head || document.body || document.documentElement).appendChild(script);
}

function warnOcrCoreNormalizer(message, error) {
  if (ocrCoreNormalizerWarningShown || typeof console === "undefined" || typeof console.warn !== "function") {
    return;
  }
  ocrCoreNormalizerWarningShown = true;
  console.warn(`[OCR Core] ${message}`, error || "");
}

loadOcrCoreNormalizerForBrowser();

function apiUrl(path) {
  return `${API_BASE}${path}`;
}

function bindElements() {
  [
    "pdfInput",
    "mineruInput",
    "pickPdfButton",
    "pickMineruButton",
    "nextRiskButton",
    "mathpixButton",
    "exportOriginalButton",
    "exportCorrectedButton",
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
  restoreColumnWidths();
  els.pickPdfButton.addEventListener("click", () => els.pdfInput.click());
  els.pickMineruButton.addEventListener("click", () => els.mineruInput.click());
  els.pdfInput.addEventListener("change", handlePdfChange);
  els.mineruInput.addEventListener("change", handleMineruChange);
  els.nextRiskButton.addEventListener("click", goToNextRiskPage);
  els.mathpixButton.addEventListener("click", recognizeCurrentPageWithMathpix);
  els.exportOriginalButton.addEventListener("click", () => exportMineruMarkdown(false));
  els.exportCorrectedButton.addEventListener("click", () => exportMineruMarkdown(true));
  els.clearButton.addEventListener("click", resetPage);
  els.prevPageButton.addEventListener("click", () => goToPage(state.currentPage - 1));
  els.nextPageButton.addEventListener("click", () => goToPage(state.currentPage + 1));
  els.pageInput.addEventListener("change", () => goToPage(Number(els.pageInput.value || 1)));
  document.addEventListener("pointerdown", handleColumnResizeStart);
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
  state.mathpixBlockDrafts.clear();
  state.mineruOverrides.clear();
  state.mineruBlockOverrides.clear();
  state.riskByPage.clear();
  state.reviewExpanded.clear();
  state.reviewInitializedPages.clear();
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
    state.mineruOverrides.clear();
    state.mineruBlockOverrides.clear();
    state.mathpixBlockDrafts.clear();
    state.reviewExpanded.clear();
    state.reviewInitializedPages.clear();
    analyzeMineruRiskPages();
    if (!state.pdfPageCount) {
      state.pdfPageCount = pdfInfo.length;
    }
    updatePager();
    await renderCurrentPage();
    setStatus("Ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    state.mineruInfo = null;
    state.mineruOverrides.clear();
    state.mineruBlockOverrides.clear();
    state.mathpixBlockDrafts.clear();
    state.riskByPage.clear();
    state.reviewExpanded.clear();
    state.reviewInitializedPages.clear();
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
  state.mineruOverrides.clear();
  state.mineruBlockOverrides.clear();
  state.mathpixBlockDrafts.clear();
  state.riskByPage.clear();
  state.mathpixCache.clear();
  state.reviewExpanded.clear();
  state.reviewInitializedPages.clear();
  state.busy = false;
  els.pdfInput.value = "";
  els.mineruInput.value = "";
  els.fileName.textContent = "未选择原书 PDF";
  els.fileMeta.textContent = "中栏读取已有 MinerU 整书识别结果；优先点击高风险块进行 Mathpix 块级校正。";
  els.pageList.innerHTML = '<div class="empty-state">选择原书 PDF，再选择对应的 MinerU `_middle.json`。优先点击高风险块，只对该块调用 Mathpix。</div>';
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
  state.reviewExpanded.clear();
  updatePager();
  await renderCurrentPage();
}

async function goToNextRiskPage() {
  const riskPages = Array.from(state.riskByPage.keys()).sort((a, b) => a - b);
  if (!riskPages.length) {
    return;
  }
  const next = riskPages.find((pageNumber) => pageNumber > state.currentPage) || riskPages[0];
  await goToPage(next);
}

async function renderCurrentPage() {
  if (!state.pdfDataUrl && !state.mineruInfo) {
    return;
  }
  els.pageList.innerHTML = "";
  const row = document.createElement("article");
  row.className = "page-row";
  const page = await ensureCurrentPagePreview();
  row.append(
    renderImageCard(page),
    createColumnResizer("left"),
    renderMineruCard(),
    createColumnResizer("right"),
    renderRightWorkbench(page),
  );
  els.pageList.append(row);
  typesetMath(row);
}

function createColumnResizer(side) {
  const button = document.createElement("button");
  button.className = "column-resizer";
  button.type = "button";
  button.dataset.resizer = side;
  const labels = {
    left: "调整原文和 MinerU 栏宽",
    right: "调整 MinerU 和校对栏宽",
  };
  button.setAttribute("aria-label", labels[side] || "调整栏宽");
  return button;
}

function restoreColumnWidths() {
  const panel = document.querySelector(".preview-panel");
  if (!panel) {
    return;
  }
  LEGACY_COLUMN_WIDTHS_KEYS.forEach((key) => localStorage.removeItem(key));
  try {
    const saved = JSON.parse(localStorage.getItem(COLUMN_WIDTHS_KEY) || "null");
    if (!saved) {
      return;
    }
    setColumnRatios(normalizeColumnRatios(saved));
  } catch {
    localStorage.removeItem(COLUMN_WIDTHS_KEY);
  }
}

function handleColumnResizeStart(event) {
  const handle = event.target.closest?.(".column-resizer[data-resizer]");
  if (!handle || window.matchMedia("(max-width: 980px)").matches) {
    return;
  }
  event.preventDefault();
  const side = handle.dataset.resizer;
  const panel = document.querySelector(".preview-panel");
  const columns = readCurrentColumnWidths();
  if (!panel || !columns) {
    return;
  }

  const startX = event.clientX;
  const start = { ...columns };
  const min = { left: 180, middle: 260, right: 320 };
  document.body.classList.add("is-resizing-columns");

  const onMove = (moveEvent) => {
    const dx = moveEvent.clientX - startX;
    if (side === "left") {
      const nextLeft = clamp(start.left + dx, min.left, start.left + start.middle - min.middle);
      const nextMiddle = start.middle - (nextLeft - start.left);
      setColumnWidths({ left: nextLeft, middle: nextMiddle, right: start.right });
      return;
    }
    const nextMiddle = clamp(start.middle + dx, min.middle, start.middle + start.right - min.right);
    const nextRight = start.right - (nextMiddle - start.middle);
    setColumnWidths({ left: start.left, middle: nextMiddle, right: nextRight });
  };

  const onUp = () => {
    document.body.classList.remove("is-resizing-columns");
    const latest = readCurrentColumnWidths();
    if (latest) {
      localStorage.setItem(COLUMN_WIDTHS_KEY, JSON.stringify(widthsToRatios(latest)));
    }
    window.removeEventListener("pointermove", onMove);
    window.removeEventListener("pointerup", onUp);
  };

  window.addEventListener("pointermove", onMove);
  window.addEventListener("pointerup", onUp, { once: true });
}

function readCurrentColumnWidths() {
  const row = document.querySelector(".page-row") || document.querySelector(".column-heads");
  if (!row) {
    return null;
  }
  const columns = getComputedStyle(row)
    .gridTemplateColumns.split(/\s+/)
    .map((item) => Number.parseFloat(item))
    .filter(Number.isFinite);
  if (columns.length < 5) {
    return null;
  }
  return {
    left: columns[0],
    middle: columns[2],
    right: columns[4],
  };
}

function setColumnWidths(widths) {
  setColumnRatios(widthsToRatios(widths));
}

function setColumnRatios(ratios) {
  const panel = document.querySelector(".preview-panel");
  if (!panel) {
    return;
  }
  panel.style.setProperty("--ocr-left-ratio", String(ratios.left));
  panel.style.setProperty("--ocr-middle-ratio", String(ratios.middle));
  panel.style.setProperty("--ocr-right-ratio", String(ratios.right));
}

function widthsToRatios(widths) {
  const total = Math.max(1, widths.left + widths.middle + widths.right);
  return normalizeColumnRatios({
    left: widths.left / total,
    middle: widths.middle / total,
    right: widths.right / total,
  });
}

function normalizeColumnRatios(ratios) {
  const left = clamp(Number(ratios?.left) || 0.28, 0.12, 0.58);
  const middle = clamp(Number(ratios?.middle) || 0.42, 0.18, 0.65);
  const right = clamp(Number(ratios?.right) || 0.3, 0.18, 0.6);
  const total = Math.max(0.01, left + middle + right);
  return {
    left: roundFraction(left / total),
    middle: roundFraction(middle / total),
    right: roundFraction(right / total),
  };
}

function roundFraction(value) {
  return Math.round(value * 1000) / 1000;
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
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
  card.className = "preview-card image-card";
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
  card.className = "preview-card mineru-card";
  const markdown = mineruMarkdownForPage(state.currentPage);
  const source = state.mineruFileName ? `来自 ${state.mineruFileName}` : "未选择 middle.json";
  const hasOverride = state.mineruOverrides.has(state.currentPage) || getBlockOverrides(state.currentPage, false).size > 0;
  const risks = state.riskByPage.get(state.currentPage) || [];
  const previewHtml = renderMineruPagePreview(state.currentPage, risks);
  card.innerHTML = `
    <div class="card-head">
      <div>
        <strong>MinerU</strong>
        <span>${hasOverride ? "已应用 Mathpix 校正稿" : escapeHtml(source)}</span>
      </div>
      <div class="card-actions">
        <button class="text-button" type="button" data-copy-mineru ${markdown ? "" : "disabled"}>复制</button>
        <button class="text-button" type="button" data-reset-mineru ${hasOverride ? "" : "hidden"}>还原</button>
      </div>
    </div>
    <div class="render-body markdown-body typora-preview ${previewHtml ? "" : "is-loading"}">
      ${previewHtml || "选择 MinerU `_middle.json` 后显示当前页结果。"}
    </div>
  `;
  card.querySelector("[data-copy-mineru]").addEventListener("click", async () => {
    await copyButtonText(card.querySelector("[data-copy-mineru]"), markdown);
  });
  card.querySelector("[data-reset-mineru]")?.addEventListener("click", async () => {
    state.mineruOverrides.delete(state.currentPage);
    state.mineruBlockOverrides.delete(state.currentPage);
    updateCorrectionSummary();
    await renderCurrentPage();
  });
  return card;
}

function renderMineruPagePreview(pageNumber, risks) {
  if (state.mineruOverrides.has(pageNumber)) {
    return renderMarkdownHtml(normalizeMathMarkdown(state.mineruOverrides.get(pageNumber)));
  }
  const segments = pageSegmentsForPage(pageNumber);
  if (!segments.length) {
    return "";
  }
  const riskByBlock = new Map(risks.map((item) => [String(item.blockIndex), item]));
  const blockOverrides = getBlockOverrides(pageNumber, false);
  return `
    <div class="mineru-page-preview">
      ${segments
        .map((segment) => {
          const key = String(segment.blockIndex);
          const risk = riskByBlock.get(key);
          const markdown = blockOverrides.get(key) || segment.markdown;
          return renderMineruBlock(segment, markdown, risk, blockOverrides.has(key), { showControls: false, showSource: false });
        })
        .join("")}
    </div>
  `;
}

function renderMineruBlock(entry, markdown, risk, corrected, options = {}) {
  const showControls = options.showControls !== false;
  const showSource = options.showSource !== false;
  const isRisk = Boolean(risk);
  const labels = risk ? risk.reasons.map(riskReasonLabel).join(" · ") : "";
  const disabled = risk?.bbox ? "" : "disabled";
  const actionLabel = corrected ? "重新校正此块" : risk?.bbox ? "Mathpix 校正此块" : "缺少 bbox";
  return `
    <section class="mineru-block ${isRisk ? "is-risk" : ""} ${corrected ? "is-corrected" : ""}" data-block-index="${entry.blockIndex}">
      ${
        isRisk
          ? `<div class="block-risk-head">
              <span>${corrected ? "已校正" : "高风险"} · ${escapeHtml(labels)}</span>
              ${showControls ? `<button class="text-button risk-action" type="button" data-risk-mathpix="${entry.blockIndex}" ${disabled}>${actionLabel}</button>` : ""}
            </div>`
          : ""
      }
      <div class="mineru-block-content">
        ${renderBlockContent(markdown, entry)}
      </div>
      ${
        isRisk && showSource
          ? `<details class="block-source-detail">
              <summary>查看当前块 Markdown 源码</summary>
              <pre><code>${escapeHtml(markdown)}</code></pre>
            </details>`
          : ""
      }
    </section>
  `;
}

function renderRightWorkbench(page) {
  const card = document.createElement("section");
  card.className = "preview-card right-workbench-card";
  card.innerHTML = `
    <div class="card-head">
      <div>
        <strong>校对工作台</strong>
        <span>Mathpix draft 需应用后才会进入导出校正稿</span>
      </div>
    </div>
    <div class="right-workbench-tabs" role="tablist" aria-label="OCR correction workspace">
      <button class="right-workbench-tab is-active" type="button" data-workbench-tab="review">块级校对</button>
      <button class="right-workbench-tab" type="button" data-workbench-tab="mathpix">整页 Mathpix</button>
    </div>
    <div class="right-workbench-panel is-active" data-workbench-panel="review"></div>
    <div class="right-workbench-panel" data-workbench-panel="mathpix"></div>
  `;
  card.querySelector('[data-workbench-panel="review"]').append(renderReviewCard());
  card.querySelector('[data-workbench-panel="mathpix"]').append(renderMathpixCard(page));
  card.querySelectorAll("[data-workbench-tab]").forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.dataset.workbenchTab;
      card.querySelectorAll("[data-workbench-tab]").forEach((tabButton) => {
        tabButton.classList.toggle("is-active", tabButton.dataset.workbenchTab === target);
      });
      card.querySelectorAll("[data-workbench-panel]").forEach((panel) => {
        panel.classList.toggle("is-active", panel.dataset.workbenchPanel === target);
      });
      if (target === "mathpix") {
        typesetMath(card.querySelector('[data-workbench-panel="mathpix"]'));
      }
    });
  });
  return card;
}

function renderReviewCard() {
  const card = document.createElement("section");
  card.className = "review-card";
  const risks = state.riskByPage.get(state.currentPage) || [];
  const segments = pageSegmentsForPage(state.currentPage);
  const orderedRisks = orderRisksBySegment(risks, segments);
  ensureDefaultReviewExpansion(orderedRisks);
  const segmentByKey = new Map(segments.map((segment) => [String(segment.blockIndex), segment]));
  const blockOverrides = getBlockOverrides(state.currentPage, false);
  const mathpixDrafts = getMathpixBlockDrafts(state.currentPage, false);
  card.innerHTML = `
    <div class="card-head">
      <div>
        <strong>高风险校对</strong>
        <span>${orderedRisks.length ? `${orderedRisks.length} 个待核查块` : "当前页未发现高风险块"}</span>
      </div>
    </div>
    <div class="review-list markdown-body">
      ${
        orderedRisks.length
          ? orderedRisks
              .map((risk) => {
                const key = String(risk.blockIndex);
                const segment = segmentByKey.get(key) || {
                  blockIndex: key,
                  markdown: risk.text,
                  kind: "block",
                };
                return renderReviewItem(
                  segment,
                  risk,
                  blockOverrides.get(key) || "",
                  blockOverrides.has(key),
                  mathpixDrafts.get(key) || "",
                );
              })
              .join("")
          : `<div class="empty-inline">当前页未发现高风险块。</div>`
      }
    </div>
  `;
  card.querySelectorAll("[data-risk-mathpix]").forEach((button) => {
    button.addEventListener("click", () => recognizeRiskBlockWithMathpix(button.dataset.riskMathpix));
  });
  card.querySelectorAll("[data-review-toggle]").forEach((button) => {
    button.addEventListener("click", () => toggleReviewBlock(button.dataset.reviewToggle));
  });
  card.querySelectorAll("[data-apply-mathpix-block-edit]").forEach((button) => {
    button.addEventListener("click", () => applyMathpixBlockEdit(button.dataset.applyMathpixBlockEdit, button));
  });
  return card;
}

function ensureDefaultReviewExpansion(orderedRisks) {
  if (!orderedRisks.length || state.reviewInitializedPages.has(state.currentPage)) {
    return;
  }
  state.reviewExpanded.add(reviewBlockKey(state.currentPage, orderedRisks[0].blockIndex));
  state.reviewInitializedPages.add(state.currentPage);
}

function orderRisksBySegment(risks, segments) {
  const orderByKey = new Map(segments.map((segment, index) => [String(segment.blockIndex), index]));
  return risks
    .slice()
    .sort(
      (left, right) =>
        (orderByKey.get(String(left.blockIndex)) ?? Number.MAX_SAFE_INTEGER) -
        (orderByKey.get(String(right.blockIndex)) ?? Number.MAX_SAFE_INTEGER),
    );
}

function renderReviewItem(segment, risk, correctedMarkdown, corrected, mathpixDraftMarkdown = "") {
  const labels = risk.reasons.map(riskReasonLabel).join(" · ");
  const disabled = risk.bbox ? "" : "disabled";
  const hasMathpixDraft = Boolean(String(mathpixDraftMarkdown || "").trim());
  const editableMarkdown = prepareMathpixMarkdown(mathpixDraftMarkdown || correctedMarkdown || "");
  const hasEditableMarkdown = Boolean(editableMarkdown.trim());
  const previewMarkdown = hasMathpixDraft ? editableMarkdown : correctedMarkdown;
  const reviewKey = reviewBlockKey(state.currentPage, segment.blockIndex);
  const expanded = state.reviewExpanded.has(reviewKey);
  return `
    <article class="review-item ${corrected ? "is-corrected" : ""} ${hasMathpixDraft ? "has-mathpix-draft" : ""} ${expanded ? "is-expanded" : "is-collapsed"}">
      <div class="review-item-head">
        <div>
          <strong>${hasMathpixDraft ? "Mathpix 待应用" : corrected ? "已应用" : "待核查"} · ${escapeHtml(labels)}</strong>
          <span>Block ${escapeHtml(String(segment.blockIndex))}</span>
        </div>
        <div class="review-item-actions">
          <button class="text-button review-toggle" type="button" data-review-toggle="${escapeHtml(reviewKey)}">
            ${expanded ? "收起" : "展开"}
          </button>
          <button class="text-button risk-action" type="button" data-risk-mathpix="${segment.blockIndex}" ${disabled}>
            ${corrected ? "重新校正此块" : risk.bbox ? "Mathpix 校正此块" : "缺少 bbox"}
          </button>
        </div>
      </div>
      <div class="review-item-body" ${expanded ? "" : "hidden"}>
        <section class="review-pane">
          <div class="review-pane-title">MinerU 渲染</div>
          <div class="review-render">
            ${renderBlockContent(segment.markdown, segment)}
          </div>
          <details class="block-source-detail">
            <summary>查看当前块 Markdown 源码</summary>
            <pre><code>${escapeHtml(segment.markdown)}</code></pre>
          </details>
        </section>
        ${
          corrected || hasEditableMarkdown
            ? `<section class="review-pane mathpix-pane">
                <div class="review-pane-title">${hasMathpixDraft ? "Mathpix 识别稿（未应用）" : "校正稿渲染"}</div>
                <div class="review-render">
                  ${renderBlockContent(previewMarkdown, segment)}
                </div>
              <details class="block-source-detail">
                <summary>编辑 Markdown 源码（应用后写入校正稿）</summary>
                <textarea class="mathpix-source-editor" data-mathpix-edit="${escapeHtml(String(segment.blockIndex))}" spellcheck="false">${escapeHtml(editableMarkdown)}</textarea>
                <div class="mathpix-edit-actions">
                  <button class="text-button" type="button" data-apply-mathpix-block-edit="${escapeHtml(String(segment.blockIndex))}">
                    ${hasMathpixDraft ? "应用到校正稿" : "更新校正稿"}
                  </button>
                </div>
              </details>
            </section>`
          : `<div class="review-placeholder">确认 MinerU 有误后，再调用 Mathpix 校正此块。</div>`
      }
      </div>
    </article>
  `;
}

function reviewBlockKey(pageNumber, blockIndex) {
  return `${pageNumber}:${blockIndex}`;
}

async function toggleReviewBlock(key) {
  if (!key) {
    return;
  }
  if (state.reviewExpanded.has(key)) {
    state.reviewExpanded.delete(key);
  } else {
    state.reviewExpanded.add(key);
  }
  await renderCurrentPage();
}

async function applyMathpixBlockEdit(blockIndex, trigger) {
  const blockKey = String(blockIndex || "");
  if (!blockKey) {
    return;
  }
  const editor = trigger?.closest?.(".review-item")?.querySelector?.("[data-mathpix-edit]");
  if (!editor) {
    return;
  }
  const markdown = prepareMathpixMarkdown(editor.value || "");
  getMathpixBlockDrafts(state.currentPage).delete(blockKey);
  getBlockOverrides(state.currentPage).set(blockKey, markdown);
  expandOnlyReviewBlock(state.currentPage, blockKey);
  updateCorrectionSummary();
  setStatus("Ready", "ok");
  await renderCurrentPage();
}

function expandOnlyReviewBlock(pageNumber, blockIndex) {
  state.reviewExpanded.clear();
  state.reviewExpanded.add(reviewBlockKey(pageNumber, blockIndex));
  state.reviewInitializedPages.add(pageNumber);
}

function renderBlockContent(markdown, entry) {
  if (entry.kind === "algorithm") {
    return renderAlgorithmBlock(markdownToAlgorithmLines(markdown));
  }
  return renderMarkdownHtml(normalizeMathMarkdown(markdown));
}

function markdownToAlgorithmLines(markdown) {
  return String(markdown || "")
    .replace(/\r\n?/g, "\n")
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line && line !== "$$" && !/^```/.test(line))
    .map(cleanAlgorithmLine)
    .filter(Boolean);
}

function renderRiskPanel(risks) {
  if (!state.mineruInfo) {
    return "";
  }
  if (!risks.length) {
    return `<div class="risk-panel is-low">当前页未发现高风险块，通常不需要 Mathpix。</div>`;
  }
  const score = Math.max(...risks.map((item) => item.score));
  return `
    <div class="risk-panel">
      <div class="risk-summary">
        <strong>高风险 ${risks.length} 块</strong>
        <span>最高风险 ${score.toFixed(2)}，建议仅对本页/这些块使用 Mathpix。</span>
      </div>
      <div class="risk-list">
        ${risks.map(renderRiskItem).join("")}
      </div>
    </div>
  `;
}

function renderRiskItem(item) {
  const corrected = getBlockOverrides(item.pageNumber, false).has(item.blockIndex);
  const disabled = item.bbox ? "" : "disabled";
  const normalizedText = item.text.replace(/\s+/g, " ");
  return `
    <article class="risk-item">
      <div>
        <strong>${riskReasonLabel(item.reasons[0] || "risk")}</strong>
        <span>${item.reasons.map(riskReasonLabel).join(" · ")}</span>
      </div>
      <p>${escapeHtml(truncateText(normalizedText, 180))}</p>
      <details class="risk-detail">
        <summary>查看完整 MinerU 块</summary>
        <pre><code>${escapeHtml(item.text)}</code></pre>
      </details>
      <button class="text-button risk-action" type="button" data-risk-mathpix="${item.blockIndex}" ${disabled}>
        ${corrected ? "重新校正此块" : item.bbox ? "Mathpix 校正此块" : "缺少 bbox"}
      </button>
    </article>
  `;
}

function renderMathpixCard(page) {
  const card = document.createElement("section");
  card.className = "mathpix-page-card";
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
      const diffPanel = card.querySelector('[data-mathpix-panel="diff"]');
      if (diffPanel) {
        diffPanel.innerHTML = renderCorrectionDiff(nextText);
        bindDiffApplyButton(card);
      }
      typesetMath(preview);
    });
    bindDiffApplyButton(card);
  }
  return card;
}

function bindDiffApplyButton(card) {
  const button = card.querySelector("[data-apply-mathpix]");
  if (!button) {
    return;
  }
  button.addEventListener("click", async () => {
    const latest = state.mathpixCache.get(state.currentPage);
    const corrected = prepareMathpixMarkdown(latest?.editText || latest?.markdown || "");
    if (!corrected.trim()) {
      return;
    }
    state.mineruOverrides.set(state.currentPage, corrected);
    state.mineruBlockOverrides.delete(state.currentPage);
    updateCorrectionSummary();
    await renderCurrentPage();
  });
}

function renderMathpixBody({ markdown, error, editorId, previewId }) {
  if (error) {
    return `<div class="render-body markdown-body is-error">${escapeHtml(error)}</div>`;
  }
  if (!markdown) {
    return `<div class="render-body markdown-body is-loading">点击顶部“整页 Mathpix（备用）”后，这里会显示当前页的整页识别结果，可作为块级校对漏行时的参考。</div>`;
  }
  return `
    <div class="mathpix-workbench">
      <div class="mathpix-tabs" role="tablist" aria-label="Mathpix result view">
        <button class="mathpix-tab is-active" type="button" data-mathpix-tab="source">Markdown</button>
        <button class="mathpix-tab" type="button" data-mathpix-tab="preview">预览</button>
        <button class="mathpix-tab" type="button" data-mathpix-tab="diff">Diff</button>
      </div>
      <div class="mathpix-tab-panel is-active" data-mathpix-panel="source">
        <textarea id="${editorId}" class="markdown-editor" spellcheck="false">${escapeHtml(markdown)}</textarea>
      </div>
      <div class="mathpix-tab-panel" data-mathpix-panel="preview">
        <div id="${previewId}" class="render-body markdown-body live-preview">
          ${renderMarkdownHtml(normalizeMathMarkdown(markdown))}
        </div>
      </div>
      <div class="mathpix-tab-panel" data-mathpix-panel="diff">
        ${renderCorrectionDiff(markdown)}
      </div>
    </div>
  `;
}

function renderCorrectionDiff(mathpixMarkdown) {
  const mineruMarkdown = baseMineruMarkdownForPage(state.currentPage);
  if (!mineruMarkdown) {
    return `<div class="diff-empty">选择 MinerU middle.json 后可对照校正。</div>`;
  }
  const diff = buildLineDiff(mineruMarkdown, mathpixMarkdown);
  const changed = diff.some((item) => item.type !== "same");
  return `
    <div class="diff-toolbar">
      <span>${changed ? "检测到差异，可用 Mathpix 编辑稿替换当前页 MinerU 预览。" : "两边文本基本一致。"}</span>
      <button class="text-button" type="button" data-apply-mathpix ${mathpixMarkdown.trim() ? "" : "disabled"}>应用到 MinerU 预览</button>
    </div>
    <div class="diff-view">
      ${diff.map(renderDiffLine).join("")}
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
    const markdown = prepareMathpixMarkdown(data.markdown || data.answer || "");
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

async function recognizeRiskBlockWithMathpix(blockIndex) {
  if (state.busy || !state.pdfDataUrl) {
    return;
  }
  const blockKey = String(blockIndex);
  const risk = (state.riskByPage.get(state.currentPage) || []).find((item) => String(item.blockIndex) === blockKey);
  if (!risk?.bbox) {
    setStatus("No bbox", "error");
    return;
  }
  state.busy = true;
  updatePager();
  setStatus("Block OCR", "busy");
  try {
    const page = await ensureCurrentPagePreview();
    const cropDataUrl = await cropPageImage(page.image, risk.bbox, risk.pageSize, 10);
    const upload = await postJson("/api/model-tester/upload", {
      name: `page-${state.currentPage}-block-${blockKey.replace(/[^a-zA-Z0-9_-]+/g, "-")}.png`,
      kind: "image",
      mimeType: "image/png",
      size: estimateDataUrlBytes(cropDataUrl),
      dataUrl: cropDataUrl,
    });
    if (!upload.ok) {
      throw new Error(upload.error || "块图片上传失败");
    }
    const data = await postJson("/api/model-tester/image-to-markdown", {
      attachmentIds: [upload.id],
      prompt: "请只将这一个裁剪区域中的内容转为 markdown 格式。不要补充区域外内容。",
      model: "mathpix:mathpix-text",
      models: ["mathpix:mathpix-text"],
      allowFallback: false,
      temperature: 0.1,
    });
    if (!data.ok) {
      throw new Error(data.error || "Mathpix 块级请求失败");
    }
    const markdown = prepareMathpixMarkdown(data.markdown || data.answer || "");
    if (!markdown.trim()) {
      throw new Error("Mathpix 块级响应为空");
    }
    getMathpixBlockDrafts(state.currentPage).set(blockKey, markdown);
    expandOnlyReviewBlock(state.currentPage, blockKey);
    updateCorrectionSummary();
    setStatus("Draft ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    state.mathpixCache.set(state.currentPage, { error: error.message });
  } finally {
    state.busy = false;
    updatePager();
    await renderCurrentPage();
  }
}

function mineruMarkdownForPage(pageNumber) {
  if (state.mineruOverrides.has(pageNumber)) {
    return state.mineruOverrides.get(pageNumber);
  }
  const blockOverrides = getBlockOverrides(pageNumber, false);
  return pageSegmentsForPage(pageNumber)
    .map((segment) => blockOverrides.get(String(segment.blockIndex)) || segment.markdown)
    .filter(Boolean)
    .join("\n\n");
}

function baseMineruMarkdownForPage(pageNumber) {
  return originalBlockMarkdownsForPage(pageNumber)
    .map((entry) => entry.markdown)
    .filter(Boolean)
    .join("\n\n");
}

function originalBlockMarkdownsForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  if (!page) {
    return [];
  }
  const blocks = Array.isArray(page.para_blocks) ? page.para_blocks : [];
  return blocks.map((block, blockIndex) => ({
    block,
    blockIndex,
    bbox: getBlockBBox(block),
    markdown: blockToMarkdown(block),
    pageSize: page.page_size,
  }));
}

function pageSegmentsForPage(pageNumber) {
  const entries = originalBlockMarkdownsForPage(pageNumber);
  const segments = [];
  let index = 0;
  while (index < entries.length) {
    const entry = entries[index];
    if (!isAlgorithmStartEntry(entry)) {
      segments.push({
        ...entry,
        id: String(entry.blockIndex),
        blockIndex: String(entry.blockIndex),
        blockIndexes: [entry.blockIndex],
        kind: entry.block?.type || "block",
      });
      index += 1;
      continue;
    }

    const group = [];
    let depth = 0;
    let sawEnd = false;
    while (index < entries.length) {
      const current = entries[index];
      const cleaned = entryAlgorithmText(current);
      group.push(current);
      if (/^for\b/i.test(cleaned)) {
        depth += 1;
      }
      if (/^end\b/i.test(cleaned)) {
        depth = Math.max(0, depth - 1);
        sawEnd = true;
      }
      index += 1;
      if (sawEnd && depth === 0 && !isAlgorithmStartEntry(entries[index])) {
        break;
      }
    }

    const first = group[0].blockIndex;
    const last = group[group.length - 1].blockIndex;
    segments.push({
      id: `algo-${first}-${last}`,
      blockIndex: `algo-${first}-${last}`,
      blockIndexes: group.map((item) => item.blockIndex),
      bbox: mergeBBoxes(group.map((item) => item.bbox)),
      markdown: group.map((item) => item.markdown).filter(Boolean).join("\n"),
      pageSize: group[0].pageSize,
      kind: "algorithm",
    });
  }
  return segments;
}

function isAlgorithmStartEntry(entry) {
  return /^for\b/i.test(entryAlgorithmText(entry));
}

function entryAlgorithmText(entry) {
  return cleanAlgorithmLine(
    String(entry?.markdown || "")
      .replace(/\r\n?/g, "\n")
      .split("\n")
      .filter((line) => line.trim() && line.trim() !== "$$")
      .join(" ")
  );
}

function mergeBBoxes(boxes) {
  const valid = boxes.filter((box) => Array.isArray(box) && box.length >= 4);
  if (!valid.length) {
    return null;
  }
  return [
    Math.min(...valid.map((box) => box[0])),
    Math.min(...valid.map((box) => box[1])),
    Math.max(...valid.map((box) => box[2])),
    Math.max(...valid.map((box) => box[3])),
  ];
}

function getBlockOverrides(pageNumber, create = true) {
  if (!state.mineruBlockOverrides.has(pageNumber) && create) {
    state.mineruBlockOverrides.set(pageNumber, new Map());
  }
  return state.mineruBlockOverrides.get(pageNumber) || new Map();
}

function getMathpixBlockDrafts(pageNumber, create = true) {
  if (!state.mathpixBlockDrafts.has(pageNumber) && create) {
    state.mathpixBlockDrafts.set(pageNumber, new Map());
  }
  return state.mathpixBlockDrafts.get(pageNumber) || new Map();
}

function analyzeMineruRiskPages() {
  state.riskByPage.clear();
  const total = getMineruPageCount();
  for (let pageNumber = 1; pageNumber <= total; pageNumber += 1) {
    const risks = detectRiskCandidatesForPage(pageNumber);
    if (risks.length) {
      state.riskByPage.set(pageNumber, risks);
    }
  }
}

function detectRiskCandidatesForPage(pageNumber) {
  return pageSegmentsForPage(pageNumber)
    .map((segment) => {
      const { score, reasons } = scoreRiskBlock(segment.markdown);
      return {
        pageNumber,
        blockIndex: String(segment.blockIndex),
        bbox: segment.bbox,
        pageSize: segment.pageSize,
        text: segment.markdown,
        score,
        reasons,
      };
    })
    .filter((item) => item.text && item.score >= 0.25)
    .sort((a, b) => b.score - a.score);
}

function detectRiskCandidates(markdown, pageNumber) {
  return splitMarkdownBlocks(markdown)
    .map((block, blockIndex) => {
      const { score, reasons } = scoreRiskBlock(block);
      return {
        pageNumber,
        blockIndex,
        text: block,
        score,
        reasons,
      };
    })
    .filter((item) => item.score >= 0.25)
    .sort((a, b) => b.score - a.score);
}

function splitMarkdownBlocks(markdown) {
  return String(markdown || "")
    .split(/\n{2,}/)
    .map((block) => block.trim())
    .filter(Boolean);
}

function scoreRiskBlock(text) {
  const reasons = [];
  let score = 0;
  if (hasTable(text) && hasMathSignal(text)) {
    score += 0.38;
    reasons.push("table_with_math");
  }
  if (hasCompactFormulaLoss(text)) {
    score += 0.36;
    reasons.push("compact_formula_maybe_missing_superscript");
  }
  if (hasSplitFormulaTokens(text)) {
    score += 0.32;
    reasons.push("split_formula_tokens");
  }
  if (hasMatrixSignal(text)) {
    score += 0.34;
    reasons.push("matrix_like_layout");
  }
  if (hasPseudocodeSignal(text)) {
    score += 0.28;
    reasons.push("pseudocode_like_layout");
  }
  if ((text.match(/\$/g) || []).length % 2 === 1) {
    score += 0.2;
    reasons.push("unbalanced_math_delimiter");
  }
  if (/\\[a-zA-Z]+\s+[a-zA-Z0-9]/.test(text)) {
    score += 0.12;
    reasons.push("latex_command_spacing");
  }
  return { score: Math.min(score, 1), reasons };
}

function hasTable(text) {
  return /<\s*\/?\s*(table|thead|tbody|tr|td|th)\b/i.test(text) || text.split("\n").filter((line) => line.includes("|")).length >= 2;
}

function hasMathSignal(text) {
  const plain = text.replace(/<[^>]+>/g, " ");
  return /\\\(|\\\[|\$|\\frac|\\sum|\\int|\\sqrt|\\begin\{|[_^=<>≤≥±×÷∑∫∂αβγδλμπΩ∞≈≠]/.test(plain);
}

function hasSplitFormulaTokens(text) {
  return [
    /\b[A-Za-z]\s+\d\b/,
    /\b\d\s+\d\b/,
    /\^\s+\d/,
    /_\s+\d/,
    /\\\(\s*[^)]*\s{2,}[^)]*\\\)/,
    /\$\s*[^$]*\s{2,}[^$]*\$/,
  ].some((pattern) => pattern.test(text));
}

function hasCompactFormulaLoss(text) {
  if (!hasTable(text)) {
    return false;
  }
  const compact = text.replace(/\s+/g, "");
  return [
    /(?:^|[<>|,;，；])(?:w|x|y|z|n|m|k|p|q|r|t)={0,1}2\d{1,3}(?:[<>|,;，；]|$)/i,
    /(?:^|[<>|,;，；])(?:w|x|y|z|n|m|k|p|q|r|t)\d{2,4}(?:[<>|,;，；]|$)/i,
    /(?:^|[<>|,;，；])2\d{1,3}\$(?:[<>|,;，；]|$)/i,
  ].some((pattern) => pattern.test(compact));
}

function hasMatrixSignal(text) {
  const lowered = text.toLowerCase();
  return (
    /\\begin\{(align|cases|array|matrix|pmatrix|bmatrix|tabular)\*?\}/.test(lowered) ||
    /[\[(]\s*(?:[-+0-9a-zA-Z_.]+\s+){2,}[-+0-9a-zA-Z_.]+/.test(text) ||
    (text.includes("矩阵") && (text.includes("\n") || text.includes("|")))
  );
}

function hasPseudocodeSignal(text) {
  const lowered = text.replace(/<[^>]+>/g, " ").toLowerCase();
  return (
    /\b(input|output|procedure|return|for|while|if|else)\b/.test(lowered) ||
    /(?:^|\n)\s*algorithm\s+\d+/.test(lowered) ||
    ["伪代码", "输入", "输出", "算法", "步骤"].some((marker) => text.includes(marker))
  );
}

function buildLineDiff(original, revised) {
  const left = String(original || "").replace(/\r\n?/g, "\n").split("\n");
  const right = String(revised || "").replace(/\r\n?/g, "\n").split("\n");
  const rows = left.length;
  const cols = right.length;
  const dp = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));
  for (let row = rows - 1; row >= 0; row -= 1) {
    for (let col = cols - 1; col >= 0; col -= 1) {
      dp[row][col] =
        left[row] === right[col] ? dp[row + 1][col + 1] + 1 : Math.max(dp[row + 1][col], dp[row][col + 1]);
    }
  }
  const diff = [];
  let row = 0;
  let col = 0;
  while (row < rows && col < cols) {
    if (left[row] === right[col]) {
      diff.push({ type: "same", text: left[row] });
      row += 1;
      col += 1;
    } else if (dp[row + 1][col] >= dp[row][col + 1]) {
      diff.push({ type: "remove", text: left[row] });
      row += 1;
    } else {
      diff.push({ type: "add", text: right[col] });
      col += 1;
    }
  }
  while (row < rows) {
    diff.push({ type: "remove", text: left[row] });
    row += 1;
  }
  while (col < cols) {
    diff.push({ type: "add", text: right[col] });
    col += 1;
  }
  return diff;
}

function renderDiffLine(item) {
  const marker = item.type === "add" ? "+" : item.type === "remove" ? "-" : " ";
  return `<div class="diff-line is-${item.type}"><span>${marker}</span><code>${escapeHtml(item.text || " ")}</code></div>`;
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

function getBlockBBox(block) {
  const boxes = [];
  collectBBoxes(block, boxes);
  if (!boxes.length) {
    return null;
  }
  return [
    Math.min(...boxes.map((box) => box[0])),
    Math.min(...boxes.map((box) => box[1])),
    Math.max(...boxes.map((box) => box[2])),
    Math.max(...boxes.map((box) => box[3])),
  ];
}

function collectBBoxes(node, boxes) {
  if (!node || typeof node !== "object") {
    return;
  }
  if (Array.isArray(node.bbox) && node.bbox.length >= 4) {
    boxes.push(node.bbox.slice(0, 4).map(Number));
  }
  if (Array.isArray(node.lines)) {
    node.lines.forEach((line) => collectBBoxes(line, boxes));
  }
  if (Array.isArray(node.spans)) {
    node.spans.forEach((span) => collectBBoxes(span, boxes));
  }
  if (Array.isArray(node.blocks)) {
    node.blocks.forEach((block) => collectBBoxes(block, boxes));
  }
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
  els.nextRiskButton.disabled = !state.riskByPage.size;
  els.mathpixButton.disabled = !state.pdfDataUrl || state.busy;
  els.pageInput.max = hasPages ? String(total) : "";
  els.pageInput.value = String(state.currentPage);
  els.pageCountLabel.textContent = `/ ${hasPages ? total : "-"}`;
  els.exportOriginalButton.disabled = !state.mineruInfo;
  els.exportCorrectedButton.disabled = !state.mineruInfo;
  updateCorrectionSummary();
}

function updateCorrectionSummary() {
  if (!state.mineruInfo) {
    return;
  }
  const count = state.mineruOverrides.size;
  const blockCount = Array.from(state.mineruBlockOverrides.values()).reduce((sum, blocks) => sum + blocks.size, 0);
  const total = getMineruPageCount();
  const riskPages = state.riskByPage.size;
  const riskBlocks = Array.from(state.riskByPage.values()).reduce((sum, items) => sum + items.length, 0);
  const prefix = state.pdfFile
    ? `${state.pdfFile.type || "unknown"} · ${formatBytes(state.pdfFile.size)} · ${state.pdfPageCount || total || "-"} 页`
    : `${total || "-"} 页 MinerU`;
  els.fileMeta.textContent = `${prefix} · 高风险 ${riskPages} 页 / ${riskBlocks} 块 · 已应用校正 ${count} 页 / ${blockCount} 块`;
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

function exportMineruMarkdown(useCorrections) {
  if (!state.mineruInfo) {
    return;
  }
  const markdown = buildBookMarkdown(useCorrections);
  const suffix = useCorrections ? "corrected" : "mineru-original";
  const filename = `${baseExportName()}-${suffix}.md`;
  downloadTextFile(filename, markdown);
  setStatus("Exported", "ok");
}

function buildBookMarkdown(useCorrections) {
  const total = getMineruPageCount();
  const pages = [];
  for (let pageNumber = 1; pageNumber <= total; pageNumber += 1) {
    const markdown = prepareMarkdownForExport(useCorrections ? mineruMarkdownForPage(pageNumber) : baseMineruMarkdownForPage(pageNumber));
    pages.push(`<!-- page: ${pageNumber} -->\n\n${markdown || ""}`.trim());
  }
  const correctionNote = useCorrections
    ? `<!-- corrected_pages: ${correctedPageNumbers().join(", ") || "none"} -->\n\n`
    : "";
  return `${correctionNote}${pages.join("\n\n---\n\n")}\n`;
}

function prepareMarkdownForExport(markdown) {
  return normalizeSingleLineDisplayMath(
    wrapBareDisplayMathBlocks(normalizeMathMarkdown(markdown)),
  )
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function prepareMathpixMarkdown(markdown) {
  return normalizeSingleLineDisplayMath(
    removeDanglingSingleDollarLines(
      wrapLikelyDisplayMathLines(
        wrapBareDisplayMathBlocks(repairBrokenDisplayMathDelimiters(stripMarkdownFence(markdown))),
      ),
    ),
  )
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function removeDanglingSingleDollarLines(markdown) {
  return String(markdown || "")
    .replace(/\r\n?/g, "\n")
    .split("\n")
    .filter((line) => String(line || "").trim() !== "$")
    .join("\n");
}

function normalizeSingleLineDisplayMath(markdown) {
  return String(markdown || "")
    .replace(/\r\n?/g, "\n")
    .split("\n")
    .flatMap((line) => {
      const trimmed = String(line || "").trim();
      const match = trimmed.match(/^\$\$(.+)\$\$$/);
      if (!match) {
        return [line];
      }
      const body = match[1].trim();
      return body ? ["$$", body, "$$"] : ["$$"];
    })
    .join("\n");
}

function repairBrokenDisplayMathDelimiters(markdown) {
  const normalized = String(markdown || "")
    .replace(/\$\$\s*(\\begin\s*\{(?:aligned|align|array|tabular|table|matrix|pmatrix|bmatrix|cases)\*?\})/g, "$$\n$1")
    .replace(/(\\end\s*\{(?:aligned|align|array|tabular|table|matrix|pmatrix|bmatrix|cases)\*?\})\s*\$\$/g, "$1\n$$");
  const lines = normalized.replace(/\r\n?/g, "\n").split("\n");
  const output = [];
  let mathEnvDepth = 0;
  for (const line of lines) {
    const trimmed = String(line || "").trim();
    if (trimmed === "$$" && mathEnvDepth > 0) {
      continue;
    }
    const begins = countMathEnvironmentTokens(trimmed, "begin");
    const ends = countMathEnvironmentTokens(trimmed, "end");
    output.push(line);
    mathEnvDepth = Math.max(0, mathEnvDepth + begins - ends);
  }
  return output.join("\n");
}

function countMathEnvironmentTokens(text, kind) {
  const pattern = new RegExp(`\\\\${kind}\\s*\\{(?:aligned|align|array|tabular|table|matrix|pmatrix|bmatrix|cases)\\*?\\}`, "g");
  return (String(text || "").match(pattern) || []).length;
}

function wrapBareDisplayMathBlocks(markdown) {
  const lines = String(markdown || "").replace(/\r\n?/g, "\n").split("\n");
  const output = [];
  let index = 0;
  while (index < lines.length) {
    if (String(lines[index] || "").trim() === "|") {
      const nextIndex = nextNonEmptyLineIndex(lines, index + 1);
      if (nextIndex >= 0 && isBareDisplayMathStart(lines[nextIndex])) {
        index += 1;
        continue;
      }
    }
    if (isBareDisplayMathStart(lines[index])) {
      const { blockLines, nextIndex } = collectBareDisplayMathBlock(lines, index);
      output.push("$$", ...blockLines, "$$");
      index = nextIndex;
      continue;
    }
    output.push(lines[index]);
    index += 1;
  }
  return output.join("\n");
}

function wrapLikelyDisplayMathLines(markdown) {
  const lines = String(markdown || "").replace(/\r\n?/g, "\n").split("\n");
  const output = [];
  let inFence = false;
  let inDisplayMath = false;
  for (const line of lines) {
    const trimmed = String(line || "").trim();
    if (/^```/.test(trimmed)) {
      inFence = !inFence;
      output.push(line);
      continue;
    }
    if (trimmed === "$$") {
      inDisplayMath = !inDisplayMath;
      output.push(line);
      continue;
    }
    if (inFence || inDisplayMath || !isLikelyStandaloneMathLine(trimmed)) {
      output.push(line);
      continue;
    }
    output.push("$$", trimmed, "$$");
  }
  return output.join("\n");
}

function isLikelyStandaloneMathLine(trimmed) {
  if (!trimmed || trimmed.includes("$") || trimmed.includes("|") || /^#{1,6}\s+/.test(trimmed) || /^[-*+]\s+/.test(trimmed)) {
    return false;
  }
  if (!/[=<>^_]/.test(trimmed)) {
    return false;
  }
  if (/\\(?:frac|sin|cos|tan|quad|widehat|hat|sqrt|left|right|epsilon|varepsilon|leq|geq|times|begin|end|sum|int|infty|kappa|ldots)/.test(trimmed)) {
    return true;
  }
  const plainMathLike = /^[A-Za-z0-9\\{}()[\]\s+\-*/^_=,.;:<>]+$/.test(trimmed);
  return plainMathLike && trimmed.length <= 180;
}

function isBareDisplayMathStart(line) {
  const trimmed = String(line || "").trim();
  if (!trimmed || trimmed === "$$" || trimmed.startsWith("```")) {
    return false;
  }
  return /^\\begin\s*\{(?:array|tabular|table|aligned|align|matrix|pmatrix|bmatrix|cases)\*?\}/.test(trimmed);
}

function collectBareDisplayMathBlock(lines, startIndex) {
  const firstLine = String(lines[startIndex] || "");
  const match = firstLine.match(/\\begin\s*\{([a-zA-Z*]+)\}/);
  const env = match ? match[1].replace(/\*$/, "") : "";
  const endPattern = env ? new RegExp(`\\\\end\\s*\\{${escapeRegExp(env)}\\*?\\}`) : /\\end\s*\{[a-zA-Z*]+\}/;
  const blockLines = [];
  let index = startIndex;
  while (index < lines.length) {
    blockLines.push(lines[index]);
    if (endPattern.test(lines[index])) {
      index += 1;
      break;
    }
    index += 1;
  }
  return { blockLines, nextIndex: index };
}

function escapeRegExp(text) {
  return String(text).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function correctedPageNumbers() {
  const blockPages = Array.from(state.mineruBlockOverrides.entries())
    .filter(([, blocks]) => blocks.size > 0)
    .map(([pageNumber]) => pageNumber);
  return Array.from(new Set([...state.mineruOverrides.keys(), ...blockPages])).sort((a, b) => a - b);
}

function baseExportName() {
  const raw = state.mineruFileName || state.pdfFile?.name || "ocr-document";
  return raw
    .replace(/\.[^.]+$/, "")
    .replace(/[\\/:*?"<>|]+/g, "-")
    .replace(/\s+/g, "-")
    .slice(0, 120);
}

function downloadTextFile(filename, text) {
  const blob = new Blob([text], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
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

function truncateText(text, maxLength) {
  const value = String(text || "");
  return value.length > maxLength ? `${value.slice(0, maxLength - 1)}…` : value;
}

function riskReasonLabel(reason) {
  return (
    {
      table_with_math: "表格含公式",
      compact_formula_maybe_missing_superscript: "疑似上标丢失",
      split_formula_tokens: "公式被拆散",
      matrix_like_layout: "矩阵/二维排版",
      pseudocode_like_layout: "伪代码/代码块",
      unbalanced_math_delimiter: "数学定界符不平衡",
      latex_command_spacing: "LaTeX 命令异常空格",
      risk: "高风险",
    }[reason] || reason
  );
}

function estimateDataUrlBytes(dataUrl) {
  const base64 = String(dataUrl || "").split(",", 2)[1] || "";
  return Math.round((base64.length * 3) / 4);
}

function loadImage(dataUrl) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => reject(new Error("加载页面截图失败"));
    image.src = dataUrl;
  });
}

async function cropPageImage(pageDataUrl, bbox, pageSize, padding = 8) {
  const image = await loadImage(pageDataUrl);
  const sourceWidth = Number(pageSize?.[0]) || image.naturalWidth || image.width;
  const sourceHeight = Number(pageSize?.[1]) || image.naturalHeight || image.height;
  const scaleX = (image.naturalWidth || image.width) / sourceWidth;
  const scaleY = (image.naturalHeight || image.height) / sourceHeight;
  const x = Math.max(0, Math.floor((bbox[0] - padding) * scaleX));
  const y = Math.max(0, Math.floor((bbox[1] - padding) * scaleY));
  const right = Math.min(image.naturalWidth || image.width, Math.ceil((bbox[2] + padding) * scaleX));
  const bottom = Math.min(image.naturalHeight || image.height, Math.ceil((bbox[3] + padding) * scaleY));
  const width = Math.max(1, right - x);
  const height = Math.max(1, bottom - y);
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  const context = canvas.getContext("2d");
  context.drawImage(image, x, y, width, height, 0, 0, width, height);
  return canvas.toDataURL("image/png");
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
  const markdown = String(text || "");
  const normalizeMathDelimiters = getOcrCoreNormalizeMathDelimiters();
  if (!normalizeMathDelimiters) {
    warnOcrCoreNormalizer("mathDelimiterNormalizer 不可用，已保守返回原始 Markdown。");
    return markdown;
  }
  try {
    const result = normalizeMathDelimiters({
      blockId: "legacy-normalizeMathMarkdown",
      blockText: markdown,
      blockType: "unknown",
    });
    return typeof result?.normalizedText === "string" ? result.normalizedText : markdown;
  } catch (error) {
    warnOcrCoreNormalizer("normalizeMathMarkdown 调用 mathDelimiterNormalizer 失败，已保守返回原始 Markdown。", error);
    return markdown;
  }
}

function isLikelyMarkdownTableLine(line) {
  const trimmed = String(line || "").trim();
  if (!trimmed.includes("|")) {
    return false;
  }
  if (/\\(?:left|right)?\|/.test(trimmed)) {
    return false;
  }
  return trimmed.startsWith("|") || trimmed.endsWith("|") || /\s\|\s/.test(trimmed);
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

function isDisplayMathStart(line) {
  const trimmed = String(line || "").trim();
  return trimmed === "$$" || /^\$\$.+\$\$$/.test(trimmed);
}

function collectDisplayMathBlock(lines, startIndex) {
  const first = String(lines[startIndex] || "").trim();
  const singleLine = first.match(/^\$\$(.+)\$\$$/);
  if (singleLine) {
    return { blockLines: [singleLine[1].trim()], nextIndex: startIndex + 1 };
  }
  const blockLines = [];
  let index = startIndex + 1;
  while (index < lines.length && String(lines[index] || "").trim() !== "$$") {
    blockLines.push(lines[index]);
    index += 1;
  }
  if (index < lines.length) {
    index += 1;
  }
  return { blockLines, nextIndex: index };
}

function renderDisplayMathBlock(lines) {
  return `<div class="math-display">$$\n${escapeHtml(lines.join("\n").trim())}\n$$</div>`;
}

function renderCodeBlock(lines) {
  const opener = lines[0].trim();
  const language = opener.replace(/^```/, "").trim();
  const body = lines.slice(1, -1).join("\n");
  if (looksLikeAlgorithmLines(lines.slice(1, -1))) {
    return renderAlgorithmBlock(lines.slice(1, -1));
  }
  const languageClass = language ? ` class="language-${escapeHtml(language)}"` : "";
  return `<pre><code${languageClass}>${escapeHtml(body)}</code></pre>`;
}

function looksLikeAlgorithmLines(lines) {
  const meaningful = lines.map((line) => String(line || "").trim()).filter(Boolean);
  if (meaningful.length < 2) {
    return false;
  }
  const hasLoop = meaningful.some((line) => /^for\b/i.test(cleanAlgorithmLine(line)));
  const hasEnd = meaningful.some((line) => /^end\b/i.test(cleanAlgorithmLine(line)));
  const hasAssignment = meaningful.some((line) => /^[A-Za-z]\s*=/.test(cleanAlgorithmLine(line)));
  return hasLoop && (hasEnd || hasAssignment);
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

function isLatexTableAt(lines, index) {
  const current = String(lines[index] || "").trim();
  const next = String(lines[index + 1] || "").trim();
  return isLatexTableStart(current) || (current === "$$" && isLatexTableStart(next));
}

function isLatexTableStart(line) {
  return /^\\begin\s*\{(?:array|tabular|table)\*?\}/.test(String(line || "").trim());
}

function collectLatexTableBlock(lines, startIndex) {
  const blockLines = [];
  let index = startIndex;
  let openedDisplayMath = false;
  if (String(lines[index] || "").trim() === "$$") {
    openedDisplayMath = true;
    index += 1;
  }
  while (index < lines.length) {
    blockLines.push(lines[index]);
    if (/\\end\s*\{(?:array|tabular|table)\*?\}/.test(lines[index])) {
      index += 1;
      break;
    }
    index += 1;
  }
  if (openedDisplayMath && String(lines[index] || "").trim() === "$$") {
    index += 1;
  }
  return { blockLines, nextIndex: index };
}

function renderLatexTableBlock(lines) {
  const raw = lines.join("\n").replace(/^\s*\|\s*\n+/, "");
  const captionMatch = raw.match(/\\caption\{([^}]*)\}/);
  const caption = captionMatch ? captionMatch[1].trim() : "";
  const tableMatch = raw.match(
    /\\begin\s*\{(?:array|tabular)\*?\}\s*(?:\{[^}\n]*\})?([\s\S]*?)\\end\s*\{(?:array|tabular)\*?\}/,
  );
  const tableSource = tableMatch ? tableMatch[1] : raw;
  const body = tableSource
    .replace(/\\begin\s*\{table\*?\}/g, "")
    .replace(/\\end\s*\{table\*?\}/g, "")
    .replace(/\\captionsetup\{[^}]*\}/g, "")
    .replace(/\\caption\{[^}]*\}/g, "")
    .replace(/\\begin\s*\{(?:array|tabular)\*?\}\s*(?:\{[^}\n]*\})?/, "")
    .replace(/\\end\s*\{(?:array|tabular)\*?\}/, "")
    .trim();
  const rows = body
    .split(/\\\\/)
    .map((row) => row.replace(/\\hline/g, "").trim())
    .filter(Boolean)
    .map((row) => row.split("&").map((cell) => formatLatexTableCell(cell)));
  if (!rows.length) {
    return `<div class="math-display">$$\n${escapeHtml(raw)}\n$$</div>`;
  }
  const width = Math.max(...rows.map((row) => row.length), 1);
  const normalizeRow = (row) => row.concat(Array(Math.max(0, width - row.length)).fill(""));
  const [header, ...bodyRows] = rows;
  const headHtml = normalizeRow(header)
    .map((cell) => `<th>${escapeHtml(cell)}</th>`)
    .join("");
  const bodyHtml = bodyRows
    .map((row) => `<tr>${normalizeRow(row).map((cell) => `<td>${escapeHtml(cell)}</td>`).join("")}</tr>`)
    .join("");
  return `<figure class="latex-table-figure">
    ${caption ? `<figcaption>${escapeHtml(caption)}</figcaption>` : ""}
    <div class="markdown-table-wrap latex-table-wrap"><table><thead><tr>${headHtml}</tr></thead><tbody>${bodyHtml}</tbody></table></div>
  </figure>`;
}

function formatLatexTableCell(cell) {
  const text = String(cell || "")
    .trim()
    .replace(/^\$+|\$+$/g, "")
    .replace(/\s+/g, " ");
  if (!text) {
    return "";
  }
  if (/[\\_^{}]|(?:^|\s)[a-zA-Z]\s*=|\\times|\\widehat|\\left|\\right/.test(text)) {
    return `$${text}$`;
  }
  return text;
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
    /^\$[^$\n]+?\$\s*\S+/.test(trimmed) ||
    /^[A-Za-z]\s*=/.test(trimmed)
  );
}

function cleanAlgorithmLine(line) {
  let text = String(line || "")
    .trim()
    .replace(/\$([^$\n]+)\$/g, "$1")
    .replace(/^\$\$?\s*/, "")
    .replace(/\s*\$\$?$/, "")
    .replace(/\\sqrt\{\}\s*\(([^)]+)\)/g, "\\sqrt{$1}")
    .replace(/\\sqrt\{\}\{([^}]+)\}/g, "\\sqrt{$1}")
    .replace(/\\sqrt\{\s*\}\s*([A-Za-z0-9]+)/g, "\\sqrt{$1}")
    .replace(/\bfor\s+([^:]+?)\s*:\s*(\d+)/i, (_match, left, right) => `for ${left.replace(/\s+/g, " ").trim()}:${right}`)
    .replace(/\b([A-Za-z])\s*=\s*\1\s+2\b/g, "$1 = $1^2")
    .replace(/\b([A-Za-z])\s*=\s*\1\s*\^\s*2\b/g, "$1 = $1^2")
    .replace(/\b([A-Za-z])=([A-Za-z])\^2\b/g, "$1 = $2^2")
    .replace(/\s+/g, " ");
  text = text.replace(/\s*=\s*/g, " = ");
  return text;
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

function nextNonEmptyLineIndex(lines, startIndex) {
  for (let index = startIndex; index < lines.length; index += 1) {
    if (String(lines[index] || "").trim()) {
      return index;
    }
  }
  return -1;
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
    if (lines[index].trim() === "$") {
      index += 1;
      continue;
    }

    if (lines[index].trim() === "|") {
      const nextIndex = nextNonEmptyLineIndex(lines, index + 1);
      if (nextIndex >= 0 && isLatexTableAt(lines, nextIndex)) {
        index += 1;
        continue;
      }
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

    if (isDisplayMathStart(lines[index]) && !isLatexTableAt(lines, index)) {
      const { blockLines, nextIndex } = collectDisplayMathBlock(lines, index);
      parts.push(renderDisplayMathBlock(blockLines));
      index = nextIndex;
      continue;
    }

    if (isLatexTableAt(lines, index)) {
      const { blockLines, nextIndex } = collectLatexTableBlock(lines, index);
      parts.push(renderLatexTableBlock(blockLines));
      index = nextIndex;
      continue;
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
      !isDisplayMathStart(lines[index]) &&
      !isLatexTableAt(lines, index) &&
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
