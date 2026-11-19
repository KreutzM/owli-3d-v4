# Owli 3D v4

Reproducible, Python-driven Blender 5.2 LTS project for **Owli**, a stylized blue owl avatar. The objective is a recognizable 360° character, exportable animation rig, and TTS-driven beak synchronization.

**Current status: M0 foundation / M1 blockout starting point — not a finished avatar.** The generated blockout is deliberately simplistic and is not yet rigged or speech-enabled.

## Prerequisites

- Python 3.11+ for ordinary tests; Blender **5.2 LTS** for generating scenes (its embedded Python executes `bpy`)
- Git and Git LFS (for .blend, .glb, .wav and similar large deliverables)
- Codex CLI, signed in using your ChatGPT account

## Quick start

```bash
git clone https://github.com/KreutzM/owli-3d-v4.git
cd owli-3d-v4
git lfs install
python -m pip install -e ".[dev]"
python -m pytest -q
blender --background --factory-startup --python-exit-code 1 --python scripts/build.py -- --config configs/character.json --output build/owli.blend --renders
blender --background build/owli.blend --python-exit-code 1 --python scripts/validate.py -- --output build/validation.json
```

If `blender` is not on PATH, use the absolute executable path. Generated BLEND, images, reports and GLB artifacts belong in `build/` or `dist/` (ignored by Git).

## Required reference sheet

**The binary reference image is not committed yet.** Add the original file to `references/Owli_Character-Sheet.png`. This filename is part of the reference contract; see `references/README.md`. Do not claim visual similarity before that file is present and actual 8-view renders have been compared.

## Work autonomously with Codex

```bash
codex login
codex --ask-for-approval never --sandbox workspace-write
```

The checked-in `.codex/config.toml` selects `gpt-6.2-astra`, medium reasoning, sandboxed workspace writing and no routine approval prompts. Trust the repository in Codex so its project config is loaded. System or machine-level policies can take precedence. Network access inside the sandbox is enabled for routine development; never store API keys in this repository. `AGENTS.md` describes autonomous work boundaries.

Start with: **"Implement the next uncompleted milestone in docs/roadmap.md. Execute tests and Blender headless validation, render all eight angles, and document the result without claiming unverified quality."**

## Project layout

- `AGENTS.md` – persistent autonomous agent policy
- `.codex/config.toml` – project-scoped Codex defaults
- `configs/` – dependency-free JSON character and render parameters
- `src/owli/` – reusable pure Python, geometry and speech components
- `scripts/` – Blender headless entry points
- `docs/` – visual, rig, speech and acceptance contracts
- `tests/` and `.github/workflows/` – fast Python checks
- `references/` – human-authoritative art reference

GitHub Actions runs fast Python tests plus a separate Blender 5.2.1 headless smoke workflow. The smoke workflow validates a generated BLEND; eight rendered angles can additionally be requested through its manual workflow input. Visual similarity to the concept sheet still requires a human reference comparison.

## Safety and limitations

`approval_policy="never"` means Codex does not ask routine permission; it **does not bypass** workspace sandbox restrictions. Some Codex environments protect `.git/` and `.codex/` even for workspace-write sessions. Only elevate access in a dedicated, trusted environment, never as a default. Confirm externally billable TTS calls or publishing production artifacts separately.

## Roadmap

See [roadmap](docs/roadmap.md), [character specification](docs/character-spec.md), [rig contract](docs/rig-contract.md) and [acceptance criteria](docs/acceptance-criteria.md).
