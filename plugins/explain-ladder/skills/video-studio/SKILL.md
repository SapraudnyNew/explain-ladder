---
name: video-studio
description: "Make a finished video end to end: cut real footage (video-use), build motion and explainer scenes in HyperFrames, voice them with ElevenLabs, check frames and sound, and learn from each round of feedback. Use for explain as a video, make a video, video explainer, animate it, 3b1b style, product promo, or edit these clips."
license: MIT
---

# Video studio

One route from a brief or raw clips to a checked MP4. This skill decides the order and the checks.
The craft lives in the tools it calls, so read their skills when you reach their stage.

## Stage 0. Brief and cost, before any render

1. Write the brief in five lines: audience, the one message, length, format (16:9, 9:16, 1:1), and
   whether real footage exists.
2. Read the project's design tokens: a `DESIGN.md`, a design-system skill or a tokens file. No
   tokens, no guessing: ask for the palette and fonts, or use HyperFrames defaults and say so.
3. Read `.video-studio/lessons.md` in the project if it exists. Every rule there is binding.
4. State the cost: minutes of voice (ElevenLabs), minutes of transcription (ElevenLabs Scribe) and
   render time. Wait for the user's go when money is spent.
5. Privacy gate: client recordings and third-party material go to ElevenLabs only with the user's
   explicit yes for that file. Otherwise skip transcription and work from a script.

## Stage 1. Real footage (only when there are clips)

Use `video-use`. Run its helpers with `~/.venvs/video-use/bin/python` when that file exists
(the README sets it up), otherwise with `python3`. In order: inventory with `ffprobe`, transcribe, cut pauses and retakes (the last
take wins), switch between talking head and screen where the speaker refers to the screen, grade,
subtitles. Keep 0.15 to 0.25 seconds of air between sentences. Never cut inside a word.

## Stage 2. Motion and explainer scenes

Use HyperFrames (`hyperframes` plugin): start at its `hyperframes` skill, which routes to the right
workflow. For a topic explainer with no footage, its `faceless-explainer`; for a website or product
tour, its `product-launch-video`.

- Timing and easing: `gsap-skills`.
- Product launch or UI promo: add the technique from `product-launch-motion` (one shape that never
  cuts, cursor-driven clicks, springs, beat-synced cuts).
- Long renders: the chunked render from `motion-design` when a film runs past 25 seconds.
- Every scene is deterministic: no random numbers, no wall clock; everything is driven from the
  timeline.
- One event every 0.5 to 1.2 seconds keeps attention; never dump paragraphs on screen.

## Voice

ElevenLabs is the voice. The key comes from `ELEVENLABS_API_KEY` or `~/.config/elevenlabs/key`
(mode 600); never ask for it in chat and never print it. Generate the voiceover through HyperFrames'
audio tools (`media-use`), then mix with `hyperframes-audio` (duck the music under the voice). No
key: use the local voice HyperFrames offers and say the voice is a placeholder.

## Stage 3. Quality gate, every time

1. `npx hyperframes check` (or the check its CLI skill names) passes with no layout or contrast
   errors.
2. Sample frames at each transition with `ffmpeg` (one or two per second) and look at them: text
   overflow, overlap, cut-off cards, black frames.
3. `ffprobe` and a loudness read: voice clear, effects under the voice, no clipping.
4. Watch the first and the last three seconds in full.
5. Write the final file path and a five-line change log.

## Stage 4. Lessons, after every round of feedback

When the user corrects timing, cuts, motion or text, append one dated line per lesson to
`.video-studio/lessons.md` in the project (create it if missing): what went wrong, the rule that
prevents it. Never write lessons into this skill's own folder: a plugin update would erase them.

## Anti-patterns

- Rendering before the brief and the cost are agreed.
- Sending client footage to a cloud service without a yes for that file.
- Generic gradients and stock fonts when the project has its own tokens.
- Delivering without Stage 3.
