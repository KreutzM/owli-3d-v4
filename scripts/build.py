"""Create M1 blockout scene in Blender: --background --python scripts/build.py -- [args]."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from owli.config import load_character, load_render  # noqa: E402
from owli.geometry.blockout import create_blockout  # noqa: E402
from owli.rendering import render_turntable, setup_scene  # noqa: E402


def options():
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description="Build procedural Owli blockout in Blender")
    parser.add_argument("--config", default="configs/character.json")
    parser.add_argument("--render-config", default="configs/render.json")
    parser.add_argument("--output", default="build/owli.blend")
    parser.add_argument("--renders", action="store_true", help="Render eight 45-degree angles")
    return parser.parse_args(argv)


def main():
    import bpy

    args = options()
    character = load_character(ROOT / args.config)
    settings = load_render(ROOT / args.render_config)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    create_blockout(bpy, character)
    setup_scene(bpy, character, settings)

    reference = ROOT / character["reference_image"]
    if not reference.is_file():
        print(f"WARNING: missing reference image: {reference}; visual comparison is blocked")

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(output.resolve()))
    print(f"Saved BLEND blockout: {output.resolve()}")

    if args.renders:
        rendered = render_turntable(bpy, character, settings, output.parent / "turntable")
        for image in rendered:
            print(f"Rendered: {image}")


if __name__ == "__main__":
    main()
