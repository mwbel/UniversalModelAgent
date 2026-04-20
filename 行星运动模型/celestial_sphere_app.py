#!/usr/bin/env python3
"""
天球坐标系可视化应用
参考MATLAB视运动程序，实现地平坐标系和天球坐标系的3D可视化
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
from realtime_calculator import RealtimePlanetaryCalculator
from de_model import julian_date
import os

# 页面配置
st.set_page_config(
    page_title="天球坐标系可视化",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 添加自定义CSS来固定布局，减少抖动
st.markdown("""
<style>
    /* 固定主内容区域 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }

    /* 固定图表容器高度 */
    .stPlotlyChart {
        height: 800px !important;
    }

    /* 减少不必要的动画 */
    * {
        transition: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 初始化计算器
@st.cache_resource
def init_calculator():
    """初始化计算器（缓存）"""
    spk_file = 'de440.bsp'
    if not os.path.exists(spk_file):
        st.error(f"❌ 未找到星历文件: {spk_file}")
        st.stop()
    return RealtimePlanetaryCalculator(spk_file)

def calculate_sun_position_horizontal(calc, date, latitude, longitude, timezone):
    """
    计算太阳在地平坐标系中的位置

    参数:
        calc: 计算器实例
        date: 日期时间
        latitude: 纬度（度）
        longitude: 经度（度）
        timezone: 时区

    返回:
        azimuth: 方位角（度，从北向东）
        altitude: 高度角（度）
        declination: 赤纬角（度）
    """
    # 计算太阳位置（地心坐标系）
    pos, vel, dist = calc.compute_position('sun', date, relative_to='barycenter')

    # 计算地球位置
    earth_pos, earth_vel, earth_dist = calc.compute_position('earth', date, relative_to='barycenter')

    # 太阳相对地球的位置
    sun_rel = pos - earth_pos

    # 转换为球坐标
    x, y, z = sun_rel
    r = np.sqrt(x**2 + y**2 + z**2)

    # 计算赤经和赤纬
    ra = np.arctan2(y, x) * 180 / np.pi  # 赤经（度）
    dec = np.arcsin(z / r) * 180 / np.pi  # 赤纬（度）

    # 计算本地恒星时（简化计算）
    jd = julian_date(date.year, date.month, date.day, date.hour, date.minute, date.second)
    T = (jd - 2451545.0) / 36525.0
    GMST = 280.46061837 + 360.98564736629 * (jd - 2451545.0) + 0.000387933 * T**2
    GMST = GMST % 360
    LST = (GMST + longitude) % 360  # 本地恒星时

    # 计算时角
    hour_angle = (LST - ra) % 360
    if hour_angle > 180:
        hour_angle -= 360

    # 转换为地平坐标
    lat_rad = np.radians(latitude)
    ha_rad = np.radians(hour_angle)
    dec_rad = np.radians(dec)

    # 高度角
    altitude = np.arcsin(np.sin(lat_rad) * np.sin(dec_rad) +
                        np.cos(lat_rad) * np.cos(dec_rad) * np.cos(ha_rad))
    altitude = np.degrees(altitude)

    # 方位角（从北向东）
    azimuth = np.arctan2(np.sin(ha_rad),
                        np.cos(ha_rad) * np.sin(lat_rad) - np.tan(dec_rad) * np.cos(lat_rad))
    azimuth = np.degrees(azimuth)
    azimuth = (azimuth + 360) % 360

    return azimuth, altitude, dec

def create_celestial_sphere(latitude, show_horizon=True, show_equator=True, show_ecliptic=True):
    """
    创建天球坐标系

    参数:
        latitude: 观测地纬度
        show_horizon: 是否显示地平面
        show_equator: 是否显示天赤道
        show_ecliptic: 是否显示黄道
    """
    fig = go.Figure()

    # 创建天球（半透明球面）
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        colorscale=[[0, 'rgba(100,100,150,0.1)'], [1, 'rgba(100,100,150,0.1)']],
        showscale=False,
        hoverinfo='skip',
        name='天球'
    ))

    # 地平面（z=0平面）
    if show_horizon:
        theta = np.linspace(0, 2*np.pi, 100)
        x_horizon = np.cos(theta)
        y_horizon = np.sin(theta)
        z_horizon = np.zeros_like(theta)

        fig.add_trace(go.Scatter3d(
            x=x_horizon, y=y_horizon, z=z_horizon,
            mode='lines',
            line=dict(color='gray', width=4),
            name='地平圈',
            hoverinfo='skip'
        ))

        # 填充地平面
        theta_fill = np.linspace(0, 2*np.pi, 50)
        r_fill = np.linspace(0, 1, 20)
        theta_grid, r_grid = np.meshgrid(theta_fill, r_fill)
        x_fill = r_grid * np.cos(theta_grid)
        y_fill = r_grid * np.sin(theta_grid)
        z_fill = np.zeros_like(x_fill)

        fig.add_trace(go.Surface(
            x=x_fill, y=y_fill, z=z_fill,
            colorscale=[[0, 'rgba(100,100,100,0.3)'], [1, 'rgba(100,100,100,0.3)']],
            showscale=False,
            hoverinfo='skip',
            name='地平面'
        ))

    # 天赤道（与地球赤道平行）
    if show_equator:
        theta = np.linspace(0, 2*np.pi, 100)
        x_equator = np.cos(theta)
        y_equator = np.sin(theta)
        z_equator = np.zeros_like(theta)

        fig.add_trace(go.Scatter3d(
            x=x_equator, y=y_equator, z=z_equator,
            mode='lines',
            line=dict(color='cyan', width=2, dash='dot'),
            name='天赤道',
            hoverinfo='skip'
        ))

    # 黄道（倾斜23.5度）
    if show_ecliptic:
        theta = np.linspace(0, 2*np.pi, 100)
        obliquity = np.radians(23.5)  # 黄赤交角
        x_ecliptic = np.cos(theta)
        y_ecliptic = np.sin(theta) * np.cos(obliquity)
        z_ecliptic = np.sin(theta) * np.sin(obliquity)

        fig.add_trace(go.Scatter3d(
            x=x_ecliptic, y=y_ecliptic, z=z_ecliptic,
            mode='lines',
            line=dict(color='yellow', width=2, dash='dot'),
            name='黄道',
            hoverinfo='skip'
        ))

    # 天轴（连接南北天极）
    lat_rad = np.radians(latitude)
    north_pole = np.array([0, np.cos(lat_rad), np.sin(lat_rad)]) * 1.3
    south_pole = -north_pole

    fig.add_trace(go.Scatter3d(
        x=[south_pole[0], north_pole[0]],
        y=[south_pole[1], north_pole[1]],
        z=[south_pole[2], north_pole[2]],
        mode='lines',
        line=dict(color='white', width=3, dash='dash'),
        name='天轴',
        hoverinfo='skip'
    ))

    # 标记北天极
    fig.add_trace(go.Scatter3d(
        x=[north_pole[0]], y=[north_pole[1]], z=[north_pole[2]],
        mode='markers+text',
        marker=dict(size=8, color='white'),
        text=['北天极'],
        textposition='top center',
        textfont=dict(color='white', size=12),
        name='北天极',
        hoverinfo='skip'
    ))

    # 标记方位
    directions = {
        '东': (1.2, 0, 0),
        '西': (-1.2, 0, 0),
        '南': (0, -1.2, 0),
        '北': (0, 1.2, 0),
        '天顶': (0, 0, 1.2)
    }

    for name, pos in directions.items():
        fig.add_trace(go.Scatter3d(
            x=[pos[0]], y=[pos[1]], z=[pos[2]],
            mode='text',
            text=[name],
            textfont=dict(color='white', size=14),
            name=name,
            hoverinfo='skip',
            showlegend=False
        ))

    return fig

def add_sun_annual_path(fig, calc, year, latitude, longitude, timezone, fixed_hour=12):
    """
    添加太阳周年视运动轨迹（光行迹）
    在固定时间（如每天12:00）记录太阳位置，形成一年的轨迹
    """
    days_in_year = 365 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    positions = []
    dates = []

    for day in range(days_in_year):
        date = datetime(year, 1, 1) + timedelta(days=day)
        date = date.replace(hour=fixed_hour, minute=0, second=0)

        try:
            azimuth, altitude, dec = calculate_sun_position_horizontal(
                calc, date, latitude, longitude, timezone
            )

            # 转换为笛卡尔坐标（地平坐标系）
            az_rad = np.radians(azimuth)
            alt_rad = np.radians(altitude)

            x = np.cos(alt_rad) * np.sin(az_rad)
            y = np.cos(alt_rad) * np.cos(az_rad)
            z = np.sin(alt_rad)

            positions.append([x, y, z])
            dates.append(date)
        except:
            continue

    if positions:
        positions = np.array(positions)

        fig.add_trace(go.Scatter3d(
            x=positions[:, 0],
            y=positions[:, 1],
            z=positions[:, 2],
            mode='lines+markers',
            line=dict(color='yellow', width=3),
            marker=dict(size=2, color='yellow'),
            name=f'太阳周年轨迹({fixed_hour}:00)',
            hovertext=[d.strftime('%Y-%m-%d') for d in dates],
            hoverinfo='text'
        ))

        # 标记特殊日期（春分、夏至、秋分、冬至）
        special_days = [80, 172, 266, 355]  # 大约的日期
        special_names = ['春分', '夏至', '秋分', '冬至']
        colors = ['green', 'red', 'orange', 'blue']

        for day, name, color in zip(special_days, special_names, colors):
            if day < len(positions):
                fig.add_trace(go.Scatter3d(
                    x=[positions[day, 0]],
                    y=[positions[day, 1]],
                    z=[positions[day, 2]],
                    mode='markers+text',
                    marker=dict(size=8, color=color),
                    text=[name],
                    textposition='top center',
                    textfont=dict(color=color, size=12),
                    name=name,
                    hoverinfo='skip'
                ))

    return fig

def main():
    """主应用"""

    st.title("🌍 天球坐标系可视化")
    st.markdown("基于地平坐标系的太阳视运动轨迹")

    # 创建固定的占位符（在侧边栏配置之前）
    chart_placeholder = st.empty()

    # 初始化计算器
    calc = init_calculator()

    # 侧边栏配置
    st.sidebar.header("⚙️ 观测地点配置")

    # 预设地点
    preset_locations = {
        "北京": (116.39, 39.90, 8),
        "上海": (121.47, 31.23, 8),
        "拉萨": (91.13, 29.65, 8),
        "广州": (113.26, 23.13, 8),
        "乌鲁木齐": (87.62, 43.82, 8),
        "自定义": (0, 0, 0)
    }

    location = st.sidebar.selectbox("选择地点", list(preset_locations.keys()))

    if location == "自定义":
        longitude = st.sidebar.number_input("经度（度）", -180.0, 180.0, 116.39)
        latitude = st.sidebar.number_input("纬度（度）", -90.0, 90.0, 39.90)
        timezone = st.sidebar.number_input("时区", -12, 12, 8)
    else:
        longitude, latitude, timezone = preset_locations[location]
        st.sidebar.info(f"📍 经度: {longitude}°, 纬度: {latitude}°, 时区: UTC+{timezone}")

    # 年份选择
    year = st.sidebar.number_input("年份", 2000, 2100, 2025)

    # 固定观测时间
    fixed_hour = st.sidebar.slider("固定观测时间（小时）", 0, 23, 12)

    # 显示选项
    st.sidebar.subheader("显示选项")
    show_horizon = st.sidebar.checkbox("显示地平面", value=True)
    show_equator = st.sidebar.checkbox("显示天赤道", value=True)
    show_ecliptic = st.sidebar.checkbox("显示黄道", value=True)
    show_annual_path = st.sidebar.checkbox("显示太阳周年轨迹", value=True)

    # 创建可视化
    with st.spinner("正在生成天球坐标系..."):
        fig = create_celestial_sphere(latitude, show_horizon, show_equator, show_ecliptic)

        if show_annual_path:
            fig = add_sun_annual_path(fig, calc, year, latitude, longitude, timezone, fixed_hour)

        # 设置布局
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='东-西', showgrid=False, showbackground=False),
                yaxis=dict(title='南-北', showgrid=False, showbackground=False),
                zaxis=dict(title='天顶-天底', showgrid=False, showbackground=False),
                aspectmode='cube',
                bgcolor='black'
            ),
            paper_bgcolor='black',
            plot_bgcolor='black',
            height=800,
            showlegend=True,
            legend=dict(x=0.02, y=0.98, bgcolor='rgba(0,0,0,0.5)', font=dict(color='white')),
            margin=dict(l=0, r=0, t=30, b=0)
        )

    # 使用占位符显示图表，实现原地更新
    with chart_placeholder.container():
        st.plotly_chart(fig, use_container_width=True, key="celestial_sphere_chart")

    # 说明信息
    with st.expander("ℹ️ 说明"):
        st.markdown("""
        ### 天球坐标系说明

        **坐标系定义**：
        - **地平坐标系**：以观测者为中心，地平面为基准
        - **X轴**：指向东方
        - **Y轴**：指向北方
        - **Z轴**：指向天顶

        **主要元素**：
        - **地平圈**：灰色圆圈，表示地平线
        - **天赤道**：青色虚线，与地球赤道平行
        - **黄道**：黄色虚线，太阳在天球上的视运动轨迹
        - **天轴**：白色虚线，连接南北天极

        **太阳周年视运动轨迹（光行迹）**：
        - 在固定时间（如每天12:00）记录太阳位置
        - 一年形成的轨迹呈"8"字形（日行迹）
        - 标记了春分、夏至、秋分、冬至四个节气点

        **参考**：
        - 本可视化参考了MATLAB视运动程序的实现
        - 使用JPL DE440星历表计算太阳位置
        - 采用地平坐标系进行展示
        """)

if __name__ == "__main__":
    main()
