#!/usr/bin/env bash
# init.sh — the initializer agent writes this ONCE; every coding session runs it at start.
# Two jobs: (1) boot the dev server, (2) run a basic end-to-end smoke test so the agent
# instantly knows if the app was left broken — and saves tokens re-deriving how to test.
# Anthropic "Effective Harnesses for Long-Running Agents": the session-start liveness check.
#
# Fill in the <PLACEHOLDERS> for your project. Keep it fast and deterministic. Exit non-zero
# on a broken app so the coding agent fixes it BEFORE starting new feature work.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "== init.sh: install =="
<INSTALL_CMD>            # e.g. npm ci  /  pnpm install --frozen-lockfile  /  uv sync

echo "== init.sh: start dev server (background) =="
<START_SERVER_CMD> &    # e.g. npm run dev  /  uvicorn app:app --port 8000
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT

echo "== init.sh: wait for ready =="
for i in $(seq 1 30); do
  if curl -fsS "<HEALTH_URL>" >/dev/null 2>&1; then break; fi   # e.g. http://localhost:3000
  sleep 1
  [ "$i" -eq 30 ] && { echo "init.sh: server never became ready" >&2; exit 1; }
done

echo "== init.sh: end-to-end smoke test =="
# Drive ONE real user path and assert the observable outcome. Prefer Playwright/Puppeteer MCP
# for UI apps ("do all testing as a human user would"); a curl assertion is fine for APIs.
<SMOKE_TEST_CMD>        # e.g. curl -fsS http://localhost:3000/api/health | grep -q '"ok":true'

echo "init.sh: OK — app is live and the smoke path passed."
