---
name: loop-designer
description: Design, build, and harden autonomous agent loops with native Claude Code primitives (/loop, /goal, Routines, hooks, subagents, worktrees). Use when the user wants to automate a recurring task, set up a loop/cron/routine/schedule, build a self-running or unattended agent, add a verifier/gate, instrument loop cost, or decide whether a task is even worth looping. Covers the 4-condition test, the maker/checker split, the Ralph-Wiggum premature-completion guard, cost-per-accepted-change (CAPO), the security tax for unattended loops, and how to route between native primitives and this setup's bespoke harness (bin/autonomous-loop, next-work, work-packets, claudelab). Trigger phrases: loop engineering, design a loop, loop designer, /loop, /goal, routine, schedule agent, automate this, unattended agent, self-running.
---

# Loop Designer

The leverage point moved from *typing prompts* to *designing the system that prompts*.
This skill is the decision + design layer for building that system on Claude Code **2.1.170**.
It is not a harness generator (for that, see `autonomous-skill` / `nonstop-agent`) — it tells
you **whether to loop, which primitive to reach for, how to gate it so it converges instead of
spending, and how to not get owned while it runs unattended.**

Everything here is verified against the 2.1.170 docs (2026-06-30). The deep tables live in
`references/` and load on demand:
- `references/native-primitives.md` — exact syntax for `/loop`, `/goal`, Routines, the full hook surface, subagents, worktrees.
- `references/verifier-discipline.md` — how to build a gate that doesn't rot (the hard part).
- `references/economics.md` — CAPO / cost-per-accepted-change, prompt-cache math, model routing, budget caps.
- `references/security-tax.md` — the lethal trifecta + the hardening checklist for unattended loops.
- `references/features-json.template.json` — the verify-before-flip state schema.

---

## Step 0 — Should this even be a loop? (run before building anything)

A loop earns its cost only when **all four** hold. Miss one → keep it a manual prompt; a good
single prompt is faster and cheaper.

1. **It repeats** (≈weekly or higher volume). One-offs never amortize the setup.
2. **Bad output can be rejected automatically** — a test, type-check, build, lint, or a hard
   rule that can fail the work *without you in the room*. No mechanical gate ⇒ the agent grades
   its own homework, and the maker is a generous grader (see the gate section).
3. **The agent can run the code end-to-end** — it has the senior-engineer tools (logs, a repro
   environment, the ability to execute what it writes and see what breaks). Otherwise it iterates blind.
4. **"Done" is objective.** If quality is a judgment call, a human still wins.

Then the 30-second tactical check before turning a *specific* task into a loop:
- [ ] Happens ≥ weekly. - [ ] A test/typecheck/build/lint can reject bad output.
- [ ] The agent can run what it changes. - [ ] There is a **hard stop** (token / iteration / time cap).
- [ ] A human reviews before merge / deploy / dependency or auth/payments changes.

**Good first loops:** CI-failure triage → draft fix PRs; dependency-bump PRs; lint-and-fix on PR-open;
flaky-test reproduction; issue→PR drafts on a strongly-tested codebase.
**Bad first loops (keep a human in the chair):** architecture rewrites, auth/payments, production
deploys, vague product work, anything where "done" is a judgment call.

---

## Step 1 — The build order (never skip ahead)

> Get **one manual run** reliable → turn it into a **skill** → wrap the skill in a **loop**
> (add the gate + stop condition) → **then** schedule it.

Scheduling something you haven't made reliable by hand is how loops blow up while you sleep.

---

## Step 2 — Pick the primitive (native first, bespoke when you need the ladder)

Five building blocks, mapped to **verified** 2.1.170 primitives. Full syntax in
`references/native-primitives.md`; the load-bearing gotchas are inline here.

| Block | Native primitive | The gotcha that bites |
|---|---|---|
| **Heartbeat** | `/loop [interval] [prompt]`; bare `/loop` runs `~/.claude/loop.md` | Self-pacing picks 1 min–1 hr; **7-day expiry** on recurring; `Esc` clears; `CLAUDE_CODE_DISABLE_CRON=1` kills all. Keep iterations **< 300 s apart** or you lose the prompt cache (see economics). |
| **Run-until-true** | `/goal <condition>` | The checker is a **separate Haiku model that reads the TRANSCRIPT ONLY — no tool calls, no file reads.** It can confirm text *claiming* tests passed, not that they did. → Make the agent **paste the raw `npm test` exit/output into the conversation**, or push the real check into a Stop-hook *script*. ≤4000 chars; add `… or stop after N turns`. |
| **Laptop-closed schedule** | Routines / `/schedule` | **Research preview.** 1-hr min interval; needs claude.ai login (not API key); pushes only to `claude/*` branches by default; **a green run status means it *ran*, not that the task *succeeded*** — open the transcript. |
| **Parallel without collision** | `claude --worktree`, subagent `isolation: worktree` | Each parallel agent gets its own checkout; auto-removed if it made no changes. Your review bandwidth, not the tool, is the ceiling on parallel agents. |
| **Project knowledge** | Skills (`SKILL.md`, progressive disclosure) | Body loads only on invoke — long reference material is ~free until needed. Without a skill the loop re-derives context every iteration. |
| **Maker ≠ checker** | Subagents (`.claude/agents/*.md`), `Agent` tool, `/goal`'s fresh Haiku | The model that wrote the code is too nice grading it. Use a **different model + independent context** for the checker. See the gate section. |
| **Acts, not suggests** | MCP connectors | Per-routine scoping is a security control, not a nicety (see security tax). |

**Lifecycle levers you're probably not using** (full list in references): `PreCompact` hook
(snapshot state before compaction → goal-drift insurance), `TeammateIdle` (keeps an agent-team
teammate working — harness-level continuation), `prompt` handler type (model yes/no eval — what
`/goal` is built on).

**Native vs this setup's bespoke harness** — reach for native for simple cadence/condition loops;
reach for the bespoke ladder when you need budget-enforced multi-session work. See the routing map below.

---

## Step 3 — Build the gate (this is the whole game)

A loop with a weak verifier doesn't converge toward *correct* — it converges toward *whatever the
verifier rewards*. Reward-hacking is **structural**, not a quirk (SpecBench: a Codex run built a
2,900-line lookup table to pass visible tests, 0% held-out; Cursor: 14–21 pts of SWE-bench "score"
was pure answer-leakage). The non-rotting-gate checklist (full detail + citations in
`references/verifier-discipline.md`):

1. **Objective first.** Express every criterion you can as a deterministic check (test exit code,
   typecheck, lint, diff allow-list, schema). Reserve a model judge for the *semantic residue only*.
2. **Separate maker from checker.** Never let the generating model+context grade its own output.
   Different model family, independent context. (`/goal`'s fresh Haiku does this structurally.)
3. **Force unforgeable evidence into the transcript.** For any transcript-judged gate (incl. `/goal`,
   LLM-as-judge over logs), require the *raw artifact* — exit code, full output, file count — not the
   agent's summary of it. Push deterministic checks into a Stop-hook *script*, not a prompt judge.
4. **Grade the grader.** Periodically inject the exact bug you fear and confirm the gate goes **red**.
   A test that stays green under the injected fault is decoration, not a gate.
5. **Hold out a test the agent never sees.** A large validation-vs-held-out gap *is* your
   reward-hacking signal.
6. **Prefer invariants over examples** (property / metamorphic / differential) where the agent could
   memorize fixed cases — fuzzed invariants can't be hardcoded or looked up.
7. **Seal the environment.** Strip `.git` history and allowlist network for eval loops — kill the
   answer-retrieval channel.
8. **Gate intermediate milestones on long tasks** — reliability decays with horizon; a single
   end-of-run gate on a multi-hour task is near-useless.
9. **Never equate "ran" with "succeeded."** Process-completed ≠ goal-achieved.

---

## Step 4 — Hard stops + the Ralph-Wiggum guard

Loops fail **two** ways. This setup's continuation protocol already guards the first
(premature *stopping*). This skill adds the second.

- **Premature completion ("Ralph Wiggum").** The agent emits a completion signal on half-done work
  and the loop exits — or runs forever billing in silence. The guard: completion must be backed by an
  **objective signal**, not transcript narration. Use the `features.json` verify-before-flip pattern
  (`references/features-json.template.json`): a feature flips `passes:false → true` **only after
  end-to-end verification**, edits touch *only* the `passes` field, and you work **one feature at a
  time**. *This is now hook-enforced: `fabric_stop.py` emits a FEATURES GUARD advisory at Stop when an
  in-scope `features.json` still has `passes:false` items (file-gated → dormant when absent); the
  standalone `bin/check-features-complete` does the same check on demand.*
- **Runaway spend.** Every serious loop has two exits: success, and a hard cap. Use the bespoke
  driver's preemptive caps — `CLAUDE_LOOP_MAX_USD`, `_MAX_TOKENS`, `_MAX_ITERS` (in `lib/loop_config.py`;
  `loop_budget.py` *projects* the next worker's cost and rejects the dispatch **before** spending,
  fail-closed). Set caps from your own ledger: dollar ≈ `target_CAPO × expected_accepted × margin`;
  iters ≈ `p95(iters_to_accept) × 1.5`. Plus the operator kill-switch: `touch AGENT_STOP` in the
  project root halts the loop (`hooks/kill_switch.py`); `rm AGENT_STOP` resumes.

---

## Step 5 — The metric: cost per accepted change (CAPO)

The number that matters is **not** tokens spent or loops scheduled. It is **cost per *accepted*
change** — the code instantiation of CAPO (Cost-per-Accepted-Outcome). Discipline: divide **all**
loop spend (accepted + rejected + retried) by **accepted changes only**, so every failure is paid
for by the successes.

```
CAPC = Σ(all loop spend) / max(1, accepted_changes)
accept_rate = (accepted + 1) / (accepted + rejected + 2)        # Laplace, for reporting
FailureCostShare = (total_spend − spend_on_accepted) / total_spend
```

Below a healthy accept rate you're doing the review work the loop was meant to remove — but the
real break-even is `CAPC ≥ baseline_value_per_change`, **not** a folk "50%" line. This setup
instruments CAPC from `logs/loop_history.jsonl ⋈ experiments.tsv`
(`probe_cost_per_accepted_change` in the claudelab harness; `/lab probes`). **Promote CAPC to a hard
budget gate only at n ≥ 30 and Wilson-lower-bound ≥ target** — until then it is advisory. Full
recipe + prompt-cache and model-routing levers in `references/economics.md`.

---

## Step 6 — The security tax (an unattended loop is an unattended attack surface)

Before any loop runs **unattended**, close the supply-chain + exfil surface. An agent with private
data + exposure to untrusted content + an outward channel is the *lethal trifecta* — one injected
instruction reads your secrets and ships them out. Checklist (full, ranked, in
`references/security-tax.md`; this machine's live audit is in
`plans/glistening-plotting-reddy.md` Phase 0):

- **No secret reachable by a printing skill.** Debug-logging-into-context is the #1 credential-leak
  vector — stdout flows into the model's window. Keep keys out of readable config; `suppressOutput`
  on non-interactive hooks; scrub logs the loop writes.
- **Deny-side rules.** Deny overrides allow — add `permissions.deny` for secret-file reads and exfil
  binaries even while keeping broad allows.
- **Scope connectors per routine.** An overnight code loop does not need Slack/Zapier/webhook
  connectors or github *write* live. Treat third-party skills/plugins as untrusted code (audit
  description **and** scripts — injection hides in either).
- **Branch + permission blast-radius.** Restrict unattended writes to `claude/*`; never
  `--dangerously-skip-permissions` in a routine or teammate-inherited context; prefer a network
  allowlist (Trusted, not Full) — it defeats exfil even when a shell deny is bypassed.

---

## The routing map — native vs. what this setup already has

The point of *enhancing what we have*: don't reinvent. Reach for —

| You need… | Use |
|---|---|
| Recurring cadence in-session | native `/loop` (bare → `~/.claude/loop.md` maintenance cycle) |
| Run until a transcript-checkable condition | native `/goal` (surface raw evidence!) |
| Laptop-closed / event-triggered | Routines `/schedule` (after security Phase 0) |
| Budget-enforced multi-session autonomous work | `bin/autonomous-loop --run` (preemptive caps; `--supervised` first) |
| "What should I do next?" | `bin/next-work` (6-rung ladder) |
| Generate a fresh 2-agent harness for a project | `autonomous-skill` / `nonstop-agent` skills |
| Pick the work unit / file a valid stop | `bin/work-packets` (`--claim-stop`) |
| Safe self-modification (snapshot/verify/revert) | `bin/claude-iterate` |
| Evidence-before-assertions verification | `quality-gates` skill |
| Stop-condition gating (5 layers) | `hooks/fabric_stop.py` |
| Operator halt | `touch AGENT_STOP` (`hooks/kill_switch.py`) |
| Continuation discipline (don't stop early) | `rules/autonomous-continuation.md` |

Native = simplest cadence/condition loops. Bespoke ladder = budget-enforced, multi-rung, stop-validated
autonomous work. This skill is the layer that decides which, and gates it so it converges.

---

## The loop-harness suite (Anthropic-grade, installed in this setup)

Built from Anthropic's own corpus (`plans/anthropic-loop-harness-playbook.md`). Reach for:

| Need | Capability |
|---|---|
| A separate skeptical checker grades the maker each round | `evaluator-optimizer` skill + `lib/eval_optimizer.py` |
| Multi-session build with verify-before-flip + session-start ritual | `long-running-harness` skill (+ init.sh/progress/features templates) |
| Don't declare done while features still fail | `bin/check-features-complete` (the Ralph-Wiggum guard; opt-in Stop hook) |
| Measure if the output is good (pass^k, per-dim judge, kappa) | `agent-eval` skill + `lib/agent_eval.py` |
| Run `/goal` until the condition is *machine*-true | `goal-gate` skill + `goal-stop-gate.sh` |
| Cost-per-accepted-change | `probe_cost_per_accepted_change` (`/lab probes`) |
| Cheap-maker model routing in the bespoke loop | `CLAUDE_LOOP_MODEL_ROUTING=on` (`lib/loop_model_routing.py`) |
| Secret-leak scan over logs/transcripts | `bin/scan-secret-leaks` |

## The ten mistakes that turn loops into money pits

1. Building a loop without the 4-condition test. 2. No objective gate (a second optimist isn't a gate).
3. One agent both writing and grading. 4. No state file (tomorrow restarts from zero). 5. Vague stop
condition. 6. No token/iteration/$ cap. 7. Heavy verification on a metered plan. 8. Auto-installing
unaudited community skills. 9. Looping judgment-call work (architecture/auth/payments). 10. Not reading
the diffs — comprehension debt compounds; the day you debug a system no one read costs more than the tokens.
