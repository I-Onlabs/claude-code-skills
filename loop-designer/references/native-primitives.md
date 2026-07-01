# Native loop primitives — verified reference (Claude Code 2.1.170, docs 2026-06-30)

Load this when you need exact syntax. Every row was confirmed against `code.claude.com/docs`.
Preview/experimental items are flagged — don't hard-wire against them.

## `/loop` — recurring / self-paced prompting  (stable, v2.1.72+)
- Syntax: `/loop [interval] [prompt]` · bare `/loop` · `/loop 20m /skill-name` (skill autorun v2.1.196+).
- **Bare `/loop` runs `~/.claude/loop.md` (or project `.claude/loop.md`) if present**, else a generic
  built-in maintenance prompt (continue unfinished work → tend the branch's PR → cleanup).
- `loop.md` format: plain Markdown, **no required structure, ≤25,000 bytes**; edits apply next iteration.
- Interval units `s/m/h/d` (`s` rounds up to 1 min); cron via `CronCreate`; omit interval → **self-paced**
  (Claude picks 1 min–1 hr each iteration and prints the delay + reason; can end the loop itself).
- Underlying tools: `CronCreate` / `CronList` / `CronDelete` (5-field cron, **50 tasks max/session**, 8-char IDs).
- **7-day expiry** on recurring tasks (fires a final time, self-deletes). `Esc` clears the pending wakeup.
- `CLAUDE_CODE_DISABLE_CRON=1` disables all scheduling. Jitter: recurring ≤30 min (or half-interval if <1 hr).
- Restored on `--resume`/`--continue` if unexpired; cleared on `--clear`. Bedrock/Vertex/Foundry: no-prompt
  prints usage; prompts run on a fixed 10-min schedule (no dynamic self-pacing).

## `/goal` — run until a condition holds  (stable, v2.1.139+)
- Syntax: `/goal <condition>` · `/goal` (status) · `/goal clear` (aliases stop/off/reset/none/cancel). One goal/session.
- Checker = a **separate small fast model (defaults to Haiku)** run via a session-scoped **prompt-based Stop
  hook**. After each turn it reads the condition + transcript, returns yes/no + reason. "No" → continue with
  the reason as guidance; "yes" → clears.
- **CRITICAL LIMIT: the checker does not call tools, run commands, or read files.** It can only judge what
  the transcript already contains. So: write conditions demonstrable from surfaced output ("`npm test` exits
  0" *with the agent instructed to paste the real output*), or move the real check into a deterministic
  Stop-hook script and let `/goal` adjudicate only the semantic residue.
- Condition ≤ **4000 chars**. Bound runtime with `… or stop after N turns`. Headless: `claude -p "/goal …"`.
- **Unavailable** when `disableAllHooks` or `allowManagedHooksOnly` is set. Restores on `--resume` if still active.

## Routines / `/schedule` — cloud, laptop-closed  (RESEARCH PREVIEW)
- CLI `/schedule <description>` | `list` | `update` | `run`; web at claude.ai/code/routines.
- Triggers (combinable): **Scheduled** (recurring/one-off), **API** (POST `/v1/claude_code/routines/{id}/fire`,
  bearer token, beta header `experimental-cc-routine-2026-04-01`), **GitHub** (PR/release events with filters).
- **Min interval 1 hour** (recurring); API/GitHub unthrottled. Needs claude.ai login (Pro/Max/Team/Enterprise
  with CC-on-web) — **not** API-key/Bedrock/Vertex auth.
- Each run = fresh clone; **pushes only to `claude/*` branches** unless "Allow unrestricted branch pushes".
- **Green status = the session started/exited without infra error, NOT that the task succeeded** — open the run.
- Daily per-account cap (one-off runs exempt). Token shown once. Org toggle at claude.ai/admin-settings/claude-code.

## Hooks — full 2.1.170 event surface (★ = can block; exit 2 blocks, stderr → error msg)
SessionStart · Setup · SessionEnd · UserPromptSubmit★ · UserPromptExpansion★ · Stop★ · StopFailure ·
PreToolUse★ (matcher=tool) · PostToolUse · PostToolUseFailure · **PostToolBatch★** · PermissionRequest★ ·
PermissionDenied · SubagentStart · SubagentStop★ · **TeammateIdle★** (keeps a teammate working) ·
**TaskCreated★ / TaskCompleted★** · FileChanged · CwdChanged · ConfigChange★ · InstructionsLoaded ·
WorktreeCreate★ / WorktreeRemove · MessageDisplay · Notification · **PreCompact★** · **PostCompact** ·
Elicitation★ / ElicitationResult★.
- Handler types: `command`, `http`, `mcp_tool`, `prompt` (model yes/no — what `/goal` uses) — all **stable**;
  `agent` (spawns a Read/Grep/Glob verify subagent) — **experimental**.
- Current `~/.claude/settings.json` uses only PreCompact/SessionStart/PreToolUse/PostToolUse/Stop. PostCompact
  is **not** a native blockable event — emulate post-compaction re-injection via SessionStart/UserPromptSubmit.

## Subagents — `.claude/agents/*.md` (Markdown + YAML frontmatter)
Fields (stable unless noted): `name`, `description` (required); `tools`, `disallowedTools`, `model`
(`sonnet/opus/haiku/fable/<id>/inherit`), `permissionMode`, `maxTurns`, `skills` (preload), `mcpServers`,
`hooks`, `memory` (`user/project/local`, persistent cross-session), `background`, `effort`
(`low/medium/high/xhigh/max`), **`isolation: worktree`**, `color`, `initialPrompt`. Plugin subagents ignore
`hooks`/`mcpServers`/`permissionMode`. **Nested depth limit 5** (depth-5 agent can't spawn further). Built-ins:
Explore (read-only Haiku), Plan (read-only), general-purpose. `/fork` inherits full conversation + shares cache.

## Worktrees
`claude --worktree [name]` (`-w`) → `.claude/worktrees/<name>/` on branch `worktree-<name>`, from `origin/HEAD`
(clean) by default (`worktree.baseRef` = `"fresh"|"head"`). `claude --worktree "#1234"` checks out a PR.
`isolation: worktree` on a subagent → temp checkout, auto-removed if unchanged. `.worktreeinclude` (gitignore
syntax) copies gitignored files (e.g. `.env`) in. `WorktreeCreate`/`Remove` hooks for non-git VCS. Add
`.claude/worktrees/` to `.gitignore`. With `-p`, worktrees are **not** auto-removed.

## Agent teams — EXPERIMENTAL, off by default
`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Teammates are full independent CC sessions that message each other +
share a file-locked task list. One lead, 3–5 teammates recommended. Quality gates via TeammateIdle/TaskCreated/
TaskCompleted. Much higher token cost; no resume of in-process teammates; one team/session.
