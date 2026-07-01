---
name: goal-gate
description: Pair native /goal (run-until-condition) with a DETERMINISTIC Stop-hook script that runs the real verification /goal's transcript-only Haiku checker cannot — exit-2-blocking the stop until the actual command (tests/build/typecheck) passes. Use when you want a loop to keep going until a condition is GENUINELY met (not just claimed in the transcript), when /goal alone would rubber-stamp a hallucinated "tests pass", or when adding a deterministic completion gate to any loop. Trigger phrases: /goal gate, deterministic stop gate, goal not really done, verify before stop, stop hook gate, run until tests actually pass.
---

# /goal Deterministic Gate

`/goal` keeps Claude working until a small **Haiku checker reads the transcript** and decides the
condition holds. Its load-bearing limit (verified, 2.1.170): **the checker runs no tools and reads no
files** — it can only confirm that *text claiming* success appears in the conversation. A maker that
hallucinates "✓ all tests passed", or runs the wrong command, sails straight through.

The fix Anthropic's docs themselves point to: **push the real, deterministic check into a Stop-hook
*script***, and let `/goal` adjudicate only the semantic residue. The script actually runs the command
and **exit-2-blocks the stop** (feeding the failure back as guidance) until it genuinely passes.

## The pattern (two layers)
1. **`/goal <semantic condition>`** — drives continuation and handles the fuzzy part
   (e.g. "the auth refactor is complete and the new endpoints are documented").
2. **A `Stop` hook running `goal-stop-gate.sh`** — the objective backstop: runs your verify command
   (`pytest -q`, `npm test`, `tsc --noEmit`, `cargo build`) and:
   - exit 0 → allow the stop (genuinely done);
   - **exit 2 → block** the stop; stderr (the failing output) becomes Claude's next-turn guidance.

This is the §"force unforgeable evidence" rule from `loop-designer/references/verifier-discipline.md`
made mechanical — the gate reads the real exit code, not the agent's narration of it.

## Install (template: `templates/goal-stop-gate.sh`)
Copy the template, set your verify command, make it executable, and register it as a `Stop` hook in
`.claude/settings.json` (project) — keep it project-scoped so it only gates the loop you mean:
```json
{ "hooks": { "Stop": [ { "hooks": [
  { "type": "command", "command": "CLAUDE_GOAL_VERIFY_CMD='pytest -q' .claude/hooks/goal-stop-gate.sh", "timeout": 120000 }
] } ] } }
```
The script respects `stop_hook_active` (Claude Code's loop-guard) so it blocks **once** per stop
attempt, never infinitely — and fails **open** (allows the stop) if the verify command can't run, so a
broken gate never traps the session.

## When to use which
- **`/goal` alone** — the condition is fully demonstrable in the transcript (the agent pastes the raw
  `pytest` output) and you trust it to. Cheapest.
- **`/goal` + this gate** — the condition must be *machine-true*, not transcript-claimed. Use for
  anything that ships, merges, or runs unattended.
- **`agent`-handler Stop hook** (experimental) — when the check needs a subagent to read files/run
  several commands and reason, not a single deterministic command.

Companions: `loop-designer` (the /goal gotcha + non-rotting gate), `evaluator-optimizer` (semantic
maker≠checker), `long-running-harness` (features.json verify-before-flip), `quality-gates`.
