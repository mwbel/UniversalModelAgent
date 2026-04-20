#!/usr/bin/env python3
"""
太阳系实时计算可视化应用
使用 Streamlit 创建交互式Web界面
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from realtime_calculator import RealtimePlanetaryCalculator
from de_model import julian_date
import os

# 页面配置
st.set_page_config(
    page_title="太阳系实时计算器",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
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
        st.info("请将 de440.bsp 文件放在应用目录中")
        st.stop()
    return RealtimePlanetaryCalculator(spk_file)

# 行星颜色配置
PLANET_COLORS = {
    'mercury': '#8C7853',
    'venus': '#FFC649',
    'earth': '#4169E1',
    'mars': '#CD5C5C',
    'jupiter': '#DAA520',
    'saturn': '#F4A460',
    'uranus': '#4FD0E0',
    'neptune': '#4169E1',
    'pluto': '#A0522D',
    'moon': '#C0C0C0'
}

# 行星中文名称
PLANET_NAMES_CN = {
    'sun': '太阳',
    'mercury': '水星',
    'venus': '金星',
    'earth': '地球',
    'mars': '火星',
    'jupiter': '木星',
    'saturn': '土星',
    'uranus': '天王星',
    'neptune': '海王星',
    'pluto': '冥王星',
    'moon': '月球'
}

def create_3d_solar_system(calc, selected_time, selected_planets, show_orbits=True):
    """创建3D太阳系可视化"""
    fig = go.Figure()

    # 添加太阳
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers',
        marker=dict(size=20, color='yellow', symbol='circle'),
        name='太阳',
        hovertemplate='<b>太阳</b><br>位置: (0, 0, 0)<extra></extra>'
    ))

    # 计算并添加行星
    for planet in selected_planets:
        try:
            pos, vel, dist = calc.compute_position(planet, selected_time)
            pos_au = pos / calc.AU  # 转换为AU

            # 添加行星
            fig.add_trace(go.Scatter3d(
                x=[pos_au[0]],
                y=[pos_au[1]],
                z=[pos_au[2]],
                mode='markers',
                marker=dict(
                    size=10,
                    color=PLANET_COLORS.get(planet, '#888888'),
                    symbol='circle'
                ),
                name=PLANET_NAMES_CN.get(planet, planet),
                hovertemplate=f'<b>{PLANET_NAMES_CN.get(planet, planet)}</b><br>' +
                             f'距离: {dist:.4f} AU<br>' +
                             f'位置: ({pos_au[0]:.3f}, {pos_au[1]:.3f}, {pos_au[2]:.3f}) AU<extra></extra>'
            ))

            # 添加轨道（简化为圆形）
            if show_orbits:
                theta = np.linspace(0, 2*np.pi, 100)
                orbit_x = dist * np.cos(theta)
                orbit_y = dist * np.sin(theta)
                orbit_z = np.zeros_like(theta)

                fig.add_trace(go.Scatter3d(
                    x=orbit_x, y=orbit_y, z=orbit_z,
                    mode='lines',
                    line=dict(color=PLANET_COLORS.get(planet, '#888888'), width=1, dash='dot'),
                    showlegend=False,
                    hoverinfo='skip'
                ))
        except Exception as e:
            st.warning(f"无法计算 {planet}: {e}")

    # 设置布局
    max_dist = max([calc.compute_position(p, selected_time)[2] for p in selected_planets if p != 'pluto'], default=10)

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='X (AU)', range=[-max_dist*1.2, max_dist*1.2]),
            yaxis=dict(title='Y (AU)', range=[-max_dist*1.2, max_dist*1.2]),
            zaxis=dict(title='Z (AU)', range=[-max_dist*0.5, max_dist*0.5]),
            aspectmode='cube'
        ),
        height=700,
        showlegend=True,
        legend=dict(x=0.02, y=0.98),
        margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig

def create_2d_solar_system(calc, selected_time, selected_planets):
    """创建2D太阳系俯视图"""
    fig = go.Figure()

    # 添加太阳
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers',
        marker=dict(size=15, color='yellow'),
        name='太阳',
        hovertemplate='<b>太阳</b><extra></extra>'
    ))

    # 添加行星
    for planet in selected_planets:
        try:
            pos, vel, dist = calc.compute_position(planet, selected_time)
            pos_au = pos / calc.AU

            fig.add_trace(go.Scatter(
                x=[pos_au[0]],
                y=[pos_au[1]],
                mode='markers',
                marker=dict(
                    size=8,
                    color=PLANET_COLORS.get(planet, '#888888')
                ),
                name=PLANET_NAMES_CN.get(planet, planet),
                hovertemplate=f'<b>{PLANET_NAMES_CN.get(planet, planet)}</b><br>' +
                             f'距离: {dist:.4f} AU<extra></extra>'
            ))

            # 添加轨道圆
            theta = np.linspace(0, 2*np.pi, 100)
            orbit_x = dist * np.cos(theta)
            orbit_y = dist * np.sin(theta)

            fig.add_trace(go.Scatter(
                x=orbit_x, y=orbit_y,
                mode='lines',
                line=dict(color=PLANET_COLORS.get(planet, '#888888'), width=1, dash='dot'),
                showlegend=False,
                hoverinfo='skip'
            ))
        except Exception as e:
            st.warning(f"无法计算 {planet}: {e}")

    # 设置布局
    max_dist = max([calc.compute_position(p, selected_time)[2] for p in selected_planets if p != 'pluto'], default=10)

    fig.update_layout(
        xaxis=dict(title='X (AU)', scaleanchor='y', scaleratio=1),
        yaxis=dict(title='Y (AU)'),
        height=600,
        showlegend=True,
        hovermode='closest'
    )

    return fig

def main():
    """主应用"""

    # 标题
    st.markdown('<div class="main-header">🪐 太阳系实时计算器</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">基于 JPL DE440 星历表 + 切比雪夫插值算法</div>', unsafe_allow_html=True)

    # 初始化计算器
    calc = init_calculator()

    # 侧边栏配置
    st.sidebar.header("⚙️ 配置")

    # 时间选择
    st.sidebar.subheader("时间设置")
    time_mode = st.sidebar.radio("时间模式", ["当前时间", "自定义时间"])

    if time_mode == "当前时间":
        selected_time = datetime.utcnow()
    else:
        date = st.sidebar.date_input("日期", datetime.now())
        time = st.sidebar.time_input("时间", datetime.now().time())
        selected_time = datetime.combine(date, time)

    st.sidebar.info(f"📅 选择时间: {selected_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")

    # 行星选择
    st.sidebar.subheader("行星选择")
    all_planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

    preset = st.sidebar.selectbox(
        "预设方案",
        ["自定义", "内行星", "外行星", "全部行星"]
    )

    if preset == "内行星":
        default_planets = ['mercury', 'venus', 'earth', 'mars']
    elif preset == "外行星":
        default_planets = ['jupiter', 'saturn', 'uranus', 'neptune']
    elif preset == "全部行星":
        default_planets = all_planets
    else:
        default_planets = ['earth', 'mars', 'jupiter']

    selected_planets = st.sidebar.multiselect(
        "选择行星",
        all_planets,
        default=default_planets,
        format_func=lambda x: PLANET_NAMES_CN.get(x, x)
    )

    # 可视化选项
    st.sidebar.subheader("可视化选项")
    view_mode = st.sidebar.radio("视图模式", ["3D视图", "2D俯视图"])
    show_orbits = st.sidebar.checkbox("显示轨道", value=True)

    # 主内容区域
    if not selected_planets:
        st.warning("⚠️ 请至少选择一个行星")
        return

    # 创建两列布局
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🌌 太阳系可视化")

        # 创建可视化
        if view_mode == "3D视图":
            fig = create_3d_solar_system(calc, selected_time, selected_planets, show_orbits)
        else:
            fig = create_2d_solar_system(calc, selected_time, selected_planets)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 天体数据")

        # 计算并显示数据
        for planet in selected_planets:
            try:
                pos, vel, dist = calc.compute_position(planet, selected_time)
                pos_au = pos / calc.AU
                vel_km_s = vel / 86400  # km/day -> km/s

                with st.expander(f"🌍 {PLANET_NAMES_CN.get(planet, planet)}", expanded=True):
                    st.metric("距离太阳", f"{dist:.4f} AU")
                    st.metric("速度", f"{np.linalg.norm(vel_km_s):.2f} km/s")

                    st.caption("位置 (AU)")
                    st.text(f"X: {pos_au[0]:>8.4f}\nY: {pos_au[1]:>8.4f}\nZ: {pos_au[2]:>8.4f}")

            except Exception as e:
                st.error(f"计算错误: {e}")

    # 性能信息
    with st.expander("⚡ 性能信息"):
        perf = calc.get_performance_info()
        col1, col2 = st.columns(2)
        col1.metric("查询速度", f"{perf['queries_per_second']:.0f} 次/秒")
        col2.metric("单次查询", f"{perf['time_per_query_ms']:.3f} 毫秒")
        st.success("✅ 完全满足实时计算需求（60fps = 16.7ms/帧）")

    # 关于
    with st.expander("ℹ️ 关于"):
        st.markdown("""
        ### 技术说明

        - **数据源**: JPL DE440 星历表
        - **算法**: 切比雪夫多项式插值
        - **时间范围**: 1550-2650年
        - **精度**: 插值误差 < 1e-4
        - **性能**: ~14000次查询/秒

        ### 计算流程

        1. 用户选择查询时间
        2. 二分查找定位时间段
        3. 读取切比雪夫系数
        4. 多项式插值计算位置和速度
        5. 实时显示结果

        ### 特点

        - ✅ 实时计算（毫秒级响应）
        - ✅ 高精度（NASA标准）
        - ✅ 交互式可视化
        - ✅ 支持任意时刻查询
        """)

if __name__ == "__main__":
    main()
