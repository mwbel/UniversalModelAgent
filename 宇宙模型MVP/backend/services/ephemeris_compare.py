from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
from jplephem.spk import SPK
from pymeeus.Coordinates import mean_obliquity
from pymeeus.Earth import Earth
from pymeeus.Epoch import Epoch
from pymeeus.Jupiter import Jupiter
from pymeeus.Mars import Mars
from pymeeus.Mercury import Mercury
from pymeeus.Moon import Moon
from pymeeus.Neptune import Neptune
from pymeeus.Saturn import Saturn
from pymeeus.Uranus import Uranus
from pymeeus.Venus import Venus

UNIVMODEL_DIR = Path(__file__).resolve().parents[2].parent
EPHEMERIS_DIR = UNIVMODEL_DIR / "行星运动模型"
DE440_PATH = EPHEMERIS_DIR / "de440.bsp"
AU_KM = 149597870.7
DEFAULT_TOLERANCE_UNIT = "AU"

PLANET_NAMES_CN = {
    "mercury": "水星",
    "venus": "金星",
    "earth": "地球",
    "mars": "火星",
    "jupiter": "木星",
    "saturn": "土星",
    "uranus": "天王星",
    "neptune": "海王星",
    "moon": "月球",
}

VSOP_PLANET_CLASSES = {
    "mercury": Mercury,
    "venus": Venus,
    "earth": Earth,
    "mars": Mars,
    "jupiter": Jupiter,
    "saturn": Saturn,
    "uranus": Uranus,
    "neptune": Neptune,
}

BODY_IDS = {
    "mercury": 1,
    "venus": 2,
    "earth": 3,
    "mars": 4,
    "jupiter": 5,
    "saturn": 6,
    "uranus": 7,
    "neptune": 8,
    "moon": 301,
}

ORBIT_PERIOD_DAYS = {
    "mercury": 87.969,
    "venus": 224.701,
    "earth": 365.256,
    "mars": 686.98,
    "jupiter": 4332.59,
    "saturn": 10759.22,
    "uranus": 30688.5,
    "neptune": 60182.0,
    "moon": 27.321661,
}


def julian_date(dt: datetime) -> float:
    year = dt.year
    month = dt.month
    day = dt.day
    if month <= 2:
        year -= 1
        month += 12
    a = year // 100
    b = 2 - a + a // 4
    day_fraction = (
        day
        + dt.hour / 24.0
        + dt.minute / 1440.0
        + dt.second / 86400.0
        + dt.microsecond / 86400_000000.0
    )
    return (
        int(365.25 * (year + 4716))
        + int(30.6001 * (month + 1))
        + day_fraction
        + b
        - 1524.5
    )


def _parse_datetime(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc).replace(tzinfo=None, microsecond=0)
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo:
        parsed = parsed.astimezone(timezone.utc).replace(tzinfo=None)
    return parsed.replace(microsecond=0)


def _datetime_to_epoch(selected_time: datetime) -> Epoch:
    day_fraction = (
        selected_time.day
        + selected_time.hour / 24.0
        + selected_time.minute / 1440.0
        + selected_time.second / 86400.0
    )
    return Epoch(selected_time.year, selected_time.month, day_fraction)


def _spherical_to_equatorial_cartesian(
    longitude_rad: float,
    latitude_rad: float,
    radius_au: float,
    obliquity_rad: float,
) -> np.ndarray:
    x_ecl = radius_au * np.cos(latitude_rad) * np.cos(longitude_rad)
    y_ecl = radius_au * np.cos(latitude_rad) * np.sin(longitude_rad)
    z_ecl = radius_au * np.sin(latitude_rad)
    x_eq = x_ecl
    y_eq = y_ecl * np.cos(obliquity_rad) - z_ecl * np.sin(obliquity_rad)
    z_eq = y_ecl * np.sin(obliquity_rad) + z_ecl * np.cos(obliquity_rad)
    return np.array([x_eq, y_eq, z_eq]) * AU_KM


def _equatorial_spherical_to_cartesian(
    longitude_rad: float,
    latitude_rad: float,
    distance_km: float,
) -> np.ndarray:
    return np.array(
        [
            distance_km * np.cos(latitude_rad) * np.cos(longitude_rad),
            distance_km * np.cos(latitude_rad) * np.sin(longitude_rad),
            distance_km * np.sin(latitude_rad),
        ]
    )


@lru_cache(maxsize=1)
def _spk() -> SPK:
    return SPK.open(str(DE440_PATH))


def _compute_vsop_position(planet: str, selected_time: datetime) -> tuple[np.ndarray, np.ndarray, float]:
    epoch = _datetime_to_epoch(selected_time)
    longitude, latitude, radius_au = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(epoch)
    position_km = _spherical_to_equatorial_cartesian(
        longitude.rad(),
        latitude.rad(),
        radius_au,
        np.deg2rad(float(mean_obliquity(epoch))),
    )

    delta = timedelta(minutes=30)
    before_epoch = _datetime_to_epoch(selected_time - delta)
    after_epoch = _datetime_to_epoch(selected_time + delta)
    lon_before, lat_before, radius_before = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(before_epoch)
    lon_after, lat_after, radius_after = VSOP_PLANET_CLASSES[planet].geometric_heliocentric_position(after_epoch)
    pos_before = _spherical_to_equatorial_cartesian(
        lon_before.rad(),
        lat_before.rad(),
        radius_before,
        np.deg2rad(float(mean_obliquity(before_epoch))),
    )
    pos_after = _spherical_to_equatorial_cartesian(
        lon_after.rad(),
        lat_after.rad(),
        radius_after,
        np.deg2rad(float(mean_obliquity(after_epoch))),
    )
    velocity_km_s = (pos_after - pos_before) / (2.0 * delta.total_seconds())
    return position_km, velocity_km_s, float(np.linalg.norm(position_km) / AU_KM)


def _compute_vsop_moon_position(selected_time: datetime) -> tuple[np.ndarray, np.ndarray, float]:
    earth_position_km, _, _ = _compute_vsop_position("earth", selected_time)
    epoch = _datetime_to_epoch(selected_time)
    right_ascension, declination, distance_km, _ = Moon.apparent_equatorial_pos(epoch)
    moon_geocentric_km = _equatorial_spherical_to_cartesian(
        right_ascension.rad(),
        declination.rad(),
        distance_km,
    )
    position_km = earth_position_km + moon_geocentric_km

    delta = timedelta(minutes=30)
    before = selected_time - delta
    after = selected_time + delta
    earth_before_km, _, _ = _compute_vsop_position("earth", before)
    earth_after_km, _, _ = _compute_vsop_position("earth", after)
    ra_before, dec_before, distance_before_km, _ = Moon.apparent_equatorial_pos(_datetime_to_epoch(before))
    ra_after, dec_after, distance_after_km, _ = Moon.apparent_equatorial_pos(_datetime_to_epoch(after))
    moon_before_km = earth_before_km + _equatorial_spherical_to_cartesian(
        ra_before.rad(),
        dec_before.rad(),
        distance_before_km,
    )
    moon_after_km = earth_after_km + _equatorial_spherical_to_cartesian(
        ra_after.rad(),
        dec_after.rad(),
        distance_after_km,
    )
    velocity_km_s = (moon_after_km - moon_before_km) / (2.0 * delta.total_seconds())
    return position_km, velocity_km_s, float(np.linalg.norm(position_km) / AU_KM)


def _compute_vsop_like_position(planet: str, selected_time: datetime) -> tuple[np.ndarray, np.ndarray, float]:
    if planet == "moon":
        return _compute_vsop_moon_position(selected_time)
    return _compute_vsop_position(planet, selected_time)


def _compute_de440_like_position(planet: str, selected_time: datetime) -> tuple[np.ndarray, np.ndarray, float]:
    spk = _spk()
    jd = julian_date(selected_time)

    if planet not in {"earth", "moon"}:
        body_pos, body_vel = spk[0, BODY_IDS[planet]].compute_and_differentiate(jd)
        sun_pos, sun_vel = spk[0, 10].compute_and_differentiate(jd)
        body_pos = body_pos - sun_pos
        body_vel = body_vel - sun_vel
        return body_pos, body_vel / 86400.0, float(np.linalg.norm(body_pos) / AU_KM)

    emb_pos, emb_vel = spk[0, 3].compute_and_differentiate(jd)
    sun_pos, sun_vel = spk[0, 10].compute_and_differentiate(jd)
    rel_segment = spk[3, 399] if planet == "earth" else spk[3, 301]
    rel_pos, rel_vel = rel_segment.compute_and_differentiate(jd)
    body_pos = emb_pos + rel_pos - sun_pos
    body_vel = emb_vel + rel_vel - sun_vel
    return body_pos, body_vel / 86400.0, float(np.linalg.norm(body_pos) / AU_KM)


def _vector(values: np.ndarray, divisor: float = 1.0) -> list[float]:
    return [round(float(item) / divisor, 8) for item in values]


def _parse_tolerance(value: str | None) -> float | None:
    if not value:
        return None
    normalized = value.strip().lower().replace(" ", "")
    normalized = normalized.replace("×10^", "e").replace("*10^", "e")
    normalized = normalized.replace("10^-", "1e-").replace("10^", "1e")
    try:
        return float(normalized)
    except ValueError:
        return None


def normalize_tolerance_unit(value: str | None) -> str:
    normalized = (value or DEFAULT_TOLERANCE_UNIT).strip().lower()
    if normalized in {"km", "公里", "千米"}:
        return "km"
    return "AU"


def _recommend_model(delta_distance_km: float, tolerance_value: float | None, tolerance_unit: str) -> dict[str, Any]:
    if tolerance_value is None:
        return {
            "model": "DE440",
            "reason": "未提供精度阈值，默认推荐使用高精度 DE440 数值星历。",
            "meetsTolerance": None,
        }

    tolerance_km = tolerance_value if tolerance_unit == "km" else tolerance_value * AU_KM
    meets_tolerance = delta_distance_km <= tolerance_km
    return {
        "model": "VSOP_OK" if meets_tolerance else "DE440",
        "reason": (
            "VSOP 与 DE440 的差异低于用户阈值，可用于该精度要求。"
            if meets_tolerance
            else "VSOP 与 DE440 的差异超过用户阈值，建议使用 DE440。"
        ),
        "meetsTolerance": meets_tolerance,
        "tolerance": {
            "value": tolerance_value,
            "unit": tolerance_unit,
            "km": round(tolerance_km, 6),
        },
    }


def _sample_orbit_path(
    body: str,
    selected_time: datetime,
    model: str,
    sample_count: int = 49,
) -> list[list[float]]:
    period_days = ORBIT_PERIOD_DAYS.get(body)
    if not period_days:
        return []

    compute = _compute_de440_like_position if model == "de440" else _compute_vsop_like_position
    half_window = period_days / 2.0
    offsets = np.linspace(-half_window, half_window, sample_count)
    path: list[list[float]] = []
    for offset_days in offsets:
        sample_time = selected_time + timedelta(days=float(offset_days))
        position_km, _, _ = compute(body, sample_time)
        path.append(_vector(position_km, AU_KM))
    return path


def compare_ephemeris(
    date: str | None = None,
    bodies: str | None = None,
    tolerance: str | None = None,
    tolerance_unit: str | None = None,
    include_orbits: bool = False,
) -> dict[str, Any]:
    if not DE440_PATH.exists():
        return {
            "ok": False,
            "error": f"未找到 DE440 星历文件：{DE440_PATH}",
            "items": [],
        }

    selected_time = _parse_datetime(date)
    parsed_tolerance = _parse_tolerance(tolerance)
    normalized_tolerance_unit = normalize_tolerance_unit(tolerance_unit)
    requested = [item.strip().lower() for item in (bodies or "").split(",") if item.strip()]
    selected_bodies = [body for body in requested if body in BODY_IDS] or [
        "mercury",
        "venus",
        "earth",
        "mars",
        "jupiter",
        "saturn",
    ]

    items: list[dict[str, Any]] = []
    for body in selected_bodies:
        if body not in BODY_IDS or (body not in VSOP_PLANET_CLASSES and body != "moon"):
            continue
        try:
            de_position_km, de_velocity_km_s, de_distance_au = _compute_de440_like_position(body, selected_time)
            vsop_position_km, vsop_velocity_km_s, vsop_distance_au = _compute_vsop_like_position(body, selected_time)
        except Exception as error:  # noqa: BLE001
            items.append({"body": body, "name": PLANET_NAMES_CN.get(body, body), "error": str(error)})
            continue

        delta_vector_km = vsop_position_km - de_position_km
        delta_distance_km = float(np.linalg.norm(delta_vector_km))
        de440_payload: dict[str, Any] = {
            "positionKm": _vector(de_position_km),
            "positionAu": _vector(de_position_km, AU_KM),
            "velocityKmS": _vector(de_velocity_km_s),
            "distanceAu": round(de_distance_au, 8),
        }
        vsop_payload: dict[str, Any] = {
            "positionKm": _vector(vsop_position_km),
            "positionAu": _vector(vsop_position_km, AU_KM),
            "velocityKmS": _vector(vsop_velocity_km_s),
            "distanceAu": round(vsop_distance_au, 8),
        }
        if include_orbits:
            try:
                de440_payload["orbitPathAu"] = _sample_orbit_path(body, selected_time, "de440")
                vsop_payload["orbitPathAu"] = _sample_orbit_path(body, selected_time, "vsop")
            except Exception:
                pass

        items.append(
            {
                "body": body,
                "name": PLANET_NAMES_CN.get(body, body),
                "de440": de440_payload,
                "vsop": vsop_payload,
                "delta": {
                    "vectorKm": _vector(delta_vector_km),
                    "distanceKm": round(delta_distance_km, 3),
                    "distanceAu": round(delta_distance_km / AU_KM, 10),
                    "speedKmS": round(float(np.linalg.norm(vsop_velocity_km_s - de_velocity_km_s)), 8),
                },
                "recommendation": _recommend_model(
                    delta_distance_km=delta_distance_km,
                    tolerance_value=parsed_tolerance,
                    tolerance_unit=normalized_tolerance_unit,
                ),
            }
        )

    return {
        "ok": True,
        "date": selected_time.isoformat() + "Z",
        "source": str(EPHEMERIS_DIR),
        "models": ["VSOP/PyMeeus", "DE440"],
        "referenceFrame": "heliocentric-equatorial",
        "tolerance": {
            "value": parsed_tolerance,
            "unit": normalized_tolerance_unit,
        },
        "items": items,
    }
