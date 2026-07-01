---
name: long-running-harness
description: Set up a multi-session autonomous coding loop the way Anthropic prescribes — a two-prompt initializer/coding split, a machine-checkable features.json with verify-before-flip, init.sh + progress-file durable state, and a session-start liveness ritual that survives context resets. Use when building a long-running or multi-session agent that must make incremental progress across many context windows without re-exploring, one-shotting, or prematurely declaring done. Implements "Effective Harnesses for Long-Running Agents". Trigger phrases: long-running agent, multi-session, autonomous build, features.json, initializer agent, session handoff, build across sessions, durable state, init.sh, progress file.
---

# Long-Running Harness (Anthropic's durable-state loop)

Anthropic's empirical finding: **"compaction isn't sufficient … even Opus 4.5 running in a loop
across multiple context windows will fall short if it's only given a high-level prompt."** Durable
on-disk artifacts — not summarization — are what survive. This skill operationalizes their canonical
harness. (Source: anthropic.com/engineering/effective-harnesses-for-long-running-agents; the full
prescription is in `plans/anthropic-loop-harness-playbook.md`.)

## The two failure modes this kills
1. **Over-ambition** — the agent tries to one-shot the app, runs out of context mid-feature, leaves
   it half-done. → fixed by **one feature at a time**.
2. **Premature completion** — a later session "sees that progress had been made, and declares the job
   done." → fixed by the **features.json `passes` ledger** (verify-before-flip).

## The two-prompt split (same system prompt + tools; only the first user prompt differs)

**Initializer (runs ONCE).** Expand the high-level goal into the scaffold, then STOP — do no feature work:
- `features.json` — every feature seeded `passes:false` (the full outline of "done").
- `init.sh` — boots the dev server + runs a basic end-to-end smoke test (saves tokens every session).
- `claude-progress.txt` — the running work log (seed it).
- the initial git commit (the baseline to revert to).

Templates: `templates/init.sh`, `templates/claude-progress.txt`, and the verify-before-flip schema at
`../loop-designer/references/features-json.template.json`.

**Coding agent (every session after).** Runs the session-start ritual below, works ONE feature, leaves
clean state. Identical prompt each session — the *files*, not the context, carry continuity.

## The session-start ritual (put this in the coding-agent prompt / CLAUDE.md / loop.md)
1. `pwd` — confirm the only-editable directory.
2. Read `git log` + `claude-progress.txt` — reconstruct what happened, don't re-explore.
3. **Liveness health-check:** run `./init.sh`, drive the app end-to-end (Playwright/Puppeteer MCP:
   real user action → observe result). **If broken, fix that FIRST** before any new feature.
4. Read `features.json`; pick the single highest-priority `passes:false` feature.
5. Implement **that one feature only**.
6. Verify against its `steps` end-to-end; flip `passes:false→true` **only on success**.
7. Commit with a descriptive message; append a `claude-progress.txt` entry; leave merge-clean state.

## The features.json contract (the anti-premature-completion ledger)
- One object per feature: `{category, description, steps[], verify{command,expected}, passes}`.
- The coding agent may edit **ONLY the `passes` boolean** — never add, remove, or reword entries.
  Header rule (verbatim Anthropic): *"It is unacceptable to remove or edit tests because this could
  lead to missing or buggy functionality."*
- **Flip to `true` ONLY after end-to-end verification**, never when code is merely written.
- **JSON, not Markdown** — "the model is less likely to inappropriately change or overwrite JSON files."
- A "done" claim while any `passes:false` remains is a premature-completion violation (the Ralph-Wiggum
  guard). **Now hook-enforced:** `fabric_stop.py` emits a FEATURES GUARD advisory at every Stop when an
  in-scope `features.json` has `passes:false` items (file-gated → dormant when absent). Also check on
  demand with `~/.claude/bin/check-features-complete` (exit 1 = features still failing), or wire it as
  a hard `Stop` block via `--stop-hook` mode (exit 2) per the script's header.

## Durable state (disk > context)
- **git** = the revert/recover state machine (descriptive commits; revert bad changes to a working state).
- **`claude-progress.txt`** = human-readable session log (see template for the per-session schema).
- **`features.json`** = the machine-checkable completion ledger.
- (SDK/API path) mirror these under the memory tool's `/memories` and treat ASSUME-INTERRUPTION as law:
  anything not written to disk/memory is assumed lost on the next context reset.

## Context economy (keep the loop inside the window)
Smallest high-signal token set; CLAUDE.md < 200 lines (it re-injects after `/compact`; nested ones
don't); push detail into path-scoped `.claude/rules/` loaded on demand. Strip harness components on each
model upgrade — "every component encodes an assumption about what the model can't do; stress-test them."

## Wire it to this setup
- Drive the per-session loop with native `/loop` (bare `/loop` → `~/.claude/loop.md`) or the bespoke
  `bin/autonomous-loop --run` (preemptive budget caps).
- Use `evaluator-optimizer` for the per-feature verify (separate skeptical checker).
- Feed accept/reject into the CAPC ledger (`probe_cost_per_accepted_change`).
- Decision layer: `loop-designer`. Bespoke 2-agent generator: `autonomous-skill` / `nonstop-agent`.
