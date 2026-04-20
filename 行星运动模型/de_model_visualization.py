#!/usr/bin/env python3
"""
DE模型可视化示例

展示如何使用DE模型算法计算和可视化行星轨道
"""

import numpy as np
import matplotlib.pyplot as plt
from de_model import ChebyshevInterpolator, DEModel, julian_date

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def create_circular_orbit_model(radius_au: float, period_days: float,
                                  name: str = "planet") -> tuple:
    """
    创建圆轨道模型的切比雪夫系数

    参数:
        radius_au: 轨道半径（天文单位）
        period_days: 轨道周期（天）
        name: 天体名称

    返回:
        (model, t_start, t_end) 元组
    """
    AU = 149597870.7  # km
    radius = radius_au * AU

    # 时间范围：一个完整周期
    t_start = 2451545.0  # J2000.0
    t_end = t_start + period_days

    # 角速度
    omega = 2 * np.pi / period_days

    # 使用切比雪夫多项式拟合圆轨道
    # 对于圆轨道：x = r*cos(ωt), y = r*sin(ωt)
    # 使用足够多的系数来精确表示
    n_coeffs = 15

    # 在时间区间内采样，计算切比雪夫系数
    t_samples = np.linspace(t_start, t_end, 100)

    # 归一化时间
    t_norm = 2.0 * (t_samples - t_start) / (t_end - t_start) - 1.0

    # 计算实际位置
    theta = omega * (t_samples - t_start)
    x_samples = radius * np.cos(theta)
    y_samples = radius * np.sin(theta)
    z_samples = np.zeros_like(x_samples)

    # 使用最小二乘法拟合切比雪夫系数
    T_matrix = np.zeros((len(t_norm), n_coeffs))
    for i, t in enumerate(t_norm):
        T = np.zeros(n_coeffs)
        T[0] = 1.0
        if n_coeffs > 1:
            T[1] = t
        for k in range(2, n_coeffs):
            T[k] = 2.0 * t * T[k-1] - T[k-2]
        T_matrix[i] = T

    # 拟合系数
    coeffs_x = np.linalg.lstsq(T_matrix, x_samples, rcond=None)[0]
    coeffs_y = np.linalg.lstsq(T_matrix, y_samples, rcond=None)[0]
    coeffs_z = np.linalg.lstsq(T_matrix, z_samples, rcond=None)[0]

    coeffs = np.array([coeffs_x, coeffs_y, coeffs_z])

    # 创建插值器
    interpolator = ChebyshevInterpolator(coeffs, t_start, t_end)

    # 创建模型
    model = DEModel()
    model.add_body(name, interpolator)

    return model, t_start, t_end


def plot_orbit_comparison():
    """绘制轨道对比图"""
    print("=" * 70)
    print("DE模型可视化 - 轨道计算与绘制")
    print("=" * 70)

    # 创建地球轨道模型
    print("\n创建地球轨道模型...")
    earth_model, t_start, t_end = create_circular_orbit_model(
        radius_au=1.0,
        period_days=365.25,
        name="earth"
    )

    # 创建火星轨道模型
    print("创建火星轨道模型...")
    mars_model, _, _ = create_circular_orbit_model(
        radius_au=1.524,
        period_days=687.0,
        name="mars"
    )

    # 计算轨道点
    print("计算轨道位置...")
    n_points = 200
    times = np.linspace(t_start, t_end, n_points)

    earth_positions = np.array([earth_model.get_position("earth", t) for t in times])
    mars_positions = np.array([mars_model.get_position("mars", t) for t in times])

    # 转换为AU
    earth_positions_au = earth_positions / 149597870.7
    mars_positions_au = mars_positions / 149597870.7

    # 创建图形
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 左图：轨道对比
    ax1 = axes[0]
    ax1.plot(earth_positions_au[:, 0], earth_positions_au[:, 1],
             'b-', linewidth=2, label='地球轨道')
    ax1.plot(mars_positions_au[:, 0], mars_positions_au[:, 1],
             'r-', linewidth=2, label='火星轨道')
    ax1.plot(0, 0, 'yo', markersize=15, label='太阳')
    ax1.plot(earth_positions_au[0, 0], earth_positions_au[0, 1],
             'bo', markersize=8, label='地球起点')
    ax1.plot(mars_positions_au[0, 0], mars_positions_au[0, 1],
             'ro', markersize=8, label='火星起点')

    ax1.set_xlabel('X (AU)', fontsize=12)
    ax1.set_ylabel('Y (AU)', fontsize=12)
    ax1.set_title('行星轨道 (切比雪夫插值)', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.axis('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)

    # 右图：距离随时间变化
    ax2 = axes[1]
    earth_distances = np.linalg.norm(earth_positions_au, axis=1)
    mars_distances = np.linalg.norm(mars_positions_au, axis=1)
    days = (times - t_start)

    ax2.plot(days, earth_distances, 'b-', linewidth=2, label='地球-太阳距离')
    ax2.plot(days, mars_distances, 'r-', linewidth=2, label='火星-太阳距离')
    ax2.axhline(y=1.0, color='b', linestyle='--', alpha=0.5, label='1 AU')
    ax2.axhline(y=1.524, color='r', linestyle='--', alpha=0.5, label='1.524 AU')

    ax2.set_xlabel('时间 (天)', fontsize=12)
    ax2.set_ylabel('距离 (AU)', fontsize=12)
    ax2.set_title('日心距离随时间变化', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    # 保存图形
    output_file = 'de_model_orbits.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n图形已保存到: {output_file}")

    # 显示图形
    plt.show()

    # 输出统计信息
    print("\n" + "=" * 70)
    print("轨道统计信息")
    print("=" * 70)
    print(f"\n地球轨道:")
    print(f"  平均距离: {np.mean(earth_distances):.6f} AU")
    print(f"  最大距离: {np.max(earth_distances):.6f} AU")
    print(f"  最小距离: {np.min(earth_distances):.6f} AU")
    print(f"  距离变化: {np.max(earth_distances) - np.min(earth_distances):.6f} AU")

    print(f"\n火星轨道:")
    print(f"  平均距离: {np.mean(mars_distances):.6f} AU")
    print(f"  最大距离: {np.max(mars_distances):.6f} AU")
    print(f"  最小距离: {np.min(mars_distances):.6f} AU")
    print(f"  距离变化: {np.max(mars_distances) - np.min(mars_distances):.6f} AU")


def demonstrate_interpolation_accuracy():
    """演示插值精度"""
    print("\n" + "=" * 70)
    print("切比雪夫插值精度测试")
    print("=" * 70)

    # 创建模型
    model, t_start, t_end = create_circular_orbit_model(1.0, 365.25, "earth")

    # 测试点
    test_times = np.linspace(t_start, t_start + 100, 50)

    # 计算插值位置和理论位置
    AU = 149597870.7
    omega = 2 * np.pi / 365.25

    errors = []
    for t in test_times:
        # 插值位置
        pos_interp = model.get_position("earth", t)

        # 理论位置（圆轨道）
        theta = omega * (t - t_start)
        pos_theory = np.array([
            AU * np.cos(theta),
            AU * np.sin(theta),
            0.0
        ])

        # 误差
        error = np.linalg.norm(pos_interp - pos_theory)
        errors.append(error)

    errors = np.array(errors)

    print(f"\n插值误差统计 (前100天):")
    print(f"  平均误差: {np.mean(errors):.2f} km")
    print(f"  最大误差: {np.max(errors):.2f} km")
    print(f"  最小误差: {np.min(errors):.2f} km")
    print(f"  相对误差: {np.mean(errors)/AU*100:.6f}%")

    print("\n结论: 切比雪夫插值精度极高，适合高精度天文计算")


if __name__ == "__main__":
    try:
        plot_orbit_comparison()
        demonstrate_interpolation_accuracy()

        print("\n" + "=" * 70)
        print("可视化完成！")
        print("=" * 70)

    except Exception as e:
        print(f"\n错误: {e}")
        print("如果无法显示图形，请检查matplotlib是否正确安装")
