# Speech and Beak-Sync Contract (M4 pending)

Speech is **provider independent**: TTS and alignment produce audio plus time cues; Blender consumes normalized cues and bakes an animation. Never put API keys, TTS provider clients or network requests in geometry modules.

## Cue schema (v1)

```json
{
  "schema_version": 1,
  "audio": "hello_de.wav",
  "duration": 1.2,
  "cues": [
    { "time": 0.0, "beak_open": 0.0 },
    { "time": 0.15, "beak_open": 0.7 },
    { "time": 0.35, "beak_open": 0.0 }
  ]
}
```

Times are seconds from the start of the audio, strictly increasing, finite, within duration. `beak_open` is finite and clamped/validated in [0,1]. The final pose may close automatically on playback but the file should contain a closure cue. Cues are **illustrative unless aligned to real audio**.

## Suggested pipeline

1. Generate speech audio from a configured TTS provider with explicit permission for paid calls.
2. Obtain real phoneme/viseme timing or run offline forced alignment.
3. Map articulation to three–five stylized beak states plus optional throat/head nuance. A bird cannot form human lip shapes.
4. Smooth with short interpolation while preserving hard closures for pauses.
5. Bake `beak_open` into a rig controller/shape key; align animation FPS with audio duration.
6. Test drift at beginning, middle and end of utterances; use audio playback in the target runtime.

Never infer that text token timestamps equal phonetic timing. Audio/video exports are separate from the JSON control interface.
