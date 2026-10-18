#!/usr/bin/env bash
# Run one command with the video environment: the ElevenLabs key from ~/.config/elevenlabs/key
# (when ELEVENLABS_API_KEY is not already set) and the video-use Python environment first on PATH.
# Prints nothing about the key. Usage: bash with-env.sh <command> [args...]
set -eu
if [ -z "${ELEVENLABS_API_KEY:-}" ] && [ -s "$HOME/.config/elevenlabs/key" ]; then
  ELEVENLABS_API_KEY="$(tr -d '[:space:]' < "$HOME/.config/elevenlabs/key")"
  export ELEVENLABS_API_KEY
fi
if [ -x "$HOME/.venvs/video-use/bin/python" ]; then
  export PATH="$HOME/.venvs/video-use/bin:$PATH"
fi
exec "$@"
