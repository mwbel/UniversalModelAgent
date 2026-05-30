const state = {
  history: [],
  ragStrategies: [],
  knowledgeBases: [],
  selectedVariant: null,
  selectedKbId: null,
  theme: "day",
};

async function initialize() {
  initializeTheme();
  bindThemeSwitch();
  bindExampleQuestions();
  bindForm();
  appendMessage("assistant", "系统已就绪。你可以先问一个天文学问题，或者直接打开右侧的可视化展厅。");
  await loadConfig();
  await loadVisualizations();
  await checkHealth();
}

function bindExampleQuestions() {
  document.querySelectorAll(".example-chip").forEach((button) => {
    button.addEventListener("click", () => {
      document.getElementById("questionInput").value = button.dataset.question || "";
      document.getElementById("questionInput").focus();
    });
  });
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

function bindForm() {
  document.getElementById("chatForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const input = document.getElementById("questionInput");
    const question = input.value.trim();
    if (!question) {
      return;
    }

    input.value = "";
    setRequestState("Thinking");
    appendMessage("user", question);

    const payload = {
      question,
      history: state.history,
      ragVariant: state.selectedVariant,
      kbId: state.selectedKbId,
    };

    state.history.push({ role: "user", content: question });

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      appendAssistantResult(data);
      state.history.push({ role: "assistant", content: data.answer || "" });
    } catch (error) {
      appendMessage("assistant", `请求失败：${error.message}`);
    } finally {
      setRequestState("Ready");
    }
  });
}

async function loadConfig() {
  const response = await fetch("/api/config");
  const config = await response.json();
  document.getElementById("mineruUrl").textContent = config.mineruBaseUrl || "-";
  document.getElementById("knowledgeEngineStatus").textContent = config.ragBaseUrl ? "已连接" : "未连接";

  state.ragStrategies = [];
  const strategyResponse = await fetch("/api/rag/strategies");
  const strategyData = await strategyResponse.json();
  state.ragStrategies = strategyData.items || [];
  state.selectedVariant =
    state.ragStrategies.find((variant) => variant.id === (config.defaultRagStrategy || "naive"))?.id ||
    state.ragStrategies[0]?.id ||
    null;

  const kbResponse = await fetch("/api/rag/kbs");
  const kbData = await kbResponse.json();
  state.knowledgeBases = kbData.items || [];
  state.selectedKbId =
    state.knowledgeBases.find((kb) => kb.kb_id === (config.defaultKbId || ""))?.kb_id ||
    state.knowledgeBases[0]?.kb_id ||
    null;
  document.getElementById("knowledgeStatus").textContent = state.selectedKbId ? "Online" : "Ready";
}

async function loadVisualizations() {
  const response = await fetch("/api/visualizations");
  const data = await response.json();
  renderVisualizations(data.items || []);
}

async function checkHealth() {
  const response = await fetch("/api/health");
  const health = await response.json();
  document.getElementById("healthBadge").textContent = health.ok ? "Online" : "Offline";
}

function appendMessage(role, text) {
  const messages = document.getElementById("messages");
  const article = document.createElement("article");
  article.className = `message ${role}`;
  article.innerHTML = `
    <div class="message-role">${role === "user" ? "User" : "Assistant"}</div>
    <div class="message-body"></div>
  `;
  article.querySelector(".message-body").textContent = text;
  messages.appendChild(article);
  messages.scrollTop = messages.scrollHeight;
}

function appendAssistantResult(data) {
  const messages = document.getElementById("messages");
  const article = document.createElement("article");
  article.className = "message assistant";

  const recommendationMarkup = (data.recommendedVisualizations || [])
    .map(
      (item) => `
        <div class="visualization-item">
          <a href="./interactive-visualizations/index.html?page=${encodeURIComponent(item.pageId)}" target="_blank" rel="noreferrer">
            ${escapeHtml(item.title)}
          </a>
          <p class="citation-snippet">${escapeHtml(item.description || "")}</p>
        </div>
      `
    )
    .join("");

  article.innerHTML = `
    <div class="message-role">Assistant</div>
    <div class="message-body">${escapeHtml(data.answer || "")}</div>
    ${recommendationMarkup ? `<div class="visualization-list">${recommendationMarkup}</div>` : ""}
  `;
  messages.appendChild(article);
  messages.scrollTop = messages.scrollHeight;
}

function renderVisualizations(items) {
  const container = document.getElementById("visualizationList");
  container.innerHTML = "";
  items.forEach((item) => {
    const node = document.createElement("div");
    node.className = "visualization-item";
    node.innerHTML = `
      <a href="./interactive-visualizations/index.html?page=${encodeURIComponent(item.pageId)}" target="_blank" rel="noreferrer">
        ${escapeHtml(item.title)}
      </a>
      <p class="citation-snippet">${escapeHtml(item.description || "")}</p>
    `;
    container.appendChild(node);
  });
}

function setRequestState(text) {
  document.getElementById("requestState").textContent = text;
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
