const RUNTIME_CONFIG = window.__UMA_RUNTIME_CONFIG__ || {};
const API_BASE =
  RUNTIME_CONFIG.apiBaseUrl ||
  RUNTIME_CONFIG.backendUrl ||
  (window.location.protocol === "file:" || window.location.port !== "8787"
    ? "http://127.0.0.1:8787"
    : "");

const DEFAULT_PDF_IMAGE_ZOOM = 1.25;

const state = {
  pdfFile: null,
  pdfDataUrl: "",
  pdfPageCount: 0,
  currentPage: 1,
  pageCache: new Map(),
  mineruInfo: null,
  mineruFileName: "",
  contentListItems: [],
  contentListFileName: "",
  mineruOverrides: new Map(),
  mineruBlockOverrides: new Map(),
  mathpixBlockDrafts: new Map(),
  ocrPatches: [],
  acceptedPatchPreview: null,
  acceptedPatchBookPreview: null,
  riskByPage: new Map(),
  mathpixCache: new Map(),
  reviewExpanded: new Set(),
  reviewInitializedPages: new Set(),
  pdfImageZoom: DEFAULT_PDF_IMAGE_ZOOM,
  middleColumnCollapsed: false,
  busy: false,
};
state.ocrPatches = state.ocrPatches || [];

const els = {};
const COLUMN_WIDTHS_KEY = "uma-ocr-compare-column-ratios-v6";
const MIDDLE_COLUMN_COLLAPSED_KEY = "uma-ocr-compare-middle-collapsed-v1";
const OCR_WORKSPACE_STORAGE_PREFIX = "uma-ocr-compare-workspace-v1";
const PDF_IMAGE_ZOOM_LEVELS = [1, 1.25, 1.5, 1.75, 2, 2.5];
const BLOCK_MATHPIX_CROP_PADDING = { horizontal: 4, vertical: 1 };
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
let ocrCoreAdaptMathpixToTargetMarkdown = null;
let ocrCoreMathpixAdapterLoadStarted = false;
let ocrCoreMathpixAdapterWarningShown = false;
let ocrCoreHashBlockText = null;
let ocrCoreCreateOcrPatch = null;
let ocrCoreMergeAcceptedPatches = null;
let ocrCoreValidateRenderability = null;
let ocrCorePatchLoadStarted = false;
let ocrCorePatchWarningShown = false;

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

function getOcrCoreAdaptMathpixToTargetMarkdown() {
  if (ocrCoreAdaptMathpixToTargetMarkdown) {
    return ocrCoreAdaptMathpixToTargetMarkdown;
  }
  const browserModule = globalThis?.OcrCoreMathpixAdapter;
  if (typeof browserModule?.adaptMathpixToTargetMarkdown === "function") {
    ocrCoreAdaptMathpixToTargetMarkdown = browserModule.adaptMathpixToTargetMarkdown;
    return ocrCoreAdaptMathpixToTargetMarkdown;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/mathpix/mathpixToTargetMarkdownAdapter");
      if (typeof module?.adaptMathpixToTargetMarkdown === "function") {
        ocrCoreAdaptMathpixToTargetMarkdown = module.adaptMathpixToTargetMarkdown;
        return ocrCoreAdaptMathpixToTargetMarkdown;
      }
    } catch (error) {
      warnOcrCoreMathpixAdapter("无法通过 require 加载 mathpixToTargetMarkdownAdapter。", error);
    }
  }
  return null;
}

function loadOcrCoreMathpixAdapterForBrowser() {
  if (ocrCoreMathpixAdapterLoadStarted || typeof document === "undefined" || typeof document.createElement !== "function") {
    return;
  }
  ocrCoreMathpixAdapterLoadStarted = true;
  const script = document.createElement("script");
  script.src = "./ocr-core/mathpix/mathpixToTargetMarkdownAdapter.browser.js";
  script.async = false;
  script.dataset.ocrCore = "mathpix-adapter";
  script.addEventListener("error", () => {
    warnOcrCoreMathpixAdapter("浏览器兼容入口 mathpixToTargetMarkdownAdapter.browser.js 加载失败。");
  });
  (document.head || document.body || document.documentElement).appendChild(script);
}

function warnOcrCoreMathpixAdapter(message, error) {
  if (ocrCoreMathpixAdapterWarningShown || typeof console === "undefined" || typeof console.warn !== "function") {
    return;
  }
  ocrCoreMathpixAdapterWarningShown = true;
  console.warn(`[OCR Core] ${message}`, error || "");
}

loadOcrCoreMathpixAdapterForBrowser();

function getOcrCoreHashBlockText() {
  if (ocrCoreHashBlockText) {
    return ocrCoreHashBlockText;
  }
  const browserModule = globalThis?.OcrCorePatch;
  if (typeof browserModule?.hashBlockText === "function") {
    ocrCoreHashBlockText = browserModule.hashBlockText;
    return ocrCoreHashBlockText;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/patch/blockHasher");
      if (typeof module?.hashBlockText === "function") {
        ocrCoreHashBlockText = module.hashBlockText;
        return ocrCoreHashBlockText;
      }
    } catch (error) {
      warnOcrCorePatch("无法通过 require 加载 blockHasher。", error);
    }
  }
  loadOcrCorePatchForBrowser();
  return null;
}

function getOcrCoreCreateOcrPatch() {
  if (ocrCoreCreateOcrPatch) {
    return ocrCoreCreateOcrPatch;
  }
  const browserModule = globalThis?.OcrCorePatch;
  if (typeof browserModule?.createOcrPatch === "function") {
    ocrCoreCreateOcrPatch = browserModule.createOcrPatch;
    return ocrCoreCreateOcrPatch;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/patch/patchGenerator");
      if (typeof module?.createOcrPatch === "function") {
        ocrCoreCreateOcrPatch = module.createOcrPatch;
        return ocrCoreCreateOcrPatch;
      }
    } catch (error) {
      warnOcrCorePatch("无法通过 require 加载 patchGenerator。", error);
    }
  }
  loadOcrCorePatchForBrowser();
  return null;
}

function getOcrCoreMergeAcceptedPatches() {
  if (ocrCoreMergeAcceptedPatches) {
    return ocrCoreMergeAcceptedPatches;
  }
  const browserModule = globalThis?.OcrCorePatch;
  if (typeof browserModule?.mergeAcceptedPatches === "function") {
    ocrCoreMergeAcceptedPatches = browserModule.mergeAcceptedPatches;
    return ocrCoreMergeAcceptedPatches;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/patch/patchMerger");
      if (typeof module?.mergeAcceptedPatches === "function") {
        ocrCoreMergeAcceptedPatches = module.mergeAcceptedPatches;
        return ocrCoreMergeAcceptedPatches;
      }
    } catch (error) {
      warnOcrCorePatch("无法通过 require 加载 patchMerger。", error);
    }
  }
  loadOcrCorePatchForBrowser();
  return null;
}

function loadOcrCorePatchForBrowser() {
  if (ocrCorePatchLoadStarted || typeof document === "undefined" || typeof document.createElement !== "function") {
    return;
  }
  ocrCorePatchLoadStarted = true;
  const script = document.createElement("script");
  script.src = "./ocr-core/patch/ocrPatch.browser.js";
  script.async = false;
  script.dataset.ocrCore = "ocr-patch";
  script.addEventListener("error", () => {
    warnOcrCorePatch("浏览器兼容入口 ocrPatch.browser.js 加载失败。");
  });
  (document.head || document.body || document.documentElement).appendChild(script);
}

function getOcrCoreValidateRenderability() {
  if (ocrCoreValidateRenderability) {
    return ocrCoreValidateRenderability;
  }
  if (typeof require === "function") {
    try {
      const module = require("./ocr-core/validation/renderValidator");
      if (typeof module?.validateRenderability === "function") {
        ocrCoreValidateRenderability = module.validateRenderability;
        return ocrCoreValidateRenderability;
      }
    } catch (error) {
      warnOcrCorePatch("无法通过 require 加载 renderValidator。", error);
    }
  }
  const browserModule = globalThis?.OcrCoreRenderValidator;
  if (typeof browserModule?.validateRenderability === "function") {
    ocrCoreValidateRenderability = browserModule.validateRenderability;
    return ocrCoreValidateRenderability;
  }
  return null;
}

function warnOcrCorePatch(message, error) {
  if (ocrCorePatchWarningShown || typeof console === "undefined" || typeof console.warn !== "function") {
    return;
  }
  ocrCorePatchWarningShown = true;
  console.warn(`[OCR Core] ${message}`, error || "");
}

loadOcrCorePatchForBrowser();

function apiUrl(path) {
  return `${API_BASE}${path}`;
}

function bindElements() {
  [
    "pdfInput",
    "mineruInput",
    "contentListInput",
    "pickPdfButton",
    "pickMineruButton",
    "pickContentListButton",
    "nextRiskButton",
    "mathpixButton",
    "exportOriginalButton",
    "exportCorrectedButton",
    "clearButton",
    "fileName",
    "fileMeta",
    "pageList",
    "statusBadge",
    "firstPageButton",
    "prevPageButton",
    "nextPageButton",
    "lastPageButton",
    "pageInput",
    "pageCountLabel",
  ].forEach((id) => {
    els[id] = document.getElementById(id);
  });
}

function initialize() {
  bindElements();
  restoreColumnWidths();
  restoreMiddleColumnCollapsed();
  applyMiddleColumnCollapsedState();
  els.pickPdfButton.addEventListener("click", () => els.pdfInput.click());
  els.pickMineruButton.addEventListener("click", () => els.mineruInput.click());
  els.pickContentListButton.addEventListener("click", () => els.contentListInput.click());
  els.pdfInput.addEventListener("change", handlePdfChange);
  els.mineruInput.addEventListener("change", handleMineruChange);
  els.contentListInput.addEventListener("change", handleContentListChange);
  els.nextRiskButton.addEventListener("click", goToNextRiskPage);
  els.mathpixButton.addEventListener("click", recognizeCurrentPageWithMathpix);
  els.exportOriginalButton.addEventListener("click", () => exportMineruMarkdown(false));
  els.exportCorrectedButton.addEventListener("click", () => exportMineruMarkdown(true));
  els.clearButton.addEventListener("click", resetPage);
  els.firstPageButton.addEventListener("click", () => goToPagerTarget("first"));
  els.prevPageButton.addEventListener("click", () => goToPage(state.currentPage - 1));
  els.nextPageButton.addEventListener("click", () => goToPage(state.currentPage + 1));
  els.lastPageButton.addEventListener("click", () => goToPagerTarget("last"));
  els.pageInput.addEventListener("change", () => goToPage(Number(els.pageInput.value || 1)));
  document.addEventListener("pointerdown", handleColumnResizeStart);
  window.addEventListener("resize", schedulePdfFocusSync);
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
  state.ocrPatches = [];
  state.acceptedPatchPreview = null;
  state.acceptedPatchBookPreview = null;
  state.riskByPage.clear();
  state.reviewExpanded.clear();
  state.reviewInitializedPages.clear();
  state.pdfImageZoom = DEFAULT_PDF_IMAGE_ZOOM;
  state.currentPage = 1;
  els.fileName.textContent = "PDF 已加载";
  els.fileMeta.textContent = `${file.type || "unknown"} · ${formatBytes(file.size)} · 正在读取页数`;
  setStatus("Preparing", "busy");

  try {
    const preview = await loadPagePreview(1);
    state.pdfPageCount = preview.pageCount || preview.pages?.length || 1;
    if (state.mineruInfo) {
      analyzeMineruRiskPages();
      restoreOcrWorkspaceState();
    }
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
    state.ocrPatches = [];
    state.acceptedPatchPreview = null;
    state.acceptedPatchBookPreview = null;
    state.reviewExpanded.clear();
    state.reviewInitializedPages.clear();
    analyzeMineruRiskPages();
    if (!state.pdfPageCount) {
      state.pdfPageCount = pdfInfo.length;
    }
    restoreOcrWorkspaceState();
    updatePager();
    await renderCurrentPage();
    setStatus("Ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    state.mineruInfo = null;
    state.mineruOverrides.clear();
    state.mineruBlockOverrides.clear();
    state.mathpixBlockDrafts.clear();
    state.ocrPatches = [];
    state.acceptedPatchPreview = null;
    state.acceptedPatchBookPreview = null;
    state.riskByPage.clear();
    state.reviewExpanded.clear();
    state.reviewInitializedPages.clear();
    renderCurrentPage();
  }
}

async function handleContentListChange() {
  const file = els.contentListInput.files?.[0] || null;
  if (!file) {
    return;
  }
  setStatus("content_list", "busy");
  try {
    const text = await readFileAsText(file);
    const data = JSON.parse(text);
    const items = normalizeContentListItems(data);
    if (!items.length) {
      throw new Error("这个 JSON 没有找到 content_list 条目。");
    }
    state.contentListItems = items;
    state.contentListFileName = file.name;
    state.reviewExpanded.clear();
    state.reviewInitializedPages.clear();
    analyzeMineruRiskPages();
    updatePager();
    updateCorrectionSummary();
    await renderCurrentPage();
    setStatus("Ready", "ok");
  } catch (error) {
    setStatus("Error", "error");
    state.contentListItems = [];
    state.contentListFileName = "";
    analyzeMineruRiskPages();
    updatePager();
    await renderCurrentPage();
  }
}

function resetPage() {
  clearPersistedOcrWorkspaceState();
  state.pdfFile = null;
  state.pdfDataUrl = "";
  state.pdfPageCount = 0;
  state.currentPage = 1;
  state.pageCache.clear();
  state.mineruInfo = null;
  state.mineruFileName = "";
  state.contentListItems = [];
  state.contentListFileName = "";
  state.mineruOverrides.clear();
  state.mineruBlockOverrides.clear();
  state.mathpixBlockDrafts.clear();
  state.ocrPatches = [];
  state.acceptedPatchPreview = null;
  state.acceptedPatchBookPreview = null;
  state.riskByPage.clear();
  state.mathpixCache.clear();
  state.reviewExpanded.clear();
  state.reviewInitializedPages.clear();
  state.pdfImageZoom = DEFAULT_PDF_IMAGE_ZOOM;
  state.busy = false;
  els.pdfInput.value = "";
  els.mineruInput.value = "";
  els.contentListInput.value = "";
  els.fileName.textContent = "未选择原书 PDF";
  els.fileMeta.textContent = "中栏读取已有 MinerU 整书识别结果；优先点击高风险块进行 Mathpix 块级校正。";
  els.pageList.innerHTML = '<div class="empty-state">选择原书 PDF，再选择对应的 MinerU `_middle.json`。优先点击高风险块，只对该块调用 Mathpix。</div>';
  updatePager();
  setStatus("Ready", "ok");
}

function ocrWorkspaceStorageKey() {
  if (!state.mineruFileName) {
    return "";
  }
  const pageCount = getMineruPageCount() || state.pdfPageCount || 0;
  return `${OCR_WORKSPACE_STORAGE_PREFIX}:${state.mineruFileName}:${pageCount}`;
}

function getOcrWorkspaceStorage() {
  try {
    if (typeof globalThis !== "undefined" && globalThis.localStorage) {
      return globalThis.localStorage;
    }
    if (typeof window !== "undefined" && window.localStorage) {
      return window.localStorage;
    }
    return null;
  } catch (error) {
    return null;
  }
}

function saveOcrWorkspaceState() {
  const storage = getOcrWorkspaceStorage();
  const key = ocrWorkspaceStorageKey();
  if (!storage || !key) {
    return false;
  }
  const payload = {
    version: 1,
    savedAt: new Date().toISOString(),
    mineruFileName: state.mineruFileName,
    pageCount: getMineruPageCount() || 0,
    mineruOverrides: serializePageMap(state.mineruOverrides),
    mineruBlockOverrides: serializeNestedMap(state.mineruBlockOverrides),
    mathpixBlockDrafts: serializeNestedMap(state.mathpixBlockDrafts),
    mathpixCache: serializePageMap(state.mathpixCache),
    ocrPatches: Array.isArray(state.ocrPatches) ? state.ocrPatches : [],
  };
  try {
    storage.setItem(key, JSON.stringify(payload));
    return true;
  } catch (error) {
    if (typeof console !== "undefined" && typeof console.warn === "function") {
      console.warn("[OCR Workspace] 无法保存 Mathpix 校正中间稿。", error);
    }
    return false;
  }
}

function restoreOcrWorkspaceState() {
  const storage = getOcrWorkspaceStorage();
  const key = ocrWorkspaceStorageKey();
  if (!storage || !key) {
    return false;
  }
  const raw = storage.getItem(key);
  if (!raw) {
    return false;
  }
  try {
    const payload = JSON.parse(raw);
    if (!payload || payload.version !== 1) {
      return false;
    }
    state.mineruOverrides = restorePageMap(payload.mineruOverrides);
    state.mineruBlockOverrides = restoreNestedMap(payload.mineruBlockOverrides);
    state.mathpixBlockDrafts = restoreNestedMap(payload.mathpixBlockDrafts);
    state.mathpixCache = restorePageMap(payload.mathpixCache);
    state.ocrPatches = Array.isArray(payload.ocrPatches) ? payload.ocrPatches : [];
    state.acceptedPatchPreview = null;
    state.acceptedPatchBookPreview = null;
    return true;
  } catch (error) {
    storage.removeItem(key);
    if (typeof console !== "undefined" && typeof console.warn === "function") {
      console.warn("[OCR Workspace] 已忽略损坏的 Mathpix 校正中间稿缓存。", error);
    }
    return false;
  }
}

function clearPersistedOcrWorkspaceState() {
  const storage = getOcrWorkspaceStorage();
  const key = ocrWorkspaceStorageKey();
  if (!storage || !key) {
    return false;
  }
  storage.removeItem(key);
  return true;
}

function serializePageMap(map) {
  if (!(map instanceof Map)) {
    return [];
  }
  return Array.from(map.entries()).map(([pageNumber, value]) => [Number(pageNumber), value]);
}

function restorePageMap(entries) {
  const map = new Map();
  if (!Array.isArray(entries)) {
    return map;
  }
  entries.forEach((entry) => {
    if (!Array.isArray(entry) || entry.length < 2) {
      return;
    }
    const pageNumber = Number(entry[0]);
    if (!Number.isFinite(pageNumber)) {
      return;
    }
    map.set(pageNumber, entry[1]);
  });
  return map;
}

function serializeNestedMap(map) {
  if (!(map instanceof Map)) {
    return [];
  }
  return Array.from(map.entries()).map(([pageNumber, blockMap]) => [
    Number(pageNumber),
    blockMap instanceof Map ? Array.from(blockMap.entries()) : [],
  ]);
}

function restoreNestedMap(entries) {
  const map = new Map();
  if (!Array.isArray(entries)) {
    return map;
  }
  entries.forEach((entry) => {
    if (!Array.isArray(entry) || entry.length < 2) {
      return;
    }
    const pageNumber = Number(entry[0]);
    if (!Number.isFinite(pageNumber)) {
      return;
    }
    const blockEntries = Array.isArray(entry[1]) ? entry[1] : [];
    map.set(pageNumber, new Map(blockEntries.map(([blockIndex, text]) => [String(blockIndex), String(text || "")])));
  });
  return map;
}

async function goToPage(pageNumber) {
  const total = state.pdfPageCount || getMineruPageCount() || 1;
  const nextPage = Math.max(1, Math.min(pageNumber, total));
  if (nextPage === state.currentPage && state.pageCache.has(nextPage)) {
    return;
  }
  state.currentPage = nextPage;
  state.acceptedPatchPreview = null;
  state.reviewExpanded.clear();
  updatePager();
  await renderCurrentPage();
}

async function goToPagerTarget(target) {
  const total = state.pdfPageCount || getMineruPageCount() || 1;
  const targets = {
    first: 1,
    prev: state.currentPage - 1,
    next: state.currentPage + 1,
    last: total,
  };
  await goToPage(targets[target] || state.currentPage);
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
  applyMiddleColumnCollapsedState();
  els.pageList.innerHTML = "";
  const row = document.createElement("article");
  row.className = "page-row";
  const page = await ensureCurrentPagePreview();
  if (state.middleColumnCollapsed) {
    row.append(renderImageCard(page), renderMiddleColumnRestoreRail(), renderRightWorkbench(page));
  } else {
    row.append(
      renderImageCard(page),
      createColumnResizer("left"),
      renderMineruCard(),
      createColumnResizer("right"),
      renderRightWorkbench(page),
    );
  }
  els.pageList.append(row);
  typesetMath(row);
  syncPdfFocusToExpandedReviewBlock();
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

function renderMiddleColumnRestoreRail() {
  const button = document.createElement("button");
  button.className = "middle-column-restore";
  button.type = "button";
  button.dataset.middleColumnToggle = "expand";
  button.setAttribute("aria-label", "展开 MinerU 原始识别栏");
  button.innerHTML = "<span>MinerU</span><strong>展开</strong>";
  button.addEventListener("click", () => setMiddleColumnCollapsed(false));
  return button;
}

async function setMiddleColumnCollapsed(collapsed) {
  state.middleColumnCollapsed = Boolean(collapsed);
  persistMiddleColumnCollapsed();
  applyMiddleColumnCollapsedState();
  await renderCurrentPage();
}

function restoreMiddleColumnCollapsed() {
  try {
    state.middleColumnCollapsed = localStorage.getItem(MIDDLE_COLUMN_COLLAPSED_KEY) === "1";
  } catch {
    state.middleColumnCollapsed = false;
  }
}

function persistMiddleColumnCollapsed() {
  try {
    localStorage.setItem(MIDDLE_COLUMN_COLLAPSED_KEY, state.middleColumnCollapsed ? "1" : "0");
  } catch {
    // Layout preference is non-critical.
  }
}

function applyMiddleColumnCollapsedState() {
  const panel = document.querySelector(".preview-panel");
  panel?.classList.toggle("is-middle-collapsed", Boolean(state.middleColumnCollapsed));
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
  schedulePdfFocusSync();
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
  const zoom = currentPdfImageZoom();
  const zoomIndex = PDF_IMAGE_ZOOM_LEVELS.indexOf(zoom);
  const atMinZoom = zoomIndex <= 0;
  const atMaxZoom = zoomIndex >= PDF_IMAGE_ZOOM_LEVELS.length - 1;
  card.className = `preview-card image-card ${zoom > 1 ? "is-zoomed" : ""}`;
  const imageHtml = page.image
    ? `<div class="page-image-surface"><img src="${page.image}" alt="第 ${page.pageNumber} 页 OCR 截图"><div class="page-image-focus" data-page-image-focus hidden></div></div>`
    : `<div class="empty-inline">尚未选择 PDF。</div>`;
  card.innerHTML = `
    <div class="card-head">
      <strong>第 ${state.currentPage} 页</strong>
      <div class="card-actions">
        <button class="text-button image-zoom-button" type="button" data-image-zoom="out" ${page.image && !atMinZoom ? "" : "disabled"} aria-label="缩小原文页" title="缩小">−</button>
        <span class="image-zoom-label">${Math.round(zoom * 100)}%</span>
        <button class="text-button image-zoom-button" type="button" data-image-zoom="in" ${page.image && !atMaxZoom ? "" : "disabled"} aria-label="放大原文页" title="放大">＋</button>
        <span>${page.width || "-"} × ${page.height || "-"}</span>
      </div>
    </div>
    <div class="page-image-wrap" style="--pdf-image-zoom: ${zoom};">${imageHtml}</div>
  `;
  card.querySelectorAll("[data-image-zoom]").forEach((button) => {
    button.addEventListener("click", async () => {
      setPdfImageZoom(button.dataset.imageZoom);
      await renderCurrentPage();
    });
  });
  return card;
}

function currentPdfImageZoom() {
  const value = Number(state.pdfImageZoom) || DEFAULT_PDF_IMAGE_ZOOM;
  return PDF_IMAGE_ZOOM_LEVELS.includes(value) ? value : DEFAULT_PDF_IMAGE_ZOOM;
}

function setPdfImageZoom(direction) {
  const current = currentPdfImageZoom();
  const index = PDF_IMAGE_ZOOM_LEVELS.indexOf(current);
  if (direction === "in") {
    state.pdfImageZoom = PDF_IMAGE_ZOOM_LEVELS[Math.min(PDF_IMAGE_ZOOM_LEVELS.length - 1, index + 1)];
    return;
  }
  if (direction === "out") {
    state.pdfImageZoom = PDF_IMAGE_ZOOM_LEVELS[Math.max(0, index - 1)];
    return;
  }
  state.pdfImageZoom = DEFAULT_PDF_IMAGE_ZOOM;
}

function syncPdfFocusToExpandedReviewBlock() {
  if (typeof document === "undefined" || typeof document.querySelector !== "function") {
    return false;
  }
  const wrap = document.querySelector(".page-image-wrap");
  const surface = wrap?.querySelector?.(".page-image-surface");
  const image = surface?.querySelector?.("img");
  const focus = surface?.querySelector?.("[data-page-image-focus]");
  if (!wrap || !image || !focus) {
    return false;
  }
  const risk = activeExpandedRiskForPage(state.currentPage);
  const applyFocus = () => applyPdfFocusBox(wrap, image, focus, risk);
  if (!image.complete) {
    image.addEventListener("load", applyFocus, { once: true });
    return false;
  }
  return applyFocus();
}

function schedulePdfFocusSync() {
  if (typeof window !== "undefined" && typeof window.requestAnimationFrame === "function") {
    window.requestAnimationFrame(() => syncPdfFocusToExpandedReviewBlock());
    return;
  }
  syncPdfFocusToExpandedReviewBlock();
}

function activeExpandedRiskForPage(pageNumber) {
  const prefix = `${pageNumber}:`;
  const expandedKey = Array.from(state.reviewExpanded || []).find((key) => String(key).startsWith(prefix));
  if (!expandedKey) {
    return null;
  }
  const blockIndex = String(expandedKey).slice(prefix.length);
  return reviewRiskForBlock(pageNumber, blockIndex);
}

function reviewRiskForBlock(pageNumber, blockIndex) {
  const key = String(blockIndex || "");
  const risk = (state.riskByPage.get(pageNumber) || []).find((item) => String(item.blockIndex) === key);
  if (risk) {
    return risk;
  }
  const segment = reviewSegmentsForPage(pageNumber).find((item) => String(item.blockIndex) === key);
  return segment ? reviewRiskFromSegment(segment, pageNumber) : null;
}

function applyPdfFocusBox(wrap, image, focus, risk) {
  const metrics = pdfFocusMetricsForRisk(risk, image.clientWidth || image.naturalWidth || image.width, image.clientHeight || image.naturalHeight || image.height);
  if (!metrics) {
    focus.hidden = true;
    return false;
  }
  focus.hidden = false;
  focus.style.left = `${metrics.left}px`;
  focus.style.top = `${metrics.top}px`;
  focus.style.width = `${metrics.width}px`;
  focus.style.height = `${metrics.height}px`;
  const targetTop = clamp(metrics.top + metrics.height / 2 - wrap.clientHeight / 2, 0, Math.max(0, wrap.scrollHeight - wrap.clientHeight));
  const targetLeft = clamp(metrics.left + metrics.width / 2 - wrap.clientWidth / 2, 0, Math.max(0, wrap.scrollWidth - wrap.clientWidth));
  if (typeof wrap.scrollTo === "function") {
    wrap.scrollTo({ top: targetTop, left: targetLeft, behavior: "smooth" });
  } else {
    wrap.scrollTop = targetTop;
    wrap.scrollLeft = targetLeft;
  }
  return true;
}

function pdfFocusPercentForRisk(risk) {
  const bbox = normalizedBBox(risk?.bbox);
  const pageWidth = pageSizeWidth(risk?.pageSize);
  const pageHeight = pageSizeHeight(risk?.pageSize);
  if (!bbox || !pageWidth || !pageHeight) {
    return null;
  }
  const left = clamp((bbox[0] / pageWidth) * 100, 0, 100);
  const top = clamp((bbox[1] / pageHeight) * 100, 0, 100);
  const right = clamp((bbox[2] / pageWidth) * 100, left, 100);
  const bottom = clamp((bbox[3] / pageHeight) * 100, top, 100);
  return {
    left: roundFraction(left),
    top: roundFraction(top),
    width: roundFraction(Math.max(0.1, right - left)),
    height: roundFraction(Math.max(0.1, bottom - top)),
  };
}

function pdfFocusMetricsForRisk(risk, imageWidth, imageHeight) {
  const bbox = normalizedBBox(risk?.bbox);
  const pageWidth = pageSizeWidth(risk?.pageSize);
  const pageHeight = pageSizeHeight(risk?.pageSize);
  const width = Number(imageWidth) || 0;
  const height = Number(imageHeight) || 0;
  if (!bbox || !pageWidth || !pageHeight || !width || !height) {
    return null;
  }
  const scaleX = width / pageWidth;
  const scaleY = height / pageHeight;
  const left = clamp(bbox[0] * scaleX, 0, width);
  const top = clamp(bbox[1] * scaleY, 0, height);
  const right = clamp(bbox[2] * scaleX, left, width);
  const bottom = clamp(bbox[3] * scaleY, top, height);
  return {
    left: Math.round(left),
    top: Math.round(top),
    width: Math.max(10, Math.round(right - left)),
    height: Math.max(10, Math.round(bottom - top)),
  };
}

function renderMineruCard() {
  const card = document.createElement("section");
  card.className = "preview-card mineru-card";
  const markdown = mineruMarkdownForPage(state.currentPage);
  const source = state.mineruInfo ? "当前 MinerU 识别结果" : "未选择 middle.json";
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
        <button class="text-button" type="button" data-middle-column-toggle="collapse">折叠中栏</button>
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
  card.querySelector('[data-middle-column-toggle="collapse"]').addEventListener("click", () => setMiddleColumnCollapsed(true));
  card.querySelector("[data-reset-mineru]")?.addEventListener("click", async () => {
    state.mineruOverrides.delete(state.currentPage);
    state.mineruBlockOverrides.delete(state.currentPage);
    saveOcrWorkspaceState();
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
        <span>Mathpix draft 可直接接受；编辑后保存并接受</span>
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
  const segments = reviewSegmentsForPage(state.currentPage);
  const reviewEntries = buildReviewEntriesForPage(risks, segments, state.currentPage);
  ensureDefaultReviewExpansion(reviewEntries.map((entry) => entry.risk));
  const blockOverrides = getBlockOverrides(state.currentPage, false);
  const mathpixDrafts = getMathpixBlockDrafts(state.currentPage, false);
  const showAcceptedPatchTools = hasAcceptedOcrPatches();
  card.innerHTML = `
    <div class="review-sticky-controls">
      <div class="card-head review-card-head">
        <div>
          <strong>页面校对</strong>
          <span>${reviewEntries.length ? `${reviewEntries.length} 个页面块 · ${risks.length} 个高风险/候选` : "当前页未发现可校对文本块"}</span>
        </div>
        ${renderReviewWorkbenchPager()}
      </div>
      ${renderReviewBlockNavigator(reviewEntries)}
    </div>
    <div class="review-list markdown-body">
      ${
        reviewEntries.length
          ? reviewEntries
              .map(({ key, segment, risk, displayIndex }) => {
                const ocrPatch = getLatestOcrPatchForBlock(state.currentPage, key, segment.markdown);
                return renderReviewItem(
                  segment,
                  risk,
                  blockOverrides.get(key) || "",
                  blockOverrides.has(key),
                  mathpixDrafts.get(key) || "",
                  ocrPatch,
                  { displayIndex },
                );
              })
              .join("")
          : `<div class="empty-inline">当前页未发现可校对文本块。</div>`
      }
    </div>
    ${renderReviewBottomPager()}
    ${showAcceptedPatchTools ? renderAcceptedPatchExportSection() : ""}
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
  card.querySelectorAll("[data-apply-mineru-source-edit]").forEach((button) => {
    button.addEventListener("click", () => applyMineruSourceEdit(button.dataset.applyMineruSourceEdit, button));
  });
  card.querySelectorAll("[data-mathpix-edit], [data-mineru-source-edit]").forEach((editor) => {
    editor.addEventListener("input", () => updateReviewEditorActionState(editor));
    updateReviewEditorActionState(editor);
  });
  card.querySelectorAll("[data-review-block-step]").forEach((button) => {
    button.addEventListener("click", () => navigateReviewBlock(button.dataset.reviewBlockStep));
  });
  card.querySelector("[data-review-block-select]")?.addEventListener("change", (event) => {
    selectReviewBlock(event.target.value);
  });
  card.querySelectorAll("[data-cross-page-jump-page]").forEach((button) => {
    button.addEventListener("click", () => jumpToCrossPageBlock(button.dataset.crossPageJumpPage, button.dataset.crossPageJumpBlock));
  });
  card.querySelectorAll("[data-page-jump]").forEach((button) => {
    button.addEventListener("click", () => goToPagerTarget(button.dataset.pageJump));
  });
  card.querySelectorAll("[data-page-input]").forEach((input) => {
    input.addEventListener("change", () => goToPage(Number(input.value || state.currentPage)));
  });
  card.querySelector("[data-next-risk-page]")?.addEventListener("click", () => goToNextRiskPage());
  card.querySelectorAll("[data-ocr-patch-status-action]").forEach((button) => {
    button.addEventListener("click", async () => {
      const result = updateOcrPatchStatus(button.dataset.ocrPatchId, button.dataset.ocrPatchStatusAction);
      state.acceptedPatchPreview = null;
      state.acceptedPatchBookPreview = null;
      setStatus(result.ok ? `Patch ${result.patch.status}` : "Patch unchanged", result.ok ? "ok" : "error");
      await renderCurrentPage();
    });
  });
  card.querySelector("[data-preview-accepted-patches]")?.addEventListener("click", async () => {
    state.acceptedPatchPreview = buildAcceptedPatchPreviewForPage(state.currentPage);
    setStatus(state.acceptedPatchPreview.ok ? "Patch preview" : "Preview warning", state.acceptedPatchPreview.ok ? "ok" : "error");
    await renderCurrentPage();
  });
  card.querySelector("[data-preview-accepted-book-patches]")?.addEventListener("click", async () => {
    state.acceptedPatchBookPreview = buildAcceptedPatchPreviewForBook();
    setStatus(state.acceptedPatchBookPreview.ok ? "Book patch preview" : "Book preview warning", state.acceptedPatchBookPreview.ok ? "ok" : "error");
    await renderCurrentPage();
  });
  card.querySelector("[data-download-accepted-corrected]")?.addEventListener("click", async () => {
    const result = downloadAcceptedCorrectedMarkdown();
    const statusText = result.status?.message || (result.ok ? "Downloaded accepted" : "Accepted download blocked");
    setStatus(statusText, result.ok ? "ok" : "error");
    await renderCurrentPage();
  });
  return card;
}

function hasAcceptedOcrPatches() {
  const patches = Array.isArray(state.ocrPatches) ? state.ocrPatches : [];
  return patches.some((patch) => patch?.status === "accepted");
}

function renderAcceptedPatchToolButtons() {
  return `
    <div class="mathpix-edit-actions" data-accepted-patch-tools>
      <button class="text-button" type="button" data-preview-accepted-patches>预览 accepted 校正稿</button>
      <button class="text-button" type="button" data-preview-accepted-book-patches>预览整书 accepted 校正稿</button>
      <button class="text-button" type="button" data-download-accepted-corrected>下载 accepted 校正稿</button>
    </div>
  `;
}

function renderAcceptedPatchExportSection() {
  return `
    <section class="accepted-patch-export-section" data-accepted-patch-export-section>
      <div class="review-pane-title">导出前检查</div>
      ${renderAcceptedPatchToolButtons()}
      ${renderAcceptedCorrectedDownloadStatus()}
      ${renderAcceptedPatchPreviewPanel()}
      ${renderAcceptedPatchBookPreviewPanel()}
    </section>
  `;
}

function renderAcceptedPatchPreviewPanel() {
  const preview = state.acceptedPatchPreview;
  if (!preview || Number(preview.pageNo) !== Number(state.currentPage)) {
    return "";
  }
  const warnings = Array.isArray(preview.warnings) ? preview.warnings : [];
  const errors = Array.isArray(preview.errors) ? preview.errors : [];
  const noAccepted = warnings.some((warning) => warning?.type === "no_accepted_patch");
  const summary = noAccepted
    ? "当前页没有 accepted patch"
    : `appliedPatchCount: ${preview.appliedPatchCount} · warnings: ${warnings.length} · errors: ${errors.length}`;
  return `
    <section class="ocr-patch-preview" data-accepted-patch-preview>
      <div class="review-pane-title">Accepted patch dry-run 预览</div>
      <div class="ocr-patch-preview-summary">${escapeHtml(summary)}</div>
      ${
        warnings.length || errors.length
          ? `<pre class="ocr-patch-preview-issues"><code>${escapeHtml(JSON.stringify({ warnings, errors }, null, 2))}</code></pre>`
          : ""
      }
      <textarea class="mathpix-source-editor" data-accepted-patch-preview-markdown readonly>${escapeHtml(preview.markdown || "")}</textarea>
    </section>
  `;
}

function renderAcceptedPatchBookPreviewPanel() {
  const preview = state.acceptedPatchBookPreview;
  if (!preview) {
    return "";
  }
  const warnings = Array.isArray(preview.warnings) ? preview.warnings : [];
  const errors = Array.isArray(preview.errors) ? preview.errors : [];
  return `
    <section class="ocr-patch-preview" data-accepted-patch-book-preview>
      <div class="review-pane-title">整书 accepted patch dry-run 预览</div>
      <div class="ocr-patch-preview-summary">
        acceptedPatchCount: ${preview.acceptedPatchCount} · appliedPatchCount: ${preview.appliedPatchCount} · skippedPatchCount: ${preview.skippedPatchCount} · warnings: ${warnings.length} · errors: ${errors.length}
      </div>
      <pre class="ocr-patch-preview-issues"><code>${escapeHtml(JSON.stringify({
        pageSummaries: preview.pageSummaries || [],
        warnings,
        errors,
      }, null, 2))}</code></pre>
      <textarea class="mathpix-source-editor" data-accepted-patch-book-preview-markdown readonly>${escapeHtml(preview.markdown || "")}</textarea>
    </section>
  `;
}

function renderAcceptedCorrectedDownloadStatus(status = getAcceptedCorrectedDownloadStatus()) {
  return `
    <div class="ocr-patch-preview-summary" data-accepted-download-status="${escapeHtml(status.status)}">
      <strong>下载状态：${escapeHtml(status.status)}</strong>
      <span>${escapeHtml(status.message)}</span>
      <span>accepted: ${status.acceptedPatchCount} · applied: ${status.appliedPatchCount} · warnings: ${status.warningCount} · errors: ${status.errorCount}</span>
    </div>
  `;
}

function renderReviewWorkbenchPager() {
  const riskPages = Array.from(state.riskByPage.keys()).sort((a, b) => a - b);
  return `
    <div class="review-workbench-pager">
      ${renderPageNavigator("review-workbench")}
      <button class="secondary-button review-next-risk-button" type="button" data-next-risk-page ${riskPages.length ? "" : "disabled"}>下一高风险页</button>
    </div>
  `;
}

function renderReviewBlockNavigator(reviewEntries) {
  const entries = Array.isArray(reviewEntries) ? reviewEntries : [];
  if (!entries.length) {
    return "";
  }
  const activeIndex = Math.max(0, activeReviewEntryIndex(entries));
  const active = entries[activeIndex];
  const activePatch = active
    ? getLatestOcrPatchForBlock(state.currentPage, active.key, active.segment?.markdown || active.risk?.text || "")
    : null;
  const activePatchControls = renderOcrPatchStatusControls(activePatch);
  return `
    <div class="review-block-navigator" data-review-block-navigator>
      <div>
        <strong>块导航</strong>
        <span>${activeIndex + 1} / ${entries.length}</span>
      </div>
      <div class="review-block-nav-patch">${activePatchControls || ""}</div>
      <div class="review-block-nav-controls">
        <button class="secondary-button pager-icon" type="button" data-review-block-step="prev" ${activeIndex <= 0 ? "disabled" : ""} aria-label="上一校对块" title="上一校对块">‹</button>
        <select data-review-block-select aria-label="选择校对块">
          ${entries.map((entry) => `<option value="${escapeHtml(entry.key)}" ${entry.key === active.key ? "selected" : ""}>${escapeHtml(reviewEntryLabel(entry))}</option>`).join("")}
        </select>
        <button class="secondary-button pager-icon" type="button" data-review-block-step="next" ${activeIndex >= entries.length - 1 ? "disabled" : ""} aria-label="下一校对块" title="下一校对块">›</button>
      </div>
    </div>
  `;
}

function activeReviewEntryIndex(reviewEntries) {
  const entries = Array.isArray(reviewEntries) ? reviewEntries : [];
  if (!entries.length) {
    return -1;
  }
  const prefix = `${state.currentPage}:`;
  const activeKey = Array.from(state.reviewExpanded || [])
    .map((key) => String(key))
    .find((key) => key.startsWith(prefix))
    ?.slice(prefix.length);
  const index = entries.findIndex((entry) => entry.key === activeKey);
  return index >= 0 ? index : 0;
}

function reviewEntryLabel(entry) {
  const blockLabel = `Block ${entry.displayIndex || ""}`.trim();
  const label = entry.risk?.syntheticLabel || (entry.risk?.crossPageSourcePage ? "跨页候选" : "");
  return label ? `${label} · ${blockLabel}` : blockLabel;
}

function renderReviewBottomPager() {
  return `
    <div class="review-bottom-pager">
      ${renderPageNavigator("review-bottom")}
    </div>
  `;
}

function renderPageNavigator(scope = "inline") {
  const total = state.pdfPageCount || getMineruPageCount() || 1;
  const hasPages = total > 0;
  const atFirst = !hasPages || state.currentPage <= 1;
  const atLast = !hasPages || state.currentPage >= total;
  return `
    <nav class="pager pager-compact" data-page-nav="${escapeHtml(scope)}" aria-label="页码导航">
      <button class="secondary-button pager-icon" type="button" data-page-jump="first" ${atFirst ? "disabled" : ""} aria-label="跳转到首页" title="首页">⏮</button>
      <button class="secondary-button pager-icon" type="button" data-page-jump="prev" ${atFirst ? "disabled" : ""} aria-label="上一页" title="上一页">‹</button>
      <label class="page-field">
        <span class="sr-only">页码</span>
        <input data-page-input type="number" min="1" max="${escapeHtml(String(total || ""))}" value="${escapeHtml(String(state.currentPage))}" ${hasPages ? "" : "disabled"} aria-label="页码">
      </label>
      <span class="page-count-label">/ ${hasPages ? escapeHtml(String(total)) : "-"}</span>
      <button class="secondary-button pager-icon" type="button" data-page-jump="next" ${atLast ? "disabled" : ""} aria-label="下一页" title="下一页">›</button>
      <button class="secondary-button pager-icon" type="button" data-page-jump="last" ${atLast ? "disabled" : ""} aria-label="跳转到尾页" title="尾页">⏭</button>
    </nav>
  `;
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
        riskVisualOrder(left, orderByKey) - riskVisualOrder(right, orderByKey),
    );
}

function buildReviewEntriesForPage(risks, segments, pageNumber) {
  const riskByKey = new Map((Array.isArray(risks) ? risks : []).map((risk) => [String(risk.blockIndex), risk]));
  const seen = new Set();
  const entries = segments
    .map((segment) => {
      const key = String(segment.blockIndex);
      const risk = riskByKey.get(key);
      const hasReviewText = Boolean(String(segment.markdown || "").trim());
      if (!hasReviewText && !risk) {
        return null;
      }
      seen.add(key);
      return {
        key,
        segment,
        risk: risk || reviewRiskFromSegment(segment, pageNumber),
      };
    })
    .filter(Boolean);
  (Array.isArray(risks) ? risks : []).forEach((risk) => {
    const key = String(risk.blockIndex);
    if (seen.has(key)) {
      return;
    }
    entries.push({
      key,
      segment: {
        blockIndex: key,
        markdown: risk.text,
        kind: "block",
        bbox: risk.bbox,
        pageSize: risk.pageSize,
      },
      risk,
    });
  });
  const orderByKey = new Map(segments.map((segment, index) => [String(segment.blockIndex), index]));
  return entries
    .sort((left, right) => riskVisualOrder(left.risk, orderByKey) - riskVisualOrder(right.risk, orderByKey))
    .map((entry, index) => ({
      ...entry,
      displayIndex: index + 1,
    }));
}

function reviewRiskFromSegment(segment, pageNumber = state.currentPage) {
  return {
    pageNumber,
    blockIndex: String(segment?.blockIndex ?? ""),
    bbox: segment?.bbox || null,
    pageSize: segment?.pageSize || null,
    text: segment?.markdown || "",
    score: 0,
    reasons: [],
    reviewOnly: true,
  };
}

function riskVisualOrder(risk, orderByKey) {
  if (risk?.syntheticPlacement === "page_top") {
    return -2000;
  }
  if (risk?.syntheticPlacement === "page_bottom") {
    return Number.MAX_SAFE_INTEGER - 500;
  }
  if (risk?.crossPageHint === "previous_tail") {
    return -1000 + (Number(risk.sourceBlockIndex) || 0) / 1000;
  }
  if (risk?.crossPageHint === "next_head") {
    return Number.MAX_SAFE_INTEGER - 1000 + (Number(risk.sourceBlockIndex) || 0) / 1000;
  }
  return orderByKey.get(String(risk?.blockIndex)) ?? Number.MAX_SAFE_INTEGER / 2;
}

function reviewPatchMarkdown(patch) {
  if (!patch || !["draft", "accepted"].includes(patch.status)) {
    return "";
  }
  return String(patch.newText || "").trim() ? String(patch.newText || "") : "";
}

function renderReviewItem(segment, risk, correctedMarkdown, corrected, mathpixDraftMarkdown = "", ocrPatch = null, options = {}) {
  const isCrossPage = Boolean(risk?.crossPageSourcePage);
  const isReviewOnly = Boolean(risk?.reviewOnly);
  const displayIndex = Number(options.displayIndex) > 0 ? Number(options.displayIndex) : null;
  const displayBlockLabel = `Block ${escapeHtml(String(displayIndex || segment.blockIndex))}`;
  const disabled = !isCrossPage && risk.bbox ? "" : "disabled";
  const patchMarkdown = reviewPatchMarkdown(ocrPatch);
  const hasPatchDraft = Boolean(patchMarkdown && ocrPatch?.status === "draft");
  const hasAcceptedPatchMarkdown = Boolean(patchMarkdown && ocrPatch?.status === "accepted");
  const hasMathpixDraft = Boolean(String(mathpixDraftMarkdown || "").trim()) || hasPatchDraft;
  const isCorrected = Boolean(corrected || hasAcceptedPatchMarkdown);
  const editableMarkdown = prepareMathpixMarkdown(mathpixDraftMarkdown || patchMarkdown || correctedMarkdown || "");
  const hasEditableMarkdown = Boolean(editableMarkdown.trim());
  const previewMarkdown = hasMathpixDraft || hasAcceptedPatchMarkdown ? editableMarkdown : correctedMarkdown;
  const mathpixEditorIsSaved = Boolean(hasAcceptedPatchMarkdown && !hasMathpixDraft && editableMarkdown === prepareMathpixMarkdown(patchMarkdown));
  const reviewKey = reviewBlockKey(state.currentPage, segment.blockIndex);
  const expanded = state.reviewExpanded.has(reviewKey);
  const itemState = hasMathpixDraft ? "mathpix-draft" : isCorrected ? "corrected" : isReviewOnly ? "normal" : "candidate";
  const itemStateLabel = isCrossPage
    ? risk.crossPageLabel
    : hasMathpixDraft
      ? "Mathpix draft"
      : hasAcceptedPatchMarkdown
        ? "已接受 patch"
        : corrected
          ? "已应用"
          : isReviewOnly
            ? "普通段落"
            : "";
  const correctedPaneTitle = hasMathpixDraft ? "Mathpix 识别稿（未应用）" : hasAcceptedPatchMarkdown ? "已接受校正稿" : "校正稿渲染";
  const shouldShowLatestOnly = hasMathpixDraft || isCorrected;
  const title = risk?.syntheticLabel
    ? `${escapeHtml(risk.syntheticLabel)} · ${displayBlockLabel}`
    : isCrossPage
      ? `跨页候选 · ${displayBlockLabel}`
      : displayBlockLabel;
  const mineruPaneHtml = `
        <section class="review-pane mineru-review-pane">
          <div class="review-pane-title">MinerU 渲染</div>
          <div class="review-render">
            ${renderBlockContent(segment.markdown, segment)}
          </div>
          <details class="block-source-detail">
            <summary>编辑当前块 MinerU Markdown 源码</summary>
            <textarea class="mathpix-source-editor block-source-editor" data-mineru-source-edit="${escapeHtml(String(segment.blockIndex))}" spellcheck="false">${escapeHtml(segment.markdown)}</textarea>
            <div class="mathpix-edit-actions">
              <button class="text-button" type="button" data-apply-mineru-source-edit="${escapeHtml(String(segment.blockIndex))}" data-disable-when-clean="1" data-clean-label="未修改" data-dirty-label="保存修改并接受" disabled>
                未修改
              </button>
            </div>
          </details>
        </section>`;
  const correctedPaneHtml =
    isCorrected || hasEditableMarkdown
      ? `<section class="review-pane mathpix-pane">
          <div class="review-pane-title">${correctedPaneTitle}</div>
          <div class="review-render">
            ${renderBlockContent(previewMarkdown, segment)}
          </div>
          <details class="block-source-detail">
            <summary>编辑 Markdown 源码（保存后进入 accepted 校正稿）</summary>
            <textarea class="mathpix-source-editor" data-mathpix-edit="${escapeHtml(String(segment.blockIndex))}" spellcheck="false">${escapeHtml(editableMarkdown)}</textarea>
            <div class="mathpix-edit-actions">
              <button class="text-button" type="button" data-apply-mathpix-block-edit="${escapeHtml(String(segment.blockIndex))}" ${mathpixEditorIsSaved ? 'data-disable-when-clean="1" data-clean-label="已保存" disabled' : ""} data-dirty-label="保存修改并接受">
                ${mathpixEditorIsSaved ? "已保存" : "保存修改并接受"}
              </button>
            </div>
          </details>
        </section>`
      : "";
  const originalMineruDetailHtml = `
        <details class="review-original-detail">
          <summary>查看原 MinerU 识别/源码</summary>
          ${mineruPaneHtml}
        </details>`;
  const bodyHtml = shouldShowLatestOnly
    ? `${correctedPaneHtml}${originalMineruDetailHtml}`
    : `${mineruPaneHtml}${correctedPaneHtml || `<div class="review-placeholder">确认 MinerU 有误后，再调用 Mathpix 校正此块。</div>`}`;
  return `
    <article class="review-item ${isReviewOnly ? "is-normal" : ""} ${isCorrected ? "is-corrected" : ""} ${hasMathpixDraft ? "has-mathpix-draft" : ""} ${isCrossPage ? "is-cross-page" : ""} ${expanded ? "is-expanded" : "is-collapsed"}" data-review-item-state="${escapeHtml(itemState)}" data-source-block-id="${escapeHtml(String(segment.blockIndex))}">
      <div class="review-item-head">
        <div>
          <strong>${title}</strong>
          ${itemStateLabel ? `<span class="review-item-state">${escapeHtml(itemStateLabel)}</span>` : ""}
        </div>
        <div class="review-item-actions">
          ${renderOcrPatchStatusControls(ocrPatch)}
          <button class="text-button review-toggle" type="button" data-review-toggle="${escapeHtml(reviewKey)}">
            ${expanded ? "收起" : "展开"}
          </button>
          ${
            isCrossPage
              ? `<button class="text-button risk-action" type="button" data-cross-page-jump-page="${escapeHtml(String(risk.crossPageSourcePage))}" data-cross-page-jump-block="${escapeHtml(String(risk.sourceBlockIndex))}">跳到第 ${escapeHtml(String(risk.crossPageSourcePage))} 页校对</button>`
              : `<button class="text-button risk-action" type="button" data-risk-mathpix="${segment.blockIndex}" ${disabled}>
                  ${isCorrected ? "重新校正此块" : risk.bbox ? "Mathpix 校正此块" : "缺少 bbox"}
                </button>`
          }
        </div>
      </div>
      <div class="review-item-body" ${expanded ? "" : "hidden"}>
        ${bodyHtml}
      </div>
    </article>
  `;
}

function updateReviewEditorActionState(editor) {
  const container = editor?.closest?.(".block-source-detail") || editor?.closest?.(".review-item");
  const button = container?.querySelector?.("[data-apply-mathpix-block-edit], [data-apply-mineru-source-edit]");
  if (!button) {
    return false;
  }
  const currentValue = String(editor.value || "");
  const initialValue = String(editor.defaultValue ?? "");
  const isDirty = currentValue !== initialValue;
  if (button.dataset?.disableWhenClean === "1") {
    button.disabled = !isDirty;
    button.textContent = isDirty ? button.dataset.dirtyLabel || "保存修改并接受" : button.dataset.cleanLabel || "未修改";
    return isDirty;
  }
  if (button.dataset?.dirtyLabel && isDirty) {
    button.textContent = button.dataset.dirtyLabel;
  }
  return isDirty;
}

function renderOcrPatchStatusControls(patch) {
  if (!patch) {
    return "";
  }
  const status = String(patch.status || "");
  const patchId = String(patch.patchId || "");
  const labels = {
    draft: "待确认",
    accepted: "已接受",
    rejected: "已拒绝",
    noop: "无变化",
  };
  const actionHtml =
    status === "draft"
      ? `<button class="text-button" type="button" data-ocr-patch-id="${escapeHtml(patchId)}" data-ocr-patch-status-action="accepted">接受</button>
         <button class="text-button" type="button" data-ocr-patch-id="${escapeHtml(patchId)}" data-ocr-patch-status-action="rejected">拒绝</button>`
      : `<span class="ocr-patch-state-label">${escapeHtml(labels[status] || status)}</span>`;
  return `
    <div class="ocr-patch-status" data-ocr-patch-id="${escapeHtml(patchId)}" data-ocr-patch-status="${escapeHtml(status)}">
      <span>Patch：${escapeHtml(status)}${labels[status] ? ` · ${escapeHtml(labels[status])}` : ""}</span>
      ${actionHtml}
    </div>
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
    state.reviewExpanded.clear();
    state.reviewExpanded.add(key);
  }
  await renderCurrentPage();
}

async function navigateReviewBlock(direction) {
  const entries = reviewEntriesForCurrentPage();
  if (!entries.length) {
    return;
  }
  const currentIndex = Math.max(0, activeReviewEntryIndex(entries));
  const delta = direction === "prev" ? -1 : 1;
  const nextIndex = clamp(currentIndex + delta, 0, entries.length - 1);
  await selectReviewBlock(entries[nextIndex].key);
}

async function selectReviewBlock(blockIndex) {
  const key = String(blockIndex || "");
  if (!key) {
    return;
  }
  expandOnlyReviewBlock(state.currentPage, key);
  await renderCurrentPage();
  scrollExpandedReviewItemIntoView();
}

function reviewEntriesForCurrentPage() {
  const risks = state.riskByPage.get(state.currentPage) || [];
  return buildReviewEntriesForPage(risks, reviewSegmentsForPage(state.currentPage), state.currentPage);
}

function scrollExpandedReviewItemIntoView() {
  const item = document.querySelector(".review-item.is-expanded");
  item?.scrollIntoView?.({ block: "center", behavior: "smooth" });
}

async function jumpToCrossPageBlock(pageNumber, blockIndex) {
  const targetPage = Number(pageNumber);
  if (!Number.isFinite(targetPage) || targetPage < 1) {
    return;
  }
  state.currentPage = Math.max(1, Math.min(targetPage, state.pdfPageCount || getMineruPageCount() || 1));
  state.acceptedPatchPreview = null;
  state.reviewExpanded.clear();
  expandOnlyReviewBlock(state.currentPage, String(blockIndex || ""));
  updatePager();
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
  const preparedMarkdown = prepareMathpixMarkdown(editor.value || "");
  await saveHumanAcceptedBlockEdit(blockKey, preparedMarkdown);
}

async function applyMineruSourceEdit(blockIndex, trigger) {
  const blockKey = String(blockIndex || "");
  if (!blockKey) {
    return;
  }
  const editor = trigger?.closest?.(".review-item")?.querySelector?.("[data-mineru-source-edit]");
  if (!editor) {
    return;
  }
  await saveHumanAcceptedBlockEdit(blockKey, editor.value || "");
}

async function saveHumanAcceptedBlockEdit(blockKey, newMarkdown) {
  const preparedMarkdown = String(newMarkdown || "");
  if (!preparedMarkdown.trim()) {
    setStatus("Empty block", "error");
    return;
  }
  const segment = reviewSegmentsForPage(state.currentPage).find((item) => String(item.blockIndex) === blockKey);
  const risk = reviewRiskForBlock(state.currentPage, blockKey);
  const patchResult = createAndStoreDraftOcrPatch({
    pageNo: state.currentPage,
    blockIndex: blockKey,
    oldText: segment?.markdown || risk?.text || "",
    newText: preparedMarkdown,
    source: "human",
  });
  const markdown = patchResult.normalizedText;
  if (patchResult.patch?.status === "draft") {
    rejectPriorOcrPatchesForBlock(patchResult.patch.blockId, patchResult.patch.patchId);
    updateOcrPatchStatus(patchResult.patch.patchId, "accepted");
  }
  getMathpixBlockDrafts(state.currentPage).delete(blockKey);
  // TODO: next step will switch display/export to accepted patches.
  getBlockOverrides(state.currentPage).set(blockKey, markdown);
  saveOcrWorkspaceState();
  expandOnlyReviewBlock(state.currentPage, blockKey);
  updateCorrectionSummary();
  state.acceptedPatchPreview = null;
  state.acceptedPatchBookPreview = null;
  setStatus(patchResult.patch?.status === "accepted" ? "Saved and accepted" : "Ready", "ok");
  await renderCurrentPage();
}

function rejectPriorOcrPatchesForBlock(blockId, currentPatchId) {
  const targetBlockId = String(blockId || "");
  const keepPatchId = String(currentPatchId || "");
  if (!targetBlockId || !Array.isArray(state.ocrPatches)) {
    return 0;
  }
  const updatedAt = new Date().toISOString();
  let count = 0;
  state.ocrPatches.forEach((patch) => {
    if (patch?.blockId !== targetBlockId || patch?.patchId === keepPatchId) {
      return;
    }
    if (!["draft", "accepted"].includes(patch.status)) {
      return;
    }
    patch.status = "rejected";
    patch.updatedAt = updatedAt;
    patch.metadata = {
      ...(patch.metadata || {}),
      replacedByPatchId: keepPatchId,
    };
    count += 1;
  });
  return count;
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
  const normalizedMarkdown = normalizeMathMarkdown(markdown);
  const imagePreview = renderBlockImagePreview(normalizedMarkdown, entry);
  const markdownForHtml = imagePreview ? stripMarkdownImageReferences(normalizedMarkdown) : normalizedMarkdown;
  return `${imagePreview}${renderMarkdownHtml(markdownForHtml)}`;
}

function renderBlockImagePreview(markdown, entry) {
  if (!hasMarkdownImageReference(markdown)) {
    return "";
  }
  const page = state.pageCache.get(state.currentPage);
  const bbox = expandedBBoxWithPadding(entry?.bbox, cropPaddingForMarkdownBlock(markdown, entry?.pageSize), entry?.pageSize);
  const pageWidth = pageSizeWidth(entry?.pageSize);
  const pageHeight = pageSizeHeight(entry?.pageSize);
  if (!page?.image || !bbox || !pageWidth || !pageHeight) {
    const image = extractMarkdownImageReferences(markdown)[0];
    return image ? renderMarkdownImage(image.alt || "image", image.src) : "";
  }
  const bboxWidth = Math.max(1, bbox[2] - bbox[0]);
  const bboxHeight = Math.max(1, bbox[3] - bbox[1]);
  const bgWidth = roundFraction((pageWidth / bboxWidth) * 100);
  const bgX = roundFraction((bbox[0] / Math.max(1, pageWidth - bboxWidth)) * 100);
  const bgY = roundFraction((bbox[1] / Math.max(1, pageHeight - bboxHeight)) * 100);
  return `
    <figure class="review-image-preview" style="aspect-ratio: ${roundFraction(bboxWidth)} / ${roundFraction(bboxHeight)}; background-image: url('${escapeHtml(page.image)}'); background-size: ${bgWidth}% auto; background-position: ${bgX}% ${bgY}%;">
      <figcaption>图片块预览</figcaption>
    </figure>
  `;
}

function extractMarkdownImageReferences(markdown) {
  const images = [];
  const pattern = /!\[([^\]]*)\]\(([^)\n]+)\)/g;
  let match;
  while ((match = pattern.exec(String(markdown || "")))) {
    const rawTarget = String(match[2] || "").trim();
    const srcMatch = rawTarget.match(/^<([^>]+)>$/) || rawTarget.match(/^(\S+)/);
    images.push({
      raw: match[0],
      alt: String(match[1] || "").trim(),
      src: srcMatch ? srcMatch[1] : rawTarget,
    });
  }
  return images;
}

function hasMarkdownImageReference(markdown) {
  return extractMarkdownImageReferences(markdown).length > 0;
}

function isStandaloneMarkdownImageLine(line) {
  return /^\s*!\[[^\]]*\]\([^)]+\)\s*$/.test(String(line || ""));
}

function stripMarkdownImageReferences(markdown) {
  return String(markdown || "")
    .replace(/\r\n?/g, "\n")
    .split("\n")
    .filter((line) => !isStandaloneMarkdownImageLine(line))
    .join("\n")
    .replace(/^\n+/, "");
}

function renderMarkdownImage(alt, src) {
  const safeAlt = escapeHtml(alt || "image");
  const safeSrc = escapeHtml(src || "");
  if (!safeSrc) {
    return "";
  }
  return `
    <figure class="markdown-image-reference">
      <img src="${safeSrc}" alt="${safeAlt}" loading="lazy">
      <figcaption>${safeAlt}</figcaption>
    </figure>
  `;
}

function expandedBBoxWithPadding(bbox, padding, pageSize) {
  if (!Array.isArray(bbox) || bbox.length < 4) {
    return null;
  }
  const pageWidth = pageSizeWidth(pageSize);
  const pageHeight = pageSizeHeight(pageSize);
  if (!pageWidth || !pageHeight) {
    return null;
  }
  const pad = normalizeCropPadding(padding);
  const left = clamp(Number(bbox[0]) - pad.left, 0, pageWidth);
  const top = clamp(Number(bbox[1]) - pad.top, 0, pageHeight);
  const right = clamp(Number(bbox[2]) + pad.right, left + 1, pageWidth);
  const bottom = clamp(Number(bbox[3]) + pad.bottom, top + 1, pageHeight);
  return [left, top, right, bottom];
}

function cropPaddingForMarkdownBlock(markdown, pageSize) {
  if (hasMarkdownImageReference(markdown)) {
    return cropPaddingForImageLikeBlock(pageSize);
  }
  return BLOCK_MATHPIX_CROP_PADDING;
}

function cropPaddingForRiskBlock(risk) {
  const text = String(risk?.text || "");
  const reasons = Array.isArray(risk?.reasons) ? risk.reasons.map(String) : [];
  if (hasMarkdownImageReference(text)) {
    return cropPaddingForImageLikeBlock(risk?.pageSize);
  }
  if (reasons.some((reason) => /math|formula|equation/i.test(reason)) || extractEquationNumbers(text).length) {
    const pageWidth = pageSizeWidth(risk?.pageSize);
    return {
      left: BLOCK_MATHPIX_CROP_PADDING.horizontal,
      right: Math.max(72, pageWidth * 0.1, BLOCK_MATHPIX_CROP_PADDING.horizontal),
      top: BLOCK_MATHPIX_CROP_PADDING.vertical,
      bottom: BLOCK_MATHPIX_CROP_PADDING.vertical,
    };
  }
  return BLOCK_MATHPIX_CROP_PADDING;
}

function cropPaddingForImageLikeBlock(pageSize) {
  const pageWidth = pageSizeWidth(pageSize);
  const pageHeight = pageSizeHeight(pageSize);
  return {
    left: Math.max(72, pageWidth * 0.12, BLOCK_MATHPIX_CROP_PADDING.horizontal),
    right: Math.max(24, pageWidth * 0.04, BLOCK_MATHPIX_CROP_PADDING.horizontal),
    top: Math.max(8, pageHeight * 0.015, BLOCK_MATHPIX_CROP_PADDING.vertical),
    bottom: Math.max(24, pageHeight * 0.035, BLOCK_MATHPIX_CROP_PADDING.vertical),
  };
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
      saveOcrWorkspaceState();
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
    saveOcrWorkspaceState();
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
    saveOcrWorkspaceState();
    setStatus("Ready", "ok");
  } catch (error) {
    state.mathpixCache.set(state.currentPage, { error: error.message });
    saveOcrWorkspaceState();
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
  const risk = reviewRiskForBlock(state.currentPage, blockKey);
  if (!risk?.bbox) {
    setStatus("No bbox", "error");
    return;
  }
  state.busy = true;
  updatePager();
  setStatus("Block OCR", "busy");
  try {
    const page = await ensureCurrentPagePreview();
    const cropDataUrl = await cropPageImage(page.image, risk.bbox, risk.pageSize, cropPaddingForRiskBlock(risk));
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
    const preparedMarkdown = prepareMathpixMarkdown(data.markdown || data.answer || "");
    if (!preparedMarkdown.trim()) {
      throw new Error("Mathpix 块级响应为空");
    }
    const patchResult = createAndStoreDraftOcrPatch({
      pageNo: state.currentPage,
      blockIndex: blockKey,
      oldText: risk.text || "",
      newText: preparedMarkdown,
      source: "mathpix",
    });
    const markdown = patchResult.normalizedText;
    // TODO: next step will switch display/export to accepted patches.
    getMathpixBlockDrafts(state.currentPage).set(blockKey, markdown);
    saveOcrWorkspaceState();
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
  return segmentEntries(entries);
}

function reviewBlockMarkdownsForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  if (!page) {
    return [];
  }
  const blocks = Array.isArray(page.para_blocks) ? page.para_blocks : [];
  return blocks.map((block, blockIndex) => {
    const scopedBlock = filterBlockLines(block, (line) => !lineHasCrossPageContent(line));
    return {
      block,
      blockIndex,
      bbox: getBlockBBox(scopedBlock) || getBlockBBox(block),
      markdown: blockToMarkdown(scopedBlock),
      pageSize: page.page_size,
    };
  });
}

function reviewSegmentsForPage(pageNumber) {
  return segmentEntries(reviewBlockMarkdownsForPage(pageNumber));
}

function segmentEntries(entries) {
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

function filterBlockLines(block, includeLine) {
  if (!block || typeof block !== "object") {
    return block;
  }
  const output = { ...block };
  delete output.bbox;
  delete output.bbox_fs;
  if (Array.isArray(block.lines)) {
    output.lines = block.lines
      .filter((line) => includeLine(line))
      .map((line) => ({ ...line, spans: Array.isArray(line.spans) ? line.spans.slice() : [] }));
  }
  if (Array.isArray(block.blocks)) {
    output.blocks = block.blocks.map((nested) => filterBlockLines(nested, includeLine));
  }
  return output;
}

function lineHasCrossPageContent(line) {
  if (!line || typeof line !== "object") {
    return false;
  }
  if (line.cross_page === true) {
    return true;
  }
  return (Array.isArray(line.spans) ? line.spans : []).some((span) => span?.cross_page === true);
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

function createLegacyBlockPatchContext(pageNo, blockIndex, oldText) {
  const hashBlockText = getOcrCoreHashBlockText();
  if (!hashBlockText) {
    warnOcrCorePatch("hashBlockText 不可用，无法生成 OCR draft patch。");
    return null;
  }
  const oldHash = hashBlockText(oldText);
  // TODO: migrate provisional UI blockId to blockParser.createStableBlockId() once OCR compare uses OcrBlock records.
  return {
    pageNo,
    blockIndex,
    blockId: `p${pageNo}_b${blockIndex}_${oldHash.slice(0, 8)}`,
    oldHash,
  };
}

function createAndStoreDraftOcrPatch({ pageNo, blockIndex, oldText, newText, source }) {
  const context = createLegacyBlockPatchContext(pageNo, blockIndex, oldText);
  const createOcrPatch = getOcrCoreCreateOcrPatch();
  const preservedNewText = preserveEquationNumbersFromOriginal(oldText, newText);
  if (!context || !createOcrPatch) {
    warnOcrCorePatch("createOcrPatch 不可用，已跳过 OCR draft patch 记录。");
    return {
      patch: null,
      normalizedText: preservedNewText,
      renderValidation: { severity: "warning" },
    };
  }

  const normalizedText = normalizeDraftPatchMarkdown(context.blockId, preservedNewText);
  const renderValidation = validateDraftPatchRenderability(context.blockId, normalizedText);
  const patch = createOcrPatch({
    blockId: context.blockId,
    oldText: String(oldText || ""),
    newText: normalizedText,
    source,
    status: "draft",
    metadata: {
      pageNo: Number(pageNo) || 0,
      renderStatusAfter: renderValidation.severity,
    },
  });
  state.ocrPatches = state.ocrPatches || [];
  state.ocrPatches.push(patch);
  saveOcrWorkspaceState();
  return { patch, normalizedText, renderValidation };
}

function preserveEquationNumbersFromOriginal(oldText, newText) {
  let output = String(newText || "");
  if (!output.trim()) {
    return output;
  }
  output = preserveMarkdownImageReferencesFromOriginal(oldText, output);
  output = preserveReferenceLabelsFromOriginal(oldText, output);
  output = preserveLatexTagsFromOriginal(oldText, output);
  const originalNumbers = extractEquationNumbers(oldText);
  if (!originalNumbers.length) {
    return output;
  }
  const existingNumbers = new Set(extractEquationNumbers(output));
  const missingNumbers = originalNumbers.filter((number) => !existingNumbers.has(number));
  if (!missingNumbers.length) {
    return output;
  }
  return `${output.trimEnd()} ${missingNumbers.join(" ")}`;
}

function preserveMarkdownImageReferencesFromOriginal(oldText, newText) {
  const originalImages = extractMarkdownImageReferences(oldText);
  if (!originalImages.length) {
    return String(newText || "");
  }
  const output = String(newText || "");
  const existingSrcs = new Set(extractMarkdownImageReferences(output).map((image) => image.src));
  const missingImages = originalImages.filter((image) => !existingSrcs.has(image.src));
  if (!missingImages.length) {
    return output;
  }
  return `${missingImages.map((image) => image.raw).join("\n")}\n\n${output.trimStart()}`;
}

function preserveReferenceLabelsFromOriginal(oldText, newText) {
  const originalLabels = extractReferenceLabels(oldText);
  if (!originalLabels.length) {
    return String(newText || "");
  }
  const output = String(newText || "");
  const existingLabels = new Set(extractReferenceLabels(output).map(normalizeReferenceLabel));
  const missingLabels = originalLabels.filter((label) => !existingLabels.has(normalizeReferenceLabel(label)));
  if (!missingLabels.length) {
    return output;
  }
  return insertAfterLeadingMarkdownImages(output, missingLabels.join(" "));
}

function extractReferenceLabels(text) {
  const pattern = /\b(?:Fig\.?|Figure|Table|Eq\.?|Equation)\s*\(?\d+(?:\.\d+)*[a-zA-Z]?\)?/gi;
  return Array.from(new Set((String(text || "").match(pattern) || []).map((label) => label.replace(/\s+/g, " ").trim())));
}

function normalizeReferenceLabel(label) {
  return String(label || "").replace(/\s+/g, "").replace(/\.$/, "").toLowerCase();
}

function preserveLatexTagsFromOriginal(oldText, newText) {
  const originalTags = extractLatexTags(oldText);
  if (!originalTags.length) {
    return String(newText || "");
  }
  const output = String(newText || "");
  const existingTags = new Set(extractLatexTags(output));
  const missingTags = originalTags.filter((tag) => !existingTags.has(tag));
  if (!missingTags.length) {
    return output;
  }
  return `${output.trimEnd()} ${missingTags.join(" ")}`;
}

function extractLatexTags(text) {
  return Array.from(new Set(String(text || "").match(/\\tag\{[^}]+\}/g) || []));
}

function insertAfterLeadingMarkdownImages(markdown, insertedText) {
  const lines = String(markdown || "").replace(/\r\n?/g, "\n").split("\n");
  let index = 0;
  while (index < lines.length && (!lines[index].trim() || isStandaloneMarkdownImageLine(lines[index]))) {
    index += 1;
  }
  const before = lines.slice(0, index).join("\n").trimEnd();
  const after = lines.slice(index).join("\n").trimStart();
  return `${before ? `${before}\n\n` : ""}${insertedText}${after ? `\n\n${after}` : ""}`;
}

function extractEquationNumbers(text) {
  const matches = String(text || "").match(/\(\s*\d+(?:\.\d+)+[a-zA-Z]?\s*\)/g) || [];
  return Array.from(new Set(matches.map((number) => number.replace(/\s+/g, ""))));
}

function getLatestOcrPatchForBlock(pageNo, blockIndex, oldText) {
  const context = createLegacyBlockPatchContext(pageNo, blockIndex, oldText);
  if (!context) {
    return null;
  }
  const patches = Array.isArray(state.ocrPatches) ? state.ocrPatches : [];
  for (let index = patches.length - 1; index >= 0; index -= 1) {
    const patch = patches[index];
    if (patch?.blockId === context.blockId) {
      return patch;
    }
  }
  const blockIdPrefix = `p${pageNo}_b${blockIndex}_`;
  for (let index = patches.length - 1; index >= 0; index -= 1) {
    const patch = patches[index];
    if (Number(patch?.metadata?.pageNo) === Number(pageNo) && String(patch?.blockId || "").startsWith(blockIdPrefix)) {
      return patch;
    }
  }
  return null;
}

function updateOcrPatchStatus(patchId, nextStatus) {
  const targetStatus = String(nextStatus || "");
  if (!["accepted", "rejected"].includes(targetStatus)) {
    warnOcrPatchStatus(`不支持的 OCR patch 状态切换：${targetStatus || "(empty)"}`);
    return { ok: false, reason: "unsupported_status", patch: null };
  }

  const patches = Array.isArray(state.ocrPatches) ? state.ocrPatches : [];
  const patch = patches.find((item) => item?.patchId === patchId);
  if (!patch) {
    warnOcrPatchStatus(`找不到 OCR patch：${patchId || "(empty)"}`);
    return { ok: false, reason: "not_found", patch: null };
  }

  if (patch.status !== "draft") {
    const reason = patch.status === "noop" ? "noop_not_transitionable" : "status_not_transitionable";
    warnOcrPatchStatus(`OCR patch 当前状态为 ${patch.status || "(empty)"}，不能切换为 ${targetStatus}。`);
    return { ok: false, reason, patch };
  }

  patch.status = targetStatus;
  patch.updatedAt = new Date().toISOString();
  saveOcrWorkspaceState();
  return { ok: true, reason: "", patch };
}

function warnOcrPatchStatus(message) {
  if (typeof console === "undefined" || typeof console.warn !== "function") {
    return;
  }
  console.warn(`[OCR Patch] ${message}`);
}

function buildAcceptedPatchPreviewForPage(pageNo) {
  const pageNumber = Number(pageNo) || 0;
  const mergeAcceptedPatches = getOcrCoreMergeAcceptedPatches();
  const hashBlockText = getOcrCoreHashBlockText();
  const acceptedPatches = acceptedOcrPatchesForPage(pageNumber);
  const sourceSegments = reviewSegmentsForPage(pageNumber);
  const fallbackMarkdown = sourceSegments.map((segment) => String(segment.markdown || "").replace(/\r\n?/g, "\n")).filter(Boolean).join("\n\n");

  if (!mergeAcceptedPatches || !hashBlockText) {
    return {
      ok: false,
      pageNo: pageNumber,
      markdown: fallbackMarkdown,
      appliedPatchCount: 0,
      errors: [],
      warnings: [
        {
          type: "patch_tool_unavailable",
          message: "OCR patch merge tool is not available for dry-run preview.",
        },
      ],
    };
  }

  const orderByKey = new Map(sourceSegments.map((segment, index) => [String(segment.blockIndex), index]));
  const previewSegments = syntheticSegmentsForAcceptedPatches(pageNumber, acceptedPatches, hashBlockText)
    .concat(sourceSegments)
    .sort((left, right) => acceptedPreviewSegmentOrder(left, orderByKey) - acceptedPreviewSegmentOrder(right, orderByKey));
  const blocks = previewSegments.map((segment) => {
    const text = String(segment.markdown || "").replace(/\r\n?/g, "\n");
    const oldHash = hashBlockText(text);
    return {
      blockId: `p${pageNumber}_b${segment.blockIndex}_${oldHash.slice(0, 8)}`,
      text,
    };
  });
  const result = mergeAcceptedPatches({
    blocks,
    patches: acceptedPatches,
  });
  const errors = Array.isArray(result?.errors) ? result.errors : [];
  const warnings = Array.isArray(result?.warnings) ? result.warnings.slice() : [];
  if (!acceptedPatches.length) {
    warnings.unshift({
      type: "no_accepted_patch",
      message: "当前页没有 accepted patch。",
    });
  }
  const mergedBlocks = Array.isArray(result?.mergedBlocks) ? result.mergedBlocks : blocks;
  return {
    ok: errors.length === 0,
    pageNo: pageNumber,
    markdown: mergedBlocks.map((block) => String(block?.text || "")).filter(Boolean).join("\n\n"),
    appliedPatchCount: countAppliedAcceptedPatches(acceptedPatches, blocks, errors, warnings),
    errors,
    warnings,
  };
}

function acceptedPreviewSegmentOrder(segment, orderByKey) {
  if (segment?.syntheticPlacement === "page_top") {
    return -2000;
  }
  if (segment?.syntheticPlacement === "page_bottom") {
    return Number.MAX_SAFE_INTEGER - 500;
  }
  return orderByKey.get(String(segment?.blockIndex)) ?? Number.MAX_SAFE_INTEGER / 2;
}

function syntheticSegmentsForAcceptedPatches(pageNumber, acceptedPatches, hashBlockText) {
  if (!acceptedPatches.length || typeof hashBlockText !== "function") {
    return [];
  }
  const acceptedBlockIds = new Set(acceptedPatches.map((patch) => patch?.blockId).filter(Boolean));
  return detectSupplementalRiskCandidatesForPage(pageNumber)
    .map((risk) => {
      const markdown = String(risk.text || "").replace(/\r\n?/g, "\n");
      const oldHash = hashBlockText(markdown);
      return {
        blockIndex: risk.blockIndex,
        markdown,
        kind: "synthetic",
        syntheticPlacement: risk.syntheticPlacement,
        blockId: `p${pageNumber}_b${risk.blockIndex}_${oldHash.slice(0, 8)}`,
      };
    })
    .filter((segment) => acceptedBlockIds.has(segment.blockId));
}

function buildAcceptedPatchPreviewForBook() {
  const total = getMineruPageCount();
  const acceptedPatchCount = (Array.isArray(state.ocrPatches) ? state.ocrPatches : []).filter((patch) => patch?.status === "accepted").length;
  const pageSummaries = [];
  const errors = [];
  const warnings = [];
  const pages = [];
  let appliedPatchCount = 0;
  let allPagesOk = true;

  for (let pageNo = 1; pageNo <= total; pageNo += 1) {
    const pagePreview = buildAcceptedPatchPreviewForPage(pageNo);
    allPagesOk = allPagesOk && Boolean(pagePreview.ok);
    const pageErrors = withIssuePageNo(pagePreview.errors, pageNo);
    const pageWarnings = withIssuePageNo(
      (pagePreview.warnings || []).filter((warning) => warning?.type !== "no_accepted_patch"),
      pageNo,
    );
    errors.push(...pageErrors);
    warnings.push(...pageWarnings);
    appliedPatchCount += Number(pagePreview.appliedPatchCount) || 0;
    pageSummaries.push({
      pageNo,
      appliedPatchCount: Number(pagePreview.appliedPatchCount) || 0,
      warningCount: pageWarnings.length,
      errorCount: pageErrors.length,
    });
    pages.push(`<!-- page: ${pageNo} -->\n\n${pagePreview.markdown || ""}`.trim());
  }

  if (!total) {
    warnings.push({
      type: "no_mineru_pages",
      message: "没有可预览的 MinerU 页面。",
    });
  }
  if (!acceptedPatchCount) {
    warnings.unshift({
      type: "no_accepted_patch",
      message: "整书没有 accepted patch。",
    });
  }

  return {
    ok: allPagesOk && errors.length === 0,
    markdown: `${pages.join("\n\n---\n\n")}${pages.length ? "\n" : ""}`,
    pageSummaries,
    appliedPatchCount,
    acceptedPatchCount,
    skippedPatchCount: Math.max(0, acceptedPatchCount - appliedPatchCount),
    errors,
    warnings,
  };
}

function getAcceptedCorrectedDownloadStatus() {
  const preview = buildAcceptedPatchPreviewForBook();
  const warnings = Array.isArray(preview?.warnings) ? preview.warnings : [];
  const errors = Array.isArray(preview?.errors) ? preview.errors : [];
  const acceptedPatchCount = Number(preview?.acceptedPatchCount) || 0;
  const appliedPatchCount = Number(preview?.appliedPatchCount) || 0;
  const warningCount = warnings.length;
  const errorCount = errors.length;
  const firstErrorType = errors[0]?.type || "";
  const firstWarningType = warnings[0]?.type || "";
  let status = "ready";
  let canDownload = true;
  let message = "accepted 校正稿可下载";

  if (!acceptedPatchCount) {
    status = "empty";
    canDownload = false;
    message = "当前没有 accepted patch，无法生成 accepted 校正稿";
  } else if (!preview?.ok || errorCount) {
    status = "blocked";
    canDownload = false;
    message = firstErrorType ? `存在阻塞问题，不能下载：${firstErrorType}` : "存在阻塞问题，不能下载";
  } else if (warningCount) {
    status = "warning-only";
    canDownload = true;
    message = `可下载，但存在 ${warningCount} 个 warning`;
  }

  return {
    status,
    canDownload,
    message,
    acceptedPatchCount,
    appliedPatchCount,
    warningCount,
    errorCount,
    firstErrorType,
    firstWarningType,
    preview,
  };
}

function downloadAcceptedCorrectedMarkdown() {
  const status = getAcceptedCorrectedDownloadStatus();
  const preview = status.preview;
  state.acceptedPatchBookPreview = preview;
  if (!status.canDownload) {
    return {
      ok: false,
      reason: status.status === "empty" ? "no_accepted_patch" : "preview_not_ok",
      status,
      preview,
    };
  }

  const markdown = `${acceptedPatchDownloadHeader()}\n\n${preview.markdown || ""}`;
  const filename = `${baseExportName()}-accepted-corrected.md`;
  downloadTextFile(filename, markdown);
  return {
    ok: true,
    reason: "",
    filename,
    markdown,
    status,
    preview,
  };
}

function acceptedPatchDownloadHeader() {
  return `<!--
Generated by OCR accepted patch dry-run export.
Only accepted OcrPatch entries are applied.
Original export button is unchanged.
-->`;
}

function withIssuePageNo(issues, pageNo) {
  return (Array.isArray(issues) ? issues : []).map((issue) => ({
    pageNo,
    ...issue,
  }));
}

function acceptedOcrPatchesForPage(pageNo) {
  const patches = Array.isArray(state.ocrPatches) ? state.ocrPatches : [];
  return patches.filter((patch) => patch?.status === "accepted" && ocrPatchBelongsToPage(patch, pageNo));
}

function ocrPatchBelongsToPage(patch, pageNo) {
  const metadataPageNo = Number(patch?.metadata?.pageNo);
  if (Number.isFinite(metadataPageNo) && metadataPageNo > 0) {
    return metadataPageNo === Number(pageNo);
  }
  return String(patch?.blockId || "").startsWith(`p${pageNo}_`);
}

function countAppliedAcceptedPatches(acceptedPatches, blocks, errors, warnings) {
  const existingBlockIds = new Set(blocks.map((block) => block.blockId));
  const failedBlockIds = new Set(
    []
      .concat(errors || [])
      .concat((warnings || []).filter((warning) => warning?.type === "patch_block_not_found"))
      .map((issue) => issue?.blockId)
      .filter(Boolean),
  );
  return acceptedPatches.filter((patch) => existingBlockIds.has(patch.blockId) && !failedBlockIds.has(patch.blockId)).length;
}

function normalizeDraftPatchMarkdown(blockId, markdown) {
  const rawMarkdown = String(markdown || "");
  const normalizeMathDelimiters = getOcrCoreNormalizeMathDelimiters();
  if (!normalizeMathDelimiters) {
    warnOcrCorePatch("mathDelimiterNormalizer 不可用，draft patch 将保留未规范化 Markdown。");
    return rawMarkdown;
  }
  try {
    const result = normalizeMathDelimiters({
      blockId,
      blockText: rawMarkdown,
      blockType: "unknown",
    });
    return typeof result?.normalizedText === "string" ? result.normalizedText : rawMarkdown;
  } catch (error) {
    warnOcrCorePatch("draft patch 公式分隔符规范化失败，已保守使用原文。", error);
    return rawMarkdown;
  }
}

function validateDraftPatchRenderability(blockId, markdown) {
  const validateRenderability = getOcrCoreValidateRenderability();
  if (!validateRenderability) {
    warnOcrCorePatch("renderValidator 不可用，draft patch renderStatusAfter 标记为 warning。");
    return { severity: "warning" };
  }
  try {
    return validateRenderability({
      blockId,
      markdown,
      blockType: "unknown",
      source: "unknown",
    });
  } catch (error) {
    warnOcrCorePatch("draft patch 渲染静态校验失败，renderStatusAfter 标记为 error。", error);
    return { severity: "error" };
  }
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
  return detectLocalRiskCandidatesForPage(pageNumber);
}

function detectLocalRiskCandidatesForPage(pageNumber) {
  const segmentRisks = reviewSegmentsForPage(pageNumber)
    .map((segment) => {
      const { score: baseScore, reasons: baseReasons } = scoreRiskBlock(segment.markdown);
      const reasons = baseReasons.slice();
      let score = baseScore;
      if (isPageBottomReviewCandidate(segment)) {
        score = Math.max(score, 0.26);
        reasons.push("page_bottom_boundary");
      }
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
    .filter((item) => item.text && item.score >= 0.25);
  return segmentRisks.concat(detectSupplementalRiskCandidatesForPage(pageNumber)).sort((a, b) => b.score - a.score);
}

function detectSupplementalRiskCandidatesForPage(pageNumber) {
  return detectCrossPageContinuationCandidatesForPage(pageNumber)
    .concat(detectSyntheticRiskCandidatesForPage(pageNumber))
    .concat(detectContentListRiskCandidatesForPage(pageNumber));
}

function detectSyntheticRiskCandidatesForPage(pageNumber) {
  return detectMissingBackgroundTitleCandidatesForPage(pageNumber).concat(detectMissingPageTopTextCandidatesForPage(pageNumber));
}

function detectContentListRiskCandidatesForPage(pageNumber) {
  const items = contentListItemsForPage(pageNumber);
  if (!items.length) {
    return [];
  }
  const middleTexts = new Set(
    originalBlockMarkdownsForPage(pageNumber)
      .map((entry) => normalizeTextForComparison(entry.markdown))
      .filter(Boolean),
  );
  const pageSize = inferContentListPageSize(pageNumber, items);
  return items
    .map((item, pageItemIndex) => contentListItemToRiskCandidate(item, pageNumber, pageItemIndex, pageSize, middleTexts))
    .filter(Boolean);
}

function detectCrossPageContinuationCandidatesForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  const previousPage = state.mineruInfo?.pdf_info?.[pageNumber - 2];
  if (!page || !previousPage) {
    return [];
  }
  const pageSize = page.page_size || previousPage.page_size || null;
  const blocks = Array.isArray(previousPage.para_blocks) ? previousPage.para_blocks : [];
  const currentTexts = new Set(
    reviewBlockMarkdownsForPage(pageNumber)
      .map((entry) => normalizeTextForComparison(entry.markdown))
      .filter(Boolean),
  );
  return blocks
    .map((block, sourceBlockIndex) => {
      const continuationBlock = filterBlockLines(block, lineHasCrossPageContent);
      const markdown = blockToMarkdown(continuationBlock).trim();
      if (!markdown || isTextRedundantWithNormalizedSet(markdown, currentTexts)) {
        return null;
      }
      const bbox = getBlockBBox(continuationBlock);
      const scored = scoreRiskBlock(markdown);
      return {
        pageNumber,
        blockIndex: `cross-page-continuation-${pageNumber}-${sourceBlockIndex}`,
        sourceBlockIndex: String(sourceBlockIndex),
        sourcePageNumber: pageNumber - 1,
        bbox,
        pageSize,
        text: markdown,
        score: Math.max(scored.score, 0.34),
        reasons: Array.from(new Set(["cross_page_continuation"].concat(scored.reasons))),
        syntheticPlacement: "page_top",
        syntheticLabel: "跨页续段候选",
        supplementalSource: "cross_page_continuation",
      };
    })
    .filter(Boolean);
}

function hasCrossPageContinuationForPage(pageNumber) {
  return detectCrossPageContinuationCandidatesForPage(pageNumber).length > 0;
}

function contentListItemToRiskCandidate(item, pageNumber, pageItemIndex, pageSize, middleTexts) {
  if (!item || item.type !== "discarded") {
    return null;
  }
  const text = contentListItemText(item);
  const normalized = normalizeTextForComparison(text);
  if (
    !normalized ||
    normalized.length < 4 ||
    isPageNumberOnlyText(normalized) ||
    isTextRedundantWithNormalizedSet(normalized, middleTexts)
  ) {
    return null;
  }
  const bbox = normalizedBBox(item.bbox);
  const geometry = bbox ? bboxGeometryForPageSize(bbox, pageSize) : null;
  const scored = scoreRiskBlock(text);
  const reasons = scored.reasons.slice();
  let score = scored.score;
  const isTopCandidate = Boolean(geometry?.topRatio <= 0.2 && text.length >= 6);
  if (isTopCandidate && hasCrossPageContinuationForPage(pageNumber)) {
    return null;
  }
  const isBottomCandidate = Boolean(geometry?.topRatio >= 0.82 || geometry?.bottomRatio >= 0.9);
  const isFootnoteCandidate = hasFootnoteSignal(text) && !isTopCandidate;
  if (!isFootnoteCandidate) {
    const footnoteReasonIndex = reasons.indexOf("footnote_marker_or_note");
    if (footnoteReasonIndex >= 0) {
      reasons.splice(footnoteReasonIndex, 1);
    }
  }
  if (!reasons.includes("content_list_discarded")) {
    reasons.unshift("content_list_discarded");
  }
  if (isFootnoteCandidate) {
    score = Math.max(score, 0.38);
    if (!reasons.includes("footnote_marker_or_note")) {
      reasons.push("footnote_marker_or_note");
    }
  }
  if (isTopCandidate) {
    score = Math.max(score, 0.33);
    if (!reasons.includes("background_heading_missing")) {
      reasons.push("background_heading_missing");
    }
  }
  if (isBottomCandidate) {
    score = Math.max(score, 0.31);
    if (!reasons.includes("page_bottom_boundary")) {
      reasons.push("page_bottom_boundary");
    }
  }
  if (score < 0.25) {
    return null;
  }
  return {
    pageNumber,
    blockIndex: `content-list-discarded-${pageNumber}-${pageItemIndex}`,
    bbox,
    pageSize,
    text,
    score: Math.min(score, 1),
    reasons: Array.from(new Set(reasons)),
    syntheticPlacement: isTopCandidate ? "page_top" : isBottomCandidate ? "page_bottom" : "content_list",
    syntheticLabel: isFootnoteCandidate ? "content_list 脚注候选" : isTopCandidate ? "content_list 标题候选" : "content_list 补充候选",
    supplementalSource: "content_list",
    contentListIndex: item.__contentListIndex,
  };
}

function detectCrossPageRiskCandidatesForPage(pageNumber) {
  const candidates = [];
  return candidates;
}

function appendCrossPageBoundaryCandidates(candidates, pageNumber, sourcePageNumber, hint) {
  if (sourcePageNumber < 1 || sourcePageNumber > getMineruPageCount()) {
    return;
  }
  const segments = pageSegmentsForPage(sourcePageNumber);
  const boundarySegments = hint === "previous_tail" ? segments.slice(-2) : segments.slice(0, 2);
  boundarySegments.forEach((segment) => {
    const { score, reasons } = scoreRiskBlock(segment.markdown);
    if (!segment.markdown || score < 0.25) {
      return;
    }
    const sourceBlockIndex = String(segment.blockIndex);
    const directionReason = hint === "previous_tail" ? "cross_page_previous_tail" : "cross_page_next_head";
    candidates.push({
      pageNumber,
      blockIndex: `cross-${hint}-${sourcePageNumber}-${sourceBlockIndex}`,
      sourceBlockIndex,
      crossPageSourcePage: sourcePageNumber,
      crossPageHint: hint,
      crossPageLabel: hint === "previous_tail" ? `上一页候选 · 第 ${sourcePageNumber} 页` : `下一页候选 · 第 ${sourcePageNumber} 页`,
      bbox: null,
      pageSize: segment.pageSize,
      text: segment.markdown,
      score: Math.min(score + 0.02, 1),
      reasons: Array.from(new Set([directionReason].concat(reasons))),
    });
  });
}

function isPageBottomReviewCandidate(segment) {
  const markdown = String(segment?.markdown || "").trim();
  if (markdown.length < 8 || /^[\s\dIVXLCDMivxlcdm.()-]+$/.test(markdown)) {
    return false;
  }
  const geometry = segmentPageGeometry(segment);
  if (!geometry) {
    return false;
  }
  return geometry.topRatio >= 0.68 || geometry.bottomRatio >= 0.78;
}

function detectMissingBackgroundTitleCandidatesForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  if (!page) {
    return [];
  }
  if (hasCrossPageContinuationForPage(pageNumber)) {
    return [];
  }
  const entries = originalBlockMarkdownsForPage(pageNumber);
  const pageSize = page.page_size || entries.find((entry) => entry.pageSize)?.pageSize;
  const height = pageSizeHeight(pageSize);
  const width = pageSizeWidth(pageSize);
  if (!height || !width || hasTopTitleEntry(entries)) {
    return [];
  }
  const firstContent = entries
    .filter((entry) => String(entry.markdown || "").trim().length >= 12)
    .find((entry) => segmentPageGeometry(entry));
  const geometry = segmentPageGeometry(firstContent);
  if (!firstContent || !geometry || geometry.topRatio < 0.16 || geometry.topRatio > 0.42) {
    return [];
  }
  const cropBottom = Math.max(height * 0.12, Math.min(Number(firstContent.bbox?.[1]) - 4, height * 0.3));
  if (!Number.isFinite(cropBottom) || cropBottom <= height * 0.08) {
    return [];
  }
  return [
    {
      pageNumber,
      blockIndex: `missing-heading-${pageNumber}`,
      bbox: [0, 0, width, cropBottom],
      pageSize,
      text: "疑似遗漏页首带背景标题区域。请用 Mathpix 校正此块后人工确认。",
      score: 0.31,
      reasons: ["background_heading_missing"],
      syntheticPlacement: "page_top",
      syntheticLabel: "页首标题候选",
    },
  ];
}

function detectMissingPageTopTextCandidatesForPage(pageNumber) {
  const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
  if (!page) {
    return [];
  }
  if (hasCrossPageContinuationForPage(pageNumber)) {
    return [];
  }
  const entries = originalBlockMarkdownsForPage(pageNumber);
  const pageSize = page.page_size || entries.find((entry) => entry.pageSize)?.pageSize;
  const height = pageSizeHeight(pageSize);
  const width = pageSizeWidth(pageSize);
  if (!height || !width || hasTopTitleEntry(entries)) {
    return [];
  }
  const firstContent = entries
    .filter((entry) => String(entry.markdown || "").trim().length >= 20)
    .find((entry) => segmentPageGeometry(entry));
  const geometry = segmentPageGeometry(firstContent);
  if (!firstContent || !geometry || geometry.topRatio < 0.22 || geometry.topRatio > 0.62) {
    return [];
  }
  const cropTop = height * 0.07;
  const cropBottom = Math.min(Number(firstContent.bbox?.[1]) - 4, height * 0.5);
  if (!Number.isFinite(cropBottom) || cropBottom - cropTop < height * 0.08) {
    return [];
  }
  return [
    {
      pageNumber,
      blockIndex: `missing-page-top-text-${pageNumber}`,
      bbox: [0, cropTop, width, cropBottom],
      pageSize,
      text: "疑似遗漏页首正文段落。请用 Mathpix 校正此块后人工确认。",
      score: 0.32,
      reasons: ["page_top_text_missing"],
      syntheticPlacement: "page_top",
      syntheticLabel: "页首正文候选",
    },
  ];
}

function hasTopTitleEntry(entries) {
  return entries.some((entry) => {
    const geometry = segmentPageGeometry(entry);
    if (!geometry || geometry.topRatio > 0.28) {
      return false;
    }
    const markdown = String(entry.markdown || "").trim();
    return entry.block?.type === "title" || /^#{1,6}\s+/.test(markdown);
  });
}

function segmentPageGeometry(segment) {
  const bbox = segment?.bbox;
  const pageSize = segment?.pageSize;
  if (!Array.isArray(bbox) || bbox.length < 4) {
    return null;
  }
  const height = pageSizeHeight(pageSize);
  if (!height) {
    return null;
  }
  const top = Number(bbox[1]);
  const bottom = Number(bbox[3]);
  if (!Number.isFinite(top) || !Number.isFinite(bottom)) {
    return null;
  }
  return {
    topRatio: top / height,
    bottomRatio: bottom / height,
  };
}

function bboxGeometryForPageSize(bbox, pageSize) {
  if (!Array.isArray(bbox) || bbox.length < 4) {
    return null;
  }
  const height = pageSizeHeight(pageSize);
  if (!height) {
    return null;
  }
  const top = Number(bbox[1]);
  const bottom = Number(bbox[3]);
  if (!Number.isFinite(top) || !Number.isFinite(bottom)) {
    return null;
  }
  return {
    topRatio: top / height,
    bottomRatio: bottom / height,
  };
}

function pageSizeHeight(pageSize) {
  if (Array.isArray(pageSize)) {
    return Number(pageSize[1]) || 0;
  }
  if (pageSize && typeof pageSize === "object") {
    return Number(pageSize.height || pageSize.h || pageSize[1]) || 0;
  }
  return 0;
}

function pageSizeWidth(pageSize) {
  if (Array.isArray(pageSize)) {
    return Number(pageSize[0]) || 0;
  }
  if (pageSize && typeof pageSize === "object") {
    return Number(pageSize.width || pageSize.w || pageSize[0]) || 0;
  }
  return 0;
}

function normalizeContentListItems(data) {
  const rawItems = Array.isArray(data)
    ? data
    : Array.isArray(data?.content_list)
      ? data.content_list
      : Array.isArray(data?.items)
        ? data.items
        : [];
  return rawItems
    .filter((item) => item && typeof item === "object")
    .map((item, index) => ({ ...item, __contentListIndex: index }));
}

function contentListItemsForPage(pageNumber) {
  const targetIndex = Number(pageNumber) - 1;
  if (!Number.isFinite(targetIndex) || targetIndex < 0) {
    return [];
  }
  return (Array.isArray(state.contentListItems) ? state.contentListItems : []).filter((item) => Number(item.page_idx) === targetIndex);
}

function contentListItemText(item) {
  if (!item || typeof item !== "object") {
    return "";
  }
  if (typeof item.text === "string") {
    return item.text.trim();
  }
  if (Array.isArray(item.img_caption)) {
    return item.img_caption.join("\n").trim();
  }
  if (typeof item.table_body === "string") {
    return item.table_body.trim();
  }
  if (typeof item.latex === "string") {
    return item.latex.trim();
  }
  return "";
}

function normalizedBBox(bbox) {
  if (!Array.isArray(bbox) || bbox.length < 4) {
    return null;
  }
  const normalized = bbox.slice(0, 4).map(Number);
  return normalized.every(Number.isFinite) ? normalized : null;
}

function inferContentListPageSize(pageNumber, items = contentListItemsForPage(pageNumber)) {
  const explicit = items.find((item) => Array.isArray(item.page_size) || item.pageSize)?.page_size || items.find((item) => item.pageSize)?.pageSize;
  if (explicit) {
    return explicit;
  }
  const boxes = items.map((item) => normalizedBBox(item.bbox)).filter(Boolean);
  if (!boxes.length) {
    const page = state.mineruInfo?.pdf_info?.[pageNumber - 1];
    return page?.page_size || null;
  }
  const maxX = Math.max(...boxes.map((box) => box[2]));
  const maxY = Math.max(...boxes.map((box) => box[3]));
  return [Math.ceil(Math.max(maxX + 20, maxX * 1.1)), Math.ceil(Math.max(maxY + 20, maxY * 1.08))];
}

function normalizeTextForComparison(text) {
  return String(text || "").replace(/\s+/g, " ").trim();
}

function canonicalTextForOverlap(text) {
  return normalizeTextForComparison(text)
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function isTextRedundantWithNormalizedSet(text, normalizedTexts) {
  const normalized = normalizeTextForComparison(text);
  if (!normalized) {
    return false;
  }
  const canon = canonicalTextForOverlap(normalized);
  if (!canon) {
    return false;
  }
  const sourceItems = normalizedTexts instanceof Set ? Array.from(normalizedTexts) : Array.isArray(normalizedTexts) ? normalizedTexts : [];
  return sourceItems.some((candidate) => {
    const candidateNormalized = normalizeTextForComparison(candidate);
    if (!candidateNormalized) {
      return false;
    }
    if (candidateNormalized === normalized) {
      return true;
    }
    const other = canonicalTextForOverlap(candidateNormalized);
    if (!other) {
      return false;
    }
    const shorter = canon.length <= other.length ? canon : other;
    const longer = canon.length > other.length ? canon : other;
    if (shorter.length >= 24 && longer.includes(shorter) && shorter.length / longer.length >= 0.55) {
      return true;
    }
    const shortTokens = new Set(shorter.split(/\s+/).filter((token) => token.length > 1));
    const longTokens = new Set(longer.split(/\s+/).filter((token) => token.length > 1));
    if (shortTokens.size < 6) {
      return false;
    }
    const shared = Array.from(shortTokens).filter((token) => longTokens.has(token)).length;
    return shared / shortTokens.size >= 0.88;
  });
}

function isPageNumberOnlyText(text) {
  return /^[\s\dIVXLCDMivxlcdm.()-]+$/.test(String(text || "").trim());
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
  if (hasHeadingSpecialSymbolRisk(text)) {
    score += 0.35;
    reasons.push("heading_special_symbol");
  }
  if (hasScientificSpecialSymbolRisk(text)) {
    score += 0.28;
    reasons.push("scientific_special_symbol");
  }
  if (hasFootnoteSignal(text)) {
    score += 0.26;
    reasons.push("footnote_marker_or_note");
  }
  if (hasOcrGarbledTextRisk(text)) {
    score += 0.29;
    reasons.push("ocr_garbled_text");
  }
  if (hasDisplayMathBlock(text)) {
    score += 0.42;
    reasons.push("display_math_block");
  }
  if (hasLatexMathEnvironment(text)) {
    score += 0.4;
    reasons.push("latex_math_environment");
  }
  if (hasStandaloneEquationLine(text)) {
    score += 0.34;
    reasons.push("standalone_equation_line");
  }
  if (hasMathDenseTextRisk(text)) {
    score += 0.3;
    reasons.push("math_dense_text");
  }
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

function hasHeadingSpecialSymbolRisk(text) {
  return String(text || "")
    .split("\n")
    .some((line) => {
      const match = line.match(/^\s{0,3}#{1,6}\s+(.+)$/);
      if (!match) {
        return false;
      }
      const heading = match[1].trim();
      if (!heading) {
        return false;
      }
      return /[�#]|[Α-Ωα-ωµμ∑∫∂∞±×÷≈≠≤≥]/.test(heading) || /\\[a-zA-Z]+/.test(heading);
    });
}

function hasScientificSpecialSymbolRisk(text) {
  const value = String(text || "").replace(/<[^>]+>/g, " ");
  if (!value.trim()) {
    return false;
  }
  if (/[A-Za-zÀ-ÖØ-öø-ÿ][¨´`^~][A-Za-zÀ-ÖØ-öø-ÿ]/.test(value) || /[A-Za-zÀ-ÖØ-öø-ÿ]+[¨´`^~]\s*[A-Za-zÀ-ÖØ-öø-ÿ]+/.test(value)) {
    return true;
  }
  if (/[�ℰℱℋℒℓℏℜℑ]|[\u{1D400}-\u{1D7FF}]/u.test(value)) {
    return true;
  }
  if (/[Α-Ωα-ωµμ]/.test(value) && /[A-Za-z]/.test(value)) {
    return true;
  }
  const diacriticWords = value.match(/\b[A-Za-zÀ-ÖØ-öø-ÿ]*[À-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ]*\b/g) || [];
  if (!diacriticWords.length) {
    return false;
  }
  return /(?:experiment|principle|theory|field|tensor|scalar|vector|metric|spacetime|relativ|gravitation|equivalence|EEP|Einstein|Dicke|Schiff)/i.test(value);
}

function hasFootnoteSignal(text) {
  const value = String(text || "").replace(/<[^>]+>/g, " ");
  if (!value.trim()) {
    return false;
  }
  return (
    /[A-Za-zÀ-ÖØ-öø-ÿ)”"')\]]\s*(?:[¹²³⁴⁵⁶⁷⁸⁹⁰]|\^[0-9]{1,2})(?=[\s.,;:)]|$)/.test(value) ||
    /[A-Za-zÀ-ÖØ-öø-ÿ)”"')\]],\s*[0-9]{1,2}(?=\s|$)/.test(value) ||
    /^\s*(?:[¹²³⁴⁵⁶⁷⁸⁹⁰]|\d{1,2})\s+(?:Although|Where|Here|This|In|For|See|Newton|Einstein|Dicke|Schiff|[A-Z][a-z])/m.test(value)
  );
}

function hasOcrGarbledTextRisk(text) {
  const value = String(text || "")
    .replace(/<[^>]+>/g, " ")
    .replace(/\\\$/g, "$");
  if (!value.trim()) {
    return false;
  }
  return (
    /\b1[&$)(][0-9&$)(]{1,3}[a-z]?(?=\s|[.,;:)\]]|$)/i.test(value) ||
    /(?:^|\s)\+[a-z]{2,}\b/i.test(value) ||
    /\b[a-z]{2,}\+[a-z]{2,}\b/i.test(value) ||
    /(?:^|\s),[a-z]{3,}\b/i.test(value) ||
    /\b(?:e-ect|e-ects|di-erent|con-rmed)\b/i.test(value)
  );
}

function hasMathDenseTextRisk(text) {
  const value = String(text || "").replace(/<[^>]+>/g, " ");
  if (!value.trim() || hasDisplayMathBlock(value) || hasLatexMathEnvironment(value)) {
    return false;
  }
  const inlineMathCount = (value.match(/\$[^$\n]{1,160}\$|\\\([\s\S]{1,160}?\\\)/g) || []).length;
  if (inlineMathCount >= 2) {
    return true;
  }

  const latexCommandCount = (value.match(/\\(?:frac|sqrt|sum|int|mathrm|mathit|mathbf|mu|nu|alpha|beta|gamma|delta|theta|lambda|rho|sigma|omega|Omega|Delta|Phi)\b/g) || []).length;
  const scriptCount = (value.match(/[A-Za-zΑ-Ωα-ω]\s*[_^]\s*(?:\{[^}]{1,40}\}|[A-Za-z0-9])/g) || []).length;
  const greekSymbolCount = (value.match(/[Α-Ωα-ωµμ∑∫∂∞±×÷≈≠≤≥]/g) || []).length;
  const equationLikeCount = (value.match(/[A-Za-zΑ-Ωα-ω](?:[_^]\{?[\wΑ-Ωα-ω]+\}?){0,2}\s*[=≈≃≅≠≤≥]\s*[A-Za-z0-9\\{(]/g) || []).length;
  const mathTokenScore = latexCommandCount + scriptCount + greekSymbolCount + equationLikeCount * 2;

  return mathTokenScore >= 3;
}

function hasDisplayMathBlock(text) {
  return /\$\$[\s\S]*?\$\$/.test(text) || /\\\[[\s\S]*?\\\]/.test(text);
}

function hasLatexMathEnvironment(text) {
  return /\\begin\{(?:equation|align|aligned|array|cases|matrix|pmatrix|bmatrix|gather|split|multline)\*?\}/i.test(text);
}

function hasStandaloneEquationLine(text) {
  return String(text || "")
    .split("\n")
    .some((line) => {
      const trimmed = line.trim();
      if (!trimmed || trimmed.length > 220 || !/[=≈≃≅≠≤≥<>]/.test(trimmed)) {
        return false;
      }
      return /(?:\\[a-zA-Z]+|[_^{}]|[A-Za-zΑ-Ωα-ω]\s*[=≈≃≅≠≤≥<>]|[=≈≃≅≠≤≥<>]\s*[A-Za-zΑ-Ωα-ω]|[∑∫∂∞±×÷√])/.test(trimmed);
    });
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
  els.firstPageButton.disabled = !hasPages || state.currentPage <= 1;
  els.prevPageButton.disabled = !hasPages || state.currentPage <= 1;
  els.nextPageButton.disabled = !hasPages || state.currentPage >= total;
  els.lastPageButton.disabled = !hasPages || state.currentPage >= total;
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
  const contentListSummary = state.contentListItems.length ? ` · content_list ${state.contentListItems.length} 条` : "";
  els.fileMeta.textContent = `${prefix}${contentListSummary} · 高风险 ${riskPages} 页 / ${riskBlocks} 块 · 已应用校正 ${count} 页 / ${blockCount} 块`;
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
  const rawMarkdown = String(markdown || "");
  const adaptMathpixToTargetMarkdown = getOcrCoreAdaptMathpixToTargetMarkdown();
  if (!adaptMathpixToTargetMarkdown) {
    warnOcrCoreMathpixAdapter("mathpixToTargetMarkdownAdapter 不可用，已保守返回原始 Markdown。");
    return rawMarkdown;
  }
  try {
    const result = adaptMathpixToTargetMarkdown({
      blockId: "legacy-prepareMathpixMarkdown",
      rawText: rawMarkdown,
      source: "mathpix",
      blockType: "unknown",
    });
    return typeof result?.targetMarkdown === "string" ? result.targetMarkdown : rawMarkdown;
  } catch (error) {
    warnOcrCoreMathpixAdapter("prepareMathpixMarkdown 调用 mathpixToTargetMarkdownAdapter 失败，已保守返回原始 Markdown。", error);
    return rawMarkdown;
  }
}

// Legacy Mathpix cleanup helpers are kept for now so older paths can be audited
// before a later cleanup removes unused OCR compare normalization code.
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
      display_math_block: "独立公式",
      latex_math_environment: "LaTeX 公式环境",
      standalone_equation_line: "独立方程行",
      heading_special_symbol: "标题特殊符号",
      scientific_special_symbol: "科学特殊符号",
      footnote_marker_or_note: "脚注/注释",
      ocr_garbled_text: "疑似 OCR 字符乱码",
      content_list_discarded: "content_list 补充",
      background_heading_missing: "疑似漏识别标题",
      page_top_text_missing: "疑似漏识别页首正文",
      cross_page_continuation: "跨页续段",
      cross_page_previous_tail: "上一页边界候选",
      cross_page_next_head: "下一页边界候选",
      page_bottom_boundary: "页底待核查",
      math_dense_text: "公式密集段落",
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
  const pad = normalizeCropPadding(padding);
  const x = Math.max(0, Math.floor((bbox[0] - pad.left) * scaleX));
  const y = Math.max(0, Math.floor((bbox[1] - pad.top) * scaleY));
  const right = Math.min(image.naturalWidth || image.width, Math.ceil((bbox[2] + pad.right) * scaleX));
  const bottom = Math.min(image.naturalHeight || image.height, Math.ceil((bbox[3] + pad.bottom) * scaleY));
  const width = Math.max(1, right - x);
  const height = Math.max(1, bottom - y);
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  const context = canvas.getContext("2d");
  context.drawImage(image, x, y, width, height, 0, 0, width, height);
  return canvas.toDataURL("image/png");
}

function normalizeCropPadding(padding = 8) {
  if (typeof padding === "number") {
    const value = Math.max(0, Number(padding) || 0);
    return { left: value, right: value, top: value, bottom: value };
  }
  const horizontal = Math.max(0, Number(padding?.horizontal ?? padding?.x ?? 0) || 0);
  const vertical = Math.max(0, Number(padding?.vertical ?? padding?.y ?? 0) || 0);
  return {
    left: Math.max(0, Number(padding?.left ?? horizontal) || 0),
    right: Math.max(0, Number(padding?.right ?? horizontal) || 0),
    top: Math.max(0, Number(padding?.top ?? vertical) || 0),
    bottom: Math.max(0, Number(padding?.bottom ?? vertical) || 0),
  };
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

    if (isStandaloneMarkdownImageLine(lines[index])) {
      const image = extractMarkdownImageReferences(lines[index])[0];
      if (image) {
        parts.push(renderMarkdownImage(image.alt || "image", image.src));
      }
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
