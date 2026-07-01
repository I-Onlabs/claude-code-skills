#!/usr/bin/env python3
"""Runnable evaluator-optimizer wired to REAL Claude subagents (Anthropic's #1 harness lever).

Cheap maker (Haiku) generates; strong, skeptical checker (Opus) grades against a sprint-contract each
round; loop repeats with feedback until PASS or the iteration cap — using the tested control loop in
lib/eval_optimizer.py, which ENFORCES maker≠checker and the cap.

Run:  python3 eo_with_claude.py "Write a Python function is_palindrome(s) ignoring case & non-alnum"
Requires the `claude` CLI on PATH. Each round spends maker+checker tokens — it really calls Claude.

The verdict parser is factored out (parse_verdict) and unit-tested in tests/test_eo_parse_verdict.py
so the brittle bit (reading the checker's reply) is pinned without spending tokens.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude" / "lib"))
from eval_optimizer import run_eval_optimizer, PASS, NEEDS_IMPROVEMENT, FAIL  # noqa: E402

_TIMEOUT = 300


def _claude(prompt: str, model: str) -> str:
    """One non-interactive Claude call; returns the assistant's text (or an [error] marker)."""
    try:
        r = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "json", prompt],
            capture_output=True, text=True, timeout=_TIMEOUT,
        )
        out = (r.stdout or "").strip()
        try:                                   # --output-format json wraps the text in a result field
            obj = json.loads(out)
            return obj.get("result") or obj.get("text") or out
        except json.JSONDecodeError:
            return out
    except Exception as e:                     # noqa: BLE001 — surface, don't crash the loop
        return f"[error calling claude: {type(e).__name__}: {e}]"


def parse_verdict(text: str) -> dict:
    """Extract {status, feedback} from a checker reply. PURE + TESTED (no token spend).

    Accepts a JSON object {"status": "...", "feedback": "..."}, or plain text with a STATUS: line
    (PASS / NEEDS_IMPROVEMENT / FAIL, case-insensitive) and an optional FEEDBACK: section. Defaults to
    NEEDS_IMPROVEMENT when no clear status is found — the skeptical default (never a silent PASS).
    """
    if not text:
        return {"status": NEEDS_IMPROVEMENT, "feedback": "empty checker reply"}
    # 1) JSON object anywhere in the reply
    m = re.search(r"\{[^{}]*\"status\"[^{}]*\}", text, re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            st = str(obj.get("status", "")).strip().upper()
            if st in (PASS, NEEDS_IMPROVEMENT, FAIL):
                return {"status": st, "feedback": str(obj.get("feedback", ""))}
        except json.JSONDecodeError:
            pass
    # 2) STATUS: line
    sm = re.search(r"STATUS\s*[:=]\s*(PASS|NEEDS_IMPROVEMENT|FAIL)", text, re.I)
    status = sm.group(1).upper() if sm else None
    if status is None:                         # bare keyword fallback (PASS only if unambiguous)
        up = text.upper()
        if "NEEDS_IMPROVEMENT" in up or "FAIL" in up:
            status = FAIL if "FAIL" in up and "NEEDS_IMPROVEMENT" not in up else NEEDS_IMPROVEMENT
        elif re.search(r"\bPASS\b", up):
            status = PASS
    fm = re.search(r"FEEDBACK\s*[:=]\s*(.+)", text, re.I | re.S)
    feedback = (fm.group(1).strip() if fm else text.strip())[:1500]
    return {"status": status or NEEDS_IMPROVEMENT, "feedback": feedback}


def make_generate_fn(model: str = "haiku"):
    def generate_fn(task: str, context: str | None) -> str:
        prompt = (f"You are the MAKER. Produce the best solution to the task. Output ONLY the "
                  f"deliverable (e.g. the code), no commentary.\n\n{context or 'TASK:\\n' + task}")
        return _claude(prompt, model)
    return generate_fn


def make_evaluate_fn(model: str = "opus"):
    def evaluate_fn(task: str, result: str, contract) -> dict:
        crit = "\n".join(f"- {c}" for c in (contract or [])) or "- correctly and completely solves the task"
        prompt = (
            "You are a SKEPTICAL CHECKER. Your job is to find why the work FAILS, not to praise it. "
            "Grade the deliverable against EVERY criterion. If you lack info to judge, say so.\n\n"
            f"TASK:\n{task}\n\nMUST SATISFY (all hard-threshold):\n{crit}\n\n"
            f"DELIVERABLE:\n{result}\n\n"
            "Reply EXACTLY as:\nSTATUS: PASS | NEEDS_IMPROVEMENT | FAIL\n"
            "FEEDBACK: <specific, actionable; name each unmet criterion>"
        )
        return parse_verdict(_claude(prompt, model))
    return evaluate_fn


def main(argv) -> int:
    task = argv[1] if len(argv) > 1 else "Write a Python function is_palindrome(s) that ignores case and non-alphanumerics."
    contract = [
        "is a single self-contained Python function",
        "ignores case and non-alphanumeric characters",
        "handles the empty string (returns True)",
        "no external dependencies",
    ]
    out = run_eval_optimizer(
        task,
        make_generate_fn("haiku"),          # cheap maker
        make_evaluate_fn("opus"),           # strong skeptical checker  → maker≠checker enforced
        contract=contract, max_iters=4, maker_id="haiku", checker_id="opus",
    )
    print(f"\n=== {'PASSED' if out['passed'] else 'NOT PASSED'} in {out['iters']} round(s): {out['reason']} ===")
    print(out["result"])
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
