const legacyPages = [
  {
    id: "modern-3d-solar",
    badge: "现代天文学",
    title: "3D 太阳系模拟",
    summary: "来自现代天文学模块的 Three.js 太阳系页面，支持轨道观察与点击查看天体信息。",
    src: "./legacy/modern-3d/index.html",
    source: "AlVisualization / astronomy / frontend",
    category: "Three.js 实时 3D",
    stack: "Three.js + OrbitControls + Canvas",
    notes: [
      "拖动页面内鼠标可旋转视角，滚轮可缩放。",
      "点击行星会弹出基础天体信息。",
      "这是之前已经做好的独立前端页，现已接入 Epic F 展厅。",
    ],
  },
  {
    id: "modern-toolkit",
    badge: "现代天文学",
    title: "天文学可视化工具集首页",
    summary: "现代天文学参考项目中的工具集入口页，可用于验证页面导航风格与卡片化前端呈现。",
    src: "./legacy/modern-original/index.html",
    source: "AlVisualization / astronomy / original",
    category: "工具集入口",
    stack: "HTML + CSS + 本地脚本组件",
    notes: [
      "这是历史实现中的总入口页，适合先看信息架构与视觉风格。",
      "可以继续点进内部页面做更细的交互测试。",
      "搜索框和卡片动效都保留了原有实现。",
    ],
  },
  {
    id: "modern-moon-phase",
    badge: "现代天文学",
    title: "地月月相与月食演示",
    summary: "基于 Skyfield 与 Plotly 的地月系统联动页面，左侧展示地月绕日关系，右侧同步展示月相变化。",
    src: "./legacy/generated/moon-eclipse-slider.html",
    source: "AlVisualization / astronomy / sun_earth_moon_phase_slider.v6",
    category: "月相与地月系统联动",
    stack: "Python + Skyfield + Plotly + 纹理月相渲染",
    notes: [
      "左侧是太阳、地球、月球的空间关系，右侧同步显示月相圆盘。",
      "支持播放、暂停、日期滑块与年份切换。",
      "当前月食相关推荐已替换为这份 Plotly 实现。",
    ],
  },
  {
    id: "kepler-third-law",
    badge: "现代天文学",
    title: "开普勒第三定律实验台",
    summary: "通过半长轴滑块、轨道对比和 T²-a³ 曲线直观理解开普勒第三定律。",
    src: "./legacy/generated/kepler-third-law.html",
    source: "UniverseModel / generated / kepler-third-law",
    category: "概念关系实验台",
    stack: "HTML + Canvas + SVG",
    notes: [
      "拖动半长轴即可看到轨道周期如何按幂律增长。",
      "左侧轨道视图强调直观空间感，右侧关系曲线强调公式关系。",
      "适合问答中内嵌，用于解释开普勒第三定律。",
    ],
  },
  {
    id: "modern-annual-motion",
    badge: "现代天文学",
    title: "太阳周年视运动轨迹",
    summary: "已实现的周年视运动页面，包含轨迹画布与 3D 天球辅助视图。",
    src: "./legacy/modern-original/planetary_annual_motion.html",
    source: "AlVisualization / astronomy / original",
    category: "轨迹可视化",
    stack: "Canvas + 轨迹算法 + 嵌入式 3D 视图",
    notes: [
      "可切换年份与时刻，观察太阳轨迹变化。",
      "原页面自带 3D 天球容器，适合检验复合页面的承载能力。",
      "这是 Epic F 后续做统一容器时的重要参考页面。",
    ],
  },
  {
    id: "solar-system-compare-streamlit",
    badge: "现代天文学",
    title: "🪐 太阳系行星运动对照",
    summary: "基于本地 Streamlit 的行星位置对照页，支持 VSOP、DE440 与藏历历算联动查看。",
    src: "http://127.0.0.1:8503",
    source: "行星运动模型 / solar_system_app.py",
    category: "Streamlit 对照工作台",
    stack: "Python + Streamlit + Plotly + DE440 + PyMeeus",
    notes: [
      "这是当前项目里最新的行星运动对照页，可切换 2D/3D 视图。",
      "页面包含 VSOP / DE440 对照、藏历日期换算和五要素展示。",
      "如果预览为空，先确认本地 8503 端口的 Streamlit 服务仍在运行。",
    ],
  },
  {
    id: "tibetan-solar-system",
    badge: "藏历天文学",
    title: "藏历项目太阳系开场页",
    summary: "从藏历星图项目接入的太阳系动态页，保留其原有视觉风格，用于前端展示联调。",
    src: "./legacy/tibetan-solar-system.html",
    source: "藏历星图 APP / 0313 / templates",
    category: "风格化开场页",
    stack: "Canvas 轨道动画 + 图像素材",
    notes: [
      "这里主要验证藏历项目既有视觉语言能否纳入 Epic F 展示层。",
      "原模板中的自动跳转已移除，便于持续预览。",
      "页面强调氛围感和科普导览式呈现。",
    ],
  },
  {
    id: "tibetan-zodiac",
    badge: "藏历天文学",
    title: "黄道十二宫交互页",
    summary: "来自藏历项目的 Three.js 黄道十二宫页面，可测试日期选择、3D 视图和信息叠层。",
    src: "./legacy/tibetan-zodiac.html",
    source: "藏历星图 APP / 0313 / templates",
    category: "Three.js 天球主题页",
    stack: "Three.js + CSS2DRenderer + 日期交互",
    notes: [
      "页面右上角日期控件可以直接驱动视图变化。",
      "保留了原项目中的深色紫调视觉风格。",
      "适合对比现代天文学页面与藏历页面的风格差异。",
    ],
  },
];

const state = {
  activePageId: legacyPages[0].id,
  embedMode: false,
};

function initialize() {
  const params = new URLSearchParams(window.location.search);
  state.embedMode = params.get("embed") === "1";
  if (state.embedMode) {
    document.body.classList.add("embed-mode");
  }

  document.getElementById("pageCount").textContent = String(legacyPages.length);
  buildPageRail();
  const pageId = params.get("page");
  if (pageId && legacyPages.some((page) => page.id === pageId)) {
    state.activePageId = pageId;
  }
  setPage(state.activePageId);
  bindEvents();
}

function buildPageRail() {
  const rail = document.getElementById("pageRail");
  rail.innerHTML = "";
  legacyPages.forEach((page) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "page-button";
    button.dataset.pageId = page.id;
    button.innerHTML = `
      <span class="page-kicker">${page.badge}</span>
      <span class="page-name">${page.title}</span>
      <span class="page-meta">${page.summary}</span>
    `;
    button.addEventListener("click", () => setPage(page.id));
    rail.appendChild(button);
  });
}

function setPage(pageId) {
  const page = legacyPages.find((item) => item.id === pageId);
  if (!page) {
    return;
  }
  state.activePageId = pageId;
  document.getElementById("pageTitle").textContent = page.title;
  document.getElementById("pageSummary").textContent = page.summary;
  document.getElementById("pageSource").textContent = page.source;
  document.getElementById("pageCategory").textContent = page.category;
  document.getElementById("pageStack").textContent = page.stack;
  document.getElementById("previewFrame").src = page.src;
  document.getElementById("openPageButton").href = page.src;
  renderNotes(page.notes);
  if (!state.embedMode) {
    syncActiveState();
    updateDeepLinkSummary();
  }
  document.title = state.embedMode ? `${page.title} · 交互式可视化` : "Epic F · 已实现交互式可视化页面展厅";
}

function renderNotes(notes) {
  const list = document.getElementById("pageNotes");
  list.innerHTML = "";
  notes.forEach((note) => {
    const li = document.createElement("li");
    li.textContent = note;
    list.appendChild(li);
  });
}

function syncActiveState() {
  document.querySelectorAll(".page-button").forEach((button) => {
    button.classList.toggle("active", button.dataset.pageId === state.activePageId);
  });
}

function bindEvents() {
  document.getElementById("reloadFrameButton").addEventListener("click", () => {
    const iframe = document.getElementById("previewFrame");
    iframe.src = iframe.src;
  });

  document.getElementById("copyLinkButton").addEventListener("click", async () => {
    const url = buildDeepLink();
    try {
      await navigator.clipboard.writeText(url);
      document.getElementById("deepLinkSummary").textContent = `已复制：${url}`;
    } catch (error) {
      document.getElementById("deepLinkSummary").textContent = `复制失败，可手动使用：${url}`;
    }
  });
}

function updateDeepLinkSummary() {
  const url = buildDeepLink();
  document.getElementById("deepLinkSummary").textContent =
    `可直接用 page=${state.activePageId} 打开当前展示页。当前链接：${url}`;
  window.history.replaceState({}, "", url);
}

function buildDeepLink() {
  const params = new URLSearchParams();
  params.set("page", state.activePageId);
  return `${window.location.pathname}?${params.toString()}`;
}

initialize();
