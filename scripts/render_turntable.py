"""Render eight standard angles from a previously saved .blend scene."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from owli.config import load_character, load_render  # noqa: E402
from owli.rendering import render_turntable  # noqa: E402


def main():
    import bpy

    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/character.json")
    parser.add_argument("--render-config", default="configs/render.json")
    parser.add_argument("--output", default="build/turntable")
    args = parser.parse_args(argv)
    character = load_character(ROOT / args.config)
    render = load_render(ROOT / args.render_config)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    for image in render_turntable(bpy, character, render, output):
        print(f"Rendered: {image}")


if __name__ == "__main__":
    main()
