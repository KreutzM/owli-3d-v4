# Owli Rig Contract (proposed; M3 pending)

## Space and export assumptions

Z up; character forward is -Y; X positive denotes **world-space right**. Naming suffix `_L` / `_R` refers to the owl's anatomical sides (confirm mapping while facing the character) and must remain consistent across mirroring, tests and exports. Asset rests in an upright neutral stance with folded wings and closed beak.

## Minimal deform hierarchy

```text
root
└── body
    ├── neck
    │   └── head
    │       ├── beak_lower
    │       ├── eye_L
    │       └── eye_R
    ├── wing_L
    │   └── wing_mid_L
    │       └── wing_tip_L
    ├── wing_R
    │   └── wing_mid_R
    │       └── wing_tip_R
    ├── tail
    ├── leg_L
    │   └── foot_L
    └── leg_R
        └── foot_R
```

This is a contract for future implementation, **not evidence the current blockout is rigged**. Control bones may be additional; export only deform bones or baked animation as appropriate.

## Stable animation channels

- `beak_open`: normalized [0,1], **0 = closed**; opens mostly the lower beak.
- `blink_L` / `blink_R`: [0,1].
- `look_yaw` / `look_pitch`: small natural eye motion, neutral 0.
- `wing_spread_L` / `wing_spread_R`: [0,1].
- `head_yaw` / `head_pitch` / `head_roll`: radians.
- `tail_sway`: radians.

Animation clips (eventually): `idle`, `blink`, `look`, `talk`, `hop`, `wing_wave`. Root motion and feet-on-perch constraints must be explicitly documented per clip.

## Acceptance criteria

Closed beak hides seams; fully opened lower jaw does not intersect chest. Wing root geometry looks attached throughout motions; feathers deform/follow properly. Both eyelids close without penetrating eye globes. Repeatable foot and perch contact. GLB export must reimport with expected hierarchy, actions and allowed shape keys; Blender drivers do not automatically transfer.
