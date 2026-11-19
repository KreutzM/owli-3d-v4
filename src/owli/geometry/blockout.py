"""Deliberately simple procedural M1 Owli blockout (not production geometry).

Coordinate space: Z up, character front -Y, world right +X.
No bpy import at module load time so ordinary Python tests can import this file.
"""

import math

from owli.config import color_srgb_to_linear

REQUIRED_MESHES = (
    "OWLI_Body",
    "OWLI_Head",
    "OWLI_Chest",
    "OWLI_Beak_Upper",
    "OWLI_Beak_Lower",
    "OWLI_Eye_L",
    "OWLI_Eye_R",
    "OWLI_Wing_L",
    "OWLI_Wing_R",
    "OWLI_Foot_L",
    "OWLI_Foot_R",
    "OWLI_Tuft_L",
    "OWLI_Tuft_R",
    "OWLI_Forehead_Mark",
)


def _material(bpy, name: str, color: str):
    mat = bpy.data.materials.new(f"OWLI_MAT_{name}")
    rgba = color_srgb_to_linear(color)
    mat.diffuse_color = rgba
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = rgba
    shader.inputs["Roughness"].default_value = 0.44
    return mat


def _orb(bpy, name, pos, radii, material, size):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=20, location=[p * size for p in pos])
    obj = bpy.context.object
    obj.name = name
    obj.scale = [r * size for r in radii]
    obj.data.materials.append(material)
    for polygon in obj.data.polygons:
        polygon.use_smooth = True
    obj["owli_stage"] = "M1_BLOCKOUT"
    return obj


def create_blockout(bpy, character: dict) -> None:
    """Build a recognizable but intentionally approximate owl from primitives."""
    palette = character["palette"]
    mats = {name: _material(bpy, name, value) for name, value in palette.items()}
    size = character["height_m"] / 3.0

    _orb(bpy, "OWLI_Body", (0, 0.03, 1.06), (0.73, 0.59, 0.72), mats["blue"], size)
    _orb(bpy, "OWLI_Chest", (0, -0.48, 1.18), (0.55, 0.20, 0.53), mats["white"], size)
    _orb(bpy, "OWLI_Head", (0, 0, 2.20), (0.81, 0.59, 0.65), mats["blue"], size)

    for sign, side in ((-1, "L"), (1, "R")):
        tuft = _orb(
            bpy,
            f"OWLI_Tuft_{side}",
            (sign * 0.62, -0.02, 2.75),
            (0.20, 0.18, 0.42),
            mats["navy"],
            size,
        )
        tuft.rotation_euler[1] = sign * math.radians(28)
        _orb(
            bpy,
            f"OWLI_Wing_{side}",
            (sign * 0.70, 0.13, 1.28),
            (0.33, 0.42, 0.62),
            mats["navy"],
            size,
        )
        _orb(
            bpy,
            f"OWLI_Foot_{side}",
            (sign * 0.34, -0.27, 0.23),
            (0.22, 0.29, 0.16),
            mats["orange"],
            size,
        )
        for toe_index in (-1, 0, 1):
            _orb(
                bpy,
                f"OWLI_Toe_{side}_{toe_index}",
                (sign * 0.34 + toe_index * 0.13, -0.46, 0.16),
                (0.08, 0.20, 0.09),
                mats["orange"],
                size,
            )

        # Separate facial disc, eyeball, iris, pupil and highlight for future rigging.
        x = sign * 0.36
        _orb(bpy, f"OWLI_FaceDisk_{side}", (x, -0.48, 2.19), (0.40, 0.17, 0.45), mats["white"], size)
        _orb(bpy, f"OWLI_Eye_{side}", (x, -0.62, 2.26), (0.31, 0.21, 0.34), mats["white"], size)
        _orb(bpy, f"OWLI_Iris_{side}", (x, -0.80, 2.26), (0.24, 0.075, 0.25), mats["cyan"], size)
        _orb(bpy, f"OWLI_Pupil_{side}", (x, -0.86, 2.26), (0.15, 0.05, 0.19), mats["navy"], size)
        _orb(
            bpy,
            f"OWLI_EyeHighlight_{side}",
            (x - 0.065, -0.91, 2.37),
            (0.062, 0.035, 0.066),
            mats["white"],
            size,
        )

    for index, x in enumerate((-0.25, 0.0, 0.25)):
        _orb(
            bpy,
            f"OWLI_TailFeather_{index}",
            (x, 0.51, 0.64),
            (0.23, 0.18, 0.46),
            mats["cyan"] if index == 1 else mats["blue"],
            size,
        )

    bpy.ops.mesh.primitive_cone_add(
        vertices=4,
        radius1=0.25 * size,
        radius2=0.01 * size,
        depth=0.34 * size,
        location=(0, -0.76 * size, 2.02 * size),
        rotation=(math.pi / 2, 0, math.pi / 4),
    )
    upper = bpy.context.object
    upper.name = "OWLI_Beak_Upper"
    upper.data.materials.append(mats["orange"])
    upper["owli_stage"] = "M1_BLOCKOUT"
    _orb(
        bpy, "OWLI_Beak_Lower", (0, -0.81, 1.88), (0.16, 0.13, 0.10), mats["yellow"], size
    )
    _orb(
        bpy, "OWLI_Forehead_Mark", (0, -0.57, 2.72), (0.10, 0.06, 0.12), mats["cyan"], size
    )
