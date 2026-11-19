"""Validated, interpolated beak-opening cues; no TTS provider dependency."""

import math
from bisect import bisect_right


def _is_number(value) -> bool:
    return type(value) in (int, float) and math.isfinite(value)


def validate_timeline(data: dict) -> None:
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("unsupported speech timeline schema")
    duration = data.get("duration")
    if not _is_number(duration) or duration <= 0:
        raise ValueError("duration must be positive finite seconds")
    cues = data.get("cues")
    if not isinstance(cues, list) or not cues:
        raise ValueError("nonempty cues array required")
    previous = -1.0
    for cue in cues:
        if not isinstance(cue, dict):
            raise ValueError("invalid cue")
        time = cue.get("time")
        amount = cue.get("beak_open")
        if not _is_number(time) or not previous < time <= duration:
            raise ValueError("cues must have strictly increasing times within duration")
        if not _is_number(amount) or not 0.0 <= amount <= 1.0:
            raise ValueError("beak_open must be between 0 and 1")
        previous = time


def sample_beak(data: dict, time: float) -> float:
    """Return linearly interpolated beak aperture; closed outside cue range."""
    validate_timeline(data)
    if not _is_number(time):
        raise ValueError("time must be finite")
    cues = data["cues"]
    if time < cues[0]["time"] or time > cues[-1]["time"]:
        return 0.0
    times = [cue["time"] for cue in cues]
    index = bisect_right(times, time) - 1
    if index == len(cues) - 1 or time == cues[index]["time"]:
        return float(cues[index]["beak_open"])
    left, right = cues[index], cues[index + 1]
    ratio = (time - left["time"]) / (right["time"] - left["time"])
    return (1.0 - ratio) * left["beak_open"] + ratio * right["beak_open"]
