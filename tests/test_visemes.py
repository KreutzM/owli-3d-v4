"""Timing validation and aperture interpolation are Blender-independent."""

import pytest

from owli.speech.visemes import sample_beak, validate_timeline

TIMELINE = {
    "schema_version": 1,
    "audio": "sample.wav",
    "duration": 1.0,
    "cues": [
        {"time": 0.0, "beak_open": 0.0},
        {"time": 0.5, "beak_open": 1.0},
        {"time": 1.0, "beak_open": 0.0},
    ],
}


def test_speech_interpolation():
    validate_timeline(TIMELINE)
    assert sample_beak(TIMELINE, 0.25) == pytest.approx(0.5)
    assert sample_beak(TIMELINE, 0.5) == pytest.approx(1.0)
    assert sample_beak(TIMELINE, 0.75) == pytest.approx(0.5)
    assert sample_beak(TIMELINE, 1.1) == 0.0


def test_reject_out_of_order():
    data = {**TIMELINE, "cues": [
        {"time": 0.7, "beak_open": 0.2},
        {"time": 0.3, "beak_open": 0.3},
    ]}
    with pytest.raises(ValueError):
        validate_timeline(data)


def test_reject_out_of_range_aperture():
    data = {**TIMELINE, "cues": [{"time": 0.0, "beak_open": 2.0}]}
    with pytest.raises(ValueError):
        validate_timeline(data)


def test_reject_nan():
    data = {**TIMELINE, "cues": [{"time": 0.0, "beak_open": float("nan")}]}
    with pytest.raises(ValueError):
        validate_timeline(data)
