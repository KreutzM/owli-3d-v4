# Roadmap — milestone-oriented implementation

Status legend: DONE = tested; IN PROGRESS = code exists but not fully validated; TODO = not delivered.

- **M0 foundation — DONE (repository files):** docs, project configuration, fast Python CI, reusable config/speech helpers, Blender headless blockout entry points. Blender execution is not verified until run in a Blender 5.2 environment.
- **M1 blockout — IN PROGRESS:** recognizable head, body, eyes, beak, tufts and wing masses; consistent 8-angle images; documented deviations and visual review. Initial procedural blockout is a starting point only.
- **M2 visual fidelity — TODO:** layered feather geometry, precise owl silhouette, face/chest patterns, emblem, materials, front/back/side reference check and human aesthetic gate.
- **M3 deformation rig — TODO:** stable bones/weights, blinking, looking, wings, legs and feet, beak open/close, idle/wave/hop animations; bake/export tests.
- **M4 speech — TODO:** actual TTS integration, real timed alignment, normalized viseme/beak cues, German sample and accurate audio/video synchronization.
- **M5 distribution/runtime — TODO:** optimized GLB, import smoke tests, LOD, documented runtime integration and reproducible release.

## Autonomous iteration procedure

Select the earliest unfinished task in the current milestone. Implement the smallest coherent change, run cheap checks, render when possible, inspect evidence, then repeat. Do not mark M1+ DONE based on a code-only pass. Save important screenshots/reports to ignored `build/`. Discuss subjective visual approval only at M2 gate or when blocked by a genuine ambiguity.
