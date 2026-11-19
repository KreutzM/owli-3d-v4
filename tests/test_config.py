"""Pure-Python, no Blender required."""

from pathlib import Path

import pytest

from owli.config import ANGLES, color_srgb_to_linear, load_character, load_render

ROOT = Path(__file__).resolve().parents[1]


def test_character_config():
    data = load_character(ROOT / "configs/character.json")
    assert data["character"] == "Owli"
    assert sum(data["proportions"].values()) == pytest.approx(1.0)
    assert data["palette"]["cyan"] == "#12D7EB"


def test_render_contract():
    settings = load_render(ROOT / "configs/render.json")
    assert tuple(settings["angles_deg"]) == ANGLES
    assert settings["resolution_px"] == [640, 640]


def test_linear_color_roundtrip_endpoints():
    assert color_srgb_to_linear("#FFFFFF") == (1.0, 1.0, 1.0, 1.0)
    assert color_srgb_to_linear("#000000") == (0.0, 0.0, 0.0, 1.0)


def test_invalid_color_rejected():
    with pytest.raises(ValueError):
        color_srgb_to_linear("#BAD")
