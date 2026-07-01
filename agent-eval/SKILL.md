---
name: agent-eval
description: Evaluate whether an agent's or loop's OUTPUT is actually good, the way Anthropic prescribes — grade final-state not trajectory, per-dimension isolated LLM-as-judge with an "Unknown" escape, pass^k reliability (not just pass@k), Cohen's-kappa judge calibration, and trajectory metrics kept as diagnostics. Use when measuring an agent/loop, building an eval suite or eval-as-CI gate, judging generated output quality, deciding if a prompt change helped, or calibrating an LLM judge. Backed by lib/agent_eval.py. Trigger phrases: eval, evaluate agent, llm as judge, pass^k, pass at k, grade output, eval harness, judge calibration, measure the loop, eval as CI.
---

# Agent-Output Evaluation

"Build evals before you trust the loop." This skill packages Anthropic's eval discipline
(*Demystifying evals for AI agents*; *multi-agent research system*) over the tested primitives in
`lib/agent_eval.py`. The full prescription is in `plans/anthropic-loop-harness-playbook.md` §Evaluation.

## The seven rules (each maps to a lib function or a practice)

1. **Grade the outcome / final state, not the trajectory.** "Agents find alternative paths to the
   same goal." Your `grade_fn` checks the end state (reservation exists, tests pass, file count) — not
   the tool-call sequence. `run_eval_suite` keeps turns/tool-calls/tokens/cost in `diagnostics`,
   separate from pass/fail.
2. **Per-dimension isolated judge.** Grade each rubric dimension with its own judge call, then
   `aggregate_dimensions(verdicts)` → one outcome (any FAIL → FAIL; all PASS → PASS).
3. **Give the judge an "Unknown" escape.** Instruct the judge to return `UNKNOWN` when it lacks
   info, instead of hallucinating a verdict. `aggregate_dimensions` never lets UNKNOWN pass silently —
   it surfaces `needs_human: true` (or use `unknown_is_fail=True` for a strict gate).
4. **Report pass^k, not just pass@k.** `pass_at_k(n,c,k)` = ≥1 of k succeeds (flatters);
   `pass_hat_k(n,c,k)` = ALL k succeed (the real reliability). They tell opposite stories at high k —
   gate production on `pass_hat_k`.
5. **Calibrate the judge against humans.** `cohen_kappa(judge_labels, human_labels)` ≥ **0.6** before
   you trust an LLM judge; re-check when you change the rubric or the judge model.
6. **Start with 20–50 realistic tasks**, run **multiple trials** each (non-determinism), and use
   **balanced two-sided** sets (cases where the behavior should AND shouldn't occur).
7. **Evals as CI + read the transcripts.** Run on every commit; keep regression evals ~100%, rotate
   saturated capability evals in. Layer Swiss-Cheese (automated → monitoring → A/B → human). Actually
   read failing transcripts — tooling for that is non-optional.

## Wire real judges to the lib

```python
import agent_eval as ae

DIMENSIONS = ["correctness", "completeness", "no-regression"]   # rubric, one judge each

def grade_fn(task, run_result):
    # outcome grade: per-dimension isolated judges, each a SEPARATE Agent/claude -p call with a
    # rubric + the produced artifact, instructed to answer PASS / FAIL / UNKNOWN only.
    verdicts = [judge_one_dimension(dim, task, run_result) for dim in DIMENSIONS]  # your LLM calls
    return ae.aggregate_dimensions(verdicts)        # -> {status, needs_human, ...}

def run_fn(task):
    # the agent/loop under test; return the final artifact + trajectory diagnostics
    return {"result": ..., "turns": ..., "tokens": ..., "cost_usd": ...}

suite = ae.run_eval_suite(TASKS, run_fn, grade_fn, trials=5, k=5)
# gate on suite["mean_pass_hat_k"]; inspect suite["diagnostics"] for cost/turn trends
```

Judge construction: use a **different model** than the maker (Opus/Fable judging Haiku/Sonnet output),
a **fresh context**, a **skeptical** rubric ("find why it fails; answer UNKNOWN if unsure"). For
quick in-loop accept/reject use the `evaluator-optimizer` skill; for suite-level reliability use this.

## Wire to this setup
- Run as a claudelab probe (mirror `probe_skill_realworld_hit`'s -1 sentinel until n≥sample) or as a
  pre-merge CI gate. Feed the suite's accept-rate into the CAPC ledger
  (`probe_cost_per_accepted_change`) so eval pass-rate and cost-per-accepted-change move together.
- Companions: `evaluator-optimizer` (the in-loop checker), `quality-gates` (evidence discipline),
  `loop-designer` (the non-rotting-gate checklist this operationalizes).
