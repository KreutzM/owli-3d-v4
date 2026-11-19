"""Check blockout contents: blender -b build/owli.blend --python scripts/validate.py -- --output build/validation.json"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from owli.geometry.blockout import REQUIRED_MESHES  # noqa: E402


def main():
    import bpy

    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/validation.json")
    args = parser.parse_args(argv)
    present = {obj.name for obj in bpy.data.objects if obj.type == "MESH"}
    missing = sorted(set(REQUIRED_MESHES) - present)
    errors = []
    if missing:
        errors.append("missing required M1 meshes: " + ", ".join(missing))
    if bpy.context.scene.camera is None:
        errors.append("scene has no active camera")
    if bpy.context.scene.render.engine != "BLENDER_EEVEE":
        errors.append("unexpected render engine (expected Blender 5.2 EEVEE)")
    result = {
        "stage": "M1_BLOCKOUT",
        "status": "PASS" if not errors else "FAIL",
        "mesh_count": len(present),
        "required_meshes": list(REQUIRED_MESHES),
        "errors": errors,
        "rigged": False,
        "speech_enabled": False,
        "visual_reviewed": False,
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
