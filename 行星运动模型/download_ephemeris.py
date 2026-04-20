#!/usr/bin/env python3
"""
使用 astropy 和 jplephem 获取行星星历数据
这些库会自动处理数据下载和缓存
"""

# 方法1: 使用 astropy 的内置星历
from astropy.coordinates import solar_system_ephemeris, get_body
from astropy.time import Time
import astropy.units as u

def get_planet_position_astropy(planet_name, time):
    """
    使用 astropy 获取行星位置

    参数:
        planet_name: 行星名称 ('earth', 'mars', 'jupiter' 等)
        time: 时间 (astropy.time.Time 对象)

    返回:
        行星的位置坐标
    """
    with solar_system_ephemeris.set('builtin'):
        position = get_body(planet_name, time)
    return position

# 方法2: 使用 jplephem (需要手动下载数据文件)
def setup_jplephem():
    """
    使用 jplephem 库
    这个库可以从其他源下载星历数据
    """
    try:
        from jplephem.spk import SPK
        print("jplephem 已安装")
        print("可以从以下备用源下载 DE440:")
        print("1. https://ssd.jpl.nasa.gov/ftp/eph/planets/bsp/de440.bsp")
        print("2. 或使用 astropy 的内置星历（不需要额外下载）")
    except ImportError:
        print("需要安装: pip install jplephem")

# 方法3: 使用 skyfield (最简单，自动下载)
def setup_skyfield():
    """
    使用 Skyfield 库 - 会自动下载和管理星历数据
    """
    try:
        from skyfield.api import load

        # Skyfield 会自动下载需要的星历文件到本地缓存
        ts = load.timescale()
        planets = load('de421.bsp')  # 使用 DE421，比 DE440 小但精度足够

        print("Skyfield 设置成功！")
        print("星历数据会自动下载到: ~/.skyfield/")

        return ts, planets
    except ImportError:
        print("需要安装: pip install skyfield")
        return None, None

if __name__ == "__main__":
    print("=" * 60)
    print("行星星历数据获取方案")
    print("=" * 60)

    print("\n推荐方案：使用 Skyfield 库")
    print("-" * 60)
    print("优点：")
    print("  - 自动下载和管理星历数据")
    print("  - 使用简单")
    print("  - 不需要手动处理 .bsp 文件")
    print("\n安装命令：")
    print("  pip install skyfield")

    print("\n" + "=" * 60)
    print("备选方案：使用 astropy 内置星历")
    print("-" * 60)
    print("优点：")
    print("  - 不需要下载额外文件")
    print("  - astropy 是标准天文库")
    print("\n安装命令：")
    print("  pip install astropy")

    print("\n" + "=" * 60)

    # 尝试运行
    print("\n正在测试 Skyfield...")
    setup_skyfield()
