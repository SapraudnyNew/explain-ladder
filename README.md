# explain-ladder

A Claude Code plugin marketplace for one job: presenting an answer so a person can absorb it.
Five levels, one rule, five aliases per level.

The idea comes from Andrej Karpathy's thread of 2 October 2026 on making model output easier to
understand: controlled English, diagrams, HTML pages, explainer videos. This repository adds
markdown as level 0, the aliases, and the tools that produce each level. It is not affiliated with
or endorsed by him.

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

Needs: Node.js 22 or newer (Archify, HyperFrames), `ffmpeg` and `ffprobe`, Python 3.10 or newer
for `video-use` (run `pip install -e .` once inside its skill folder), and an ElevenLabs key for
voice and transcription, read from `ELEVENLABS_API_KEY` or `~/.config/elevenlabs/key` (mode 600).
Nothing asks for a key in chat.

## What is inside

| Skill | What it does | Origin |
|---|---|---|
| `explain-ladder` | picks the level, holds the aliases and the level 1 writing rules, routes to the tools | this repository |
| alias hook | a `UserPromptSubmit` hook that spots an alias in your message and names the level and skill, so triggering does not depend on luck ([evals](evals/README.md)) | this repository |
| `video-studio` | brief and cost, raw cut, motion, voice, quality gate, a lessons file per project | this repository |
| `archify` | validated diagrams as standalone HTML, SVG and PNG | [tt-a1i/archify](https://github.com/tt-a1i/archify), MIT |
| `video-use` | cut real footage by conversation | [browser-use/video-use](https://github.com/browser-use/video-use), MIT |
| `product-launch-motion` | launch film technique on top of HyperFrames | [AbubakrChan/product-launch-motion](https://github.com/AbubakrChan/product-launch-motion), MIT |
| `motion-design` | chunked render and QA technique for long code-only films | [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design), MIT |

Vendored skills keep their own `LICENSE` and notices, and an `UPSTREAM` file with the commit taken
and every local edit. Credits and licence terms: [NOTICE.md](NOTICE.md).

## Privacy

`video-use` and the ElevenLabs voice send audio to ElevenLabs. `video-studio` asks before any
client or third-party recording leaves the machine.

## Licence

MIT for this repository's own files, see [LICENSE](LICENSE). Vendored skills keep their licences.
