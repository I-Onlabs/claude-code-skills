# Loop economics — verified reference

## The metric: CAPO / cost-per-accepted-change
The named industry metric is **CAPO = Cost-per-Accepted-Outcome** (InfoWorld FinOps, 2025): the
fully-loaded cost to deliver one *accepted* outcome. **Cost-per-accepted-change is its code instantiation.**
Numerator = **all** spend (accepted + rejected + abandoned + retried); denominator = **accepted only** —
every failure is paid for by the successes.

```
CAPC              = Σ(all loop spend) / max(1, accepted_changes)
accept_rate       = (accepted + 1) / (accepted + rejected + 2)         # Laplace — for reporting
FailureCostShare  = (total_spend − spend_on_accepted) / total_spend
CAPC              = cost_per_run / accept_rate                         # accept rate is a pure multiplier
```
The "<50% accept ⇒ losing" line is a **folk heuristic** — no authoritative source. The real gate is
`CAPC ≥ baseline_value_per_change` (human cost / prior tooling / value of the change). The Kitchen Loop's
~$0.38/merged-PR (arXiv:2603.25697) is **flat-rate subscription ÷ PRs**, not metered token spend — keep it
in a separate, labeled column; don't compare head-to-head with a metered CAPC. Per-task metered sizing
(Morph 2026): bug-fix ≈ $0.54 Sonnet / $0.90 Opus; feature ≈ $2.28 / $3.80.

## Prompt-cache math (the biggest cost lever for loops)
Loops re-send a growing prefix every iteration → cost grows ~quadratically without caching. Anthropic
prompt caching: **write 1.25× (5-min) / 2× (1-hr) base input; read 0.1× (90% off)**. Break-even: 5-min TTL
after 1 hit, 1-hr after 2 hits.
- **5-min TTL is a sliding window** — every cache hit resets the 300 s timer for free.
- **Idle > 300 s between iterations → eviction → the next iteration pays the 1.25× write again.** Repeatedly
  sleeping past 300 s makes every iteration a miss+rewrite (worst case). Keep loop iterations < 300 s apart,
  or set `"ttl":"1h"` when review gates are slower.
- **Stable prefix first, volatile last** (`tools → system → messages`); put `cache_control` on the last
  static block; the per-iteration timestamp/diff goes at the very end. Append history, don't rewrite it
  (rewriting invalidates the prefix). Min cacheable size or it silently no-ops (Opus/Sonnet 1024 tok, Haiku 4096).

## Model routing (cheap maker / GATED strong checker)
Route each step to the cheapest adequate tier: Haiku (~$1/M) classify · Sonnet (~$3/M) standard · Opus
(~$5/M) hard reasoning. Reported 40–86% bill cuts at <2% quality loss; ~60–80% of coding requests are routine.
- A **strong checker run every iteration dominates total cost** (Haiku maker + Opus checker on similar volume ≈
  5× the maker). Cheapest correct design: cheap maker, **gate the strong checker to accept/merge boundaries** or
  to cases where the cheap checker/tests are inconclusive. Anthropic's own multi-agent system = Opus lead +
  Sonnet workers, not strong-everywhere.
- **Multi-agent burns ~15× chat tokens** (Anthropic, 2025-06; token use explains ~80% of variance) — only
  justified for high-value tasks. For a normal coding loop, one strong agent + cheap subagents is the right
  economic point, not a token-hungry fan-out.

## Budget enforcement (monitoring ≠ enforcement)
The canonical failure: a 2-agent loop ran 11 days, produced nothing, billed ~$47K — no hard cap, only
post-hoc monitoring. **Preemptive is the only correct posture:** *project* the next worker's cost and **reject
the dispatch if it would breach** any ceiling, before spending, fail-closed. This setup's `lib/loop_budget.py`
already does exactly this (`project_next()` / `can_dispatch()`). Five independent caps (any one trips → halt):
loop/iteration, tool-call, token, wall-clock, tenant/concurrency. Set them from your ledger: dollar ≈
`target_CAPO × expected_accepted × margin`; iters ≈ `p95(iters_to_accept) × 1.5`; token ≈
`p95(tokens_per_accepted) × margin` + history-summarization so the prefix doesn't grow unbounded.

## Instrumenting CAPC from `logs/loop_history.jsonl`
Each record: `run_id`, `action` (DISPATCHED/BUDGET_HALT), `result_ok`, `budget_after.spent_usd`/`spent_tokens`
(cumulative within a run). Recipe:
1. Reduce per `run_id`: `usd = max(spent_usd over the run)`, same for tokens.
2. Join outcome: `experiments.tsv` keep → `accepted`, discard → `rejected`; halts/timeouts → own buckets
   (still counted in the numerator).
3. Metrics: `CAPC = total_spend / max(1, accepted)`; `accept_rate` (Laplace); `wilson_lower(accepted, n)`
   via `lib/moving_peak.py::wilson_interval`; `FailureCostShare`.
4. **Promote to a hard gate only when** `n ≥ 30 AND wilson_lower ≥ target_accept_rate`. Wilson (not the
   normal/Wald approx) keeps honest coverage at small n; the n≥30 floor guards against promoting on noise.
   Below that, CAPC is **provisional / advisory** — per scientific-calibration discipline.

## Sources
InfoWorld *FinOps for agents* (2025); Kitchen Loop arXiv:2603.25697 (2026-03); Anthropic *multi-agent research
system* (2025-06) + *prompt caching* docs; Huntley *Ralph Wiggum* / LinearB (2025); Requesty / digitalapplied /
Morph routing + cost guides (2026); Wilson (1927) / Brown-Cai-DasGupta (2001) for small-n binomial intervals.
