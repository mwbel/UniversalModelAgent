# DE模型数值算法实现

## 概述

本项目实现了JPL DE (Development Ephemeris) 模型的核心数值算法。DE模型是目前最精确的行星星历模型，使用切比雪夫多项式插值方法来表示太阳系天体的位置和速度。

## 核心算法

### 1. 切比雪夫多项式插值

DE模型的核心是切比雪夫多项式插值。对于任意时刻 t，天体的位置可以表示为：

```
r(t) = Σ c_k * T_k(t_normalized)
```

其中：
- `c_k` 是切比雪夫系数（从SPK文件中读取）
- `T_k` 是k阶切比雪夫多项式
- `t_normalized` 是归一化到 [-1, 1] 区间的时间

### 2. 切比雪夫多项式计算

使用递推关系高效计算：

```
T_0(x) = 1
T_1(x) = x
T_{k+1}(x) = 2x * T_k(x) - T_{k-1}(x)
```

时间复杂度：O(n)，其中 n 是多项式阶数

### 3. 速度计算

速度是位置对时间的导数：

```
v(t) = dr/dt = Σ c_k * dT_k/dt
```

其中导数也使用递推关系计算：

```
T'_0(x) = 0
T'_1(x) = 1
T'_{k+1}(x) = 2 * T_k(x) + 2x * T'_k(x) - T'_{k-1}(x)
```

## 文件说明

### de_model.py

核心算法实现，包含：

- `ChebyshevInterpolator`: 切比雪夫插值器类
  - `chebyshev_polynomials()`: 计算切比雪夫多项式值
  - `chebyshev_derivatives()`: 计算切比雪夫多项式导数
  - `evaluate_position()`: 计算位置
  - `evaluate_velocity()`: 计算速度
  - `evaluate()`: 同时计算位置和速度

- `DEModel`: DE模型管理类
  - `add_body()`: 添加天体
  - `get_position()`: 获取位置
  - `get_velocity()`: 获取速度
  - `get_state()`: 获取状态（位置+速度）
  - `get_relative_position()`: 计算相对位置

- 辅助函数：
  - `julian_date()`: 计算儒略日
  - `format_vector()`: 格式化向量输出
  - `create_example_model()`: 创建示例模型

### de_model_integration.py

与实际SPK文件集成的示例，展示如何：
- 使用 jplephem 库读取 DE440 数据
- 计算真实的行星位置
- 比较不同算法的性能

## 使用方法

### 基本使用

```python
from de_model import ChebyshevInterpolator, DEModel
import numpy as np

# 创建插值器（系数通常从SPK文件读取）
coeffs = np.array([
    [1.0, 0.5, 0.2],  # x坐标系数
    [0.0, 1.0, 0.3],  # y坐标系数
    [0.0, 0.0, 0.1]   # z坐标系数
])
interpolator = ChebyshevInterpolator(coeffs, t_start=0.0, t_end=1.0)

# 计算位置和速度
position = interpolator.evaluate_position(t=0.5)
velocity = interpolator.evaluate_velocity(t=0.5)
```

### 使用DE模型

```python
from de_model import DEModel, create_example_model

# 创建模型
model = create_example_model()

# 获取地球位置（J2000.0时刻）
earth_pos = model.get_position("earth", t=2451545.0)
earth_vel = model.get_velocity("earth", t=2451545.0)
```

### 运行演示

```bash
# 运行核心算法演示
python3 de_model.py

# 运行SPK文件集成演示（需要先安装 jplephem）
pip install jplephem
python3 de_model_integration.py
```

## 算法特点

### 优点

1. **高精度**：切比雪夫多项式具有最优逼近性质
2. **高效率**：递推计算，时间复杂度 O(n)
3. **数值稳定**：不易产生振荡
4. **可微性**：可同时计算位置和速度
5. **灵活性**：支持任意时刻查询

### 适用场景

- 高精度天文计算
- 行星轨道预报
- 航天器轨道设计
- 天体力学研究
- 教学和学习

## 与其他方法的比较

| 方法 | 精度 | 速度 | 适用范围 |
|------|------|------|----------|
| 切比雪夫插值 (DE模型) | 极高 | 快 | 通用 |
| 数值积分 (RK4等) | 中等 | 慢 | 通用 |
| 解析方法 (开普勒轨道) | 低 | 极快 | 二体问题 |

## 数学背景

### 切比雪夫多项式的优势

1. **最优逼近性**：在所有多项式中，切比雪夫多项式对连续函数的逼近误差最小
2. **正交性**：在 [-1, 1] 区间上带权正交
3. **递推性**：可以高效计算任意阶多项式
4. **数值稳定性**：系数不会过大，避免数值溢出

### 时间归一化

将实际时间 t ∈ [t_start, t_end] 映射到 [-1, 1]：

```
t_normalized = 2 * (t - t_start) / (t_end - t_start) - 1
```

这确保了切比雪夫多项式在其最优区间上工作。

## 依赖库

```
numpy>=1.20.0      # 数值计算
jplephem>=2.15     # 读取SPK文件（可选）
skyfield>=1.40     # 替代方案（可选）
```

## 参考资料

1. JPL Planetary and Lunar Ephemerides: https://ssd.jpl.nasa.gov/planets/eph_export.html
2. Chebyshev Polynomials: https://en.wikipedia.org/wiki/Chebyshev_polynomials
3. SPK File Format: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/spk.html

## 扩展方向

1. 支持更多天体（小行星、彗星等）
2. 实现多线程并行计算
3. 添加误差估计功能
4. 与可视化工具集成
5. 实现轨道预报功能

## 作者说明

本实现基于JPL DE模型的数学原理，展示了切比雪夫多项式插值在天体力学中的应用。代码注释详细，适合学习和教学使用。
