#!/usr/bin/env python3
"""
DE模型完整测试套件

测试DE模型数值算法的各个组件
"""

import numpy as np
from de_model import (
    ChebyshevInterpolator,
    DEModel,
    julian_date,
    format_vector,
    create_example_model
)


def test_chebyshev_polynomials():
    """测试切比雪夫多项式计算"""
    print("=" * 70)
    print("测试 1: 切比雪夫多项式计算")
    print("=" * 70)

    coeffs = np.array([[1.0], [0.0], [0.0]])
    interp = ChebyshevInterpolator(coeffs, 0.0, 1.0)

    # 测试已知值
    test_cases = [
        (-1.0, [1.0, -1.0, 1.0, -1.0]),
        (0.0, [1.0, 0.0, -1.0, 0.0]),
        (1.0, [1.0, 1.0, 1.0, 1.0])
    ]

    all_passed = True
    for x, expected in test_cases:
        result = interp.chebyshev_polynomials(x, 4)
        if np.allclose(result, expected):
            print(f"✓ T(x={x:4.1f}) = {result} (正确)")
        else:
            print(f"✗ T(x={x:4.1f}) = {result} (期望: {expected})")
            all_passed = False

    return all_passed


def test_time_normalization():
    """测试时间归一化"""
    print("\n" + "=" * 70)
    print("测试 2: 时间归一化")
    print("=" * 70)

    coeffs = np.array([[1.0], [0.0], [0.0]])
    interp = ChebyshevInterpolator(coeffs, 0.0, 10.0)

    test_cases = [
        (0.0, -1.0),
        (5.0, 0.0),
        (10.0, 1.0)
    ]

    all_passed = True
    for t, expected in test_cases:
        result = interp.normalize_time(t)
        if np.isclose(result, expected):
            print(f"✓ normalize_time({t:4.1f}) = {result:6.3f} (正确)")
        else:
            print(f"✗ normalize_time({t:4.1f}) = {result:6.3f} (期望: {expected})")
            all_passed = False

    return all_passed


def test_position_calculation():
    """测试位置计算"""
    print("\n" + "=" * 70)
    print("测试 3: 位置计算")
    print("=" * 70)

    # 简单的线性插值测试
    coeffs = np.array([
        [0.0, 1.0],  # x = t_norm
        [1.0, 0.0],  # y = 1
        [0.0, 0.0]   # z = 0
    ])
    interp = ChebyshevInterpolator(coeffs, 0.0, 1.0)

    # 在 t=0.5 时，t_norm=0，应该得到 [0, 1, 0]
    pos = interp.evaluate_position(0.5)
    expected = np.array([0.0, 1.0, 0.0])

    if np.allclose(pos, expected):
        print(f"✓ position(t=0.5) = {format_vector(pos)} (正确)")
        return True
    else:
        print(f"✗ position(t=0.5) = {format_vector(pos)} (期望: {format_vector(expected)})")
        return False


def test_velocity_calculation():
    """测试速度计算"""
    print("\n" + "=" * 70)
    print("测试 4: 速度计算")
    print("=" * 70)

    # 使用线性位置，速度应该是常数
    coeffs = np.array([
        [0.0, 1.0],  # x = t_norm, dx/dt = 2/(t_end-t_start) = 2
        [0.0, 0.0],  # y = 0
        [0.0, 0.0]   # z = 0
    ])
    interp = ChebyshevInterpolator(coeffs, 0.0, 1.0)

    vel = interp.evaluate_velocity(0.5)
    expected_vx = 2.0  # dx/dt_norm * dt_norm/dt = 1 * 2

    if np.isclose(vel[0], expected_vx):
        print(f"✓ velocity(t=0.5) = {format_vector(vel)} (正确)")
        return True
    else:
        print(f"✗ velocity(t=0.5) = {format_vector(vel)} (期望 vx={expected_vx})")
        return False


def test_de_model():
    """测试DE模型类"""
    print("\n" + "=" * 70)
    print("测试 5: DE模型类")
    print("=" * 70)

    model = DEModel()

    # 添加两个天体
    coeffs1 = np.array([[1.0], [0.0], [0.0]])
    coeffs2 = np.array([[0.0], [1.0], [0.0]])

    interp1 = ChebyshevInterpolator(coeffs1, 0.0, 1.0)
    interp2 = ChebyshevInterpolator(coeffs2, 0.0, 1.0)

    model.add_body("body1", interp1)
    model.add_body("body2", interp2)

    # 测试列表
    bodies = model.list_bodies()
    if len(bodies) == 2 and "body1" in bodies and "body2" in bodies:
        print(f"✓ 天体列表: {bodies} (正确)")
    else:
        print(f"✗ 天体列表: {bodies} (期望: ['body1', 'body2'])")
        return False

    # 测试相对位置
    rel_pos = model.get_relative_position("body1", "body2", 0.5)
    expected = np.array([-1.0, 1.0, 0.0])

    if np.allclose(rel_pos, expected):
        print(f"✓ 相对位置 = {format_vector(rel_pos)} (正确)")
        return True
    else:
        print(f"✗ 相对位置 = {format_vector(rel_pos)} (期望: {format_vector(expected)})")
        return False


def test_julian_date():
    """测试儒略日计算"""
    print("\n" + "=" * 70)
    print("测试 6: 儒略日计算")
    print("=" * 70)

    # J2000.0 = 2000年1月1日 12:00:00 = JD 2451545.0
    jd = julian_date(2000, 1, 1, 12, 0, 0)
    expected = 2451545.0

    if np.isclose(jd, expected):
        print(f"✓ J2000.0 = {jd:.6f} (正确)")
        return True
    else:
        print(f"✗ J2000.0 = {jd:.6f} (期望: {expected})")
        return False


def test_interpolation_accuracy():
    """测试插值精度"""
    print("\n" + "=" * 70)
    print("测试 7: 插值精度 (圆轨道)")
    print("=" * 70)

    # 创建圆轨道的切比雪夫系数
    t_start = 0.0
    t_end = 2 * np.pi
    n_coeffs = 10

    # 采样点
    t_samples = np.linspace(t_start, t_end, 100)
    t_norm = 2.0 * (t_samples - t_start) / (t_end - t_start) - 1.0

    # 圆轨道: x = cos(t), y = sin(t)
    x_samples = np.cos(t_samples)
    y_samples = np.sin(t_samples)

    # 拟合切比雪夫系数
    T_matrix = np.zeros((len(t_norm), n_coeffs))
    for i, t in enumerate(t_norm):
        T = np.zeros(n_coeffs)
        T[0] = 1.0
        if n_coeffs > 1:
            T[1] = t
        for k in range(2, n_coeffs):
            T[k] = 2.0 * t * T[k-1] - T[k-2]
        T_matrix[i] = T

    coeffs_x = np.linalg.lstsq(T_matrix, x_samples, rcond=None)[0]
    coeffs_y = np.linalg.lstsq(T_matrix, y_samples, rcond=None)[0]
    coeffs_z = np.zeros(n_coeffs)

    coeffs = np.array([coeffs_x, coeffs_y, coeffs_z])
    interp = ChebyshevInterpolator(coeffs, t_start, t_end)

    # 测试插值误差
    test_times = np.linspace(t_start, t_end, 50)
    errors = []

    for t in test_times:
        pos = interp.evaluate_position(t)
        expected = np.array([np.cos(t), np.sin(t), 0.0])
        error = np.linalg.norm(pos - expected)
        errors.append(error)

    max_error = np.max(errors)
    avg_error = np.mean(errors)

    print(f"平均误差: {avg_error:.6e}")
    print(f"最大误差: {max_error:.6e}")

    if max_error < 1e-4:
        print("✓ 插值精度测试通过 (误差 < 1e-4)")
        return True
    else:
        print("✗ 插值精度测试失败 (误差过大)")
        return False


def run_all_tests():
    """运行所有测试"""
    print("\n" + "=" * 70)
    print("DE模型数值算法测试套件")
    print("=" * 70)

    tests = [
        ("切比雪夫多项式计算", test_chebyshev_polynomials),
        ("时间归一化", test_time_normalization),
        ("位置计算", test_position_calculation),
        ("速度计算", test_velocity_calculation),
        ("DE模型类", test_de_model),
        ("儒略日计算", test_julian_date),
        ("插值精度", test_interpolation_accuracy)
    ]

    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"\n✗ 测试 '{name}' 出错: {e}")
            results.append((name, False))

    # 总结
    print("\n" + "=" * 70)
    print("测试总结")
    print("=" * 70)

    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)

    for name, passed in results:
        status = "✓ 通过" if passed else "✗ 失败"
        print(f"{status}: {name}")

    print(f"\n总计: {passed_count}/{total_count} 测试通过")

    if passed_count == total_count:
        print("\n🎉 所有测试通过！DE模型实现正确。")
    else:
        print(f"\n⚠️  有 {total_count - passed_count} 个测试失败，请检查实现。")

    return passed_count == total_count


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
