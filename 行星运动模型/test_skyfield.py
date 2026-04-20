#!/usr/bin/env python3
"""
测试 Skyfield 库 - 自动下载和使用星历数据
"""

from skyfield.api import load

print("=" * 60)
print("使用 Skyfield 获取行星位置")
print("=" * 60)

# 加载时间尺度
print("\n1. 加载时间尺度...")
ts = load.timescale()

# 加载星历数据（会自动下载到 ~/.skyfield/ 目录）
print("\n2. 加载星历数据（首次运行会自动下载）...")
print("   使用 DE421 星历（1900-2050年，文件较小）")
planets = load('de421.bsp')

print("\n   星历数据已加载！")
print("   文件位置: ~/.skyfield/de421.bsp")

# 获取当前时间
print("\n3. 获取当前时间的行星位置...")
t = ts.now()
print(f"   当前时间: {t.utc_iso()}")

# 获取地球和火星的位置
earth = planets['earth']
mars = planets['mars']

print("\n4. 计算地球和火星的位置...")
earth_pos = earth.at(t)
mars_pos = mars.at(t)

print(f"\n   地球位置 (相对太阳系质心, AU):")
print(f"   x = {earth_pos.position.au[0]:.6f}")
print(f"   y = {earth_pos.position.au[1]:.6f}")
print(f"   z = {earth_pos.position.au[2]:.6f}")

print(f"\n   火星位置 (相对太阳系质心, AU):")
print(f"   x = {mars_pos.position.au[0]:.6f}")
print(f"   y = {mars_pos.position.au[1]:.6f}")
print(f"   z = {mars_pos.position.au[2]:.6f}")

# 计算火星相对地球的位置
print("\n5. 计算火星相对地球的位置...")
mars_from_earth = earth.at(t).observe(mars)
distance = mars_from_earth.distance().au

print(f"   地球到火星的距离: {distance:.6f} AU")
print(f"   (1 AU = 1.496 × 10^8 km)")

print("\n" + "=" * 60)
print("测试成功！")
print("=" * 60)
print("\n说明：")
print("- DE421 星历文件已自动下载")
print("- 不需要手动下载 de440.bsp")
print("- DE421 精度对大多数应用已足够")
print("- 如需更高精度或更长时间范围，可使用 'de440.bsp'")
print("  但需要从其他源下载（文件较大，114MB）")
