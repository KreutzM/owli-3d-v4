# Acceptance Criteria

## M0: infrastructure
- [x] Traceable project structure, AGENTS instructions and Codex defaults.
- [x] Static validation tests and GitHub Actions workflow defined.
- [ ] Verified GitHub Actions run (requires remote Actions execution).
- [ ] Local Blender 5.2 headless smoke build executed.

## M1: blockout
- [ ] Head/body/feet roughly respect 45/45/10 silhouette.
- [ ] Eight images at fixed angles generated, framing stable.
- [ ] Face, eye glints, tufts, beak and wings recognizable from 0/90/180/270.
- [ ] Visual review performed with supplied source sheet.
- [ ] No unintended missing objects or invisible geometry.

## M2: fidelity
- [ ] Side-by-side source comparison for all eight views; differences recorded.
- [ ] Layered feather volume visible in rear and wings; no paper-thin intersections.
- [ ] Eyes, emblem, chest and feet read clearly at avatar size.
- [ ] Human accepts silhouette and expression.

## M3: rig
- [ ] Named hierarchy and channels match `docs/rig-contract.md`.
- [ ] Extreme pose deformation checked for gaps and intersections.
- [ ] Idle, blink, glance, wing gesture, hop test clips.
- [ ] GLB reimport and action playback confirmed.

## M4: speech
- [ ] Real German TTS audio and aligned viseme/beak timeline.
- [ ] Deterministic baking; closed-rest and pauses.
- [ ] No perceptible systematic A/V drift in representative long utterance.
- [ ] Audio length, cue bounds, frame count validated.

## M5: runtime
- [ ] Valid GLB with materials, deform rig and baked animation.
- [ ] Test in documented target runtime; FPS and memory budget selected.
- [ ] No leaked secrets or unapproved licensed assets.
