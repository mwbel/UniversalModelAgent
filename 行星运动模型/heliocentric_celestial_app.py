#!/usr/bin/env python3
"""
太阳为球心的 3D 天球可视化
对照 VSOP / DE440 在同一公历日内的行星方向变化轨迹
"""

import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from pymeeus.Coordinates import mean_obliquity
from pymeeus.Earth import Earth
from pymeeus.Epoch import Epoch
from pymeeus.Jupiter import Jupiter
from pymeeus.Mars import Mars
from pymeeus.Mercury import Mercury
from pymeeus.Neptune import Neptune
from pymeeus.Saturn import Saturn
from pymeeus.Uranus import Uranus
from pymeeus.Venus import Venus

from de_model import julian_date
from realtime_calculator import RealtimePlanetaryCalculator


st.set_page_config(
    page_title="太阳系周日视运动天球",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    .main .block-container {
        padding-top: 1.4rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #dbeafe;
        text-align: center;
        margin-bottom: 0.4rem;
    }
    .hero-subtitle {
        font-size: 1.08rem;
        color: #93a4b7;
        text-align: center;
        margin-bottom: 1.1rem;
    }
    .legend-chip {
        display: inline-block;
        padding: 0.24rem 0.72rem;
        border-radius: 999px;
        margin-right: 0.5rem;
        margin-bottom: 0.4rem;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .chip-de440 {
        color: #f8fafc;
        background: rgba(59, 130, 246, 0.18);
        border: 1px solid rgba(147, 197, 253, 0.35);
    }
    .chip-vsop {
        color: #f8fafc;
        background: rgba(250, 204, 21, 0.16);
        border: 1px solid rgba(253, 224, 71, 0.3);
    }
</style>
""",
    unsafe_allow_html=True,
)


PLANET_COLORS = {
    "sun": "#FFD54A",
    "mercury": "#F3F4F6",
    "venus": "#FFD23F",
    "earth": "#33D1E6",
    "mars": "#FF5A3C",
    "jupiter": "#F4B942",
    "saturn": "#D8C27A",
    "uranus": "#56E0E8",
    "neptune": "#3F8CFF",
}

PLANET_NAMES_CN = {
    "mercury": "水星",
    "venus": "金星",
    "earth": "地球",
    "mars": "火星",
    "jupiter": "木星",
    "saturn": "土星",
    "uranus": "天王星",
    "neptune": "海王星",
}

VSOP_PLANET_CLASSES = {
    "mercury": Mercury,
    "venus": Venus,
    "earth": Earth,
    "mars": Mars,
    "jupiter": Jupiter,
    "saturn": Saturn,
    "uranus": Uranus,
    "neptune": Neptune,
}

SUPPORTED_PLANETS = list(VSOP_PLANET_CLASSES.keys())
AU_KM = 149597870.7


@st.cache_resource
def init_calculator():
    """Initialize DE440 calculator."""
    spk_file = "de440.bsp"
    if not os.path.exists(spk_file):
        st.error(f"❌ 未找到星历文件: {spk_file}")
        st.stop()
    return RealtimePlanetaryCalculator(spk_file)


def datetime_to_epoch(selected_time):
    """Convert datetime to PyMeeus epoch."""
    day_fraction = (
        selected_time.day
        + selected_time.hour / 24.0
        + selected_time.minute / 1440.0
        + selected_time.second / 86400.0
    )
    return Epoch(selected_time.year, selected_time.month, day_fraction)


def get_obliquity_rad(epoch):
    """Return mean obliquity in radians."""
    return np.deg2rad(float(mean_obliquity(epoch)))


def spherical_to_equatorial_cartesian(longitude_rad, latitude_rad, radius_au, obliquity_rad):
    """Convert heliocentric ecliptic spherical coordinates to equatorial Cartesian."""
    x_ecl = radius_au * np.cos(latitude_rad) * np.cos(longitude_rad)
    y_ecl = radius_au * np.cos(latitude_rad) * np.sin(longitude_rad)
    z_ecl = radius_au * np.sin(latitude_rad)

    x_eq = x_ecl
    y_eq = y_ecl * np.cos(obliquity_rad) - z_ecl * np.sin(obliquity_rad)
    z_eq = y_ecl * np.sin(obliquity_rad) + z_ecl * np.cos(obliquity_rad)
    return np.array([x_eq, y_eq, z_eq]) * AU_KM


def compute_vsop_position(planet, selected_time):
    """Compute heliocentric VSOP position in equatorial Cartesian frame."""
    epoch = datetime_to_epoch(selected_time)
    longitude, latitude, radius_au = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(epoch)
    return spherical_to_equatorial_cartesian(
        longitude.rad(),
        latitude.rad(),
        radius_au,
        get_obliquity_rad(epoch),
    )


def compute_de440_position(calc, planet, selected_time):
    """Compute heliocentric DE440 position in equatorial Cartesian frame."""
    if planet != "earth":
        position_km, _, _ = calc.compute_position(planet, selected_time, relative_to="sun")
        return position_km

    jd = julian_date(
        selected_time.year,
        selected_time.month,
        selected_time.day,
        selected_time.hour,
        selected_time.minute,
        selected_time.second,
    )
    emb_pos, _ = calc.spk[0, 3].compute_and_differentiate(jd)
    sun_pos, _ = calc.spk[0, 10].compute_and_differentiate(jd)
    earth_rel, _ = calc.spk[3, 399].compute_and_differentiate(jd)
    return emb_pos + earth_rel - sun_pos


def normalize_vector(vector):
    """Project a vector onto the unit sphere."""
    norm = np.linalg.norm(vector)
    if norm == 0:
        return np.zeros(3)
    return vector / norm


def ra_dec_from_vector(vector):
    """Convert Cartesian vector to right ascension / declination."""
    unit = normalize_vector(vector)
    ra_rad = np.arctan2(unit[1], unit[0]) % (2 * np.pi)
    dec_rad = np.arcsin(np.clip(unit[2], -1.0, 1.0))
    return np.degrees(ra_rad), np.degrees(dec_rad)


def degrees_to_ra_string(ra_deg):
    """Format right ascension in hours."""
    total_hours = (ra_deg / 15.0) % 24.0
    hours = int(total_hours)
    minutes = int((total_hours - hours) * 60)
    seconds = int(round((((total_hours - hours) * 60) - minutes) * 60))
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours = (hours + 1) % 24
    return f"{hours:02d}h {minutes:02d}m {seconds:02d}s"


def angular_separation_arcsec(vector_a, vector_b):
    """Angular separation between two direction vectors."""
    a = normalize_vector(vector_a)
    b = normalize_vector(vector_b)
    cosine = np.clip(np.dot(a, b), -1.0, 1.0)
    return np.degrees(np.arccos(cosine)) * 3600.0


def blend_hex_color(hex_color, target_hex, ratio):
    """Blend two colors for model-specific brightness adjustments."""
    base = hex_color.lstrip("#")
    target = target_hex.lstrip("#")
    base_rgb = tuple(int(base[index : index + 2], 16) for index in (0, 2, 4))
    target_rgb = tuple(int(target[index : index + 2], 16) for index in (0, 2, 4))
    blended = tuple(
        round(base_rgb[index] * (1 - ratio) + target_rgb[index] * ratio) for index in range(3)
    )
    return "#{:02X}{:02X}{:02X}".format(*blended)


def build_track_times(selected_date, step_minutes):
    """Build a full day's time samples in UTC."""
    start = datetime(selected_date.year, selected_date.month, selected_date.day, 0, 0)
    samples = int((24 * 60) / step_minutes)
    return [start + timedelta(minutes=index * step_minutes) for index in range(samples + 1)]


def build_planet_track(calc, planet, track_times, current_time):
    """Compute DE440 / VSOP unit-sphere tracks and current positions for a planet."""
    de_track = []
    vsop_track = []
    for time_point in track_times:
        de_track.append(normalize_vector(compute_de440_position(calc, planet, time_point)))
        vsop_track.append(normalize_vector(compute_vsop_position(planet, time_point)))

    de_current = normalize_vector(compute_de440_position(calc, planet, current_time))
    vsop_current = normalize_vector(compute_vsop_position(planet, current_time))
    return {
        "planet": planet,
        "times": track_times,
        "de_track": np.array(de_track),
        "vsop_track": np.array(vsop_track),
        "de_current": de_current,
        "vsop_current": vsop_current,
    }


def add_celestial_wireframe(fig):
    """Add a dark spherical shell with RA/Dec grid."""
    grid_radius = 1.0

    ra_values = np.arange(0, 360, 15)
    dec_values = np.arange(-75, 90, 15)

    for ra_deg in ra_values:
        ra_rad = np.radians(ra_deg)
        dec_line = np.linspace(-np.pi / 2, np.pi / 2, 120)
        x_line = grid_radius * np.cos(dec_line) * np.cos(ra_rad)
        y_line = grid_radius * np.cos(dec_line) * np.sin(ra_rad)
        z_line = grid_radius * np.sin(dec_line)
        is_major = ra_deg % 30 == 0
        fig.add_trace(
            go.Scatter3d(
                x=x_line,
                y=y_line,
                z=z_line,
                mode="lines",
                line=dict(
                    color="#CBD5E1" if is_major else "#64748B",
                    width=4 if is_major else 2,
                ),
                hoverinfo="skip",
                showlegend=False,
            )
        )

    for dec_deg in dec_values:
        dec_rad = np.radians(dec_deg)
        ra_line = np.linspace(0, 2 * np.pi, 180)
        x_line = grid_radius * np.cos(dec_rad) * np.cos(ra_line)
        y_line = grid_radius * np.cos(dec_rad) * np.sin(ra_line)
        z_line = np.full_like(ra_line, grid_radius * np.sin(dec_rad))
        is_major = dec_deg % 30 == 0
        fig.add_trace(
            go.Scatter3d(
                x=x_line,
                y=y_line,
                z=z_line,
                mode="lines",
                line=dict(
                    color="#CBD5E1" if is_major else "#64748B",
                    width=4 if is_major else 2,
                ),
                hoverinfo="skip",
                showlegend=False,
            )
        )


def add_grid_labels(fig):
    """Add longitude and latitude labels on the celestial sphere."""
    longitude_labels = [
        ("0°", 0),
        ("30°", 30),
        ("60°", 60),
        ("90°", 90),
        ("120°", 120),
        ("150°", 150),
        ("180°", 180),
        ("210°", 210),
        ("240°", 240),
        ("270°", 270),
        ("300°", 300),
        ("330°", 330),
    ]
    for label, ra_deg in longitude_labels:
        ra_rad = np.radians(ra_deg)
        fig.add_trace(
            go.Scatter3d(
                x=[1.08 * np.cos(ra_rad)],
                y=[1.08 * np.sin(ra_rad)],
                z=[0],
                mode="text",
                text=[label],
                textfont=dict(color="#CBD5E1", size=10),
                hoverinfo="skip",
                showlegend=False,
            )
        )

    latitude_labels = [-60, -30, 30, 60]
    for dec_deg in latitude_labels:
        dec_rad = np.radians(dec_deg)
        radius = np.cos(dec_rad)
        z_value = np.sin(dec_rad)
        fig.add_trace(
            go.Scatter3d(
                x=[1.04 * radius],
                y=[0],
                z=[1.04 * z_value],
                mode="text",
                text=[f"{dec_deg:+d}°"],
                textfont=dict(color="#94A3B8", size=10),
                hoverinfo="skip",
                showlegend=False,
            )
        )


def add_equator_and_ecliptic(fig):
    """Add celestial equator and ecliptic."""
    theta = np.linspace(0, 2 * np.pi, 240)
    fig.add_trace(
        go.Scatter3d(
            x=np.cos(theta),
            y=np.sin(theta),
            z=np.zeros_like(theta),
            mode="lines",
            line=dict(color="rgba(91,192,235,0.65)", width=4),
            name="天赤道",
            hoverinfo="skip",
        )
    )

    obliquity = np.radians(23.4393)
    fig.add_trace(
        go.Scatter3d(
            x=np.cos(theta),
            y=np.sin(theta) * np.cos(obliquity),
            z=np.sin(theta) * np.sin(obliquity),
            mode="lines",
            line=dict(color="rgba(255,212,74,0.75)", width=4, dash="dash"),
            name="黄道",
            hoverinfo="skip",
        )
    )


def add_axis_labels(fig):
    """Add key direction labels."""
    points = {
        "春分点": (1.16, 0, 0),
        "RA 6h": (0, 1.16, 0),
        "秋分点": (-1.16, 0, 0),
        "RA 18h": (0, -1.16, 0),
        "北天极": (0, 0, 1.18),
        "南天极": (0, 0, -1.18),
    }
    for label, position in points.items():
        fig.add_trace(
            go.Scatter3d(
                x=[position[0]],
                y=[position[1]],
                z=[position[2]],
                mode="text",
                text=[label],
                textfont=dict(color="#E2E8F0", size=11),
                hoverinfo="skip",
                showlegend=False,
            )
        )


def create_celestial_figure(track_results, show_hour_labels):
    """Create the 3D celestial sphere comparison plot."""
    fig = go.Figure()
    add_celestial_wireframe(fig)
    add_equator_and_ecliptic(fig)
    add_axis_labels(fig)
    add_grid_labels(fig)

    fig.add_trace(
        go.Scatter3d(
            x=[0],
            y=[0],
            z=[0],
            mode="markers",
            marker=dict(size=11, color=PLANET_COLORS["sun"]),
            name="太阳",
            hovertemplate="<b>太阳</b><br>球心<extra></extra>",
        )
    )

    for result in track_results:
        planet = result["planet"]
        color = PLANET_COLORS[planet]
        de_color = blend_hex_color(color, "#FFFFFF", 0.18)
        vsop_color = blend_hex_color(color, "#050608", 0.26)

        hover_texts = [time_point.strftime("%Y-%m-%d %H:%M UTC") for time_point in result["times"]]

        fig.add_trace(
            go.Scatter3d(
                x=result["de_track"][:, 0],
                y=result["de_track"][:, 1],
                z=result["de_track"][:, 2],
                mode="lines",
                line=dict(color=de_color, width=6),
                name=f"{PLANET_NAMES_CN[planet]} · DE440",
                legendgroup=f"{planet}_de",
                hovertext=hover_texts,
                hovertemplate="<b>%{fullData.name}</b><br>%{hovertext}<extra></extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=result["vsop_track"][:, 0],
                y=result["vsop_track"][:, 1],
                z=result["vsop_track"][:, 2],
                mode="lines",
                line=dict(color=vsop_color, width=4, dash="dash"),
                name=f"{PLANET_NAMES_CN[planet]} · VSOP",
                legendgroup=f"{planet}_vsop",
                hovertext=hover_texts,
                hovertemplate="<b>%{fullData.name}</b><br>%{hovertext}<extra></extra>",
            )
        )

        fig.add_trace(
            go.Scatter3d(
                x=[result["de_current"][0]],
                y=[result["de_current"][1]],
                z=[result["de_current"][2]],
                mode="markers",
                marker=dict(
                    size=7,
                    color=de_color,
                    line=dict(color=blend_hex_color(de_color, "#FFFFFF", 0.42), width=1.2),
                ),
                name=f"{PLANET_NAMES_CN[planet]} 当前 · DE440",
                legendgroup=f"{planet}_de",
                showlegend=False,
                hovertemplate=f"<b>{PLANET_NAMES_CN[planet]} 当前 · DE440</b><extra></extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[result["vsop_current"][0]],
                y=[result["vsop_current"][1]],
                z=[result["vsop_current"][2]],
                mode="markers",
                marker=dict(size=6, color=vsop_color, symbol="diamond"),
                name=f"{PLANET_NAMES_CN[planet]} 当前 · VSOP",
                legendgroup=f"{planet}_vsop",
                showlegend=False,
                hovertemplate=f"<b>{PLANET_NAMES_CN[planet]} 当前 · VSOP</b><extra></extra>",
            )
        )

        if show_hour_labels:
            label_indices = [0, len(result["times"]) // 4, len(result["times"]) // 2, 3 * len(result["times"]) // 4]
            label_indices = sorted(set(min(index, len(result["times"]) - 1) for index in label_indices))
            label_points = result["de_track"][label_indices]
            label_text = [result["times"][index].strftime("%H") for index in label_indices]
            fig.add_trace(
                go.Scatter3d(
                    x=label_points[:, 0],
                    y=label_points[:, 1],
                    z=label_points[:, 2],
                    mode="text",
                    text=label_text,
                    textfont=dict(color=de_color, size=10),
                    hoverinfo="skip",
                    showlegend=False,
                )
            )

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="cube",
            bgcolor="#020407",
            camera=dict(eye=dict(x=1.45, y=1.45, z=1.15)),
        ),
        paper_bgcolor="#020407",
        plot_bgcolor="#020407",
        height=860,
        margin=dict(l=0, r=0, t=10, b=0),
        legend=dict(
            x=0.01,
            y=0.99,
            bgcolor="rgba(5,8,12,0.72)",
            bordercolor="rgba(148,163,184,0.15)",
            borderwidth=1,
            font=dict(color="#E2E8F0", size=12),
        ),
    )
    return fig


def build_summary_rows(track_results):
    """Create current-time comparison table."""
    rows = []
    for result in track_results:
        de_ra, de_dec = ra_dec_from_vector(result["de_current"])
        vsop_ra, vsop_dec = ra_dec_from_vector(result["vsop_current"])
        rows.append(
            {
                "行星": PLANET_NAMES_CN[result["planet"]],
                "DE440 赤经": degrees_to_ra_string(de_ra),
                "VSOP 赤经": degrees_to_ra_string(vsop_ra),
                "DE440 赤纬": f"{de_dec:+.4f}°",
                "VSOP 赤纬": f"{vsop_dec:+.4f}°",
                "模型角距": f"{angular_separation_arcsec(result['de_current'], result['vsop_current']):.2f}\"",
                "DE440 日扫角": f"{np.degrees(np.arccos(np.clip(np.dot(result['de_track'][0], result['de_track'][-1]), -1, 1))):.4f}°",
                "VSOP 日扫角": f"{np.degrees(np.arccos(np.clip(np.dot(result['vsop_track'][0], result['vsop_track'][-1]), -1, 1))):.4f}°",
            }
        )
    return pd.DataFrame(rows)


def main():
    """Render the heliocentric celestial sphere app."""
    st.markdown('<div class="hero-title">🌐 太阳系周日视运动天球</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">太阳位于球心，比较同一公历日内各行星在单位天球上的方向轨迹，并同步给出 VSOP / DE440 结果。</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="legend-chip chip-de440">DE440: 同色亮线</span>'
        '<span class="legend-chip chip-vsop">VSOP: 同色虚线</span>',
        unsafe_allow_html=True,
    )

    calc = init_calculator()

    st.sidebar.header("⚙️ 时间与目标")
    selected_date = st.sidebar.date_input("公历日期（UTC）", datetime.utcnow().date())
    hour = st.sidebar.selectbox("时（UTC）", list(range(24)), index=datetime.utcnow().hour)
    minute = st.sidebar.selectbox("分（UTC）", list(range(0, 60, 5)), index=(datetime.utcnow().minute // 5))
    current_time = datetime(selected_date.year, selected_date.month, selected_date.day, hour, minute)

    selected_planets = st.sidebar.multiselect(
        "选择行星",
        SUPPORTED_PLANETS,
        default=["mercury", "venus", "earth", "mars", "jupiter"],
        format_func=lambda planet: PLANET_NAMES_CN[planet],
    )
    step_minutes = st.sidebar.select_slider("轨迹采样间隔（分钟）", options=[30, 60, 120], value=60)
    show_hour_labels = st.sidebar.checkbox("显示时刻标签", value=len(selected_planets) <= 3)

    st.sidebar.caption(f"当前高亮时刻：{current_time.strftime('%Y-%m-%d %H:%M')} UTC")

    if not selected_planets:
        st.warning("⚠️ 请至少选择一个行星。")
        return

    track_times = build_track_times(selected_date, step_minutes)
    track_results = []
    for planet in selected_planets:
        try:
            track_results.append(build_planet_track(calc, planet, track_times, current_time))
        except Exception as exc:
            st.error(f"{PLANET_NAMES_CN[planet]} 轨迹计算失败: {exc}")

    if not track_results:
        st.warning("⚠️ 当前没有可展示的数据。")
        return

    figure = create_celestial_figure(track_results, show_hour_labels)
    st.plotly_chart(figure, use_container_width=True)

    st.subheader("📋 当前时刻 VSOP / DE440 对照")
    st.dataframe(build_summary_rows(track_results), use_container_width=True, hide_index=True)

    with st.expander("ℹ️ 说明"):
        st.markdown(
            """
### 这一页在看什么

- 这是一个**以太阳为球心**的单位天球，不是地面观测者的地平坐标天球。
- 每条轨迹表示该行星在同一公历日 24 小时内的**方向变化**，因此重点是方向而不是日心距离。
- `DE440` 走 JPL 星历表，`VSOP` 走 PyMeeus 的 VSOP87 解析公式。
- 表格里的“模型角距”表示同一时刻两套模型在天球方向上的夹角差，单位为角秒。
- “日扫角”表示该行星从 00:00 UTC 到 24:00 UTC 在单位天球上扫过的角距离。
"""
        )


if __name__ == "__main__":
    main()
