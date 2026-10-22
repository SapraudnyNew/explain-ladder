# explain-ladder

A Claude Code plugin marketplace for one job: presenting an answer so a person can absorb it.
Five levels, one rule, five aliases per level.

The idea comes from Andrej Karpathy's thread of 2 October 2026 on making model output easier to
understand: controlled English, diagrams, HTML pages, explainer videos. This repository adds
markdown as level 0, the aliases, and the tools that produce each level. It is not affiliated with
or endorsed by him.

**Status: shared as is, read only.** Issues and pull requests are not taken. Fork it and change
what you need under the MIT licence. Security reports: [SECURITY.md](SECURITY.md).

## The rule

Use the lowest level that answers the question fully. Go higher only when it cuts the reader's
effort. An alias from you always wins.

| Level | You get | Say any of these |
|---|---|---|
| 0 | a markdown note | `write it up` · `as markdown` · `make a note` · `doc it` · `in md` |
| 1 | plain English (about 80% ASD-STE100) | `plain english` · `simple words` · `no jargon` · `ste mode` · `explain simply` |
| 2 | a diagram | `draw a diagram` · `diagram it` · `show the flow` · `map it` · `sketch it` |
| 3 | an interactive HTML page | `explain in html` · `make a page` · `html it` · `interactive page` · `build a page` |
| 4 | an explainer video | `explain as a video` · `make a video` · `video explainer` · `animate it` · `3b1b style` |

## Install

```
claude plugin marketplace add SapraudnyNew/explain-ladder
claude plugin install explain-ladder@explain-ladder
claude plugin install hyperframes@explain-ladder
claude plugin install gsap-skills@explain-ladder
claude plugin install answer-me-with-html@explain-ladder
```

The last three are the authors' own plugins, installed from their repositories through this
catalogue, so they update with their upstream.

Needs: Node.js 22 or newer (Archify, HyperFrames), `ffmpeg` and `ffprobe`, `git-lfs` (the
HyperFrames repository uses Git LFS, its install fails without it), Python 3.10 or newer for
`video-use`, and an ElevenLabs key for voice and transcription, read from `ELEVENLABS_API_KEY` or
`~/.config/elevenlabs/key` (mode 600). Nothing asks for a key in chat.

On macOS with Homebrew:

```
brew install git-lfs ffmpeg uv && git lfs install
uv venv ~/.venvs/video-use && uv pip install --python ~/.venvs/video-use requests librosa matplotlib pillow numpy
```

The Python packages go into their own environment at `~/.venvs/video-use`, outside the plugin
folder, so a plugin update does not wipe them and the system Python stays untouched.

## What is inside

| Skill | What it does | Origin |
|---|---|---|
| `explain-ladder` | picks the level, holds the aliases and the level 1 writing rules, routes to the tools | this repository |
| alias hook | a `UserPromptSubmit` hook that spots an alias in your message and names the level and skill, so triggering does not depend on luck ([evals](evals/README.md)) | this repository |
| `video-studio` | brief and cost, raw cut, motion, voice, quality gate, a lessons file per project | this repository |
| `archify` | validated diagrams as standalone HTML, SVG and PNG | [tt-a1i/archify](https://github.com/tt-a1i/archify), MIT |
| `video-use` | cut real footage by conversation | [browser-use/video-use](https://github.com/browser-use/video-use), MIT |
| `product-launch-motion` | launch film technique on top of HyperFrames | [AbubakrChan/product-launch-motion](https://github.com/AbubakrChan/product-launch-motion), MIT |
| `scroll-craft` | scroll-driven landing pages in the Apple keynote manner: scroll scrubs video, pins sections, animates type, and checks itself in a headless browser | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft), MIT |
| `motion-design` | chunked render and QA technique for long code-only films | [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design), MIT |

Vendored skills keep their own `LICENSE` and notices, and an `UPSTREAM` file with the commit taken
and every local edit. Credits and licence terms: [NOTICE.md](NOTICE.md).

## Costs and privacy

Levels 0 to 3 run locally and need no paid key: markdown, plain English, `archify` diagrams and
HTML pages. Two parts can spend your money and send data to a cloud service:

- **ElevenLabs** (level 4): voiceover and transcription in `video-studio` and `video-use` bill your
  ElevenLabs account by the minute and send the audio to ElevenLabs. `video-studio` states the cost
  before a render and asks before any client or third-party recording leaves the machine. Without
  a key, HyperFrames uses a local placeholder voice.
- **kie.ai** (optional, in `scroll-craft`): generated photoreal images and footage are paid per
  asset and follow kie.ai's terms. Supply your own photos and footage and nothing is bought.

Keys are read from environment variables or a file: `ELEVENLABS_API_KEY` or
`~/.config/elevenlabs/key`, and `KIE_AI_API_KEY` or the `.env` file of your project (keep that file
out of git). Nothing in this repository asks for a key in chat or stores one.

## Licence

MIT for this repository's own files, see [LICENSE](LICENSE). Vendored skills keep their licences.
