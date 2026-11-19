# Owli Classic — Visual Character Specification (v0.1)

## Authority and uncertainty

Primary source: `references/Owli_Character-Sheet.png` (provided by project owner). The image is an illustrated character reference, **not calibrated orthographic geometry**. View-to-view inconsistency is to be resolved by consistent 3D silhouette and visual review, never by claiming exact measurements.

Eight view captions are: 0° Front, 45° right-front, 90° right, 135° right-rear, 180° rear, 225° left-rear, 270° left, 315° left-front. Additional views: top, bottom, spread wings, face/eye, forehead symbol, beak, chest, wing, tail and claws.

## Signature appearance

- Friendly juvenile stylized owl; **large head** and compact pear-shaped body, not a realistic bird.
- Two prominent swept, outward/upward ear/feather tufts create a crown silhouette.
- Extremely large, glossy **blue/cyan eyes**, dark pupils, bright white highlights and broad off-white facial discs.
- Short orange-to-yellow wedge-shaped beak, small compared with the eyes. Separate movable lower jaw without visible gaps at rest.
- Layered feather surfaces: dark navy structural shadows, cobalt/royal-blue main feathers, cyan edge and tip accents.
- Symmetrical cream-white heart-shaped chest and face, with cyan and warm orange/gold feather accents at lower face/shoulders.
- Small orange feet with three front toes and one rear toe on each foot; black/dark claws.
- Cyan glowing forehead mark (star/dot/circuit-like ornament), recognizable at small sizes.
- Dense, tapered layered tail; wings can fold against body or unfold for expression.

## Relative proportions

Concept reference: head ~45% of height, torso ~45%, feet/legs ~10%. Width approximately similar to torso height in front view. These are **visual constraints** for the finished character, not measurements of the starting blockout.

## Palette — from source image

| Role | Hex |
| --- | --- |
| Deep navy/shadow | `#0B234C` |
| Royal blue feathers | `#0E6FC5` |
| Cyan/turquoise highlights | `#12D7EB` |
| White/off-white face and chest | `#F9F9FB` |
| Orange beak/claws | `#FF9A1F` |
| Yellow/amber accents | `#FFD166` |

Colors are nominal sRGB targets; actual appearance depends on shader, lighting and color-management settings. Use palette from `configs/character.json`.

## Axes and turntable

Coordinate system: Z up, front -Y, camera +X at right-side 90°. Same orthographic camera distance, focal target, lighting, exposure and background for 8 renders. Angle order: 0, 45, 90, 135, 180, 225, 270, 315.

## Visual comparison checklist

1. Front: ear tufts, eye spacing/size, creamy face/chest, beak scale and feet placement.
2. Right/left: beak projection, facial discs, wing mass, tail and leg contours.
3. Rear: chevron feather layering, tail and wing continuity.
4. 45-degree views: volume coherence (not paper cutouts); no missing feather transitions.
5. Top/bottom: crown/tuft rhythm; toes and feather bases.
6. Deformations: no wing-body intersections, beak gaps, detached feathers or eye clipping.

No automatic score substitutes for manually viewing rendered results. Keep a milestone image grid of reference versus rendered angles in `build/`.
