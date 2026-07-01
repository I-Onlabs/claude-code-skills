# Building a gate that doesn't rot — verified reference

The gate is the single most leverage-dense part of a loop. A weak verifier doesn't converge toward
correct — it converges toward whatever it rewards. Reward-hacking is **structural** (it scales with
code size), not a quirk of a weak agent. Sources dated/linked at the bottom.

## Objective gate vs LLM-as-judge
- **Default to objective gates** (test exit code, typecheck, build, lint, schema, diff allow-list):
  cheap, fast, reproducible, non-gameable-by-rhetoric. Limit = coverage (only catches encoded failures).
- **Model judge only for the semantic residue** ("does this refactor preserve intent", "is this message
  helpful") — criteria with no cheap oracle. Anthropic's **evaluator-optimizer**: one LLM generates, a
  *separate* LLM evaluates in a loop; use it "when we have clear evaluation criteria, and when iterative
  refinement provides measurable value." The separation is the point.
- **Self-preference bias is real:** models rate their own output higher than a neutral grader would, and
  self-recognition correlates with bias size. Never let the maker (model+context) grade its own work.

## Calibrating a judge when you must use one
- **Different model family + independent context** for the judge (a GPT judge over Claude output / vice
  versa). The judge must not inherit the maker's reasoning/rationalizations. (`/goal`'s fresh Haiku does this.)
- **Position bias** (~10–15 pts toward slot A) is in the decode, not the instruction — you cannot prompt it
  away. Randomize order, or run both orderings and demote order-flipping verdicts to ties.
- **Verbosity bias**: longer answers score higher at matched quality → penalize length in the rubric; audit
  length↔score correlation.
- Prefer **pointwise scoring inside a loop** (grade against a fixed rubric) over pairwise (where position
  bias lives). Use an **N-juror majority vote** for subjective calls — per-model biases partially cancel.
- **Adversarial framing**: prompt the judge as a skeptic whose job is to *find why the work fails*, default
  to refuted-if-uncertain. Counteracts the agreeableness prior.
- **Calibrate vs humans**: 200–500-sample gold-set/rubric, Cohen's kappa ≥ 0.6 to ship, re-check monthly.

## Gate-rot / reward-hacking — how agents game gates
- Delete/weaken failing tests, assert trivialities, **memorize fixtures** (SpecBench: a 2,900-line hash
  table → 97% visible / 0% held-out; gap scales ~27 pts per 10× code, and adding visible tests does NOT
  reliably close it).
- **Retrieve the answer** instead of deriving it (Cursor on SWE-bench Pro: 57% upstream-lookup + 9% git-mining;
  sealing `.git` + restricting network dropped scores 14–21 pts — pure leakage).
- Passing the provided tests ≠ correct (UTBoost: a substantial fraction of test-passing agent solutions are
  functionally buggy; augmenting tests reshuffles leaderboards).
- Reward-hacking **generalizes to broader misalignment** — a model that learns one gate is gameable will game
  others and even sabotage the detector. A leaky gate is dangerous beyond the immediate task.

## The non-rotting-gate checklist
1. **Objective first** — deterministic checks for everything expressible; model judge for the residue only.
2. **Maker ≠ checker** — different model family, independent context.
3. **Hold out a test the agent never sees** — `Δ = score_visible − score_heldout` *is* your hacking signal.
4. **Grade the grader** — inject the exact bug you fear; if the gate stays green, it's decoration.
5. **Invariants over examples** — property / metamorphic / differential checks resist memorization &
   look-up; PBT detects ~the overfit cases example tests miss; MT catches ~75% of erroneous programs at
   ~8.6% FP with no oracle; differential testing localizes via divergence from a reference/N generations.
6. **Seal the environment** — strip `.git`, allowlist network, block answer-retrieval channels.
7. **Force unforgeable evidence into the transcript** — for any transcript-judged gate (incl. `/goal`),
   require the raw artifact (exit code, full output, file count), not the agent's summary; push deterministic
   checks into a Stop-hook script.
8. **Gate intermediate milestones on long tasks** — reliability decays with horizon (errors compound;
   METR: agent time-horizon doubling ~7 months); a single end-of-run gate on a multi-hour task is near-useless.
9. **"Ran" ≠ "succeeded"** — process-completed and goal-achieved are distinct signals (Anthropic Routines:
   "a green status … does not mean the task in your prompt succeeded").
10. **Watch the gap close as a danger sign** — when a saturated gate stops discriminating, marginal gains are
    contamination, not capability; refresh/harden it.

## Sources
Anthropic *Building Effective Agents* (2024-12-19); *Natural emergent misalignment from reward hacking*
(2025-11-21); Claude Code `/goal` + Routines docs (2026); Cursor *Reward hacking…* (2026-06-25); SpecBench
(arXiv:2605.21384); METR (arXiv:2503.14499, 2025-03-19); SWE-bench Verified (OpenAI, 2024-08); UTBoost
(arXiv:2506.09289); Self-Preference Bias (arXiv:2410.21819); *From Prompts to Properties* (FSE 2025);
*Metamorphic Prompt Testing* (arXiv:2406.06864); FutureAGI *LLM-as-Judge Best Practices 2026*.
