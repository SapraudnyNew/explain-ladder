#!/usr/bin/env python3
"""UserPromptSubmit hook for the explain-ladder plugin.

Reads the prompt from stdin (JSON), looks for a level alias or "level N", and adds one line of
context naming the level and the skill to load. Prints nothing when no alias matches, so ordinary
prompts are untouched. Standard library only; never fails the prompt.
"""
import json
import re
import sys

LEVELS = [
    (4, "explainer video", "video-studio",
     ["explain as a video", "make a video", "video explainer", "animate it", "3b1b style"]),
    (3, "interactive HTML page", "explain-ladder (then answer-me-with-html or a page)",
     ["explain in html", "make a page", "html it", "interactive page", "build a page"]),
    (2, "diagram", "explain-ladder (then archify)",
     ["draw a diagram", "diagram it", "show the flow", "map it", "sketch it"]),
    (1, "plain English, about 80% ASD-STE100", "explain-ladder",
     ["plain english", "simple words", "no jargon", "ste mode", "explain simply"]),
    (0, "markdown note", "explain-ladder",
     ["write it up", "as markdown", "make a note", "doc it", "in md"]),
]


def find(prompt):
    text = " " + re.sub(r"\s+", " ", prompt.lower()) + " "
    m = re.search(r"\blevel\s*([0-4])\b", text)
    if m:
        n = int(m.group(1))
        return next(l for l in LEVELS if l[0] == n), f"level {n}"
    for level in LEVELS:  # highest level first, so "make a video" wins over "make a note"
        for alias in level[3]:
            if re.search(r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])", text):
                return level, alias
    return None, None


def main():
    try:
        prompt = json.load(sys.stdin).get("prompt", "")
    except Exception:
        return 0
    level, alias = find(prompt)
    if not level:
        return 0
    n, what, skill, _ = level
    note = (f'Explain ladder: the user said "{alias}", so answer at level {n} ({what}). '
            f"Load the {skill} skill before answering.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": note}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
