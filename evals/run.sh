#!/usr/bin/env bash
# Trigger evaluation. Needs Claude Code logged in and this plugin installed in CLAUDE_CONFIG_DIR.
set -u; cd "$(dirname "$0")"; out=results; mkdir -p $out
while IFS=$'\t' read -r id lvl prompt; do
  claude -p "$prompt" --max-turns 2 --allowedTools Skill --output-format stream-json --verbose > "$out/$id.jsonl" 2>/dev/null
  skills=$(grep -o '"name":"Skill","input":{"skill":"[^"]*"' "$out/$id.jsonl" | sed 's/.*"skill":"//;s/"$//' | tr '\n' ' ')
  echo "$id [$lvl] ${skills:-none}"
done < trigger-prompts.tsv
