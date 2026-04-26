---
name: github-project-management
title: GitHub Project Management
version: 2.1.0
category: github
description: Manage GitHub issues, project boards, sprints, and milestones with swarm-coordinated automation — issue triage, decomposition into subtasks, board sync, sprint planning, KPI tracking. Use when asked to "github project management", "manage github projects", "github issue automation", "swarm project board", "automate sprint", "triage issues", or "set up project board".
author: Claude Code
tags:
  - github
  - project-management
  - issue-tracking
  - project-boards
  - sprint-planning
  - agile
  - swarm-coordination
difficulty: intermediate
prerequisites:
  - GitHub CLI (gh) v2.40+ installed and authenticated (`gh auth status`)
  - jq v1.6+
  - Node.js 18+ (for `npx ruv-swarm`)
  - ruv-swarm OR claude-flow MCP server configured (only required for swarm-* commands)
  - Repository access (write scope for mutating commands; project scope for boards)
tools_required:
  - mcp__github__*
  - mcp__claude-flow__*
  - Bash
  - Read
  - Write
  - TodoWrite
related_skills:
  - github-pr-workflow
  - github-release-management
  - sparc-orchestrator
estimated_time: 30-45 minutes
---

# GitHub Project Management

Coordinates GitHub issue management, project board automation, and sprint planning using AI swarm agents. Supports issue triage / decomposition, bidirectional board sync, automated progress tracking, and KPI reporting.

## Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## When to Use

- "Triage these unlabelled issues"
- "Break down this epic into subtasks"
- "Sync GitHub issues with the project board"
- "Set up a sprint with velocity tracking"
- "Generate a sprint-summary report"
- "Coordinate work across multiple repos / boards"

## Prerequisites

See [`references/troubleshooting.md`](references/troubleshooting.md#tool-prerequisites) for full tool versions, required token scopes, and GitHub API limits.

Minimum to run the plain `gh` examples: `gh` + `jq`. Swarm features additionally need `ruv-swarm` or `claude-flow` MCP server running — see those projects' docs for install. The skill degrades gracefully: anything prefixed with `npx ruv-swarm` requires the MCP server; everything else is plain `gh` + `jq`.

## Quick Start

```bash
# Create a coordinated issue
gh issue create \
  --title "Feature: Advanced Authentication" \
  --body "Implement OAuth2 with social login..." \
  --label "enhancement,swarm-ready"

# Initialise swarm tracking
npx claude-flow@alpha hooks pre-task --description "Feature implementation"

# Set up the board
PROJECT_ID=$(gh project list --owner @me --format json | jq -r '.projects[0].id')

npx ruv-swarm github board-init \
  --project-id "$PROJECT_ID" \
  --sync-mode "bidirectional"
```

## Workflow

1. **Triage** incoming issues — auto-label, link duplicates ([`issue-management.md`](references/issue-management.md))
2. **Decompose** large issues into subtasks with priority ([`issue-management.md`](references/issue-management.md))
3. **Sync** issues to the project board ([`board-automation.md`](references/board-automation.md))
4. **Pick the right swarm topology** (mesh / hierarchical / ring / star — see [`swarm-topologies.md`](references/swarm-topologies.md))
5. **Track sprint velocity & KPIs** ([`sprint-and-analytics.md`](references/sprint-and-analytics.md))
6. **Automate** via GitHub Actions + comment commands ([`automation-patterns.md`](references/automation-patterns.md))
7. **Verify** (see below)

## Verification

After running a workflow, confirm:

- [ ] Every issue acted on shows the expected label change in `gh issue view <num> --json labels`
- [ ] Every board-synced issue appears as a project card in the expected column
- [ ] Subtask checklists in issue bodies are valid Markdown (parseable; no broken `- [ ]` syntax)
- [ ] Progress comments posted by automation are idempotent — re-running doesn't duplicate
- [ ] `gh api rate_limit` shows headroom (running this against thousands of issues can exhaust the 5,000 req/hr limit; see [`troubleshooting.md`](references/troubleshooting.md#github-constraints-to-watch))
- [ ] Closed-as-stale issues match the explicit `STALE_DATE` cutoff — spot-check three

## References

- [`references/issue-management.md`](references/issue-management.md) — creation, batch, issue→swarm, triage, decomposition, progress, stale management
- [`references/board-automation.md`](references/board-automation.md) — board init, mapping config, sync, smart card management, views, dashboards
- [`references/sprint-and-analytics.md`](references/sprint-and-analytics.md) — sprint setup, kanban/scrum, analytics, KPIs, release planning
- [`references/swarm-topologies.md`](references/swarm-topologies.md) — multi-board sync, dependencies/epics, cross-repo, team collab, topology guide
- [`references/templates.md`](references/templates.md) — issue templates (integration / bug / feature / swarm task)
- [`references/automation-patterns.md`](references/automation-patterns.md) — GitHub Actions workflow, specialised swarms, complete worked example, command quick-reference
- [`references/troubleshooting.md`](references/troubleshooting.md) — sync, performance, recovery, GitHub constraints, required permissions, security checklist
