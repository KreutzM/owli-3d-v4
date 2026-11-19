"""Small, dependency-free validated JSON configuration loader."""

import json
import math
import re
from pathlib import Path

HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
ANGLES = (0, 45, 90, 135, 180, 225, 270, 315)


def _read_json(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("configuration must be a JSON object")
    if data.get("schema_version") != 1:
        raise ValueError("unsupported configuration schema_version")
    return data


def load_character(path: str | Path) -> dict:
    """Load character settings, rejecting visually inconsistent dimensions."""
    data = _read_json(path)
    if data.get("character") != "Owli":
        raise ValueError("character must be Owli")
    height = data.get("height_m")
    if isinstance(height, bool) or not isinstance(height, (int, float)):
        raise ValueError("height_m must be numeric")
    if not math.isfinite(height) or not 0.1 <= height <= 10.0:
        raise ValueError("height_m must be between 0.1 and 10 metres")
    proportions = data.get("proportions", {})
    if set(proportions) != {"head", "body", "legs"}:
        raise ValueError("proportions must define head, body and legs")
    for name, ratio in proportions.items():
        if isinstance(ratio, bool) or not isinstance(ratio, (int, float)):
            raise ValueError(f"invalid {name} ratio")
        if not math.isfinite(ratio) or ratio <= 0.0 or ratio >= 1.0:
            raise ValueError(f"invalid {name} ratio")
    if not math.isclose(sum(proportions.values()), 1.0, abs_tol=0.001):
        raise ValueError("proportion ratios must add up to 1")
    palette = data.get("palette", {})
    needed = {"navy", "blue", "cyan", "white", "orange", "yellow"}
    if not needed.issubset(palette):
        raise ValueError("incomplete Owli palette")
    if any(not isinstance(v, str) or not HEX.fullmatch(v) for v in palette.values()):
        raise ValueError("all palette values must use #RRGGBB")
    return data


def load_render(path: str | Path) -> dict:
    """Validate required eight-view turntable framing."""
    data = _read_json(path)
    angles = data.get("angles_deg")
    if not isinstance(angles, list) or tuple(angles) != ANGLES:
        raise ValueError("render angles must be the eight standard 45-degree views")
    resolution = data.get("resolution_px")
    if (
        not isinstance(resolution, list)
        or len(resolution) != 2
        or any(type(x) is not int or not 64 <= x <= 8192 for x in resolution)
    ):
        raise ValueError("resolution_px must be two integers between 64 and 8192")
    for key in ("camera_ortho_scale", "camera_distance"):
        value = data.get(key)
        if (
            isinstance(value, bool)
            or not isinstance(value, (float, int))
            or not math.isfinite(value)
            or value <= 0
        ):
            raise ValueError(f"{key} must be positive finite")
    fps = data.get("fps")
    if type(fps) is not int or not 1 <= fps <= 120:
        raise ValueError("fps must be an integer between 1 and 120")
    return data


def color_srgb_to_linear(code: str) -> tuple[float, float, float, float]:
    """Convert sRGB #RRGGBB to scene-linear Blender-compatible RGBA."""
    if not HEX.fullmatch(code):
        raise ValueError("invalid hex color")
    srgb = [int(code[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in srgb)
    return (*linear, 1.0)
