#!/usr/bin/env python3
"""
太阳系行星运动 VSOP / DE440 / 藏历天文历算 对照可视化应用
使用 Streamlit 创建交互式 Web 界面
"""

import calendar
import os
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings("ignore", message=".*Alignment Warning.*", category=UserWarning)
import caltib
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
from pymeeus.Moon import Moon
from pymeeus.Neptune import Neptune
from pymeeus.Saturn import Saturn
from pymeeus.Uranus import Uranus
from pymeeus.Venus import Venus

from de_model import julian_date
from realtime_calculator import RealtimePlanetaryCalculator
from tibetan_five_elements_v1 import compute_tibetan_five_elements_v1, result_to_dict


st.set_page_config(
    page_title="太阳系行星运动对照",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    section[data-testid="stSidebar"] {
        width: 320px !important;
        min-width: 320px !important;
    }
    section[data-testid="stSidebar"] > div:first-child {
        width: 320px !important;
        min-width: 320px !important;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #51606f;
        text-align: center;
        margin-bottom: 1.8rem;
    }
    .model-chip {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }
    .chip-vsop {
        background: #e8f4ff;
        color: #005ea8;
    }
    .chip-de440 {
        background: #fff2d6;
        color: #8a5300;
    }
    .calendar-shell {
        margin-top: 0.35rem;
        padding: 0.7rem 0.7rem 0.6rem;
        border: 1px solid rgba(31, 78, 121, 0.12);
        border-radius: 16px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,252,0.98));
        box-shadow: 0 10px 24px rgba(31, 78, 121, 0.06);
    }
    .calendar-title {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.88rem;
        font-weight: 600;
        color: #244563;
        margin-bottom: 0.4rem;
    }
    .calendar-today {
        display: inline-block;
        padding: 0.14rem 0.45rem;
        border-radius: 999px;
        background: rgba(31, 78, 121, 0.08);
        color: #315b82;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .calendar-weekday {
        text-align: center;
        font-size: 0.76rem;
        font-weight: 600;
        color: #738296;
        letter-spacing: 0.02em;
        padding-bottom: 0.2rem;
    }
    .calendar-empty {
        height: 2.25rem;
        border-radius: 10px;
        background: rgba(148, 163, 184, 0.08);
        border: 1px dashed rgba(148, 163, 184, 0.18);
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
        min-height: 2.25rem;
        border-radius: 12px;
        border: 1px solid rgba(49, 91, 130, 0.16);
        background: rgba(255, 255, 255, 0.96);
        color: #274764;
        font-weight: 600;
        font-size: clamp(0.78rem, 1.5vw, 0.95rem);
        line-height: 1;
        white-space: nowrap;
        padding: 0.35rem 0.1rem;
        box-shadow: none;
        transition: all 120ms ease;
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
        border-color: rgba(49, 91, 130, 0.34);
        background: rgba(242, 247, 252, 1);
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button[kind="primary"] {
        border: 2px solid #1f4e79;
        background: linear-gradient(180deg, #f2f8ff, #dceeff);
        color: #153a5d;
        box-shadow: 0 0 0 3px rgba(31, 78, 121, 0.08);
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
    "moon": "#9B7CFF",
    "mars": "#FF5A3C",
    "jupiter": "#F4B942",
    "saturn": "#D8C27A",
    "uranus": "#56E0E8",
    "neptune": "#3F8CFF",
}

PLANET_NAMES_CN = {
    "sun": "太阳",
    "mercury": "水星",
    "venus": "金星",
    "earth": "地球",
    "mars": "火星",
    "jupiter": "木星",
    "saturn": "土星",
    "uranus": "天王星",
    "neptune": "海王星",
    "moon": "月亮",
}

TIBETAN_ELEMENTS = ["铁", "铁", "水", "水", "木", "木", "火", "火", "土", "土"]
TIBETAN_ZODIAC = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"]

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

AU_KM = 149597870.7
SUPPORTED_PLANETS = list(VSOP_PLANET_CLASSES.keys()) + ["moon"]
ORBITAL_PERIOD_DAYS = {
    "mercury": 87.969,
    "venus": 224.701,
    "earth": 365.256,
    "mars": 686.980,
    "jupiter": 4332.589,
    "saturn": 10759.22,
    "uranus": 30688.5,
    "neptune": 60182.0,
    "moon": 27.321661,
}


@st.cache_resource
def init_calculator():
    """初始化 DE440 计算器。"""
    spk_file = "de440.bsp"
    if not os.path.exists(spk_file):
        st.error(f"❌ 未找到星历文件: {spk_file}")
        st.info("请将 de440.bsp 文件放在应用目录中")
        st.stop()
    return RealtimePlanetaryCalculator(spk_file)


def datetime_to_epoch(selected_time):
    """将 datetime 转换为 PyMeeus Epoch。"""
    day_fraction = (
        selected_time.day
        + selected_time.hour / 24.0
        + selected_time.minute / 1440.0
        + selected_time.second / 86400.0
    )
    return Epoch(selected_time.year, selected_time.month, day_fraction)


def get_obliquity_rad(epoch):
    """获取黄赤交角弧度值。"""
    return np.deg2rad(float(mean_obliquity(epoch)))


def spherical_to_equatorial_cartesian(longitude_rad, latitude_rad, radius_au, obliquity_rad):
    """将黄道球坐标转为赤道直角坐标。"""
    x_ecl = radius_au * np.cos(latitude_rad) * np.cos(longitude_rad)
    y_ecl = radius_au * np.cos(latitude_rad) * np.sin(longitude_rad)
    z_ecl = radius_au * np.sin(latitude_rad)

    x_eq = x_ecl
    y_eq = y_ecl * np.cos(obliquity_rad) - z_ecl * np.sin(obliquity_rad)
    z_eq = y_ecl * np.sin(obliquity_rad) + z_ecl * np.cos(obliquity_rad)

    return np.array([x_eq, y_eq, z_eq]) * AU_KM


def equatorial_spherical_to_cartesian(longitude_rad, latitude_rad, distance_km):
    """将赤道球坐标转为直角坐标。"""
    x = distance_km * np.cos(latitude_rad) * np.cos(longitude_rad)
    y = distance_km * np.cos(latitude_rad) * np.sin(longitude_rad)
    z = distance_km * np.sin(latitude_rad)
    return np.array([x, y, z])


def blend_hex_color(hex_color, target_hex, ratio):
    """Blend two hex colors by ratio in [0, 1]."""
    base = hex_color.lstrip("#")
    target = target_hex.lstrip("#")
    base_rgb = tuple(int(base[index : index + 2], 16) for index in (0, 2, 4))
    target_rgb = tuple(int(target[index : index + 2], 16) for index in (0, 2, 4))
    blended = tuple(
        round(base_rgb[index] * (1 - ratio) + target_rgb[index] * ratio) for index in range(3)
    )
    return "#{:02X}{:02X}{:02X}".format(*blended)


def compute_vsop_position(planet, selected_time):
    """计算 VSOP 模型下的行星位置与速度。"""
    epoch = datetime_to_epoch(selected_time)
    longitude, latitude, radius_au = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(epoch)
    obliquity_rad = get_obliquity_rad(epoch)

    position_km = spherical_to_equatorial_cartesian(
        longitude.rad(),
        latitude.rad(),
        radius_au,
        obliquity_rad,
    )

    # 用中心差分近似速度，兼顾稳定性与性能。
    delta = timedelta(minutes=30)
    epoch_before = datetime_to_epoch(selected_time - delta)
    epoch_after = datetime_to_epoch(selected_time + delta)
    lon_before, lat_before, radius_before = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(epoch_before)
    lon_after, lat_after, radius_after = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(epoch_after)

    pos_before = spherical_to_equatorial_cartesian(
        lon_before.rad(),
        lat_before.rad(),
        radius_before,
        get_obliquity_rad(epoch_before),
    )
    pos_after = spherical_to_equatorial_cartesian(
        lon_after.rad(),
        lat_after.rad(),
        radius_after,
        get_obliquity_rad(epoch_after),
    )

    velocity_km_s = (pos_after - pos_before) / (2.0 * delta.total_seconds())
    distance_au = np.linalg.norm(position_km) / AU_KM
    return position_km, velocity_km_s, distance_au


def compute_vsop_moon_position(selected_time):
    """计算 VSOP + PyMeeus 月球模型下的月亮日心位置。"""
    earth_position_km, _, _ = compute_vsop_position("earth", selected_time)
    epoch = datetime_to_epoch(selected_time)
    right_ascension, declination, distance_km, _ = Moon.apparent_equatorial_pos(epoch)
    moon_geocentric_km = equatorial_spherical_to_cartesian(
        right_ascension.rad(),
        declination.rad(),
        distance_km,
    )
    position_km = earth_position_km + moon_geocentric_km

    delta = timedelta(minutes=30)
    epoch_before = datetime_to_epoch(selected_time - delta)
    epoch_after = datetime_to_epoch(selected_time + delta)
    ra_before, dec_before, distance_before_km, _ = Moon.apparent_equatorial_pos(epoch_before)
    ra_after, dec_after, distance_after_km, _ = Moon.apparent_equatorial_pos(epoch_after)

    earth_before_km, _, _ = compute_vsop_position("earth", selected_time - delta)
    earth_after_km, _, _ = compute_vsop_position("earth", selected_time + delta)
    moon_before_km = earth_before_km + equatorial_spherical_to_cartesian(
        ra_before.rad(),
        dec_before.rad(),
        distance_before_km,
    )
    moon_after_km = earth_after_km + equatorial_spherical_to_cartesian(
        ra_after.rad(),
        dec_after.rad(),
        distance_after_km,
    )

    velocity_km_s = (moon_after_km - moon_before_km) / (2.0 * delta.total_seconds())
    distance_au = np.linalg.norm(position_km) / AU_KM
    return position_km, velocity_km_s, distance_au


def compute_vsop_like_position(planet, selected_time):
    """统一入口：行星走 VSOP，月亮走 PyMeeus 月球模型。"""
    if planet == "moon":
        return compute_vsop_moon_position(selected_time)
    return compute_vsop_position(planet, selected_time)


def compute_de440_like_position(calc, planet, selected_time):
    """统一入口：对 Earth/Moon 使用 DE440 子段拼装真实位置。"""
    if planet not in {"earth", "moon"}:
        return calc.compute_position(planet, selected_time)

    jd = julian_date(
        selected_time.year,
        selected_time.month,
        selected_time.day,
        selected_time.hour,
        selected_time.minute,
        selected_time.second,
    )
    emb_pos, emb_vel = calc.spk[0, 3].compute_and_differentiate(jd)
    sun_pos, sun_vel = calc.spk[0, 10].compute_and_differentiate(jd)

    if planet == "earth":
        rel_pos, rel_vel = calc.spk[3, 399].compute_and_differentiate(jd)
    else:
        rel_pos, rel_vel = calc.spk[3, 301].compute_and_differentiate(jd)

    body_pos = emb_pos + rel_pos - sun_pos
    body_vel = emb_vel + rel_vel - sun_vel
    distance_au = np.linalg.norm(body_pos) / calc.AU
    return body_pos, body_vel, distance_au


def sexagesimal_arc_to_degrees(values):
    """将藏历星宿/弧刻编码转换为黄经度数。"""
    values = [float(value) for value in values]
    star = values[0]
    arc_minute = values[1] / 60.0 if len(values) > 1 else 0.0
    arc_second = values[2] / 3600.0 if len(values) > 2 else 0.0
    arc_breath = values[3] / (3600.0 * 6.0) if len(values) > 3 else 0.0
    qiaxi_67 = values[4] / (3600.0 * 6.0 * 67.0) if len(values) > 4 else 0.0
    qiaxi_707 = values[5] / (3600.0 * 6.0 * 67.0 * 707.0) if len(values) > 5 else 0.0
    return (star + arc_minute + arc_second + arc_breath + qiaxi_67 + qiaxi_707) * (360.0 / 27.0)


def gregorian_to_tibetan(gregorian_date):
    """Use caltib to convert a Gregorian date into a Tibetan calendar date."""
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=".*Alignment Warning.*",
            category=UserWarning,
        )
        info = caltib.day_info(gregorian_date.date(), engine="phugpa")
    return info


def compute_tibetan_from_gregorian(gregorian_date):
    """Convert Gregorian date and compute the v1 Tibetan five-element result."""
    info = gregorian_to_tibetan(gregorian_date)
    tib = info.tibetan
    five_elements = result_to_dict(
        compute_tibetan_five_elements_v1(
            year=int(tib.year),
            month=int(tib.month),
            day=int(tib.tithi),
            is_leap_month=bool(tib.is_leap_month),
        )
    )
    five_elements["converted"] = {
        "year": int(tib.year),
        "month": int(tib.month),
        "day": int(tib.tithi),
        "is_leap_month": bool(tib.is_leap_month),
        "occurrence": int(tib.occ),
        "status": info.status,
    }
    return five_elements


def compute_comparison(calc, planet, selected_time):
    """计算同一时刻下 VSOP 与 DE440 的对照数据。"""
    de_position_km, de_velocity_day, de_distance_au = compute_de440_like_position(calc, planet, selected_time)
    de_velocity_km_s = de_velocity_day / 86400.0

    vsop_position_km, vsop_velocity_km_s, vsop_distance_au = compute_vsop_like_position(planet, selected_time)

    delta_vector_km = vsop_position_km - de_position_km
    delta_distance_km = np.linalg.norm(delta_vector_km)

    return {
        "planet": planet,
        "de440": {
            "position_km": de_position_km,
            "velocity_km_s": de_velocity_km_s,
            "distance_au": de_distance_au,
        },
        "vsop": {
            "position_km": vsop_position_km,
            "velocity_km_s": vsop_velocity_km_s,
            "distance_au": vsop_distance_au,
        },
        "delta": {
            "vector_km": delta_vector_km,
            "distance_km": delta_distance_km,
            "distance_au": delta_distance_km / AU_KM,
            "speed_km_s": np.linalg.norm(vsop_velocity_km_s - de_velocity_km_s),
        },
    }


def get_model_position_au(result, model_name):
    """提取指定模型的 AU 坐标。"""
    return result[model_name]["position_km"] / AU_KM


def add_sun_trace(fig, is_3d):
    """添加太阳位置。"""
    common = dict(
        mode="markers",
        marker=dict(size=18, color=PLANET_COLORS["sun"], symbol="circle"),
        name="太阳",
        hovertemplate="<b>太阳</b><br>位置: (0, 0, 0)<extra></extra>",
    )
    if is_3d:
        fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], **common))
    else:
        fig.add_trace(go.Scatter(x=[0], y=[0], **common))


def add_orbit_trace(fig, calc, planet, selected_time, color, is_3d):
    """用真实采样轨迹替代圆形示意轨道，保证行星点落在轨迹上。"""
    period_days = ORBITAL_PERIOD_DAYS.get(planet, 365.256)
    sample_count = 181
    offsets = np.linspace(-period_days / 2.0, period_days / 2.0, sample_count)
    orbit_points = []

    for offset_day in offsets:
        sample_time = selected_time + timedelta(days=float(offset_day))
        position_km, _, _ = compute_de440_like_position(calc, planet, sample_time)
        orbit_points.append(position_km / AU_KM)

    orbit_points = np.asarray(orbit_points)
    line_style = dict(color=color, width=1, dash="dot")
    if is_3d:
        fig.add_trace(
            go.Scatter3d(
                x=orbit_points[:, 0],
                y=orbit_points[:, 1],
                z=orbit_points[:, 2],
                mode="lines",
                line=line_style,
                showlegend=False,
                hoverinfo="skip",
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                x=orbit_points[:, 0],
                y=orbit_points[:, 1],
                mode="lines",
                line=line_style,
                showlegend=False,
                hoverinfo="skip",
            )
        )


def create_comparison_figure(calc, results, selected_time, view_mode, show_orbits, show_delta_links):
    """创建 VSOP / DE440 对照图。"""
    is_3d = view_mode == "3D对照"
    space_background = "#050608"
    axis_text_color = "#9fb3c8"
    fig = go.Figure()
    add_sun_trace(fig, is_3d)

    max_dist = 1.0
    for result in results:
        planet = result["planet"]
        color = PLANET_COLORS.get(planet, "#888888")
        de_color = blend_hex_color(color, "#FFFFFF", 0.18)
        vsop_color = blend_hex_color(color, "#0A0D12", 0.28)
        de_position_au = get_model_position_au(result, "de440")
        vsop_position_au = get_model_position_au(result, "vsop")
        max_dist = max(
            max_dist,
            np.linalg.norm(de_position_au),
            np.linalg.norm(vsop_position_au),
        )

        if show_orbits:
            add_orbit_trace(fig, calc, planet, selected_time, color, is_3d)

        common_hover = (
            f"<b>{PLANET_NAMES_CN.get(planet, planet)}</b><br>"
            f"DE440 距离: {result['de440']['distance_au']:.6f} AU<br>"
            f"VSOP 距离: {result['vsop']['distance_au']:.6f} AU<br>"
            f"位置差: {result['delta']['distance_km']:.0f} km"
        )

        de_trace = dict(
            x=[de_position_au[0]],
            y=[de_position_au[1]],
            mode="markers",
            marker=dict(
                size=10,
                color=de_color,
                symbol="circle",
                line=dict(color=blend_hex_color(de_color, "#FFFFFF", 0.42), width=1.4),
            ),
            name=f"{PLANET_NAMES_CN.get(planet, planet)} · DE440",
            legendgroup=planet,
            hovertemplate=common_hover + "<br>模型: DE440<extra></extra>",
        )
        vsop_trace = dict(
            x=[vsop_position_au[0]],
            y=[vsop_position_au[1]],
            mode="markers",
            marker=dict(
                size=9,
                color=vsop_color,
                symbol="diamond",
                line=dict(color=blend_hex_color(vsop_color, "#000000", 0.25), width=0.8),
            ),
            name=f"{PLANET_NAMES_CN.get(planet, planet)} · VSOP",
            legendgroup=planet,
            hovertemplate=common_hover + "<br>模型: VSOP<extra></extra>",
        )

        if is_3d:
            fig.add_trace(go.Scatter3d(z=[de_position_au[2]], **de_trace))
            fig.add_trace(go.Scatter3d(z=[vsop_position_au[2]], **vsop_trace))
        else:
            fig.add_trace(go.Scatter(**de_trace))
            fig.add_trace(go.Scatter(**vsop_trace))

        if show_delta_links:
            link_style = dict(color=color, width=2)
            if is_3d:
                fig.add_trace(
                    go.Scatter3d(
                        x=[de_position_au[0], vsop_position_au[0]],
                        y=[de_position_au[1], vsop_position_au[1]],
                        z=[de_position_au[2], vsop_position_au[2]],
                        mode="lines",
                        line=link_style,
                        showlegend=False,
                        hovertemplate=f"{PLANET_NAMES_CN.get(planet, planet)} 模型偏差<extra></extra>",
                    )
                )
            else:
                fig.add_trace(
                    go.Scatter(
                        x=[de_position_au[0], vsop_position_au[0]],
                        y=[de_position_au[1], vsop_position_au[1]],
                        mode="lines",
                        line=link_style,
                        showlegend=False,
                        hovertemplate=f"{PLANET_NAMES_CN.get(planet, planet)} 模型偏差<extra></extra>",
                    )
                )

    if is_3d:
        fig.update_layout(
            scene=dict(
                xaxis=dict(
                    title="",
                    range=[-max_dist * 1.2, max_dist * 1.2],
                    showbackground=False,
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                    ticks="",
                    showticklabels=False,
                ),
                yaxis=dict(
                    title="",
                    range=[-max_dist * 1.2, max_dist * 1.2],
                    showbackground=False,
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                    ticks="",
                    showticklabels=False,
                ),
                zaxis=dict(
                    title="",
                    range=[-max_dist * 0.6, max_dist * 0.6],
                    showbackground=False,
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                    ticks="",
                    showticklabels=False,
                ),
                aspectmode="cube",
                bgcolor=space_background,
            ),
            height=760,
            legend=dict(
                x=0.01,
                y=0.99,
                bgcolor="rgba(5, 6, 8, 0.55)",
                bordercolor="rgba(159, 179, 200, 0.18)",
                borderwidth=1,
                font=dict(color="#e7eef6"),
            ),
            margin=dict(l=0, r=0, t=30, b=0),
            paper_bgcolor=space_background,
            plot_bgcolor=space_background,
            font=dict(color=axis_text_color),
        )
    else:
        fig.update_layout(
            xaxis=dict(
                title="X (AU)",
                scaleanchor="y",
                scaleratio=1,
                color=axis_text_color,
                gridcolor="rgba(159, 179, 200, 0.08)",
                zeroline=False,
            ),
            yaxis=dict(
                title="Y (AU)",
                color=axis_text_color,
                gridcolor="rgba(159, 179, 200, 0.08)",
                zeroline=False,
            ),
            height=680,
            hovermode="closest",
            paper_bgcolor=space_background,
            plot_bgcolor=space_background,
            font=dict(color=axis_text_color),
            legend=dict(
                bgcolor="rgba(5, 6, 8, 0.55)",
                bordercolor="rgba(159, 179, 200, 0.18)",
                borderwidth=1,
                font=dict(color="#e7eef6"),
            ),
        )

    return fig


def build_summary_table(results):
    """生成差异摘要表。"""
    rows = []
    for result in results:
        planet = result["planet"]
        rows.append(
            {
                "行星": PLANET_NAMES_CN.get(planet, planet),
                "DE440距离(AU)": round(result["de440"]["distance_au"], 6),
                "VSOP距离(AU)": round(result["vsop"]["distance_au"], 6),
                "位置差(km)": round(result["delta"]["distance_km"], 0),
                "位置差(AU)": round(result["delta"]["distance_au"], 8),
                "速度差(km/s)": round(result["delta"]["speed_km_s"], 5),
            }
        )
    return pd.DataFrame(rows)


def build_vector_dataframe(columns):
    """Render Tibetan encoded results as website-style column vectors."""
    max_len = max(len(values) for values in columns.values())
    rows = []
    for index in range(max_len):
        row = {"序号": index + 1}
        for label, values in columns.items():
            row[label] = values[index] if index < len(values) else ""
        rows.append(row)
    return pd.DataFrame(rows)


def format_tibetan_year_name(year):
    """Format Tibetan year as element + zodiac, matching the website convention."""
    return f"{TIBETAN_ELEMENTS[year % 10]}{TIBETAN_ZODIAC[year % 12]}年"


def render_planet_expanders(results):
    """渲染单行星详细数据。"""
    for result in results:
        planet = result["planet"]
        planet_name = PLANET_NAMES_CN.get(planet, planet)
        de_position_au = get_model_position_au(result, "de440")
        vsop_position_au = get_model_position_au(result, "vsop")
        de_speed = np.linalg.norm(result["de440"]["velocity_km_s"])
        vsop_speed = np.linalg.norm(result["vsop"]["velocity_km_s"])

        with st.expander(f"🛰️ {planet_name}", expanded=(planet == results[0]["planet"])):
            metric_col1, metric_col2 = st.columns(2)
            metric_col1.metric("DE440 距离", f"{result['de440']['distance_au']:.6f} AU")
            metric_col2.metric("VSOP 距离", f"{result['vsop']['distance_au']:.6f} AU")

            metric_col3, metric_col4 = st.columns(2)
            metric_col3.metric("DE440 速度", f"{de_speed:.3f} km/s")
            metric_col4.metric("VSOP 速度", f"{vsop_speed:.3f} km/s")

            st.metric("模型位置差", f"{result['delta']['distance_km']:.0f} km")
            st.caption("DE440 位置 (AU)")
            st.code(
                f"X: {de_position_au[0]: .6f}\nY: {de_position_au[1]: .6f}\nZ: {de_position_au[2]: .6f}",
                language="text",
            )
            st.caption("VSOP 位置 (AU)")
            st.code(
                f"X: {vsop_position_au[0]: .6f}\nY: {vsop_position_au[1]: .6f}\nZ: {vsop_position_au[2]: .6f}",
                language="text",
            )


def render_day_calendar_picker(year, month, default_day):
    """Render a month-view day picker with seven columns per week."""
    calendar_key = f"calendar_day_{year}_{month}"
    weeks = calendar.monthcalendar(year, month)
    weekday_labels = ["一", "二", "三", "四", "五", "六", "日"]
    today = datetime.utcnow()
    is_current_month = today.year == year and today.month == month

    if calendar_key not in st.session_state:
        st.session_state[calendar_key] = default_day

    selected_day = st.session_state[calendar_key]
    if selected_day > calendar.monthrange(year, month)[1]:
        selected_day = default_day
        st.session_state[calendar_key] = default_day

    today_label = f"今天 {today.day}" if is_current_month else "今天"
    st.sidebar.markdown(
        (
            "<div class='calendar-shell'>"
            f"<div class='calendar-title'><span>{year} 年 {month} 月</span>"
            f"<span class='calendar-today'>{today_label}</span></div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )
    header_cols = st.sidebar.columns(7)
    for index, label in enumerate(weekday_labels):
        header_cols[index].markdown(f"<div class='calendar-weekday'>{label}</div>", unsafe_allow_html=True)

    for week_index, week in enumerate(weeks):
        cols = st.sidebar.columns(7)
        for day_index, day_value in enumerate(week):
            if day_value == 0:
                cols[day_index].markdown("<div class='calendar-empty'></div>", unsafe_allow_html=True)
                continue
            label = str(day_value)
            if is_current_month and day_value == today.day and day_value != st.session_state[calendar_key]:
                label = f"{day_value} ·"
            if cols[day_index].button(
                label,
                key=f"{calendar_key}_{week_index}_{day_index}_{day_value}",
                type="primary" if day_value == st.session_state[calendar_key] else "secondary",
                use_container_width=True,
            ):
                st.session_state[calendar_key] = day_value

    return st.session_state[calendar_key]


def build_custom_time():
    """Render Gregorian Y/M/D + HH:MM input and return the selected UTC datetime."""
    current_utc = datetime.utcnow().replace(second=0, microsecond=0)
    years = list(range(1550, 2651))
    months = list(range(1, 13))

    year = st.sidebar.selectbox("年", years, index=years.index(current_utc.year))
    month = st.sidebar.selectbox("月", months, index=current_utc.month - 1)

    day_count = calendar.monthrange(year, month)[1]
    default_day = min(current_utc.day, day_count)
    day = render_day_calendar_picker(year, month, default_day)

    selected_clock = st.sidebar.time_input(
        "时间（UTC, HH:MM）",
        value=current_utc.time().replace(second=0, microsecond=0),
        step=300,
    )
    return datetime(year, month, day, selected_clock.hour, selected_clock.minute)


def main():
    """主应用。"""
    st.markdown('<div class="main-header">🪐 太阳系行星运动对照</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">以公历日期驱动 VSOP、DE440 与西藏时轮历五要素的对照展示</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="model-chip chip-vsop">VSOP / PyMeeus</span>'
        '<span class="model-chip chip-de440">DE440 数值星历</span>',
        unsafe_allow_html=True,
    )

    calc = init_calculator()

    st.sidebar.header("⚙️ 配置")
    st.sidebar.subheader("公历时间设置")
    selected_time = build_custom_time()

    st.sidebar.info(f"📅 当前查询时刻: {selected_time.strftime('%Y-%m-%d %H:%M')} UTC")

    st.sidebar.subheader("行星选择")
    preset = st.sidebar.selectbox("预设方案", ["自定义", "内行星", "外行星", "全部行星"])
    if preset == "内行星":
        default_planets = ["mercury", "venus", "earth", "mars"]
    elif preset == "外行星":
        default_planets = ["jupiter", "saturn", "uranus", "neptune"]
    elif preset == "全部行星":
        default_planets = SUPPORTED_PLANETS
    else:
        default_planets = ["earth", "mars", "jupiter"]

    selected_planets = st.sidebar.multiselect(
        "选择行星",
        SUPPORTED_PLANETS,
        default=default_planets,
        format_func=lambda planet: PLANET_NAMES_CN.get(planet, planet),
    )

    st.sidebar.subheader("可视化选项")
    view_mode = st.sidebar.radio("视图模式", ["3D对照", "2D对照"])
    show_orbits = st.sidebar.checkbox("显示轨道示意", value=True)
    show_delta_links = st.sidebar.checkbox("显示 VSOP / DE440 连线", value=True)

    if not selected_planets:
        st.warning("⚠️ 请至少选择一个行星。")
        return

    comparison_results = []
    for planet in selected_planets:
        try:
            comparison_results.append(compute_comparison(calc, planet, selected_time))
        except Exception as exc:
            st.error(f"{PLANET_NAMES_CN.get(planet, planet)} 计算失败: {exc}")

    if not comparison_results:
        st.warning("⚠️ 当前没有可展示的数据。")
        return

    st.subheader("🌌 行星位置对照图")
    figure = create_comparison_figure(calc, comparison_results, selected_time, view_mode, show_orbits, show_delta_links)
    st.plotly_chart(figure, width="stretch")

    st.subheader("📋 差异摘要")
    st.dataframe(build_summary_table(comparison_results), width="stretch", hide_index=True)

    st.subheader("🕉️ 西藏时轮历五要素")
    st.caption("先把公历自动换算成时轮历年月日，再按 `shilun_calendar_months12_compare_v1.m` 的步骤计算五要素。")
    try:
        tibetan_result = compute_tibetan_from_gregorian(selected_time)
        converted = tibetan_result["converted"]
        summary_col1, summary_col2 = st.columns([1.1, 1])
        with summary_col1:
            leap_label = "闰月" if converted["is_leap_month"] else "平月"
            occ_label = f"重日第 {converted['occurrence']} 次" if converted["occurrence"] > 1 else "正常日"
            st.info(
                f"公历 `{selected_time.strftime('%Y-%m-%d')}` 自动换算为 "
                f"`藏历 {converted['year']} 年（{format_tibetan_year_name(converted['year'])}）"
                f" {converted['month']} 月 {converted['day']} 日`"
                f"（{leap_label}，{occ_label}）"
            )
        with summary_col2:
            st.metric("换算状态", converted["status"])
            st.caption("换算引擎：`caltib / phugpa`")

        five_elements_table = build_vector_dataframe(
            {
                "定曜": tibetan_result["ding_yao"],
                "太阳日月宿": tibetan_result["taiyang_riyuexiu"],
                "定日": tibetan_result["ding_sun"],
                "会合": tibetan_result["huihe"],
                "太阴日月宿": tibetan_result["taiyin_riyuexiu"],
            }
        )
        base_table = build_vector_dataframe(
            {
                "积月闰余": [tibetan_result["jiyue"], tibetan_result["runyu"]],
                "曜基数": tibetan_result["yao_base"],
                "整零数": [tibetan_result["runyu"]],
                "太阳基数": tibetan_result["sun_base"],
            }
        )

        tibetan_col1, tibetan_col2 = st.columns([1.2, 1])
        with tibetan_col1:
            st.caption("五要素编码列向量")
            st.dataframe(five_elements_table, width="stretch", hide_index=True)
        with tibetan_col2:
            st.caption("月度基数列向量")
            st.dataframe(base_table, width="stretch", hide_index=True)
            st.metric("作用", str(tibetan_result["zuoyong"]))
    except Exception as exc:
        st.warning(f"藏历天文历算结果暂时无法显示：{exc}")

    with st.expander("⚡ 模型与性能说明"):
        performance = calc.get_performance_info()
        perf_col1, perf_col2 = st.columns(2)
        perf_col1.metric("DE440 查询速度", f"{performance['queries_per_second']:.0f} 次/秒")
        perf_col2.metric("DE440 单次查询", f"{performance['time_per_query_ms']:.3f} ms")
        st.markdown(
            """
### 当前页面如何工作

- `DE440` 使用 JPL 星历表 `de440.bsp`，通过切比雪夫插值实时查询位置。
- `VSOP` 使用 PyMeeus 的 VSOP87 解析公式，输出行星日心黄道位置。
- `月亮` 在 VSOP 侧使用 PyMeeus 月球模型，先算地月位置，再叠加到地球日心坐标。
- 为了和 DE440 放在同一张图上，本页将 VSOP 结果转换到了赤道直角坐标系。
- VSOP 速度使用中心差分近似，重点用于页面对照展示，不作为高精度动力学积分结果。
- `公历 -> 藏历` 当前通过 `caltib` 的 `phugpa` 引擎自动换算。
- `五要素` 当前按你指定的 `shilun_calendar_months12_compare_v1.m` 逻辑翻译为 Python 计算。

### 读图建议

- 圆点表示 `DE440`，菱形表示 `VSOP`。
- 两者之间的连线越短，说明该时刻两套模型在可视化尺度上越接近。
- 摘要表适合快速筛查偏差较大的行星，再展开右侧卡片看详细坐标。
- 传统模型目前和现代模型分开展示，因为它使用的是五要素与星宿编码体系，不是同一套直角坐标输入。
"""
        )


if __name__ == "__main__":
    main()
