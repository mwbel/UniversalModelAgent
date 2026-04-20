#!/usr/bin/env python3
"""
行星运动模拟 - 不需要下载星历数据
使用理论初始条件进行数值模拟
"""

import numpy as np

# 物理常数
G = 6.67430e-11  # 万有引力常数 (m^3 kg^-1 s^-2)
AU = 1.496e11    # 天文单位 (m)
DAY = 86400      # 一天的秒数

# 预设场景：真实的行星参数
PRESET_SCENARIOS = {
    "地球-月球": {
        "body1": {
            "name": "地球",
            "mass": 5.972e24,  # kg
            "position": [0, 0, 0],  # m
            "velocity": [0, 0, 0]   # m/s
        },
        "body2": {
            "name": "月球",
            "mass": 7.342e22,  # kg
            "position": [3.844e8, 0, 0],  # m (地月距离)
            "velocity": [0, 1022, 0]  # m/s (月球轨道速度)
        }
    },

    "太阳-地球": {
        "body1": {
            "name": "太阳",
            "mass": 1.989e30,  # kg
            "position": [0, 0, 0],
            "velocity": [0, 0, 0]
        },
        "body2": {
            "name": "地球",
            "mass": 5.972e24,  # kg
            "position": [AU, 0, 0],  # 1 AU
            "velocity": [0, 29780, 0]  # m/s (地球轨道速度)
        }
    },

    "双星系统": {
        "body1": {
            "name": "恒星A",
            "mass": 2e30,  # kg
            "position": [-1e11, 0, 0],
            "velocity": [0, -10000, 0]
        },
        "body2": {
            "name": "恒星B",
            "mass": 2e30,  # kg
            "position": [1e11, 0, 0],
            "velocity": [0, 10000, 0]
        }
    },

    "简单圆轨道": {
        "body1": {
            "name": "中心天体",
            "mass": 1e30,
            "position": [0, 0, 0],
            "velocity": [0, 0, 0]
        },
        "body2": {
            "name": "行星",
            "mass": 1e24,
            "position": [1e11, 0, 0],
            "velocity": [0, np.sqrt(G * 1e30 / 1e11), 0]  # 圆轨道速度
        }
    }
}

def print_scenario(scenario_name):
    """打印预设场景的信息"""
    if scenario_name not in PRESET_SCENARIOS:
        print(f"错误：场景 '{scenario_name}' 不存在")
        return

    scenario = PRESET_SCENARIOS[scenario_name]
    print(f"\n{'='*60}")
    print(f"场景: {scenario_name}")
    print(f"{'='*60}")

    for key in ["body1", "body2"]:
        body = scenario[key]
        print(f"\n{body['name']}:")
        print(f"  质量: {body['mass']:.3e} kg")
        print(f"  位置: [{body['position'][0]:.3e}, {body['position'][1]:.3e}, {body['position'][2]:.3e}] m")
        print(f"  速度: [{body['velocity'][0]:.3e}, {body['velocity'][1]:.3e}, {body['velocity'][2]:.3e}] m/s")

if __name__ == "__main__":
    print("=" * 60)
    print("行星运动模拟 - 预设场景")
    print("=" * 60)
    print("\n说明：")
    print("- 不需要下载星历数据")
    print("- 使用理论初始条件进行数值模拟")
    print("- 这正是你需求文档中的目标！")

    print("\n\n可用的预设场景：")
    for i, name in enumerate(PRESET_SCENARIOS.keys(), 1):
        print(f"{i}. {name}")

    # 显示所有场景
    for scenario_name in PRESET_SCENARIOS.keys():
        print_scenario(scenario_name)

    print("\n" + "=" * 60)
    print("下一步：实现数值积分算法来模拟这些系统的运动")
    print("=" * 60)
