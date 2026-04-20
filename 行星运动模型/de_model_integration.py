#!/usr/bin/env python3
"""
DE模型与实际星历数据集成

演示如何将DE模型算法与实际的SPK星历文件结合使用
使用 jplephem 库读取真实的DE440数据
"""

import numpy as np
from de_model import ChebyshevInterpolator, DEModel, julian_date, format_vector

try:
    from jplephem.spk import SPK
    JPLEPHEM_AVAILABLE = True
except ImportError:
    JPLEPHEM_AVAILABLE = False
    print("警告: jplephem 未安装，无法读取SPK文件")
    print("安装命令: pip install jplephem")


class DEModelFromSPK(DEModel):
    """
    从SPK文件加载DE模型的扩展类
    """

    def __init__(self, spk_file_path: str):
        """
        从SPK文件初始化DE模型

        参数:
            spk_file_path: SPK文件路径（如 de440.bsp）
        """
        super().__init__()

        if not JPLEPHEM_AVAILABLE:
            raise ImportError("需要安装 jplephem: pip install jplephem")

        self.spk = SPK.open(spk_file_path)
        self._load_bodies()

    def _load_bodies(self):
        """从SPK文件加载所有天体"""
        # SPK文件中的天体ID映射
        body_map = {
            0: "solar_system_barycenter",
            1: "mercury_barycenter",
            2: "venus_barycenter",
            3: "earth_barycenter",
            4: "mars_barycenter",
            5: "jupiter_barycenter",
            6: "saturn_barycenter",
            7: "uranus_barycenter",
            8: "neptune_barycenter",
            9: "pluto_barycenter",
            10: "sun",
            301: "moon",
            399: "earth"
        }

        print(f"SPK文件包含的段: {len(self.spk.segments)} 个")
        for segment in self.spk.segments:
            print(f"  段: 中心={segment.center}, 目标={segment.target}, "
                  f"时间范围=[{segment.start_jd:.1f}, {segment.end_jd:.1f}]")

    def get_position_from_spk(self, target: int, observer: int, jd: float) -> np.ndarray:
        """
        从SPK文件直接获取位置

        参数:
            target: 目标天体ID
            observer: 观测者天体ID
            jd: 儒略日

        返回:
            位置向量 [x, y, z] (km)
        """
        position = self.spk[observer, target].compute(jd)
        return np.array(position)

    def get_state_from_spk(self, target: int, observer: int, jd: float):
        """
        从SPK文件获取位置和速度

        参数:
            target: 目标天体ID
            observer: 观测者天体ID
            jd: 儒略日

        返回:
            (position, velocity) 元组
        """
        position, velocity = self.spk[observer, target].compute_and_differentiate(jd)
        return np.array(position), np.array(velocity)


def demonstrate_spk_reading():
    """演示如何读取SPK文件"""
    print("=" * 70)
    print("DE模型与SPK文件集成演示")
    print("=" * 70)

    # 检查是否有SPK文件
    import os
    spk_files = [
        "de440.bsp",
        "de421.bsp",
        os.path.expanduser("~/.skyfield/de421.bsp")
    ]

    spk_file = None
    for f in spk_files:
        if os.path.exists(f):
            spk_file = f
            break

    if spk_file is None:
        print("\n未找到SPK文件。")
        print("请运行以下命令之一：")
        print("1. python3 test_skyfield.py  # 自动下载 de421.bsp")
        print("2. 手动下载 de440.bsp 到当前目录")
        return

    print(f"\n找到SPK文件: {spk_file}")
    print("-" * 70)

    try:
        # 加载SPK文件
        model = DEModelFromSPK(spk_file)

        # 计算地球相对太阳的位置
        print("\n计算地球相对太阳的位置")
        print("-" * 70)

        # J2000.0 时刻
        jd = 2451545.0
        print(f"时刻: J2000.0 (JD = {jd})")

        # 地球相对太阳系质心
        earth_pos, earth_vel = model.get_state_from_spk(399, 0, jd)
        print(f"\n地球相对太阳系质心:")
        print(f"  位置: {format_vector(earth_pos, 'km')}")
        print(f"  速度: {format_vector(earth_vel, 'km/day')}")

        # 太阳相对太阳系质心
        sun_pos, sun_vel = model.get_state_from_spk(10, 0, jd)
        print(f"\n太阳相对太阳系质心:")
        print(f"  位置: {format_vector(sun_pos, 'km')}")
        print(f"  速度: {format_vector(sun_vel, 'km/day')}")

        # 地球相对太阳
        rel_pos = earth_pos - sun_pos
        rel_vel = earth_vel - sun_vel
        distance = np.linalg.norm(rel_pos)

        print(f"\n地球相对太阳:")
        print(f"  位置: {format_vector(rel_pos, 'km')}")
        print(f"  速度: {format_vector(rel_vel, 'km/day')}")
        print(f"  距离: {distance:.2f} km = {distance/1.496e8:.6f} AU")

        # 计算多个时刻
        print("\n" + "=" * 70)
        print("2024年每月1日的地球-太阳距离")
        print("-" * 70)

        for month in range(1, 13):
            jd = julian_date(2024, month, 1)
            earth_pos = model.get_position_from_spk(399, 0, jd)
            sun_pos = model.get_position_from_spk(10, 0, jd)
            distance = np.linalg.norm(earth_pos - sun_pos)
            au = distance / 1.496e8
            print(f"2024-{month:02d}-01: {distance:12.2f} km = {au:.6f} AU")

    except Exception as e:
        print(f"\n错误: {e}")
        print("请确保SPK文件格式正确")


def compare_algorithms():
    """比较不同算法的性能"""
    print("\n" + "=" * 70)
    print("算法性能比较")
    print("=" * 70)

    print("\n1. 切比雪夫插值算法 (本实现)")
    print("-" * 70)
    print("优点:")
    print("  - 高精度：切比雪夫多项式在插值中具有最优逼近性质")
    print("  - 高效率：递推计算，时间复杂度 O(n)")
    print("  - 稳定性：数值稳定，不易产生振荡")
    print("  - 可微性：可同时计算位置和速度")
    print("\n适用场景:")
    print("  - 高精度天文计算")
    print("  - 行星轨道预报")
    print("  - 航天器轨道设计")

    print("\n2. 数值积分算法 (如 RK4)")
    print("-" * 70)
    print("优点:")
    print("  - 通用性强：可处理任意微分方程")
    print("  - 灵活性高：可加入摄动力")
    print("\n缺点:")
    print("  - 计算量大：需要逐步积分")
    print("  - 误差累积：长期积分误差增大")

    print("\n3. 解析方法 (如开普勒轨道)")
    print("-" * 70)
    print("优点:")
    print("  - 计算快速：直接公式计算")
    print("  - 物理直观：轨道参数有明确意义")
    print("\n缺点:")
    print("  - 精度有限：忽略摄动")
    print("  - 适用范围窄：仅适用于二体问题")


if __name__ == "__main__":
    if JPLEPHEM_AVAILABLE:
        demonstrate_spk_reading()
    else:
        print("\n需要安装 jplephem 库来读取SPK文件")
        print("安装命令: pip install jplephem")
        print("\n或者使用 skyfield 库（会自动下载数据）:")
        print("  pip install skyfield")
        print("  python3 test_skyfield.py")

    compare_algorithms()

    print("\n" + "=" * 70)
    print("总结")
    print("=" * 70)
    print("DE模型使用切比雪夫多项式插值，是目前最精确的行星星历模型。")
    print("本实现展示了其核心算法原理，可用于:")
    print("  1. 理解DE模型的数学基础")
    print("  2. 教学和学习天体力学")
    print("  3. 开发自定义的星历计算工具")
    print("  4. 与其他算法进行性能比较")
