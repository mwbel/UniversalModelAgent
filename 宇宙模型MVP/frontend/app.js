const state = {
  ragStrategies: [],
  knowledgeBases: [],
  selectedVariant: null,
  selectedKbId: null,
  pendingFile: null,
  theme: "day",
  sessions: [],
  activeSessionId: null,
};

const API_BASE =
  window.location.protocol === "file:" ? "http://127.0.0.1:8787" : "";

function apiUrl(path) {
  return `${API_BASE}${path}`;
}

function createSession(title = "新对话") {
  return {
    id: `session-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    title,
    messages: [],
    updatedAt: Date.now(),
  };
}

function getActiveSession() {
  return state.sessions.find((session) => session.id === state.activeSessionId) || null;
}

async function initialize() {
  initializeTheme();
  bindThemeSwitch();
  bindExampleQuestions();
  bindComposer();
  bindSessionActions();
  bindRagUpload();
  bootstrapSessions();
  renderSessions();
  renderMessages();
  await loadConfig();
  await loadVisualizations();
  await checkHealth();
}

function bootstrapSessions() {
  const firstSession = createSession();
  state.sessions = [firstSession];
  state.activeSessionId = firstSession.id;
}

function bindSessionActions() {
  document.getElementById("newChatButton").addEventListener("click", () => {
    const session = createSession();
    state.sessions.unshift(session);
    state.activeSessionId = session.id;
    renderSessions();
    renderMessages();
    document.getElementById("questionInput").focus();
  });
}

function bindRagUpload() {
  const fileInput = document.getElementById("ragFileInput");
  const pickButton = document.getElementById("pickFileButton");
  const uploadButton = document.getElementById("uploadFileButton");
  const kbInput = document.getElementById("kbIdInput");
  const kbSelect = document.getElementById("kbSelect");

  pickButton.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", () => {
    state.pendingFile = fileInput.files?.[0] || null;
    document.getElementById("selectedFileName").textContent = state.pendingFile ? state.pendingFile.name : "未选择文件";
    if (state.pendingFile) {
      const suggestedKbId = suggestKnowledgeBaseId(state.pendingFile.name);
      if (!kbInput.value.trim() || kbInput.value.trim().toLowerCase() === "default") {
        kbInput.value = suggestedKbId;
        state.selectedKbId = suggestedKbId;
      }
    }
  });

  kbSelect.addEventListener("change", () => {
    state.selectedKbId = kbSelect.value || null;
    if (state.selectedKbId) {
      kbInput.value = state.selectedKbId;
    }
  });

  const strategySelect = document.getElementById("strategySelect");
  strategySelect.addEventListener("change", () => {
    state.selectedVariant = strategySelect.value || null;
    renderStrategyOptions();
  });

  uploadButton.addEventListener("click", async () => {
    const kbId =
      kbInput.value.trim() ||
      state.selectedKbId ||
      suggestKnowledgeBaseId(state.pendingFile?.name || "") ||
      "default";
    if (!state.pendingFile) {
      setUploadStatus("请先选择一个本地文档。", true);
      return;
    }

    const formData = new FormData();
    formData.append("file", state.pendingFile);
    formData.append("kb_id", kbId);
    setUploadStatus("正在上传并摄入文档...", false);
    uploadButton.disabled = true;

    try {
      const response = await fetch(apiUrl("/api/rag/upload"), {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      if (!data.ok) {
        throw new Error(data.error || "上传失败");
      }

      state.selectedKbId = data.kbId || kbId;
      kbInput.value = state.selectedKbId;
      state.pendingFile = null;
      fileInput.value = "";
      document.getElementById("selectedFileName").textContent = "未选择文件";
      setUploadStatus(`已上传到知识库 ${state.selectedKbId}，共摄入 ${data.chunks ?? "-"} 个文档块。`, false);
      await refreshKnowledgeBases();
    } catch (error) {
      setUploadStatus(`上传失败：${error.message}`, true);
    } finally {
      uploadButton.disabled = false;
    }
  });
}

function suggestKnowledgeBaseId(filename) {
  const stem = String(filename || "")
    .replace(/\.[^.]+$/, "")
    .trim();
  const parts = stem
    .split(/[\s._\-()（）【】\[\]、，,]+/)
    .map((item) => item.trim())
    .filter(Boolean);
  if (parts.length >= 2) {
    return `${parts[0]}-${parts[1]}`;
  }
  if (parts.length === 1) {
    return parts[0];
  }
  return "default";
}

function bindExampleQuestions() {
  document.querySelectorAll(".example-chip").forEach((button) => {
    button.addEventListener("click", () => {
      document.getElementById("questionInput").value = button.dataset.question || "";
      document.getElementById("questionInput").focus();
    });
  });
}

function bindComposer() {
  const form = document.getElementById("chatForm");
  const textarea = document.getElementById("questionInput");

  textarea.addEventListener("input", autoResizeTextarea);
  textarea.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      form.requestSubmit();
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const question = textarea.value.trim();
    if (!question) {
      return;
    }

    const session = getActiveSession();
    if (!session) {
      return;
    }

    textarea.value = "";
    autoResizeTextarea();
    setRequestState("Thinking");

    if (session.messages.length === 0) {
      session.title = question.slice(0, 24);
      document.getElementById("chatTitle").textContent = session.title;
    }

    const historyPayload = session.messages.map((message) => ({
      role: message.role,
      content: message.content,
    }));

    session.messages.push({
      role: "user",
      content: question,
      recommendedVisualizations: [],
    });
    session.updatedAt = Date.now();
    renderSessions();
    renderMessages();

    try {
      const response = await fetch(apiUrl("/api/chat"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question,
          history: historyPayload,
          ragVariant: state.selectedVariant,
          kbId: state.selectedKbId,
        }),
      });
      const data = await response.json();

      session.messages.push({
        role: "assistant",
        content: data.answer || "",
        recommendedVisualizations: data.recommendedVisualizations || [],
        strategy: data.strategy || state.selectedVariant,
        citations: data.citations || [],
        contexts: data.contexts || [],
        latencyMs: data.latencyMs,
        tokenUsage: data.tokenUsage,
        service: data.service || "knowledge",
      });
      session.updatedAt = Date.now();
      renderSessions();
      renderMessages();
    } catch (error) {
      session.messages.push({
        role: "assistant",
        content: `请求失败：${error.message}`,
        recommendedVisualizations: [],
        strategy: state.selectedVariant,
        citations: [],
        contexts: [],
        service: "error",
      });
      renderMessages();
    } finally {
      setRequestState("Ready");
    }
  });
}

function renderSessions() {
  const list = document.getElementById("sessionList");
  list.innerHTML = "";
  document.getElementById("conversationCount").textContent = String(state.sessions.length);

  state.sessions.forEach((session) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `session-item ${session.id === state.activeSessionId ? "active" : ""}`;
    button.innerHTML = `
      <span class="session-title">${escapeHtml(session.title)}</span>
      <span class="session-meta">${session.messages.length ? `${session.messages.length} 条消息` : "尚未提问"}</span>
    `;
    button.addEventListener("click", () => {
      state.activeSessionId = session.id;
      renderSessions();
      renderMessages();
    });
    list.appendChild(button);
  });
}

function renderMessages() {
  const session = getActiveSession();
  const messages = document.getElementById("messages");
  const emptyState = document.getElementById("emptyState");

  messages.innerHTML = "";
  if (!session || session.messages.length === 0) {
    messages.classList.add("empty");
    emptyState.classList.remove("hidden");
    document.getElementById("chatTitle").textContent = session?.title || "新对话";
    return;
  }

  messages.classList.remove("empty");
  emptyState.classList.add("hidden");
  document.getElementById("chatTitle").textContent = session.title;

  session.messages.forEach((message) => {
    const row = document.createElement("article");
    row.className = `message-row ${message.role}`;
    row.innerHTML = `
      <div class="message">
        <div class="message-role">${message.role === "user" ? "User" : "Assistant"}</div>
        ${
          message.role === "assistant" && message.strategy
            ? `<div class="message-meta">${escapeHtml(getStrategyLabel(message.strategy))}</div>`
            : ""
        }
        <div class="message-bubble">
          <div class="message-body">${escapeHtml(message.content || "")}</div>
        </div>
        ${
          message.role === "assistant"
            ? renderRagDiagnostics(message)
            : ""
        }
        ${
          message.role === "assistant" && (message.recommendedVisualizations || []).length
            ? `<div class="visualization-list">${renderVisualizationCards(message.recommendedVisualizations)}</div>`
            : ""
        }
      </div>
    `;
    messages.appendChild(row);
  });

  messages.scrollTop = messages.scrollHeight;
}

function renderVisualizationCards(items) {
  return items
    .map(
      (item) => `
        <details class="inline-viz-card">
          <summary class="inline-viz-summary">
            <span class="inline-viz-kicker">交互式可视化</span>
            <span class="inline-viz-title">${escapeHtml(item.title)}</span>
            <span class="inline-viz-copy">${escapeHtml(item.description || "")}</span>
            ${renderA2uiMetadata(item)}
          </summary>
          <div class="inline-viz-actions">
            <a href="${escapeHtml(resolveGalleryUrl(item))}" target="_blank" rel="noreferrer" class="inline-viz-link">单独打开</a>
          </div>
          <div class="inline-viz-frame-wrap">
            <iframe
              src="${escapeHtml(resolveEmbedUrl(item))}"
              title="${escapeHtml(item.title)}"
              loading="lazy"
              class="inline-viz-frame"
            ></iframe>
          </div>
        </details>
      `
    )
    .join("");
}

function renderA2uiMetadata(item) {
  const instruction = item.a2uiInstruction || item.a2ui || {};
  const componentId = instruction.componentId || item.componentId || "";
  const intentType = instruction.intentType || item.intentType || "";
  if (!componentId && !intentType) {
    return "";
  }
  return `
    <span class="inline-viz-a2ui">
      ${componentId ? `<code>${escapeHtml(componentId)}</code>` : ""}
      ${intentType ? `<span>${escapeHtml(intentType)}</span>` : ""}
    </span>
  `;
}

function renderRagDiagnostics(message) {
  const citations = Array.isArray(message.citations) ? message.citations : [];
  const contexts = Array.isArray(message.contexts) ? message.contexts : [];
  const hasDiagnostics = citations.length || contexts.length || message.latencyMs || message.tokenUsage;

  if (!hasDiagnostics) {
    return "";
  }

  return `
    <details class="rag-diagnostics">
      <summary class="rag-diagnostics-summary">
        <span class="rag-diagnostics-title">RAG 对比详情</span>
        <span class="rag-diagnostics-meta">${buildDiagnosticsMeta(message, citations, contexts)}</span>
      </summary>
      <div class="rag-diagnostics-grid">
        <section class="rag-panel">
          <h4>引用片段</h4>
          ${
            citations.length
              ? citations.map((item) => renderCitationItem(item)).join("")
              : `<p class="rag-empty">当前回答没有返回显式引用。</p>`
          }
        </section>
        <section class="rag-panel">
          <h4>检索上下文</h4>
          ${
            contexts.length
              ? contexts.map((item, index) => renderContextItem(item, index)).join("")
              : `<p class="rag-empty">当前回答没有返回检索上下文。</p>`
          }
        </section>
      </div>
    </details>
  `;
}

function buildDiagnosticsMeta(message, citations, contexts) {
  const parts = [];
  if (contexts.length) {
    const topScore = contexts.reduce((best, item) => {
      const score = Number(item.score);
      return Number.isFinite(score) ? Math.max(best, score) : best;
    }, 0);
    parts.push(`top score ${formatScore(topScore)}`);
  }
  if (citations.length) {
    parts.push(`${citations.length} 条引用`);
  }
  if (message.latencyMs) {
    parts.push(`${Math.round(Number(message.latencyMs))} ms`);
  }
  return parts.join(" · ") || "展开查看";
}

function renderCitationItem(item) {
  return `
    <article class="rag-item">
      <div class="rag-item-head">
        <strong>${escapeHtml(item.title || "未命名来源")}</strong>
        ${
          item.url
            ? `<a href="${escapeHtml(item.url)}" target="_blank" rel="noreferrer" class="rag-item-link">打开来源</a>`
            : ""
        }
      </div>
      <p class="rag-item-copy">${escapeHtml(item.snippet || "暂无片段摘要。")}</p>
    </article>
  `;
}

function renderContextItem(item, index) {
  const source = item.source || item.metadata?.source || `上下文 ${index + 1}`;
  const page = item.page ?? item.metadata?.page;
  return `
    <article class="rag-item">
      <div class="rag-item-head">
        <strong>${escapeHtml(source)}</strong>
        <span class="rag-score">命中得分 ${formatScore(item.score)}</span>
      </div>
      <div class="rag-context-meta">
        ${page !== undefined && page !== null ? `<span>页码 ${escapeHtml(String(page))}</span>` : ""}
      </div>
      <p class="rag-item-copy">${escapeHtml(item.content || "暂无上下文内容。")}</p>
    </article>
  `;
}

function formatScore(value) {
  const score = Number(value);
  if (!Number.isFinite(score)) {
    return "-";
  }
  return score.toFixed(3);
}

async function loadConfig() {
  const response = await fetch(apiUrl("/api/config"));
  const config = await response.json();
  document.getElementById("knowledgeEngineStatus").textContent = config.ragBaseUrl ? "已连接" : "未连接";

  const strategyResponse = await fetch(apiUrl("/api/rag/strategies"));
  const strategyData = await strategyResponse.json();
  state.ragStrategies = strategyData.items || [];
  if (!strategyData.ok && strategyData.error) {
    document.getElementById("strategySummary").textContent = strategyData.error;
  }
  state.selectedVariant =
    state.ragStrategies.find((variant) => variant.id === (config.defaultRagStrategy || "naive"))?.id ||
    state.ragStrategies[0]?.id ||
    null;

  const kbResponse = await fetch(apiUrl("/api/rag/kbs"));
  const kbData = await kbResponse.json();
  state.knowledgeBases = kbData.items || [];
  if (!kbData.ok && kbData.error) {
    setUploadStatus(kbData.error, true);
  }
  state.selectedKbId =
    state.knowledgeBases.find((kb) => kb.kb_id === (config.defaultKbId || ""))?.kb_id ||
    state.knowledgeBases[0]?.kb_id ||
    null;
  document.getElementById("knowledgeStatus").textContent = state.selectedKbId ? "Online" : "Ready";
  renderStrategyOptions();
  renderKnowledgeBaseOptions();
}

async function loadVisualizations() {
  await fetch(apiUrl("/api/visualizations"));
}

async function refreshKnowledgeBases() {
  const response = await fetch(apiUrl("/api/rag/kbs"));
  const data = await response.json();
  state.knowledgeBases = data.items || [];
  if (state.selectedKbId && !state.knowledgeBases.some((kb) => kb.kb_id === state.selectedKbId)) {
    state.selectedKbId = state.knowledgeBases[0]?.kb_id || null;
  }
  renderKnowledgeBaseOptions();
}

async function checkHealth() {
  const response = await fetch(apiUrl("/api/health"));
  const health = await response.json();
  document.getElementById("healthBadge").textContent = health.ok ? "Online" : "Offline";
}

function initializeTheme() {
  const savedTheme = window.localStorage.getItem("universe-theme");
  if (savedTheme === "day" || savedTheme === "night") {
    state.theme = savedTheme;
  } else {
    const hour = new Date().getHours();
    state.theme = hour >= 19 || hour < 6 ? "night" : "day";
  }
  applyTheme(state.theme);
}

function bindThemeSwitch() {
  document.getElementById("dayThemeButton").addEventListener("click", () => {
    state.theme = "day";
    applyTheme(state.theme);
  });
  document.getElementById("nightThemeButton").addEventListener("click", () => {
    state.theme = "night";
    applyTheme(state.theme);
  });
}

function applyTheme(theme) {
  document.body.dataset.theme = theme;
  window.localStorage.setItem("universe-theme", theme);
  document.getElementById("dayThemeButton").classList.toggle("is-active", theme === "day");
  document.getElementById("nightThemeButton").classList.toggle("is-active", theme === "night");
}

function renderKnowledgeBaseOptions() {
  const select = document.getElementById("kbSelect");
  const kbInput = document.getElementById("kbIdInput");
  select.innerHTML = "";

  const placeholder = document.createElement("option");
  placeholder.value = "";
  placeholder.textContent = state.knowledgeBases.length ? "选择知识库" : "暂无知识库";
  select.appendChild(placeholder);

  state.knowledgeBases.forEach((kb) => {
    const option = document.createElement("option");
    option.value = kb.kb_id;
    option.textContent = `${kb.kb_id} (${kb.doc_count ?? 0})`;
    option.selected = kb.kb_id === state.selectedKbId;
    select.appendChild(option);
  });

  if (state.selectedKbId) {
    kbInput.value = state.selectedKbId;
    select.value = state.selectedKbId;
  }
  document.getElementById("kbCount").textContent = String(state.knowledgeBases.length);
}

function renderStrategyOptions() {
  const select = document.getElementById("strategySelect");
  const summary = document.getElementById("strategySummary");
  const activeLabel = document.getElementById("activeStrategyLabel");
  const activeWorkflow = document.getElementById("activeStrategyWorkflow");

  select.innerHTML = "";
  state.ragStrategies.forEach((strategy) => {
    const option = document.createElement("option");
    option.value = strategy.id;
    option.textContent = strategy.label || strategy.id;
    option.selected = strategy.id === state.selectedVariant;
    select.appendChild(option);
  });

  const current =
    state.ragStrategies.find((strategy) => strategy.id === state.selectedVariant) ||
    state.ragStrategies[0] ||
    null;

  if (current) {
    state.selectedVariant = current.id;
    select.value = current.id;
    summary.textContent = current.summary || "当前方案暂无说明。";
    activeLabel.textContent = current.label || current.id;
    activeWorkflow.textContent = `workflow: ${current.workflow || "-"}`;
  } else {
    summary.textContent = "当前没有可用的 RAG 方案。";
    activeLabel.textContent = "未选择";
    activeWorkflow.textContent = "workflow: -";
  }

  document.getElementById("strategyCount").textContent = String(state.ragStrategies.length);
}

function getStrategyLabel(strategyId) {
  return (
    state.ragStrategies.find((strategy) => strategy.id === strategyId)?.label ||
    strategyId ||
    "RAG"
  );
}

function autoResizeTextarea() {
  const textarea = document.getElementById("questionInput");
  textarea.style.height = "auto";
  textarea.style.height = `${Math.min(textarea.scrollHeight, 180)}px`;
}

function buildVisualizationGalleryUrl(pageId) {
  return `./interactive-visualizations/index.html?page=${encodeURIComponent(pageId)}`;
}

function buildVisualizationEmbedUrl(pageId) {
  return `./interactive-visualizations/index.html?page=${encodeURIComponent(pageId)}&embed=1`;
}

function resolveGalleryUrl(item) {
  return item.galleryUrl || buildVisualizationGalleryUrl(item.pageId);
}

function resolveEmbedUrl(item) {
  return item.embedUrl || buildVisualizationEmbedUrl(item.pageId);
}

function setRequestState(text) {
  document.getElementById("requestState").textContent = text;
}

function setUploadStatus(text, isError) {
  const node = document.getElementById("uploadStatus");
  node.textContent = text;
  node.style.color = isError ? "#dc2626" : "";
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

initialize();
