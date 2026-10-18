# Trigger evaluation

Question: does each alias load the right skill? 14 prompts in `trigger-prompts.tsv`: two aliases
per level, two open "explain" requests with no alias, two controls that must load nothing.

Method: Claude Code 2.1.302 in a clean config with only this plugin installed, headless
(`claude -p ... --max-turns 2 --allowedTools Skill --output-format stream-json`). A prompt passes
when a Skill call names the expected skill (level 2 also accepts `archify`; level 4 accepts
`video-studio`). Controls pass when no skill loads.

| Run (2026-10-18) | Setup | Aliases (10) | Open requests (2) | Controls (2) |
|---|---|---|---|---|
| 1 | description lists 5 aliases | 6 | 1 | 2 |
| 2 | description lists all level 0 to 3 aliases | 6 | 0 | 2 |
| 3 | plus the `UserPromptSubmit` alias hook | 10 | 0 | 2 |
| 4 | same as run 3, repeated | 10 | 0 | 2 |

Reading: description tuning alone left triggering at chance (runs 1 and 2 failed on different
prompts). The hook makes alias triggering deterministic. An open "explain" with no alias is left to
the model and the ladder rule; that is by design, not a defect.

Re-run: `bash evals/run.sh` after installing the plugin in a clean config dir.
