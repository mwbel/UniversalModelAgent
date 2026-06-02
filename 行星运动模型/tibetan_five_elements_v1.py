#!/usr/bin/env python3
"""
Translate `shilun_calendar_months12_compare_v1.m` into Python helpers.

This module keeps the calculation steps close to the MATLAB version so the
Streamlit page can show Tibetan five-element results from a Gregorian date.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


MOON_PERIODS = np.array([7, 60, 60, 6, 707], dtype=int)
SUN_PERIODS = np.array([27, 60, 60, 6, 67], dtype=int)


@dataclass
class TibetanFiveElementsResult:
    year: int
    month: int
    day: int
    is_leap_month: bool
    jiyue: int
    runyu: int
    yao_base: list[int]
    sun_base: list[int]
    ding_yao: list[int]
    ding_sun: list[int]
    taiyin_riyuexiu: list[int]
    taiyang_riyuexiu: list[int]
    huihe: list[int]
    zuoyong: int


def reduction(v: list[int] | np.ndarray, periods: list[int] | np.ndarray) -> np.ndarray:
    """MATLAB-compatible reduction helper from the attached program."""
    v = np.array(v, dtype=int).copy()
    periods = np.array(periods, dtype=int)
    n = len(v)

    if v[-1] < 0:
        v[-1] += periods[-1]
        v[-2] -= 1

    v_rem = np.zeros(n, dtype=int)
    v_quo = np.zeros(n, dtype=int)
    v_rem[-1] = v[-1] % periods[-1]
    v_quo[-1] = v[-1] // periods[-1]

    for j in range(n - 2, 0, -1):
        if v[j] < 0:
            v[j] += periods[j]
            v[j - 1] -= 1
        total = v[j] + v_quo[j + 1]
        v_quo[j] = total // periods[j]
        v_rem[j] = total % periods[j]

    if v[0] < 0:
        v[0] += periods[0]
        v_rem[0] = v[0]

    v_rem[0] = (v[0] + v_quo[1]) % periods[0]
    return v_rem


def s_jiaoke(v: list[int] | np.ndarray, periods: list[int] | np.ndarray) -> tuple[np.ndarray, int]:
    """Sun footstep quotient helper from the MATLAB program."""
    v = np.array(v, dtype=int)
    periods = np.array(periods, dtype=int)
    n = len(v)

    v_rem = np.zeros(n, dtype=int)
    v_quo = np.zeros(n, dtype=int)
    v_rem[0] = v[0] % 135
    v_quo[0] = v[0] // 135

    for j in range(1, n):
        total = v[j] + v_rem[j - 1] * periods[j]
        v_quo[j] = total // 135
        v_rem[j] = total % 135

    return v_quo, int(v_rem[-1])


def _build_month_state(year: int, month: int, is_leap_month: bool) -> tuple[int, int]:
    """Resolve jiyue and runyu in the same month numbering convention as v1."""
    start_y = 1027
    mark_runyue = 1 if is_leap_month else 0
    jiyue0 = ((year - start_y) % 60) * 12 + ((month - 3) % 12) + mark_runyue
    jiyue = jiyue0 + (jiyue0 * 2) // 65
    runyu = (jiyue0 * 2) % 65
    return int(jiyue), int(runyu)


def compute_tibetan_five_elements_v1(
    year: int,
    month: int,
    day: int,
    is_leap_month: bool = False,
) -> TibetanFiveElementsResult:
    """Compute the five-element blocks using the attached v1 MATLAB logic."""
    if day < 1 or day > 30:
        raise ValueError("Tibetan day must be in 1..30")

    jiyue, runyu = _build_month_state(year, month, is_leap_month)

    yao_base = reduction(
        [jiyue * 1 + 3, jiyue * 31 + 11, jiyue * 50 + 27, jiyue * 0 + 2, jiyue * 480 + 332],
        MOON_PERIODS,
    )
    sun_base = reduction(
        [jiyue * 2, jiyue * 10, jiyue * 58, jiyue * 1, jiyue * 17],
        SUN_PERIODS,
    )

    rewo_qiaxi = reduction([jiyue * 2 + 21, jiyue * 1 + 90], [28, 126])
    rewo = int(rewo_qiaxi[0])
    qiaxi = int(rewo_qiaxi[1])

    add_m = np.array([0, 59, 3, 4, 16], dtype=int)
    add_s = np.array([0, 4, 21, 5, 43], dtype=int)
    m_rem = reduction(add_m * (day - 1), MOON_PERIODS)
    s_rem = reduction(add_s * (day - 1), SUN_PERIODS)
    mid_yao = reduction(yao_base + m_rem, MOON_PERIODS)
    mid_sun = reduction(sun_base + s_rem, SUN_PERIODS)

    quo_rewo = (rewo + day) // 14
    rem_rewo = (rewo + day) % 14
    level_flag = "o" if quo_rewo % 2 != 0 else "e"

    m_mul_lookup = np.array([5, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 5], dtype=int)
    m_add_lookup = np.array([0, 5, 10, 15, 19, 22, 24, 25, 24, 22, 19, 15, 10, 5], dtype=int)
    front_foot = rem_rewo <= 6
    m_mul_num = int(m_mul_lookup[rem_rewo])
    add_index = 13 if rem_rewo == 0 else rem_rewo - 1
    m_add_num = int(m_add_lookup[add_index])

    moon_jinxinke = np.zeros(5, dtype=int)
    moon_jinxinke[0] = m_add_num
    temp_m = qiaxi
    moon_step_periods = [1, m_mul_num, 60, 6, 707]
    for i in range(1, 5):
        moon_jinxinke[i] = (temp_m * moon_step_periods[i]) // 126
        temp_m = (temp_m * moon_step_periods[i]) % 126

    yao_jiaoke0 = np.zeros(4, dtype=int)
    if front_foot:
        yao_jiaoke0[0] = moon_jinxinke[0] + moon_jinxinke[1]
        yao_jiaoke0[1:] = moon_jinxinke[2:]
    else:
        yao_jiaoke0[0] = moon_jinxinke[0] - moon_jinxinke[1] - 1
        yao_jiaoke0[1:] = reduction([59, 5, 707] - moon_jinxinke[2:], [60, 6, 707])
    yao_jiaoke = reduction(yao_jiaoke0, [60, 60, 6, 707])

    if level_flag == "o":
        bandingyao = reduction(mid_yao - np.concatenate(([0], yao_jiaoke)), MOON_PERIODS)
    else:
        bandingyao = reduction(mid_yao + np.concatenate(([0], yao_jiaoke)), MOON_PERIODS)
    bandingyao_6 = np.array(
        [
            bandingyao[0],
            bandingyao[1],
            bandingyao[2],
            bandingyao[3],
            (bandingyao[4] * 67) // 707,
            (bandingyao[4] * 67) % 707,
        ],
        dtype=int,
    )

    temp = mid_sun - np.array([6, 45, 0, 0, 0], dtype=int)
    temp_rem0 = reduction(temp, SUN_PERIODS)

    over_half = False
    if temp_rem0[0] > 13 or (temp_rem0[0] == 13 and temp_rem0[1] >= 30):
        temp_rem1 = reduction(temp_rem0 - np.array([13, 30, 0, 0, 0], dtype=int), SUN_PERIODS)
        over_half = True
    else:
        temp_rem1 = temp_rem0

    quo_s = (temp_rem1[1] + temp_rem1[0] * 60) // 135
    rem_s = (temp_rem1[1] + temp_rem1[0] * 60) % 135
    if quo_s == 6:
        quo_s = 0

    sun_mul_lookup = np.array([6, 4, 1, 1, 4, 6], dtype=int)
    sun_add_lookup = np.array([0, 6, 10, 11, 10, 6], dtype=int)
    sun_front_foot = quo_s in (0, 1, 2)
    s_mul_num = int(sun_mul_lookup[quo_s])
    s_add_num = int(sun_add_lookup[5 if quo_s == 0 else quo_s - 1])

    sun_v = np.array([rem_s, temp_rem1[2], temp_rem1[3], temp_rem1[4]], dtype=int)
    v_quo, _ = s_jiaoke(sun_v * s_mul_num, [60, 60, 6, 67])
    sun_jinxinke = np.array([s_add_num, *v_quo], dtype=int)

    sun_jiaoke0 = np.zeros(4, dtype=int)
    if sun_front_foot:
        sun_jiaoke0[0] = sun_jinxinke[0] + sun_jinxinke[1]
        sun_jiaoke0[1:] = sun_jinxinke[2:]
    else:
        sun_jiaoke0[0] = sun_jinxinke[0] - sun_jinxinke[1] - 1
        sun_jiaoke0[1:] = np.array([59, 5, 67], dtype=int) - sun_jinxinke[2:]
    sun_jiaoke = reduction(sun_jiaoke0, [60, 60, 6, 67])

    if over_half:
        ding_yao = reduction(bandingyao_6 + np.array([0, *sun_jiaoke, 0], dtype=int), [7, 60, 60, 6, 67, 707])
        ding_sun = reduction(mid_sun + np.array([0, *sun_jiaoke], dtype=int), SUN_PERIODS)
    else:
        ding_yao = reduction(bandingyao_6 - np.array([0, *sun_jiaoke, 0], dtype=int), [7, 60, 60, 6, 67, 707])
        ding_sun = reduction(mid_sun - np.array([0, *sun_jiaoke], dtype=int), SUN_PERIODS)

    t3 = np.array([0, 54], dtype=int) if day == 1 else np.array([(54 * day) // 60, (54 * day) % 60], dtype=int)
    taiyin_riyuexiu = reduction(ding_sun + np.array([t3[0], t3[1], 0, 0, 0], dtype=int), SUN_PERIODS)
    taiyin_riyuexiu = np.concatenate((taiyin_riyuexiu, [0]))
    taiyang_riyuexiu = reduction(taiyin_riyuexiu - np.array([0, *ding_yao[1:]], dtype=int), [27, 60, 60, 6, 67, 707])
    huihe = reduction(taiyang_riyuexiu + np.array([*ding_sun, 0], dtype=int), [27, 60, 60, 6, 67, 707])
    zuoyong = (2 * day - 1) % 7

    return TibetanFiveElementsResult(
        year=year,
        month=month,
        day=day,
        is_leap_month=is_leap_month,
        jiyue=jiyue,
        runyu=runyu,
        yao_base=yao_base.astype(int).tolist(),
        sun_base=sun_base.astype(int).tolist(),
        ding_yao=ding_yao.astype(int).tolist(),
        ding_sun=ding_sun.astype(int).tolist(),
        taiyin_riyuexiu=taiyin_riyuexiu.astype(int).tolist(),
        taiyang_riyuexiu=taiyang_riyuexiu.astype(int).tolist(),
        huihe=huihe.astype(int).tolist(),
        zuoyong=int(zuoyong),
    )


def result_to_dict(result: TibetanFiveElementsResult) -> dict[str, Any]:
    """Serialize dataclass result for Streamlit rendering."""
    return {
        "year": result.year,
        "month": result.month,
        "day": result.day,
        "is_leap_month": result.is_leap_month,
        "jiyue": result.jiyue,
        "runyu": result.runyu,
        "yao_base": result.yao_base,
        "sun_base": result.sun_base,
        "ding_yao": result.ding_yao,
        "ding_sun": result.ding_sun,
        "taiyin_riyuexiu": result.taiyin_riyuexiu,
        "taiyang_riyuexiu": result.taiyang_riyuexiu,
        "huihe": result.huihe,
        "zuoyong": result.zuoyong,
    }
