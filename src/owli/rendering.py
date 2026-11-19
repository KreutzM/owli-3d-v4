"""Camera, lighting and eight-view headless rendering for Blender 5.2 LTS."""

import math
from pathlib import Path


def _point_to(obj, target):
    from mathutils import Vector  # Provided by Blender at runtime.

    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def setup_scene(bpy, character: dict, render: dict) -> None:
    scene = bpy.context.scene
    scale = character["height_m"] / 3.0
    scene.render.engine = "BLENDER_EEVEE"  # Blender 5.x identifier.
    scene.render.resolution_x = render["resolution_px"][0]
    scene.render.resolution_y = render["resolution_px"][1]
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = render.get("transparent_background", False)
    scene.render.fps = render["fps"]
    scene.view_settings.view_transform = "AgX"

    world = bpy.data.worlds.new("OWLI_World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    bg.inputs["Color"].default_value = render["background_rgba"]
    bg.inputs["Strength"].default_value = 0.65

    camera_data = bpy.data.cameras.new("OWLI_Camera")
    camera = bpy.data.objects.new("OWLI_Camera", camera_data)
    scene.collection.objects.link(camera)
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = render["camera_ortho_scale"] * scale
    scene.camera = camera

    for name, pos, power, shape in (
        ("OWLI_Key", (-3.0, -4.0, 5.0), 1400, 4.0),
        ("OWLI_Fill", (3.0, 1.5, 3.8), 950, 3.0),
    ):
        data = bpy.data.lights.new(name, "AREA")
        obj = bpy.data.objects.new(name, data)
        scene.collection.objects.link(obj)
        obj.location = tuple(p * scale for p in pos)
        data.energy = power * scale * scale
        data.shape = "DISK"
        data.size = shape * scale
        _point_to(obj, (0, 0, 1.5 * scale))

    set_camera_angle(bpy, character, render, 0)


def set_camera_angle(bpy, character: dict, render: dict, angle_deg: int) -> None:
    scale = character["height_m"] / 3.0
    distance = render["camera_distance"] * scale
    angle = math.radians(angle_deg)
    camera = bpy.context.scene.camera
    camera.location = (
        math.sin(angle) * distance,
        -math.cos(angle) * distance,
        1.50 * scale,
    )
    _point_to(camera, (0, 0, 1.50 * scale))


def render_turntable(bpy, character: dict, render: dict, directory: str | Path) -> list[Path]:
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    output = []
    for angle in render["angles_deg"]:
        set_camera_angle(bpy, character, render, angle)
        filepath = (directory / f"owli_{angle:03d}.png").resolve()
        scene.render.filepath = str(filepath)
        bpy.ops.render.render(write_still=True)
        output.append(filepath)
    # Restore the canonical frontal camera in the saved working scene.
    set_camera_angle(bpy, character, render, 0)
    return output
