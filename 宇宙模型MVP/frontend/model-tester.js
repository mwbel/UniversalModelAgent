const API_BASE =
  window.location.protocol === "file:" || window.location.port !== "8787"
    ? "http://127.0.0.1:8787"
    : "";

const DEFAULT_SYSTEM_PROMPT = "你是一个严谨、直接的中文助手。回答时优先给出结论，再补充必要解释。";
const MAX_ATTACHMENT_BYTES = 4 * 1024 * 1024;
const PROMPT_PRESETS = [
  {
    id: "rigorous",
    label: "严谨助手",
    prompt: DEFAULT_SYSTEM_PROMPT,
  },
  {
    id: "researcher",
    label: "研究者",
    prompt: "你是一位研究者型中文助手。先给结论，再给依据、假设、边界条件和可验证线索；不确定时明确说出不确定点。",
  },
  {
    id: "explainer",
    label: "通俗讲解者",
    prompt: "你是一位通俗讲解者。用清楚、平实、少术语的中文解释问题，优先举直观例子，让没有背景的人也能看懂。",
  },
  {
    id: "editor",
    label: "结构整理者",
    prompt: "你是一位结构整理者。回答时先提炼要点，再按清晰结构展开，适合整理资料、改写内容和生成条理分明的结果。",
  },
];
const MODEL_HINTS = {
  vision_verified: {
    badge: "图像已验证",
    detail: "已验证可接收图片输入，适合 OCR、图表和截图类任务。",
    compareRecommended: true,
    singleRecommended: true,
  },
  vision_possible: {
    badge: "图像未稳定",
    detail: "可能支持图片，但当前服务下结果不稳定，建议作为补充对比。",
    compareRecommended: false,
    singleRecommended: false,
  },
  text_only: {
    badge: "文本优先",
    detail: "更适合纯文本对话，图片任务下可能忽略图像内容。",
    compareRecommended: false,
    singleRecommended: false,
  },
  embedding: {
    badge: "非对话",
    detail: "这是 embedding 类模型，不适合聊天或图片理解测试。",
    compareRecommended: false,
    singleRecommended: false,
  },
};

const state = {
  messages: [],
  defaultModels: [],
  attachments: [],
  activeModel: "",
  selectedModels: [],
  activePromptPresetId: "rigorous",
  imageSelectionAutoApplied: false,
  imageActiveModelAutoApplied: false,
  pending: false,
  hasBackendKey: false,
};

const els = {};

function apiUrl(path) {
  return `${API_BASE}${path}`;
}

function bindElements() {
  [
    "baseUrlInput",
    "apiKeyInput",
    "toggleKeyButton",
    "keyStatus",
    "modelSelect",
    "refreshModelsButton",
    "modelStatus",
    "modelChecklist",
    "modelChecklistHint",
    "selectAllModelsButton",
    "temperatureInput",
    "maxTokensInput",
    "modelsPathInput",
    "chatPathInput",
    "clearButton",
    "messages",
    "chatForm",
    "attachmentInput",
    "attachButton",
    "attachmentList",
    "messageInput",
    "sendButton",
    "compareButton",
    "requestBadge",
    "activeModelTitle",
    "latencyValue",
    "tokensValue",
    "finishValue",
    "pathValue",
    "promptPresetBar",
    "promptPresetStatus",
    "requestSettingsSummary",
    "systemPromptInput",
    "resetSystemButton",
    "rawResponse",
    "copyRawButton",
  ].forEach((id) => {
    els[id] = document.getElementById(id);
  });
}

async function initialize() {
  bindElements();
  bindEvents();
  restoreLocalState();
  renderPromptPresets();
  await loadConfig();
  updateRequestSettingsSummary();
  renderAttachments();
  renderMessages();
}

function bindEvents() {
  els.toggleKeyButton.addEventListener("click", () => {
    const shouldShow = els.apiKeyInput.type === "password";
    els.apiKeyInput.type = shouldShow ? "text" : "password";
    updateKeyVisibilityButton(shouldShow);
  });

  els.refreshModelsButton.addEventListener("click", () => refreshModels({ forceRemote: true }));
  els.selectAllModelsButton.addEventListener("click", handleSelectAllModels);

  els.modelSelect.addEventListener("change", () => {
    state.activeModel = els.modelSelect.value;
    state.imageActiveModelAutoApplied = false;
    localStorage.setItem("modelTester.model", state.activeModel);
    updateActiveModelTitle();
    if (hasImageAttachments(state.attachments) && !getModelHint(state.activeModel).singleRecommended) {
      setImageModelStatus();
      return;
    }
    setModelStatus(state.activeModel ? `当前模型：${state.activeModel}` : "未选择模型", false);
  });

  els.clearButton.addEventListener("click", () => {
    state.messages = [];
    state.attachments = [];
    resetMetrics();
    renderRaw({});
    renderAttachments();
    renderMessages();
    els.messageInput.focus();
  });

  els.resetSystemButton.addEventListener("click", () => {
    els.systemPromptInput.value = DEFAULT_SYSTEM_PROMPT;
    persistLocalState();
    updateRequestSettingsSummary();
  });

  els.copyRawButton.addEventListener("click", async () => {
    await navigator.clipboard.writeText(els.rawResponse.textContent || "{}");
    els.copyRawButton.textContent = "已复制";
    window.setTimeout(() => {
      els.copyRawButton.textContent = "复制";
    }, 1200);
  });

  els.messageInput.addEventListener("input", autoResizeComposer);
  els.attachButton.addEventListener("click", () => els.attachmentInput.click());
  els.attachmentInput.addEventListener("change", () => handleAttachmentFiles(els.attachmentInput.files));
  els.messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      els.chatForm.requestSubmit();
    }
  });

  els.chatForm.addEventListener("submit", handleSubmit);
  els.compareButton.addEventListener("click", handleCompareAll);

  [
    els.baseUrlInput,
    els.modelsPathInput,
    els.chatPathInput,
    els.temperatureInput,
    els.maxTokensInput,
  ].forEach((input) => {
    input.addEventListener("change", () => {
      persistLocalState();
      updateRequestSettingsSummary();
    });
  });

  els.systemPromptInput.addEventListener("input", () => {
    persistLocalState();
    syncPromptPresetState();
    updateRequestSettingsSummary();
  });

  els.apiKeyInput.addEventListener("input", () => {
    sessionStorage.setItem("modelTester.apiKey", els.apiKeyInput.value);
    updateKeyStatus();
  });
}

function restoreLocalState() {
  els.baseUrlInput.value = localStorage.getItem("modelTester.baseUrl") || "";
  els.modelsPathInput.value = localStorage.getItem("modelTester.modelsPath") || "/models";
  els.chatPathInput.value = localStorage.getItem("modelTester.chatPath") || "/chat/completions";
  els.temperatureInput.value = localStorage.getItem("modelTester.temperature") || "0.7";
  els.maxTokensInput.value = localStorage.getItem("modelTester.maxTokens") || "";
  els.apiKeyInput.value = sessionStorage.getItem("modelTester.apiKey") || "";
  els.systemPromptInput.value = localStorage.getItem("modelTester.systemPrompt") || DEFAULT_SYSTEM_PROMPT;
  syncPromptPresetState();
  updateKeyVisibilityButton(els.apiKeyInput.type === "text");
}

function persistLocalState() {
  localStorage.setItem("modelTester.baseUrl", els.baseUrlInput.value.trim());
  localStorage.setItem("modelTester.modelsPath", els.modelsPathInput.value.trim());
  localStorage.setItem("modelTester.chatPath", els.chatPathInput.value.trim());
  localStorage.setItem("modelTester.temperature", els.temperatureInput.value);
  localStorage.setItem("modelTester.maxTokens", els.maxTokensInput.value);
  localStorage.setItem("modelTester.systemPrompt", els.systemPromptInput.value);
}

async function loadConfig() {
  try {
    const response = await fetch(apiUrl("/api/model-tester/config"));
    const config = await response.json();
    if (!els.baseUrlInput.value && config.baseUrl) {
      els.baseUrlInput.value = config.baseUrl;
    }
    if (config.baseUrl && els.baseUrlInput.value.trim() === config.baseUrl && config.modelsPath) {
      els.modelsPathInput.value = config.modelsPath;
    }
    if (config.baseUrl && els.baseUrlInput.value.trim() === config.baseUrl && config.chatPath) {
      els.chatPathInput.value = config.chatPath;
    }
    state.defaultModels = Array.isArray(config.defaultModels) ? config.defaultModels : [];
    state.hasBackendKey = Boolean(config.hasApiKey);
    updateKeyStatus();
    renderModelOptions(state.defaultModels);
    await refreshModels({ forceRemote: Boolean(els.baseUrlInput.value.trim()) });
  } catch (error) {
    setModelStatus(`配置加载失败：${error.message}`, true);
    renderModelOptions(state.defaultModels);
  }
}

async function refreshModels({ forceRemote = false } = {}) {
  const baseUrl = els.baseUrlInput.value.trim();
  if (!forceRemote && !baseUrl) {
    renderModelOptions(state.defaultModels);
    setModelStatus("使用本地默认模型列表", false);
    return;
  }

  setModelStatus("正在刷新模型列表...", false);
  els.refreshModelsButton.disabled = true;
  persistLocalState();

  try {
    const response = await fetch(apiUrl("/api/model-tester/models"), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(buildConnectionPayload()),
    });
    const data = await response.json();
    const fallbackItems = data.items || state.defaultModels;
    renderModelOptions(fallbackItems);
    if (data.ok) {
      setModelStatus(`模型来源：${data.source || "service"}`, false);
    } else if (fallbackItems.length) {
      setModelStatus("模型接口暂不可用，已使用内置模型列表。", false);
      console.warn("Model list fallback:", data.error || "模型列表请求失败");
    } else {
      setModelStatus(data.error || "模型列表请求失败", true);
    }
  } catch (error) {
    renderModelOptions(state.defaultModels);
    if (state.defaultModels.length) {
      setModelStatus("模型接口暂不可用，已使用内置模型列表。", false);
      console.warn("Model list fallback:", error);
    } else {
      setModelStatus(`刷新失败：${error.message}`, true);
    }
  } finally {
    els.refreshModelsButton.disabled = false;
  }
}

function renderModelOptions(models) {
  const previous = localStorage.getItem("modelTester.model") || state.activeModel;
  const items = Array.from(new Set((models || []).filter(Boolean)));
  els.modelSelect.innerHTML = "";

  if (!items.length) {
    const option = document.createElement("option");
    option.value = "";
    option.textContent = "暂无模型";
    els.modelSelect.append(option);
    state.activeModel = "";
    updateActiveModelTitle();
    return;
  }

  items.forEach((model) => {
    const option = document.createElement("option");
    option.value = model;
    option.textContent = model;
    els.modelSelect.append(option);
  });

  state.activeModel = items.includes(previous) ? previous : items[0];
  els.modelSelect.value = state.activeModel;
  state.selectedModels = items.filter((model) => state.selectedModels.includes(model));
  if (!state.selectedModels.length) {
    state.selectedModels = [...items];
  }
  syncModelSelectionStrategy(items);
  renderModelChecklist(items);
  updateActiveModelTitle();
  if (!els.modelStatus.classList.contains("is-error")) {
    setModelStatus(`当前模型：${state.activeModel}`, false);
  }
}

function buildConnectionPayload() {
  return {
    baseUrl: els.baseUrlInput.value.trim(),
    apiKey: els.apiKeyInput.value.trim(),
    modelsPath: els.modelsPathInput.value.trim() || "/models",
    chatPath: els.chatPathInput.value.trim() || "/chat/completions",
  };
}

function getSelectedModels() {
  return state.selectedModels.filter(Boolean);
}

function getAllModels() {
  return Array.from(els.modelSelect.options)
    .map((option) => option.value)
    .filter(Boolean);
}

function hasImageAttachments(attachments) {
  return attachments.some((item) => item.kind === "image");
}

function getModelHintType(model) {
  const lowered = String(model || "").toLowerCase();
  if (!lowered) {
    return "text_only";
  }
  if (lowered.includes("medgemma")) {
    return "vision_verified";
  }
  if (
    lowered.includes("vl") ||
    lowered.includes("vision") ||
    lowered.includes("qwen-vl") ||
    lowered.includes("llava") ||
    lowered.includes("minicpm-v")
  ) {
    return "vision_verified";
  }
  if (lowered.includes("embed")) {
    return "embedding";
  }
  if (lowered.includes("gemma4") || lowered.includes("qwen3.6")) {
    return "vision_possible";
  }
  return "text_only";
}

function getModelHint(model) {
  return MODEL_HINTS[getModelHintType(model)] || MODEL_HINTS.text_only;
}

function getRecommendedImageModels(models) {
  return (models || []).filter((model) => getModelHint(model).compareRecommended);
}

function syncModelSelectionStrategy(models = getAllModels()) {
  const hasImages = hasImageAttachments(state.attachments);
  if (!hasImages) {
    state.imageSelectionAutoApplied = false;
    state.imageActiveModelAutoApplied = false;
    updateModelChecklistHint(models);
    return;
  }

  const recommended = getRecommendedImageModels(models);
  const currentSelection = getSelectedModels();
  const shouldAutoApply =
    !state.imageSelectionAutoApplied &&
    recommended.length &&
    (!currentSelection.length || currentSelection.length === models.length);

  if (shouldAutoApply) {
    state.selectedModels = [...recommended];
    state.imageSelectionAutoApplied = true;
  }
  if (recommended.length && !getModelHint(state.activeModel).singleRecommended) {
    state.activeModel = recommended[0];
    state.imageActiveModelAutoApplied = true;
    els.modelSelect.value = state.activeModel;
    localStorage.setItem("modelTester.model", state.activeModel);
    updateActiveModelTitle();
    setModelStatus(`检测到图片，已切换到更适合图片任务的模型：${state.activeModel}`, false);
  }
  updateModelChecklistHint(models);
}

function renderModelChecklist(models) {
  els.modelChecklist.innerHTML = "";
  models.forEach((model) => {
    const label = document.createElement("label");
    label.className = "model-check-item";

    const input = document.createElement("input");
    input.type = "checkbox";
    input.checked = state.selectedModels.includes(model);
    input.addEventListener("change", () => {
      if (input.checked) {
        if (!state.selectedModels.includes(model)) {
          state.selectedModels.push(model);
        }
      } else {
        state.selectedModels = state.selectedModels.filter((item) => item !== model);
      }
    });

    const content = document.createElement("div");
    content.className = "model-check-content";

    const titleRow = document.createElement("div");
    titleRow.className = "model-check-title";

    const text = document.createElement("span");
    text.textContent = model;

    const hint = document.createElement("span");
    hint.className = `model-hint-badge is-${getModelHintType(model).replace(/_/g, "-")}`;
    hint.textContent = getModelHint(model).badge;

    const detail = document.createElement("span");
    detail.className = "model-check-detail";
    detail.textContent = getModelHint(model).detail;

    titleRow.append(text, hint);
    content.append(titleRow, detail);
    label.append(input, content);
    els.modelChecklist.append(label);
  });
  updateModelChecklistHint(models);
}

function handleSelectAllModels() {
  state.selectedModels = getAllModels();
  state.imageSelectionAutoApplied = false;
  renderModelChecklist(getAllModels());
}

function updateModelChecklistHint(models = getAllModels()) {
  const hasImages = hasImageAttachments(state.attachments);
  if (!hasImages) {
    els.modelChecklistHint.textContent = "默认可多选，用于横向对比。";
    els.modelChecklistHint.className = "field-note";
    return;
  }

  const recommended = getRecommendedImageModels(models);
  if (recommended.length) {
    const autoText = state.imageSelectionAutoApplied ? "已优先勾选更适合图片任务的模型。" : "建议优先勾选更适合图片任务的模型。";
    els.modelChecklistHint.textContent = `${autoText} 当前推荐：${recommended.join("、")}。`;
    els.modelChecklistHint.className = "field-note is-ok";
    return;
  }

  els.modelChecklistHint.textContent = "检测到图片附件，但当前列表里没有已验证的视觉模型；结果可能忽略图片内容。";
  els.modelChecklistHint.className = "field-note";
}

function setImageModelStatus() {
  const recommended = getRecommendedImageModels(getAllModels());
  const recommendedText = recommended.length ? recommended.join("、") : "视觉模型";
  setModelStatus(`已上传图片，${state.activeModel} 可能无法稳定识别图像；推荐优先试 ${recommendedText}`, false);
}

function renderPromptPresets() {
  els.promptPresetBar.innerHTML = "";
  PROMPT_PRESETS.forEach((preset) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "preset-chip";
    button.dataset.presetId = preset.id;
    button.textContent = preset.label;
    button.addEventListener("click", () => {
      state.activePromptPresetId = preset.id;
      els.systemPromptInput.value = preset.prompt;
      persistLocalState();
      syncPromptPresetState();
      updateRequestSettingsSummary();
    });
    els.promptPresetBar.append(button);
  });
  syncPromptPresetState();
}

function syncPromptPresetState() {
  const currentPrompt = els.systemPromptInput.value.trim();
  const matchedPreset = PROMPT_PRESETS.find((preset) => preset.prompt === currentPrompt);
  state.activePromptPresetId = matchedPreset ? matchedPreset.id : "custom";
  els.promptPresetStatus.textContent = matchedPreset ? matchedPreset.label : "自定义";
  els.promptPresetBar.querySelectorAll(".preset-chip").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.presetId === state.activePromptPresetId);
  });
}

function buildAttachmentSummary(attachments) {
  if (!attachments.length) {
    return "";
  }
  return attachments
    .map((item) => `${item.name} (${item.kind}, ${formatBytes(item.size)})`)
    .join("；");
}

function buildUserContent(text, attachments) {
  const cleanText = text.trim();
  if (!attachments.length) {
    return cleanText;
  }

  const parts = [];
  if (cleanText) {
    parts.push({ type: "text", text: cleanText });
  }

  attachments.forEach((item) => {
    if (item.id && (item.kind === "image" || item.kind === "text" || item.kind === "metadata")) {
      parts.push({ type: "model_tester_attachment", attachment_id: item.id });
      return;
    }
    parts.push({
      type: "text",
      text: `\n\n[附件: ${item.name}]\n当前文件类型 ${item.type || "unknown"} 未内联，只提供文件名和大小 ${formatBytes(item.size)}。`,
    });
  });

  return parts;
}

function contentToDisplayText(content) {
  if (typeof content === "string") {
    return content;
  }
  if (!Array.isArray(content)) {
    return "";
  }
  const textParts = content
    .filter((item) => item.type === "text" && item.text)
    .map((item) => item.text.trim())
    .filter(Boolean);
  const imageCount = content.filter((item) => item.type === "image_url").length;
  if (imageCount) {
    textParts.push(`[${imageCount} 张图片]`);
  }
  return textParts.join("\n\n");
}

function buildChatMessages({ additionalUserMessage = null, includeHistory = true } = {}) {
  const systemPrompt = els.systemPromptInput.value.trim();
  const messages = systemPrompt ? [{ role: "system", content: systemPrompt }] : [];
  if (includeHistory) {
    state.messages.forEach((message) => {
      if (message.role === "user" || message.role === "assistant") {
        messages.push({
          role: message.role,
          content: message.apiContent || message.content,
        });
      }
    });
  }
  if (additionalUserMessage) {
    messages.push(additionalUserMessage);
  }
  return messages;
}

async function sendChatRequest(model, messages) {
  const response = await fetch(apiUrl("/api/model-tester/chat"), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      ...buildConnectionPayload(),
      model,
      messages,
      temperature: Number(els.temperatureInput.value || 0.7),
      maxTokens: els.maxTokensInput.value.trim(),
    }),
  });
  const data = await response.json();
  if (!data.ok) {
    throw new Error(data.error || "请求失败");
  }
  return data;
}

async function handleSubmit(event) {
  event.preventDefault();
  if (state.pending) {
    return;
  }

  const content = els.messageInput.value.trim();
  const attachments = [...state.attachments];
  if (!content && !attachments.length) {
    return;
  }

  persistLocalState();
  if (hasImageAttachments(attachments)) {
    const modelHint = getModelHint(state.activeModel);
    if (!modelHint.singleRecommended) {
      setImageModelStatus();
    }
  }
  const apiContent = buildUserContent(content, attachments);
  const requestMessages = buildChatMessages({
    additionalUserMessage: { role: "user", content: apiContent },
    includeHistory: true,
  });
  state.messages.push({
    role: "user",
    content: content || "附件测试",
    apiContent,
    attachments: attachments.map((item) => ({ name: item.name, kind: item.kind, size: item.size })),
    model: state.activeModel,
    createdAt: Date.now(),
  });
  els.messageInput.value = "";
  state.attachments = [];
  renderAttachments();
  autoResizeComposer();
  renderMessages();
  setRequestState("Running", "busy");

  state.pending = true;
  els.sendButton.disabled = true;
  els.compareButton.disabled = true;
  els.refreshModelsButton.disabled = true;

  try {
    const data = await sendChatRequest(state.activeModel, requestMessages);
    renderRaw(data.raw || data);

    state.messages.push({
      role: "assistant",
      content: data.answer || "(空响应)",
      reasoning: data.reasoning || "",
      model: data.model || state.activeModel,
      createdAt: Date.now(),
    });
    updateMetrics(data);
    setRequestState("Ready", "ok");
  } catch (error) {
    state.messages.push({
      role: "assistant",
      content: `请求失败：${error.message}`,
      model: state.activeModel,
      error: true,
      createdAt: Date.now(),
    });
    setRequestState("Error", "error");
  } finally {
    state.pending = false;
    els.sendButton.disabled = false;
    els.compareButton.disabled = false;
    els.refreshModelsButton.disabled = false;
    renderMessages();
  }
}

async function handleCompareAll() {
  if (state.pending) {
    return;
  }

  const content = els.messageInput.value.trim();
  const attachments = [...state.attachments];
  if (!content && !attachments.length) {
    els.messageInput.focus();
    return;
  }

  const models = getSelectedModels();
  if (!models.length) {
    setRequestState("No models", "error");
    return;
  }

  persistLocalState();
  if (hasImageAttachments(attachments) && !models.some((model) => getModelHint(model).compareRecommended)) {
    setModelStatus("已上传图片，但当前对比列表没有已验证视觉模型，结果可能忽略图片内容。", false);
  }
  const apiContent = buildUserContent(content, attachments);
  const requestMessages = buildChatMessages({
    additionalUserMessage: { role: "user", content: apiContent },
    includeHistory: false,
  });

  state.messages.push({
    role: "user",
    content: content || "附件测试",
    apiContent,
    attachments: attachments.map((item) => ({ name: item.name, kind: item.kind, size: item.size })),
    model: "compare",
    createdAt: Date.now(),
  });

  const comparison = {
    id: `comparison-${Date.now()}`,
    role: "comparison",
    content,
    createdAt: Date.now(),
    settings: {
      temperature: Number(els.temperatureInput.value || 0.7),
      maxTokens: els.maxTokensInput.value.trim() || "auto",
      systemPromptEnabled: Boolean(els.systemPromptInput.value.trim()),
      promptPresetLabel: els.promptPresetStatus.textContent || "自定义",
      attachments: buildAttachmentSummary(attachments),
    },
    results: models.map((model) => ({ model, status: "pending", answer: "", latencyMs: null, usage: null })),
  };
  state.messages.push(comparison);

  els.messageInput.value = "";
  state.attachments = [];
  renderAttachments();
  autoResizeComposer();
  renderMessages();

  state.pending = true;
  els.sendButton.disabled = true;
  els.compareButton.disabled = true;
  els.refreshModelsButton.disabled = true;
  const rawResults = [];

  try {
    for (let index = 0; index < comparison.results.length; index += 1) {
      const result = comparison.results[index];
      setRequestState(`${index + 1}/${comparison.results.length}`, "busy");
      renderMessages();
      try {
        const data = await sendChatRequest(result.model, requestMessages);
        result.status = "done";
        result.answer = data.answer || "(空响应)";
        result.reasoning = data.reasoning || "";
        result.latencyMs = data.latencyMs;
        result.usage = data.usage;
        result.finishReason = data.finishReason;
        result.path = data.path;
        rawResults.push({ model: result.model, ok: true, data: data.raw || data });
      } catch (error) {
        result.status = "error";
        result.answer = error.message;
        rawResults.push({ model: result.model, ok: false, error: error.message });
      }
    }
    updateComparisonMetrics(comparison.results);
    renderRaw({ comparison: rawResults });
    setRequestState("Ready", "ok");
  } finally {
    state.pending = false;
    els.sendButton.disabled = false;
    els.compareButton.disabled = false;
    els.refreshModelsButton.disabled = false;
    renderMessages();
  }
}

function renderMessages() {
  els.messages.innerHTML = "";

  if (!state.messages.length) {
    const empty = document.createElement("div");
    empty.className = "empty-message";
    empty.textContent = "选择模型后发送第一条测试消息。这里会保留上下文，方便比较不同模型的回答质量和速度。";
    els.messages.append(empty);
    return;
  }

  state.messages.forEach((message) => {
    if (message.role === "comparison") {
      els.messages.append(renderComparisonMessage(message));
      return;
    }

    const wrapper = document.createElement("article");
    wrapper.className = `message ${message.role}`;

    const meta = document.createElement("div");
    meta.className = "message-meta";
    meta.textContent = `${message.role === "user" ? "你" : message.model || "assistant"} · ${formatTime(message.createdAt)}`;

    const messageNodes = [meta];
    if (Array.isArray(message.attachments) && message.attachments.length) {
      messageNodes.push(renderAttachmentBadges(message.attachments));
    }

    if (message.reasoning) {
      const reasoning = document.createElement("div");
      reasoning.className = "reasoning";
      reasoning.textContent = message.reasoning;
      messageNodes.push(reasoning, bubble(message.content, message.error));
    } else {
      messageNodes.push(bubble(message.content, message.error));
    }
    wrapper.append(...messageNodes);

    els.messages.append(wrapper);
  });

  els.messages.scrollTop = els.messages.scrollHeight;
}

function renderComparisonMessage(message) {
  const wrapper = document.createElement("article");
  wrapper.className = "comparison-message";

  const header = document.createElement("div");
  header.className = "comparison-header";
  const title = document.createElement("div");
  title.innerHTML = `<strong>横向对比</strong><span>${formatTime(message.createdAt)}</span>`;
  const settings = document.createElement("div");
  settings.className = "comparison-settings";
  settings.textContent = `Temperature ${message.settings.temperature} · Max ${message.settings.maxTokens} · 角色 ${message.settings.promptPresetLabel} · System ${message.settings.systemPromptEnabled ? "on" : "off"}${message.settings.attachments ? ` · ${message.settings.attachments}` : ""}`;
  header.append(title, settings);

  const grid = document.createElement("div");
  grid.className = "comparison-grid";
  message.results.forEach((result) => {
    const card = document.createElement("section");
    card.className = `comparison-card ${result.status === "error" ? "is-error" : ""}`;

    const model = document.createElement("div");
    model.className = "comparison-model";
    model.textContent = result.model;

    const hint = document.createElement("div");
    hint.className = `comparison-hint is-${getModelHintType(result.model).replace(/_/g, "-")}`;
    hint.textContent = getModelHint(result.model).badge;

    const meta = document.createElement("div");
    meta.className = "comparison-meta";
    const totalTokens = result.usage?.total_tokens ?? result.usage?.totalTokens;
    if (result.status === "pending") {
      meta.textContent = "等待中";
    } else {
      meta.textContent = `${result.latencyMs ? `${result.latencyMs} ms` : "-"} · ${totalTokens ? `${totalTokens} tokens` : "tokens -"}`;
    }

    if (result.reasoning) {
      const reasoning = document.createElement("div");
      reasoning.className = "reasoning";
      reasoning.textContent = result.reasoning;
      card.append(model, hint, meta, reasoning, bubble(result.answer || "等待响应...", result.status === "error"));
    } else {
      card.append(model, hint, meta, bubble(result.answer || "等待响应...", result.status === "error"));
    }
    grid.append(card);
  });

  wrapper.append(header, grid);
  return wrapper;
}

function renderAttachmentBadges(attachments) {
  const list = document.createElement("div");
  list.className = "message-attachments";
  attachments.forEach((item) => {
    const badge = document.createElement("span");
    badge.textContent = `${item.name} · ${item.kind}`;
    list.append(badge);
  });
  return list;
}

function bubble(content, isError = false) {
  const node = document.createElement("div");
  node.className = "bubble";
  if (isError) {
    node.style.borderColor = "#ffc9b8";
    node.style.background = "#fff7f3";
  }
  node.textContent = content;
  return node;
}

async function handleAttachmentFiles(fileList) {
  const files = Array.from(fileList || []);
  els.attachmentInput.value = "";
  for (const file of files) {
    try {
      state.attachments.push(await readAttachment(file));
    } catch (error) {
      state.attachments.push({
        id: `attachment-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
        name: file.name,
        type: file.type,
        size: file.size,
        kind: "error",
        error: error.message,
      });
    }
  }
  syncModelSelectionStrategy();
  renderAttachments();
}

function readAttachment(file) {
  if (file.size > MAX_ATTACHMENT_BYTES) {
    return Promise.reject(new Error(`文件超过 ${formatBytes(MAX_ATTACHMENT_BYTES)}`));
  }

  if (file.type.startsWith("image/")) {
    return readFileAsDataUrl(file).then((dataUrl) =>
      uploadAttachmentToServer({
        name: file.name,
        mimeType: file.type,
        size: file.size,
        kind: "image",
        dataUrl,
      }).then((uploaded) => ({
        id: uploaded.id,
        name: uploaded.name,
        type: uploaded.mimeType,
        size: uploaded.size,
        kind: uploaded.kind,
      }))
    );
  }

  if (isTextLikeFile(file)) {
    return readFileAsText(file).then((text) =>
      uploadAttachmentToServer({
        name: file.name,
        mimeType: file.type,
        size: file.size,
        kind: "text",
        text,
      }).then((uploaded) => ({
        id: uploaded.id,
        name: uploaded.name,
        type: uploaded.mimeType,
        size: uploaded.size,
        kind: uploaded.kind,
      }))
    );
  }

  return uploadAttachmentToServer({
    name: file.name,
    mimeType: file.type,
    size: file.size,
    kind: "metadata",
  }).then((uploaded) => ({
    id: uploaded.id,
    name: uploaded.name,
    type: uploaded.mimeType,
    size: uploaded.size,
    kind: uploaded.kind,
  }));
}

function readFileAsDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(new Error("读取图片失败"));
    reader.readAsDataURL(file);
  });
}

function readFileAsText(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(new Error("读取文本失败"));
    reader.readAsText(file);
  });
}

function isTextLikeFile(file) {
  const name = file.name.toLowerCase();
  return (
    file.type.startsWith("text/") ||
    [".md", ".json", ".csv", ".tsv", ".txt", ".log", ".xml", ".yaml", ".yml"].some((suffix) => name.endsWith(suffix))
  );
}

async function uploadAttachmentToServer(payload) {
  const response = await fetch(apiUrl("/api/model-tester/upload"), {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  if (!data.ok) {
    throw new Error(data.error || "上传附件失败");
  }
  return data;
}

function renderAttachments() {
  els.attachmentList.innerHTML = "";
  if (!state.attachments.length) {
    els.attachmentList.hidden = true;
    return;
  }

  els.attachmentList.hidden = false;
  state.attachments.forEach((item) => {
    const chip = document.createElement("button");
    chip.className = `attachment-chip ${item.kind === "error" ? "is-error" : ""}`;
    chip.type = "button";
    chip.title = item.error ? `${item.name}: ${item.error}` : "点击移除附件";
    chip.textContent = `${item.name} · ${item.kind} · ${formatBytes(item.size)}`;
    chip.addEventListener("click", () => {
      state.attachments = state.attachments.filter((attachment) => attachment.id !== item.id);
      syncModelSelectionStrategy();
      renderAttachments();
    });
    els.attachmentList.append(chip);
  });
  updateModelChecklistHint();
}

function updateComparisonMetrics(results) {
  const completed = results.filter((item) => item.status === "done");
  const latencyTotal = completed.reduce((sum, item) => sum + (Number(item.latencyMs) || 0), 0);
  const tokenTotal = completed.reduce((sum, item) => {
    const usage = item.usage || {};
    return sum + Number(usage.total_tokens ?? usage.totalTokens ?? 0);
  }, 0);
  els.latencyValue.textContent = completed.length ? `${Math.round(latencyTotal / completed.length)} ms avg` : "-";
  els.tokensValue.textContent = tokenTotal ? String(tokenTotal) : "-";
  els.finishValue.textContent = `${completed.length}/${results.length}`;
  els.pathValue.textContent = "compare";
}

function updateMetrics(data) {
  els.latencyValue.textContent = data.latencyMs ? `${data.latencyMs} ms` : "-";
  const usage = data.usage || {};
  const total = usage.total_tokens ?? usage.totalTokens;
  els.tokensValue.textContent = total ? String(total) : "-";
  els.finishValue.textContent = data.finishReason || "-";
  els.pathValue.textContent = data.path || "-";
}

function resetMetrics() {
  els.latencyValue.textContent = "-";
  els.tokensValue.textContent = "-";
  els.finishValue.textContent = "-";
  els.pathValue.textContent = "-";
}

function renderRaw(data) {
  els.rawResponse.textContent = JSON.stringify(data || {}, null, 2);
}

function setRequestState(label, stateName = "ok") {
  els.requestBadge.textContent = label;
  els.requestBadge.classList.toggle("is-busy", stateName === "busy");
  els.requestBadge.classList.toggle("is-error", stateName === "error");
}

function setModelStatus(message, isError) {
  els.modelStatus.textContent = message;
  els.modelStatus.classList.toggle("is-error", Boolean(isError));
  els.modelStatus.classList.toggle("is-ok", !isError);
}

function updateKeyStatus() {
  const hasInputKey = Boolean(els.apiKeyInput.value.trim());
  if (hasInputKey) {
    els.keyStatus.textContent = "使用页面临时 key";
    els.keyStatus.className = "field-note is-ok";
    return;
  }
  if (state.hasBackendKey) {
    els.keyStatus.textContent = "使用后端环境变量 key";
    els.keyStatus.className = "field-note is-ok";
    return;
  }
  els.keyStatus.textContent = "未输入 key";
  els.keyStatus.className = "field-note";
}

function updateKeyVisibilityButton(isVisible) {
  els.toggleKeyButton.classList.toggle("is-visible", isVisible);
  els.toggleKeyButton.title = isVisible ? "隐藏 API Key" : "显示 API Key";
  els.toggleKeyButton.setAttribute("aria-label", isVisible ? "隐藏 API Key" : "显示 API Key");
}

function updateActiveModelTitle() {
  els.activeModelTitle.textContent = state.activeModel || "选择模型后开始测试";
}

function autoResizeComposer() {
  els.messageInput.style.height = "auto";
  els.messageInput.style.height = `${Math.min(els.messageInput.scrollHeight, 180)}px`;
}

function updateRequestSettingsSummary() {
  const temperature = els.temperatureInput.value || "0.7";
  const maxTokens = els.maxTokensInput.value.trim() || "auto";
  const hasSystemPrompt = Boolean(els.systemPromptInput.value.trim());
  const roleLabel = els.promptPresetStatus.textContent || "自定义";
  els.requestSettingsSummary.textContent = `Temperature ${temperature} · Max ${maxTokens} · 角色 ${roleLabel} · System prompt ${hasSystemPrompt ? "已启用" : "关闭"}`;
}

function formatBytes(bytes) {
  const value = Number(bytes) || 0;
  if (value >= 1024 * 1024) {
    return `${(value / 1024 / 1024).toFixed(1)} MB`;
  }
  if (value >= 1024) {
    return `${Math.round(value / 1024)} KB`;
  }
  return `${value} B`;
}

function formatTime(timestamp) {
  if (!timestamp) {
    return "-";
  }
  return new Intl.DateTimeFormat("zh-CN", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(timestamp);
}

initialize();
