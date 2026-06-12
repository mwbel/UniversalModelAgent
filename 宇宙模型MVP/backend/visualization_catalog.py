from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Any


@dataclass(slots=True)
class VisualizationCapability:
    id: str
    title: str
    description: str
    page_id: str
    concepts: list[str]
    keywords: list[str]
    tags: list[str]
    a2ui_hint: str
    expresses: list[str]
    educational_use: str
    cannot_express: list[str]
    implementation_kind: str
    source_entry: str
    trigger_patterns: list[str]
    priority: int = 50
    plugin_id: str = "astronomy-core"
    component_id: str = ""
    intent_type: str = "concept_explanation"
    props_schema: dict[str, Any] = field(default_factory=dict)
    default_props: dict[str, Any] = field(default_factory=dict)
    interaction_events: list[str] = field(default_factory=list)
    feedback_contract: dict[str, Any] = field(default_factory=dict)

    def public_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["pageId"] = payload.pop("page_id")
        payload["sourceEntry"] = payload.pop("source_entry")
        payload["implementationKind"] = payload.pop("implementation_kind")
        payload["triggerPatterns"] = payload.pop("trigger_patterns")
        payload["pluginId"] = payload.pop("plugin_id")
        payload["componentId"] = payload.pop("component_id") or f"{self.plugin_id}.{self.id}"
        payload["intentType"] = payload.pop("intent_type")
        payload["propsSchema"] = payload.pop("props_schema")
        payload["defaultProps"] = payload.pop("default_props")
        payload["interactionEvents"] = payload.pop("interaction_events")
        payload["feedbackContract"] = payload.pop("feedback_contract")
        payload["a2ui"] = self.a2ui_instruction()
        return payload

    def a2ui_instruction(self) -> dict[str, Any]:
        component_id = self.component_id or f"{self.plugin_id}.{self.id}"
        return {
            "protocol": "a2ui-compatible",
            "surface": "chat.inline.learning-visualization",
            "pluginId": self.plugin_id,
            "componentId": component_id,
            "intentType": self.intent_type,
            "initialProps": self.default_props,
            "propsSchema": self.props_schema,
            "events": self.interaction_events,
            "feedbackContract": self.feedback_contract,
            "fallback": {
                "renderMode": "iframe",
                "pageId": self.page_id,
            },
        }


VISUALIZATION_CAPABILITIES: list[VisualizationCapability] = [
    VisualizationCapability(
        id="ecliptic-lunar-path",
        title="黄道与白道关系示意",
        description="展示黄道、白道、约 5.145 度夹角，以及升交点和降交点的空间关系。",
        page_id="ecliptic-lunar-path",
        concepts=["ecliptic_lunar_path"],
        keywords=[
            "黄道",
            "白道",
            "交点",
            "升交点",
            "降交点",
            "黄道和白道",
            "ecliptic",
            "lunar orbit",
        ],
        tags=["黄道", "白道", "升交点", "降交点", "交食条件"],
        a2ui_hint="当用户询问黄道、白道、交点或交食发生区域时优先调用，适合直接嵌入聊天侧栏进行说明。",
        expresses=[
            "黄道与白道并不重合，而是存在约 5.145 度夹角",
            "升交点与降交点是两条轨道的相交位置",
            "月球接近交点时更容易满足日食和月食的几何条件",
        ],
        educational_use="帮助用户把黄白二道的抽象描述转成可以直接观察和拖动的几何关系。",
        cannot_express=[
            "高精度真实星历时刻",
            "地月日三维空间中完整阴影锥尺寸",
        ],
        implementation_kind="native_a2ui_component",
        source_entry="frontend-react/src/astronomy-components/EclipticLunarPath.tsx",
        trigger_patterns=["黄道", "白道", "黄白交点", "升交点", "降交点", "ecliptic", "lunar orbit"],
        priority=99,
        component_id="astronomy-core.ecliptic-lunar-path",
        intent_type="spatial_geometry_explanation",
        props_schema={
            "inclinationDeg": {"type": "number", "minimum": 0, "maximum": 15},
            "moonPositionDeg": {"type": "number", "minimum": 0, "maximum": 360},
            "showNodes": {"type": "boolean"},
            "showLabels": {"type": "boolean"},
        },
        default_props={
            "inclinationDeg": 5.145,
            "moonPositionDeg": 35,
            "showNodes": True,
            "showLabels": True,
        },
        interaction_events=["moonPositionChanged", "labelVisibilityChanged"],
        feedback_contract={
            "eventPayload": "component returns moon position and whether nodes or labels are visible",
            "agentUse": "connect the current moon position to why eclipses cluster near the nodes",
        },
    ),
    VisualizationCapability(
        id="eclipse-demo",
        title="地月月相与月食演示",
        description="通过太阳、地球、月球相对位置和月相联动理解月食相关现象。",
        page_id="modern-moon-phase",
        concepts=["eclipse_geometry"],
        keywords=["日食", "月食", "月相", "eclipse", "moon phase", "lunar eclipse", "solar eclipse"],
        tags=["月食", "月相", "地月系统", "遮挡几何", "影锥"],
        a2ui_hint=(
            "当用户询问月食、日食、月相变化时优先调用。组件内部已自带播放、日期滑块与年份切换，"
            "适合在回答后直接嵌入，帮助用户观察太阳-地球-月球空间关系与月相联动。"
        ),
        expresses=[
            "太阳、地球、月球的相对空间关系",
            "满月附近月相变化与月食条件的关系",
            "月球公转与同步自转对月相呈现的影响",
        ],
        educational_use="帮助用户把月食、月相这类文字描述转换成可操作的空间几何直觉。",
        cannot_express=[
            "地方观测点的精确食甚时刻",
            "地球本影半影的高精度真实尺寸",
            "日月食的完整观测预报",
        ],
        implementation_kind="code_generated_page",
        source_entry=(
            "AlVisualization/main-app/modules/astronomy/src/"
            "sun_earth_moon_phase_slider.v6-年份下拉框+去除伪影+月球同步自转-闰年.py"
        ),
        trigger_patterns=["月食", "日食", "月相", "lunar eclipse", "solar eclipse", "moon phase"],
        priority=95,
        component_id="astronomy-core.eclipse-geometry",
        intent_type="spatial_geometry_explanation",
        props_schema={
            "phenomenon": {"type": "string", "enum": ["lunar_eclipse", "solar_eclipse", "moon_phase"]},
            "playback": {"type": "string", "enum": ["paused", "playing"]},
            "showShadowCone": {"type": "boolean"},
        },
        default_props={"phenomenon": "lunar_eclipse", "playback": "paused", "showShadowCone": True},
        interaction_events=["playbackChanged", "phaseSelected", "viewpointChanged"],
        feedback_contract={
            "eventPayload": "component returns selected phase, viewpoint, and current explanation focus",
            "agentUse": "use interaction state to explain why alignment is or is not sufficient for an eclipse",
        },
    ),
    VisualizationCapability(
        id="retrograde-demo",
        title="行星逆行演示",
        description="观察地球与外行星的相对运动如何形成逆行现象。",
        page_id="modern-annual-motion",
        concepts=["retrograde_motion"],
        keywords=["逆行", "retrograde", "planetary motion", "行星运动"],
        tags=["逆行", "相对运动", "地心视角", "外行星"],
        a2ui_hint=(
            "当用户询问逆行、视运动、从地球看行星为何倒退时调用。组件适合展示地球与外行星的相对运动，"
            "让用户看到逆行是视运动而非真实掉头。"
        ),
        expresses=[
            "地球与外行星相对速度差导致的视运动变化",
            "恒星背景中的回环轨迹",
            "地心视角与日心真实运动之间的差异",
        ],
        educational_use="帮助用户理解逆行是参考系与相对运动造成的投影现象。",
        cannot_express=[
            "多行星长期摄动和精确星历误差比较",
            "复杂三维坐标转换的全部细节",
        ],
        implementation_kind="embedded_page",
        source_entry="frontend/interactive-visualizations/legacy/modern-original/planetary_annual_motion.html",
        trigger_patterns=["逆行", "retrograde", "视运动", "apparent motion"],
        priority=92,
        component_id="astronomy-core.retrograde-motion",
        intent_type="reference_frame_comparison",
        props_schema={
            "observerFrame": {"type": "string", "enum": ["earth", "heliocentric"]},
            "targetPlanet": {"type": "string"},
            "showSightLine": {"type": "boolean"},
        },
        default_props={"observerFrame": "earth", "targetPlanet": "mars", "showSightLine": True},
        interaction_events=["frameChanged", "planetChanged", "timeScrubbed"],
        feedback_contract={
            "eventPayload": "component returns observer frame, target planet, and time position",
            "agentUse": "connect the selected frame to apparent backward motion in the answer",
        },
    ),
    VisualizationCapability(
        id="geocentric-daily-motion-3d",
        title="地心天球周日视运动 3D",
        description="以观测者为中心展示太阳、月亮与行星在地平坐标中的全天视运动轨迹。",
        page_id="geocentric-daily-motion-3d",
        concepts=["geocentric_daily_motion"],
        keywords=[
            "地心模型",
            "地心天球",
            "周日视运动",
            "日周运动",
            "天球",
            "七政",
            "太阳",
            "月亮",
            "行星",
            "diurnal motion",
            "geocentric",
            "celestial sphere",
        ],
        tags=["地心模型", "周日视运动", "天球", "地平坐标", "七政"],
        a2ui_hint=(
            "当用户询问地心模型、天球、周日视运动、太阳月亮和行星在一天内如何升落时调用。"
            "组件应展示地平圈、天球经纬网、当前天体位置、地平线上下轨迹和整点标记。"
        ),
        expresses=[
            "观测者地心视角下的太阳、月亮与行星升落路径",
            "同一天内天体位置随地球自转产生的周日视运动",
            "地平线上可见轨迹与地平线下不可见轨迹的差异",
        ],
        educational_use="帮助用户从地心参考系理解天体为何每天东升西落，以及不同纬度下轨迹倾角为何变化。",
        cannot_express=[
            "肉眼真实亮度、天气和地形遮挡",
            "长期历算中的岁差、章动与摄动细节教学",
            "藏历算法本身的逐步推算过程",
        ],
        implementation_kind="embedded_page",
        source_entry="frontend/interactive-visualizations/legacy/modern-original/celestial_sphere_7planets.html",
        trigger_patterns=[
            "地心模型",
            "地心天球",
            "周日视运动",
            "日周运动",
            "天球",
            "七政",
            "diurnal motion",
            "geocentric",
            "celestial sphere",
        ],
        priority=96,
        component_id="astronomy-core.geocentric-daily-motion",
        intent_type="reference_frame_daily_motion",
        props_schema={
            "observerFrame": {"type": "string", "enum": ["topocentric_geocentric"]},
            "latitude": {"type": "number", "minimum": -90, "maximum": 90},
            "longitude": {"type": "number", "minimum": -180, "maximum": 180},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "showTrails": {"type": "boolean"},
            "showEquatorialGrid": {"type": "boolean"},
            "showHorizonGrid": {"type": "boolean"},
        },
        default_props={
            "observerFrame": "topocentric_geocentric",
            "latitude": 31.23,
            "longitude": 121.47,
            "date": "today",
            "time": "now",
            "showTrails": True,
            "showEquatorialGrid": True,
            "showHorizonGrid": True,
        },
        interaction_events=["observerChanged", "timeChanged", "bodyHovered", "trailVisibilityChanged"],
        feedback_contract={
            "eventPayload": "component returns observer coordinates, selected time, highlighted body, and visibility toggles",
            "agentUse": "explain the selected body's daily apparent path, rise/set relation, and horizon visibility",
        },
    ),
    VisualizationCapability(
        id="kepler-third-law-demo",
        title="开普勒第三定律实验台",
        description="拖动半长轴，观察轨道周期如何满足 T² ∝ a³，并对比两条轨道的周期变化。",
        page_id="kepler-third-law",
        concepts=["kepler_third_law"],
        keywords=["开普勒第三定律", "kepler", "周期", "半长轴", "长半轴", "a^3", "t^2"],
        tags=["开普勒", "第三定律", "轨道周期", "半长轴", "幂律关系"],
        a2ui_hint="当用户询问开普勒第三定律、周期与半长轴关系时优先调用。",
        expresses=[
            "半长轴增大时轨道周期如何变长",
            "T² 与 a³ 的对应关系",
            "两条轨道在同一坐标系下的周期差异",
        ],
        educational_use="帮助用户把抽象比例关系转成轨道长度和周期变化的直观对应。",
        cannot_express=[
            "复杂摄动下的真实长期轨道演化",
            "高精度星历计算结果",
        ],
        implementation_kind="code_generated_page",
        source_entry="frontend/interactive-visualizations/legacy/generated/kepler-third-law.html",
        trigger_patterns=["开普勒第三定律", "kepler", "半长轴", "周期", "t^2", "a^3"],
        priority=94,
        component_id="astronomy-core.kepler-third-law",
        intent_type="formula_relationship_exploration",
        props_schema={
            "semiMajorAxis": {"type": "number", "minimum": 0.2, "maximum": 8},
            "comparisonAxis": {"type": "number", "minimum": 0.2, "maximum": 8},
            "showFormula": {"type": "boolean"},
        },
        default_props={"semiMajorAxis": 1, "comparisonAxis": 2, "showFormula": True},
        interaction_events=["axisChanged", "comparisonChanged", "formulaToggled"],
        feedback_contract={
            "eventPayload": "component returns selected axes and computed period ratio",
            "agentUse": "translate slider changes into the T^2 proportional to a^3 relationship",
        },
    ),
    VisualizationCapability(
        id="solar-system-demo",
        title="3D 太阳系模拟",
        description="在 3D 太阳系中查看轨道、缩放和天体信息。",
        page_id="modern-3d-solar",
        concepts=["solar_system_structure"],
        keywords=["轨道", "太阳系", "kepler", "orbit", "solar system"],
        tags=["太阳系", "轨道", "三维", "开普勒"],
        a2ui_hint="当用户希望从宏观角度观察太阳系结构、轨道层级和相对位置时调用。",
        expresses=[
            "太阳系主要天体的三维空间分布",
            "轨道层级与相对尺度关系",
            "基础轨道观察与缩放交互",
        ],
        educational_use="帮助用户建立太阳系整体结构的空间直觉。",
        cannot_express=[
            "VSOP 与 DE440 的精度对照",
            "藏历历算结果",
            "坐标系变换细节",
        ],
        implementation_kind="embedded_page",
        source_entry="frontend/interactive-visualizations/legacy/modern-3d/index.html",
        trigger_patterns=["太阳系", "轨道", "solar system", "orbit", "kepler"],
        priority=70,
        component_id="astronomy-core.solar-system-structure",
        intent_type="spatial_structure_exploration",
        props_schema={
            "focusBody": {"type": "string"},
            "showOrbits": {"type": "boolean"},
            "cameraMode": {"type": "string", "enum": ["overview", "focused"]},
        },
        default_props={"focusBody": "sun", "showOrbits": True, "cameraMode": "overview"},
        interaction_events=["bodySelected", "cameraChanged", "orbitVisibilityChanged"],
        feedback_contract={
            "eventPayload": "component returns selected body and camera mode",
            "agentUse": "explain orbital hierarchy from the user's selected body",
        },
    ),
    VisualizationCapability(
        id="solar-system-compare",
        title="🪐 太阳系行星运动对照",
        description="查看 VSOP、DE440 与藏历历算联动的太阳系行星位置对照页面。",
        page_id="solar-system-compare-streamlit",
        concepts=["ephemeris_compare", "solar_system_structure"],
        keywords=["vsop", "de440", "行星运动", "solar system", "streamlit"],
        tags=["VSOP", "DE440", "行星位置", "精度对照", "藏历历算"],
        a2ui_hint=(
            "当用户询问行星位置、模型差异、VSOP、DE440、轨道参数对比时调用。"
            "适合从模型层面对照天体位置与轨迹。"
        ),
        expresses=[
            "VSOP 与 DE440 的位置差异",
            "太阳系行星在同一时刻的相对位置",
            "历算与现代星历的对照展示",
        ],
        educational_use="帮助用户把抽象的星历模型差异与具体位置图形对应起来。",
        cannot_express=[
            "多用户并发的大规模计算服务",
            "纯 A2UI 原生组件级细粒度交互回传",
        ],
        implementation_kind="external_streamlit_page",
        source_entry="行星运动模型/solar_system_app.py",
        trigger_patterns=["vsop", "de440", "行星位置", "星历", "模型对照"],
        priority=88,
        component_id="astronomy-core.ephemeris-comparison",
        intent_type="model_comparison",
        props_schema={
            "models": {"type": "array", "items": {"type": "string"}},
            "bodies": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string"},
        },
        default_props={"models": ["VSOP", "DE440"], "bodies": ["earth", "mars"], "date": "today"},
        interaction_events=["modelToggled", "bodySelected", "dateChanged"],
        feedback_contract={
            "eventPayload": "component returns active models, selected bodies, and comparison date",
            "agentUse": "describe the visible model differences and their likely source",
        },
    ),
]


VISUALIZATIONS = [capability.public_dict() for capability in VISUALIZATION_CAPABILITIES]
