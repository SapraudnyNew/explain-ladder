# Changelog

Versions of the `explain-ladder` plugin. Dates are UTC.

## 0.2.1, 2026-10-22

- Repository made public, shared as is and read only.
- README: status line, and a costs and privacy section naming what is paid (ElevenLabs, optional
  kie.ai) and where keys are read from.
- Added `SECURITY.md`, this changelog and a root `.gitignore` (evaluation results stay out of git).
- `scroll-craft`: narrower description; `scripts/worldflight-assert.mjs` finds the live instance
  through `ScrollCraft.instances`, accepts a `data-sc-lerp` override and checks that the engine
  uses the configured rate. All noted in its `UPSTREAM`.

## 0.2.0, 2026-10-18

- Vendored `scroll-craft` (MIT) for scroll-driven pages in the Apple keynote manner at level 3.

## 0.1.2, 2026-10-18

- `video-studio`: `scripts/with-env.sh` runs video commands with the ElevenLabs key file and the
  `video-use` Python environment.

## 0.1.1, 2026-10-18

- Documented the `git-lfs` requirement; `video-use` dependencies live in `~/.venvs/video-use`.

## 0.1.0, 2026-10-18

- Five levels with five aliases each, the `UserPromptSubmit` alias hook, `video-studio`, trigger
  evaluations, and vendored MIT skills: `archify`, `video-use`, `product-launch-motion`,
  `motion-design`.
