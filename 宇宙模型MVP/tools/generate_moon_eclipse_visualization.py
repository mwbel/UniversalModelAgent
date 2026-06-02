from __future__ import annotations

from calendar import isleap
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from PIL import Image
from plotly.subplots import make_subplots
from skyfield.api import load


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(
    "/Users/Min369/Documents/同步空间/Manju/AIProjects/AlVisualization/main-app/modules/astronomy/src"
)
OUTPUT_PATH = ROOT / "frontend" / "interactive-visualizations" / "legacy" / "generated" / "moon-eclipse-slider.html"

YEAR = datetime.now().year
SLIDER_DAYS = 366 if isleap(YEAR) else 365
MOON_DISC_RES = 256
AU_RANGE = 1.2
MOON_SCALE = 27


ts = load.timescale()
eph = load(str(SOURCE_DIR / "de421.bsp"))
sun, earth, moon = eph["sun"], eph["earth"], eph["moon"]
moon_texture = Image.open(SOURCE_DIR / "moon_texture_map.tif").convert("L")
moon_texture = np.array(moon_texture) / 255.0


def unit(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    norm = np.linalg.norm(vector)
    if norm < 1e-12:
        return vector * 0.0
    return vector / norm


def earth_helio(time_point):
    return sun.at(time_point).observe(earth).position.au


def moon_geo(time_point):
    return earth.at(time_point).observe(moon).position.au


def moon_helio(time_point):
    return earth_helio(time_point) + moon_geo(time_point)


def make_moon_phase_image(time_point, resolution: int = MOON_DISC_RES):
    e2m = moon_geo(time_point)
    m2s = -moon_helio(time_point)
    observer = unit(e2m)
    sunlight = unit(m2s)

    north_pole = np.array([0.0, 0.0, 1.0])
    x_axis = unit(np.cross(north_pole, observer))
    y_axis = unit(np.cross(observer, x_axis))

    lin = np.linspace(-1, 1, resolution, endpoint=False)
    x_grid, y_grid = np.meshgrid(lin, lin)
    radius_sq = x_grid * x_grid + y_grid * y_grid
    mask = radius_sq <= (1.0 - 1e-6)
    z_grid = np.zeros_like(x_grid)
    z_grid[mask] = np.sqrt(1.0 - radius_sq[mask])

    lon = np.arctan2(y_grid[mask], x_grid[mask])
    lat = np.arcsin(z_grid[mask])
    theta = np.arctan2(e2m[1], e2m[0])
    lon = lon - theta

    height, width = moon_texture.shape
    texture_x = ((lon + np.pi) / (2 * np.pi)) * (width - 1)
    texture_y = ((np.pi / 2 - lat) / np.pi) * (height - 1)
    texture_x = np.clip(texture_x.round().astype(int), 0, width - 1)
    texture_y = np.clip(texture_y.round().astype(int), 0, height - 1)

    texture_values = np.zeros_like(x_grid, dtype=float)
    texture_values[mask] = moon_texture[texture_y, texture_x]

    ambient = 0.08
    intensity = np.zeros_like(x_grid, dtype=float)
    intensity[mask] = np.clip(
        ambient + sunlight[0] * x_grid[mask] + sunlight[1] * y_grid[mask] + sunlight[2] * z_grid[mask],
        ambient,
        1.0,
    )

    values = np.zeros_like(x_grid, dtype=float)
    values[mask] = texture_values[mask] * intensity[mask]
    values[mask] = values[mask] ** 0.6

    image = np.zeros((resolution, resolution, 4), dtype=np.uint8)
    gray = (values * 255).astype(np.uint8)
    image[..., 0] = gray
    image[..., 1] = gray
    image[..., 2] = gray
    image[..., 3] = mask.astype(np.uint8) * 255
    return image


def calc_phase_name(time_point):
    earth_to_moon = moon_geo(time_point)
    earth_to_sun = sun.at(time_point).observe(earth).position.au
    cos_phi = np.dot(earth_to_moon, earth_to_sun) / (
        np.linalg.norm(earth_to_moon) * np.linalg.norm(earth_to_sun)
    )
    cos_phi = np.clip(cos_phi, -1.0, 1.0)
    illumination = (1 + cos_phi) / 2.0

    if illumination < 0.03:
        return "新月"
    if illumination < 0.5:
        return "娥眉月"
    if abs(illumination - 0.5) < 0.03 and np.cross(earth_to_sun, earth_to_moon)[2] > 0:
        return "上弦月"
    if 0.5 < illumination < 0.97 and np.dot(earth_to_sun, earth_to_moon) < 0:
        return "盈凸月"
    if illumination >= 0.97:
        return "满月"
    if 0.5 < illumination < 0.97 and np.dot(earth_to_sun, earth_to_moon) > 0:
        return "亏凸月"
    if abs(illumination - 0.5) < 0.03 and np.cross(earth_to_sun, earth_to_moon)[2] < 0:
        return "下弦月"
    return "残月"


def build_figure():
    start_date = date(YEAR, 1, 1)
    days = [start_date + timedelta(days=index) for index in range(SLIDER_DAYS)]
    times = [ts.utc(day.year, day.month, day.day) for day in days]

    earth_xyz = np.array([earth_helio(time_point) for time_point in times])
    moon_geo_xyz = np.array([moon_geo(time_point) for time_point in times])
    moon_xyz = earth_xyz + moon_geo_xyz * MOON_SCALE

    days_dense = [start_date + timedelta(days=index * 0.1) for index in range(SLIDER_DAYS * 10)]
    times_dense = [ts.utc(day.year, day.month, day.day) for day in days_dense]
    earth_orbit_dense = np.array([earth_helio(time_point) for time_point in times_dense]).T
    moon_orbit_dense = np.array(
        [(earth_helio(time_point) + moon_geo(time_point) * MOON_SCALE) for time_point in times_dense]
    ).T

    figure = make_subplots(
        rows=1,
        cols=2,
        column_widths=[0.68, 0.32],
        specs=[[{"type": "scene"}, {"type": "xy"}]],
        horizontal_spacing=0.04,
        subplot_titles=("地月系统与月相联动演示", "月相（地球视角）"),
    )

    idx0 = 0
    ex0, ey0, ez0 = earth_xyz[idx0]
    mx0, my0, mz0 = moon_xyz[idx0]
    phase_text0 = calc_phase_name(times[idx0])
    image0 = make_moon_phase_image(times[idx0])

    figure.add_trace(
        go.Scatter3d(
            x=earth_orbit_dense[0],
            y=earth_orbit_dense[1],
            z=earth_orbit_dense[2],
            mode="lines",
            line=dict(width=2, color="rgba(100,160,255,0.35)"),
            name="地球轨道",
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Scatter3d(
            x=moon_orbit_dense[0],
            y=moon_orbit_dense[1],
            z=moon_orbit_dense[2],
            mode="lines",
            line=dict(width=3, color="rgba(255,255,255,0.82)"),
            name="月球轨道",
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Scatter3d(x=[0], y=[0], z=[0], mode="markers", marker=dict(size=10, color="orange"), name="太阳"),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Scatter3d(
            x=[ex0], y=[ey0], z=[ez0], mode="markers", marker=dict(size=6, color="deepskyblue"), name="地球"
        ),
        row=1,
        col=1,
    )
    figure.add_trace(
        go.Scatter3d(x=[mx0], y=[my0], z=[mz0], mode="markers", marker=dict(size=4, color="white"), name="月亮"),
        row=1,
        col=1,
    )
    figure.add_trace(go.Image(z=image0), row=1, col=2)

    frames = []
    for index, time_point in enumerate(times):
        ex, ey, ez = earth_xyz[index]
        mgx, mgy, mgz = moon_geo_xyz[index]
        mx = ex + MOON_SCALE * mgx
        my = ey + MOON_SCALE * mgy
        mz = ez + MOON_SCALE * mgz
        frames.append(
            go.Frame(
                name=str(days[index]),
                data=[
                    go.Scatter3d(
                        x=[ex], y=[ey], z=[ez], mode="markers", marker=dict(size=6, color="rgba(0,191,255,0.7)")
                    ),
                    go.Scatter3d(x=[mx], y=[my], z=[mz], mode="markers", marker=dict(size=4, color="white")),
                    go.Image(z=make_moon_phase_image(time_point)),
                ],
                traces=[3, 4, 5],
                layout=go.Layout(
                    annotations=[
                        dict(
                            text=calc_phase_name(time_point),
                            xref="paper",
                            yref="paper",
                            x=0.85,
                            y=0.86,
                            xanchor="center",
                            yanchor="bottom",
                            showarrow=False,
                            font=dict(size=16, color="white"),
                        )
                    ]
                ),
            )
        )

    figure.update(frames=frames)
    figure.update_xaxes(visible=False, scaleanchor="y", scaleratio=1, fixedrange=True, row=1, col=2)
    figure.update_yaxes(visible=False, fixedrange=True, row=1, col=2)
    figure.update_layout(
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        margin=dict(l=20, r=20, t=48, b=80),
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor="black",
            camera=dict(eye=dict(x=0, y=-2.0, z=1.5)),
            dragmode="orbit",
        ),
        scene_aspectmode="data",
        updatemenus=[
            {
                "type": "buttons",
                "direction": "left",
                "x": 0.23,
                "y": -0.05,
                "xanchor": "left",
                "yanchor": "top",
                "showactive": False,
                "buttons": [
                    {
                        "label": "▶ Play",
                        "method": "animate",
                        "args": [
                            None,
                            {"frame": {"duration": 80, "redraw": True}, "fromcurrent": True, "transition": {"duration": 0}},
                        ],
                    },
                    {
                        "label": "⏸ Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": True},
                                "mode": "immediate",
                                "transition": {"duration": 0},
                            },
                        ],
                    },
                ],
            },
            {
                "buttons": [
                    {
                        "label": str(year),
                        "method": "animate",
                        "args": [
                            [frames[0].name],
                            {"mode": "immediate", "frame": {"duration": 0, "redraw": True}, "transition": {"duration": 0}},
                        ],
                    }
                    for year in range(2023, 2027)
                ],
                "direction": "down",
                "x": 0.05,
                "y": 1.15,
                "xanchor": "left",
                "yanchor": "top",
            },
        ],
        sliders=[
            {
                "active": 0,
                "x": 0.23,
                "y": -0.18,
                "len": 0.62,
                "currentvalue": {"prefix": "日期：", "visible": True},
                "steps": [
                    {
                        "args": [
                            [frame.name],
                            {"mode": "immediate", "frame": {"duration": 0, "redraw": True}, "transition": {"duration": 0}},
                        ],
                        "label": frame.name[5:],
                        "method": "animate",
                    }
                    for frame in frames
                ],
            }
        ],
        annotations=[
            dict(
                text=phase_text0,
                xref="paper",
                yref="paper",
                x=0.85,
                y=0.86,
                xanchor="center",
                yanchor="bottom",
                showarrow=False,
                font=dict(size=16, color="white"),
            )
        ],
    )
    figure.update_scenes(
        xaxis_range=[-AU_RANGE, AU_RANGE],
        yaxis_range=[-AU_RANGE, AU_RANGE],
        zaxis_range=[-AU_RANGE, AU_RANGE],
    )
    return figure


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    figure = build_figure()
    figure.write_html(
        OUTPUT_PATH,
        include_plotlyjs="cdn",
        full_html=True,
        config={"displaylogo": False, "responsive": True},
    )
    print(f"Generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
