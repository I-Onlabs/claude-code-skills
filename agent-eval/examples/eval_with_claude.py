#!/usr/bin/env python3
"""Runnable agent-output eval wired to REAL Claude judges (Anthropic eval discipline).

Runs an agent-under-test (claude -p) N trials on a task, grades each trial's FINAL OUTPUT with a
SEPARATE per-dimension Opus judge (each judge can answer UNKNOWN), aggregates, and reports pass^k
(production reliability) — using the tested primitives in lib/agent_eval.py.

Run:  python3 eval_with_claude.py "Write a function that reverses a linked list in O(n)"
Requires the `claude` CLI. Spends maker+judge tokens (trials × dimensions × 2 calls).

The judge parser is factored out (parse_dim) and unit-tested in tests/test_eval_parse_dim.py.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude" / "lib"))
from agent_eval import run_eval_suite, aggregate_dimensions, PASS, FAIL, UNKNOWN  # noqa: E402

_TIMEOUT = 300
DIMENSIONS = ["correctness", "completeness", "no_obvious_bug"]


def _claude(prompt: str, model: str) -> str:
    try:
        r = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "json", prompt],
            capture_output=True, text=True, timeout=_TIMEOUT,
        )
        out = (r.stdout or "").strip()
        try:
            obj = json.loads(out)
            return obj.get("result") or obj.get("text") or out
        except json.JSONDecodeError:
            return out
    except Exception as e:  # noqa: BLE001
        return f"[error: {type(e).__name__}: {e}]"


def parse_dim(text: str) -> str:
    """Extract PASS / FAIL / UNKNOWN from a per-dimension judge reply. PURE + TESTED.
    Defaults to UNKNOWN (the escape hatch) when no clear verdict — never a silent PASS."""
    if not text:
        return UNKNOWN
    m = re.search(r"\b(PASS|FAIL|UNKNOWN)\b", text.upper())
    return m.group(1) if m else UNKNOWN


def make_run_fn(model: str = "sonnet"):
    def run_fn(task):
        t = task if isinstance(task, str) else task.get("prompt", "")
        result = _claude(f"Solve this task. Output ONLY the deliverable.\n\nTASK:\n{t}", model)
        # trajectory diagnostics would come from the worker's JSON usage in a real harness;
        # here we just carry the result.
        return {"result": result}
    return run_fn


def make_grade_fn(judge_model: str = "opus"):
    def grade_fn(task, run_result):
        t = task if isinstance(task, str) else task.get("prompt", "")
        deliverable = run_result.get("result", "") if isinstance(run_result, dict) else str(run_result)
        verdicts = []
        for dim in DIMENSIONS:                 # one ISOLATED judge per dimension
            prompt = (
                f"You are a SKEPTICAL grader for ONE dimension only: {dim}. "
                "Answer with exactly one word: PASS, FAIL, or UNKNOWN (UNKNOWN if you lack info).\n\n"
                f"TASK:\n{t}\n\nDELIVERABLE:\n{deliverable}\n\nVerdict for '{dim}':"
            )
            verdicts.append({"dimension": dim, "status": parse_dim(_claude(prompt, judge_model))})
        return aggregate_dimensions(verdicts)   # PASS only iff every dimension PASS
    return grade_fn


def main(argv) -> int:
    task = argv[1] if len(argv) > 1 else "Write a Python function that reverses a singly linked list in O(n) time, O(1) space."
    trials = int(argv[2]) if len(argv) > 2 else 3
    suite = run_eval_suite([{"id": "t1", "prompt": task}], make_run_fn("sonnet"),
                           make_grade_fn("opus"), trials=trials, k=trials)
    print(json.dumps(suite, indent=2))
    return 0 if suite["mean_pass_hat_k"] >= 0.5 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
