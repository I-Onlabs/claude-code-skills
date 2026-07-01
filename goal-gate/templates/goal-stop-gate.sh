#!/usr/bin/env bash
# goal-stop-gate.sh — a DETERMINISTIC Stop-hook gate to pair with native /goal.
#
# /goal's Haiku checker reads only the transcript (no tools, no files), so it can be fooled by a
# hallucinated "tests passed". This script runs the REAL verify command and blocks the stop (exit 2)
# until it genuinely passes — the failing output becomes Claude's next-turn guidance.
#
# Register as a Stop hook (project .claude/settings.json):
#   { "hooks": { "Stop": [ { "hooks": [
#     { "type": "command",
#       "command": "CLAUDE_GOAL_VERIFY_CMD='pytest -q' .claude/hooks/goal-stop-gate.sh",
#       "timeout": 120000 } ] } ] } }
#
# Config:
#   CLAUDE_GOAL_VERIFY_CMD  the command to run (required). exit 0 = done, non-zero = keep working.
#   CLAUDE_GOAL_GATE_MODE   block (default) | observe (never blocks, just logs).
#
# Safety: respects `stop_hook_active` (blocks at most once per stop, never loops); fails OPEN — if the
# verify command is unset or un-runnable, it ALLOWS the stop so a broken gate can't trap the session.
set -uo pipefail

INPUT="$(cat 2>/dev/null || true)"
MODE="${CLAUDE_GOAL_GATE_MODE:-block}"
CMD="${CLAUDE_GOAL_VERIFY_CMD:-}"

# Loop guard: if Claude Code already re-entered the Stop hook, don't block again.
if printf '%s' "$INPUT" | grep -q '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

# Fail open: no command configured → nothing to verify → allow the stop.
[ -z "$CMD" ] && exit 0

# Run the real check. Capture combined output for the block reason.
OUT="$(bash -c "$CMD" 2>&1)"
RC=$?

if [ "$RC" -eq 0 ]; then
  exit 0   # genuinely done — allow the stop
fi

# Verify failed. Surface the tail of the real output as the reason.
REASON="$(printf '%s\n' "$OUT" | tail -n 40)"
if [ "$MODE" = "observe" ]; then
  printf '[goal-gate observe] verify FAILED (rc=%s); would block. Tail:\n%s\n' "$RC" "$REASON" >&2
  exit 0
fi

printf 'goal-gate: the /goal condition is NOT yet met — `%s` exited %s. Keep working; do not stop until it passes.\n--- verify output (tail) ---\n%s\n' "$CMD" "$RC" "$REASON" >&2
exit 2   # block the stop; stderr becomes Claude's next-turn guidance
