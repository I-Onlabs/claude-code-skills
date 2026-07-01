---
name: evaluator-optimizer
description: Run a maker≠checker evaluator-optimizer loop — a separate, skeptical, calibrated evaluator grades the maker's output each round and the loop repeats with feedback until a sprint-contract of hard-threshold criteria passes or an iteration cap is hit. Use when generating code/content/designs that need iterative refinement against clear criteria, when you want a second agent to catch what the maker talked itself into, or when building any verification loop. This is Anthropic's #1 stated harness lever (separating the doer from the judge). Trigger phrases: evaluator optimizer, maker checker, second-agent review, iterate until it passes, grade my output, refine with feedback, self-improving loop.
---

# Evaluator-Optimizer Loop

Anthropic's single strongest stated harness lever: **"agents tend to respond by confidently praising
the work they've produced — even when, to a human observer, the quality is obviously mediocre.
Separating the agent doing the work from the agent judging it proves to be a strong lever."** This
skill packages that loop, backed by the tested control logic in `lib/eval_optimizer.py`.

## When to use it (Anthropic's two signs of fit)
1. The output **demonstrably improves when a human articulates feedback**, AND
2. **an LLM can produce that feedback** against clear criteria.
If quality is already fine first-try, or "good" is purely subjective, skip it — the loop just burns
tokens. (Building Effective Agents, 2024.)

## The shape (4 moves)

1. **Agree a sprint-contract BEFORE work.** A list of hard-threshold, testable "done" criteria
   (Anthropic's 2026 harness used 27+). e.g. `["pytest -q exits 0", "no source file > 200 lines",
   "the /login route returns 200 for valid creds"]`. This is what the checker grades against.
2. **Maker generates** against the task + contract (round 1) or task + contract + accumulated prior
   feedback (later rounds).
3. **A SEPARATE checker evaluates** → returns `{status: PASS|NEEDS_IMPROVEMENT|FAIL, feedback}`.
   The checker must be a different agent (different model AND independent context) — never the maker.
4. **Loop** on the feedback until `PASS` or the iteration cap. Always cap (the cookbook loop omits
   the cap and spins forever — `lib/eval_optimizer.py` enforces one).

## Make the checker trustworthy (Anthropic eval discipline)
- **Different model family + fresh context.** Maker on Haiku 4.5 / Sonnet 5 (cheap); checker on
  Opus 4.8 / Fable 5 (strong). The checker must not inherit the maker's reasoning.
- **Skeptical framing** — its job is to *find why the work fails*, default to NEEDS_IMPROVEMENT when
  unsure; give it an explicit **"Unknown / not enough info"** escape so it can't hallucinate a PASS.
- **Few-shot-calibrate** it with 2–3 scored examples → aligns judgment, reduces drift across rounds.
- **Drive the real artifact** where possible (run the tests, hit the route via Playwright/Puppeteer
  MCP) — grade the running system, not a description of it. Grade **outcome/final-state, not the
  path** the maker took.
- **Weight the dimensions the model is weak at** (design, originality) higher than the ones it
  already nails (craft, functionality).

## Wire real agents to the lib

`lib/eval_optimizer.py::run_eval_optimizer(task, generate_fn, evaluate_fn, *, contract, max_iters,
maker_id, checker_id)` is injectable control logic (mirrors `autonomous_loop`'s `dispatch_fn`). It
enforces the two non-negotiables: **maker ≠ checker** (raises if same callable/id) and a **hard cap**.

Three ways to supply the two functions:
- **In-session subagents (Agent tool):** `generate_fn` calls `Agent(general-purpose, model=haiku, …)`
  to produce the artifact; `evaluate_fn` calls `Agent(code-reviewer, model=opus, …)` with a rubric +
  the contract, parsing its `{status, feedback}`. Pass `maker_id="haiku"`, `checker_id="opus"`.
- **Headless workers:** each fn shells `claude -p --model <m> --output-format json` (the bespoke
  `autonomous_loop` dispatch pattern), maker cheap / checker strong.
- **Agent SDK:** each fn is a `query()` call with its own `allowed_tools`/`model`; the checker gets
  read+exec tools to actually verify, the maker gets write tools.

**Runnable example:** `examples/eo_with_claude.py` — a working Haiku-maker / Opus-checker loop via
`claude -p` (`python3 examples/eo_with_claude.py "<task>"`). Its verdict parser is unit-tested in
`tests/test_eo_parse_verdict.py`, so the brittle read-the-checker's-reply step is pinned without spending tokens.

The return `{status, result, iters, passed, trajectory, reason}` — **read `trajectory`** (every
round's output + the checker's verdict) per Anthropic's "read the transcripts" discipline.

## Guardrails
- Cap iterations (default 5; harness post used 5–15/feature). Each round costs maker+checker tokens
  — the strong checker dominates cost, so cap it and gate multi-round on task value (see
  `loop-designer/references/economics.md`).
- The checker grading its own maker's work is the failure mode this whole pattern exists to prevent —
  `run_eval_optimizer` refuses to start if maker and checker aren't distinct.
- Feed the loop's accept/reject outcome into the CAPC ledger (`probe_cost_per_accepted_change`) so the
  cost-per-accepted-change of the loop is measured.

Companion: `loop-designer` (when/whether to loop at all), `quality-gates` (evidence-before-assertions),
`plans/anthropic-loop-harness-playbook.md` (the full Anthropic prescription this implements).
