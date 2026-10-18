---
name: explain-ladder
description: "Choose the form of an answer and produce it. Use on: write it up, as markdown, make a note, doc it, in md; plain english, simple words, no jargon, ste mode, explain simply; draw a diagram, diagram it, show the flow, map it, sketch it; explain in html, make a page, html it, interactive page, build a page; or explain/show this when the form is open."
license: MIT
---

# Explain ladder

One ladder of five levels for every answer a person has to understand. The idea comes from Andrej
Karpathy's thread of 2 October 2026 on making model output easy to absorb: controlled English,
diagrams, HTML pages, explainer videos. Level 0, markdown, is the base under all of them.

## The rule

Use the lowest level that answers the question fully. Go one level higher only when it cuts the
reader's effort: a process with more than three steps wants a diagram; a comparison the reader will
click through wants a page; a concept that moves in time wants a video. An alias from the user
always wins over this rule.

## Levels, aliases and tools

| Level | The reader gets | Aliases (any one triggers it) | Tool |
|---|---|---|---|
| 0 | a markdown note or file | `write it up`, `as markdown`, `make a note`, `doc it`, `in md` | write markdown; a file when it will be kept |
| 1 | plain English, about 80% ASD-STE100 | `plain english`, `simple words`, `no jargon`, `ste mode`, `explain simply` | the rules below |
| 2 | a diagram | `draw a diagram`, `diagram it`, `show the flow`, `map it`, `sketch it` | `archify`; a text diagram inline when no tool can run |
| 3 | an interactive HTML page | `explain in html`, `make a page`, `html it`, `interactive page`, `build a page` | `answer-me-with-html` for an answer page; `scroll-craft` for a scroll-driven page in the Apple keynote manner, or a companion page to a video |
| 4 | an explainer video | `explain as a video`, `make a video`, `video explainer`, `animate it`, `3b1b style` | `video-studio` |

Aliases work in any language the user writes in; match the meaning, not only the exact words. A
number works too: "level 2" means a diagram.

## Level 1 rules (plain English)

- One idea or one action per sentence. Instructions up to 20 words, descriptions up to 25.
- Active voice; the reader can see who does what.
- One word for one thing. Define a term in plain words the first time, then keep it.
- The answer first, the detail after. Numbered steps for a sequence.
- Do not drop words to look short. Clear beats compact.

## Levels 2 to 4

- **Diagram.** Hand the content to `archify` with the diagram type (architecture, workflow,
  sequence, dataflow, lifecycle). Check the result opens and the arrows connect. Above three steps
  or parts, a diagram is the default, not an extra.
- **Page.** One self-contained HTML file, no outside requests unless the page needs them. Conclusion
  at the top. When the page should feel like a product launch, or travel with a video, use
  `scroll-craft`; it plans the journey and screenshots its own result.
- **Video.** Load `video-studio`. A video costs real money and minutes; say the length and the
  voice cost before rendering, and use only verified material.

## Checks before sending

- The level matches the alias, or the rule above when no alias was given.
- Level 1 text passes the sentence-length rules.
- A diagram or page was opened and looked at once before it is handed over.
- No secret, no private name and no client material leaves the machine in a page or a video
  without the user's yes.

## What this skill does not do

It does not write the content; it chooses the form and calls the tool. It does not restyle a
brand: each tool reads the project's own design tokens.
