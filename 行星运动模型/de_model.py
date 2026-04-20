#!/usr/bin/env python3
"""
DE (Development Ephemeris) 模型数值算法实现

DE模型是JPL开发的高精度行星星历模型，使用切比雪夫多项式插值方法
来表示太阳系天体的位置和速度。

核心算法：
1. 切比雪夫多项式插值
2. 时间归一化
3. 位置和速度计算
"""

import numpy as np
from typing import Tuple, Optional


class ChebyshevInterpolator:
    """
    切比雪夫多项式插值器

    DE模型的核心算法，用于从切比雪夫系数计算位置和速度
    """

    def __init__(self, coefficients: np.ndarray, t_start: float, t_end: float):
        """
        初始化切比雪夫插值器

        参数:
            coefficients: 切比雪夫系数数组，形状为 (n_components, n_coeffs)
                         通常 n_components=3 (x, y, z坐标)
            t_start: 时间区间起始时刻 (儒略日)
            t_end: 时间区间结束时刻 (儒略日)
        """
        self.coefficients = np.array(coefficients)
        self.t_start = t_start
        self.t_end = t_end
        self.n_coeffs = self.coefficients.shape[1]

    def normalize_time(self, t: float) -> float:
        """
        将时间归一化到 [-1, 1] 区间

        切比雪夫多项式定义在 [-1, 1] 区间上，需要将实际时间映射到此区间

        参数:
            t: 实际时间 (儒略日)

        返回:
            归一化时间 ∈ [-1, 1]
        """
        return 2.0 * (t - self.t_start) / (self.t_end - self.t_start) - 1.0

    def chebyshev_polynomials(self, x: float, n: int) -> np.ndarray:
        """
        计算切比雪夫多项式 T_0(x), T_1(x), ..., T_{n-1}(x)

        使用递推关系：
            T_0(x) = 1
            T_1(x) = x
            T_{k+1}(x) = 2x * T_k(x) - T_{k-1}(x)

        参数:
            x: 自变量值 ∈ [-1, 1]
            n: 多项式个数

        返回:
            长度为n的数组，包含 T_0(x) 到 T_{n-1}(x)
        """
        T = np.zeros(n)
        T[0] = 1.0

        if n > 1:
            T[1] = x

        for k in range(2, n):
            T[k] = 2.0 * x * T[k-1] - T[k-2]

        return T

    def chebyshev_derivatives(self, x: float, n: int) -> np.ndarray:
        """
        计算切比雪夫多项式的导数 T'_0(x), T'_1(x), ..., T'_{n-1}(x)

        使用递推关系：
            T'_0(x) = 0
            T'_1(x) = 1
            T'_{k+1}(x) = 2 * T_k(x) + 2x * T'_k(x) - T'_{k-1}(x)

        参数:
            x: 自变量值 ∈ [-1, 1]
            n: 多项式个数

        返回:
            长度为n的数组，包含导数值
        """
        T = self.chebyshev_polynomials(x, n)
        dT = np.zeros(n)
        dT[0] = 0.0

        if n > 1:
            dT[1] = 1.0

        for k in range(2, n):
            dT[k] = 2.0 * T[k-1] + 2.0 * x * dT[k-1] - dT[k-2]

        return dT

    def evaluate_position(self, t: float) -> np.ndarray:
        """
        计算给定时刻的位置

        位置通过切比雪夫多项式展开计算：
            r(t) = Σ c_k * T_k(t_normalized)

        参数:
            t: 时间 (儒略日)

        返回:
            位置向量 [x, y, z]
        """
        # 归一化时间
        t_norm = self.normalize_time(t)

        # 计算切比雪夫多项式值
        T = self.chebyshev_polynomials(t_norm, self.n_coeffs)

        # 计算位置：对每个坐标分量求和
        position = np.zeros(3)
        for i in range(3):
            position[i] = np.dot(self.coefficients[i], T)

        return position

    def evaluate_velocity(self, t: float) -> np.ndarray:
        """
        计算给定时刻的速度

        速度是位置对时间的导数：
            v(t) = dr/dt = Σ c_k * dT_k/dt

        其中 dT_k/dt = dT_k/dx * dx/dt，dx/dt = 2/(t_end - t_start)

        参数:
            t: 时间 (儒略日)

        返回:
            速度向量 [vx, vy, vz]
        """
        # 归一化时间
        t_norm = self.normalize_time(t)

        # 计算切比雪夫多项式导数
        dT = self.chebyshev_derivatives(t_norm, self.n_coeffs)

        # 时间导数的链式法则因子
        dt_factor = 2.0 / (self.t_end - self.t_start)

        # 计算速度：对每个坐标分量求和
        velocity = np.zeros(3)
        for i in range(3):
            velocity[i] = np.dot(self.coefficients[i], dT) * dt_factor

        return velocity

    def evaluate(self, t: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        同时计算位置和速度

        参数:
            t: 时间 (儒略日)

        返回:
            (position, velocity) 元组
        """
        return self.evaluate_position(t), self.evaluate_velocity(t)


class DEModel:
    """
    DE模型主类

    管理多个天体的切比雪夫插值器，提供统一的接口
    """

    def __init__(self):
        """初始化DE模型"""
        self.interpolators = {}  # 存储各天体的插值器
        self.body_names = []

    def add_body(self, name: str, interpolator: ChebyshevInterpolator):
        """
        添加天体及其插值器

        参数:
            name: 天体名称
            interpolator: 切比雪夫插值器对象
        """
        self.interpolators[name] = interpolator
        if name not in self.body_names:
            self.body_names.append(name)

    def get_position(self, body_name: str, t: float) -> np.ndarray:
        """
        获取天体在给定时刻的位置

        参数:
            body_name: 天体名称
            t: 时间 (儒略日)

        返回:
            位置向量 [x, y, z] (单位：km)
        """
        if body_name not in self.interpolators:
            raise ValueError(f"天体 '{body_name}' 不存在")

        return self.interpolators[body_name].evaluate_position(t)

    def get_velocity(self, body_name: str, t: float) -> np.ndarray:
        """
        获取天体在给定时刻的速度

        参数:
            body_name: 天体名称
            t: 时间 (儒略日)

        返回:
            速度向量 [vx, vy, vz] (单位：km/day)
        """
        if body_name not in self.interpolators:
            raise ValueError(f"天体 '{body_name}' 不存在")

        return self.interpolators[body_name].evaluate_velocity(t)

    def get_state(self, body_name: str, t: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        获取天体在给定时刻的状态（位置和速度）

        参数:
            body_name: 天体名称
            t: 时间 (儒略日)

        返回:
            (position, velocity) 元组
        """
        if body_name not in self.interpolators:
            raise ValueError(f"天体 '{body_name}' 不存在")

        return self.interpolators[body_name].evaluate(t)

    def get_relative_position(self, body1: str, body2: str, t: float) -> np.ndarray:
        """
        计算两个天体的相对位置

        参数:
            body1: 观测天体名称
            body2: 目标天体名称
            t: 时间 (儒略日)

        返回:
            body2相对于body1的位置向量
        """
        pos1 = self.get_position(body1, t)
        pos2 = self.get_position(body2, t)
        return pos2 - pos1

    def list_bodies(self):
        """列出所有可用的天体"""
        return self.body_names.copy()


def create_example_model() -> DEModel:
    """
    创建一个示例DE模型，用于演示和测试

    使用简化的切比雪夫系数来模拟地球绕太阳的运动
    """
    model = DEModel()

    # 示例：地球的切比雪夫系数（简化版）
    # 实际DE模型会有更多系数和更高精度
    # 这里使用简单的圆轨道近似

    # 时间范围：2000年1月1日前后32天
    t_start = 2451545.0  # J2000.0
    t_end = t_start + 32.0

    # 地球轨道半径约1 AU = 149597870.7 km
    AU = 149597870.7

    # 简化的切比雪夫系数（模拟圆轨道）
    # 实际系数会从SPK文件中读取
    earth_coeffs = np.array([
        [AU, 0.0, 0.0, 0.0, 0.0, 0.0],      # x坐标系数
        [0.0, AU, 0.0, 0.0, 0.0, 0.0],      # y坐标系数
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]      # z坐标系数
    ])

    earth_interpolator = ChebyshevInterpolator(earth_coeffs, t_start, t_end)
    model.add_body("earth", earth_interpolator)

    return model


# 辅助函数

def julian_date(year: int, month: int, day: int,
                hour: int = 0, minute: int = 0, second: float = 0.0) -> float:
    """
    计算儒略日

    参数:
        year: 年
        month: 月
        day: 日
        hour: 时
        minute: 分
        second: 秒

    返回:
        儒略日数
    """
    # 儒略日计算公式
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3

    jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    # 加上时间部分
    jd = jdn + (hour - 12) / 24.0 + minute / 1440.0 + second / 86400.0

    return jd


def format_vector(vec: np.ndarray, unit: str = "") -> str:
    """
    格式化向量输出

    参数:
        vec: 向量
        unit: 单位字符串

    返回:
        格式化的字符串
    """
    unit_str = f" {unit}" if unit else ""
    return f"[{vec[0]:12.6f}, {vec[1]:12.6f}, {vec[2]:12.6f}]{unit_str}"


if __name__ == "__main__":
    print("=" * 70)
    print("DE模型数值算法实现 - 核心功能演示")
    print("=" * 70)

    # 1. 演示切比雪夫多项式计算
    print("\n1. 切比雪夫多项式计算")
    print("-" * 70)

    # 创建简单的插值器
    coeffs = np.array([
        [1.0, 0.5, 0.2],  # x坐标系数
        [0.0, 1.0, 0.3],  # y坐标系数
        [0.0, 0.0, 0.1]   # z坐标系数
    ])
    interpolator = ChebyshevInterpolator(coeffs, 0.0, 1.0)

    # 计算几个时刻的切比雪夫多项式值
    print("切比雪夫多项式 T_0, T_1, T_2 在不同点的值：")
    for x in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        T = interpolator.chebyshev_polynomials(x, 3)
        print(f"  x = {x:5.1f}: T = [{T[0]:6.3f}, {T[1]:6.3f}, {T[2]:6.3f}]")

    # 2. 演示位置和速度计算
    print("\n2. 位置和速度计算")
    print("-" * 70)

    t_test = 0.5
    position = interpolator.evaluate_position(t_test)
    velocity = interpolator.evaluate_velocity(t_test)

    print(f"时刻 t = {t_test}")
    print(f"位置: {format_vector(position)}")
    print(f"速度: {format_vector(velocity)}")

    # 3. 演示DE模型使用
    print("\n3. DE模型使用示例")
    print("-" * 70)

    model = create_example_model()
    print(f"已加载天体: {', '.join(model.list_bodies())}")

    # 计算J2000.0时刻的地球位置
    t_j2000 = 2451545.0
    earth_pos = model.get_position("earth", t_j2000)
    earth_vel = model.get_velocity("earth", t_j2000)

    print(f"\nJ2000.0 时刻 (JD = {t_j2000}):")
    print(f"地球位置: {format_vector(earth_pos, 'km')}")
    print(f"地球速度: {format_vector(earth_vel, 'km/day')}")

    # 4. 演示儒略日计算
    print("\n4. 儒略日计算")
    print("-" * 70)

    jd_2000 = julian_date(2000, 1, 1, 12, 0, 0)
    jd_2024 = julian_date(2024, 1, 1, 0, 0, 0)

    print(f"2000年1月1日 12:00:00 的儒略日: {jd_2000:.6f}")
    print(f"2024年1月1日 00:00:00 的儒略日: {jd_2024:.6f}")
    print(f"相差天数: {jd_2024 - jd_2000:.2f} 天")

    # 5. 算法性能说明
    print("\n5. 算法特点")
    print("-" * 70)
    print("✓ 使用切比雪夫多项式插值，精度高、计算效率高")
    print("✓ 递推计算多项式值，避免重复计算")
    print("✓ 同时计算位置和速度，满足动力学模拟需求")
    print("✓ 支持任意时刻查询，时间复杂度 O(n)，n为系数个数")
    print("✓ 可扩展到多个天体，支持相对位置计算")

    print("\n" + "=" * 70)
    print("核心算法实现完成！")
    print("=" * 70)
    print("\n说明：")
    print("- 这是DE模型的核心数值算法实现")
    print("- 实际使用时需要从SPK文件读取切比雪夫系数")
    print("- 可以使用 jplephem 或 skyfield 库来读取SPK文件")
    print("- 本实现展示了算法原理，可用于教学和理解DE模型")

