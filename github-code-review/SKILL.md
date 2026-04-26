---
name: github-code-review
version: 1.1.0
description: Run a multi-agent code review on a GitHub pull request, with parallel security / performance / architecture / style passes, inline comments, and quality-gate enforcement. Use when asked to "github code review", "review github pr", "run code review on PR", "swarm review", "automated PR review", or "post inline review comments".
category: github
tags: [code-review, github, swarm, pr-management, automation]
author: Claude Code Flow
requires:
  - github-cli
  - ruv-swarm
  - claude-flow
capabilities:
  - Multi-agent code review
  - Automated PR management
  - Security and performance analysis
  - Swarm-based review orchestration
  - Inline comment generation
  - Quality gate enforcement
---

# GitHub Code Review

Coordinates parallel review agents (security, performance, architecture, style, accessibility) against a GitHub PR. Each agent focuses on one dimension; the swarm aggregates findings, posts inline comments, and enforces quality gates.

## Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## When to Use

- "Run a code review on PR #123"
- "Do a security review on this PR"
- "Set up automated review on every PR"
- "Generate inline review comments for the diff"
- "Add quality gates to branch protection"

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth status`)
- `ruv-swarm` and/or `claude-flow` MCP server configured
- Repository access permissions for the target PR
- For automated review: `GITHUB_TOKEN` available in CI

## Quick Start

```bash
PR=123
PR_DATA=$(gh pr view "$PR" --json files,additions,deletions,title,body)
PR_DIFF=$(gh pr diff "$PR")

npx ruv-swarm github review-init \
  --pr "$PR" \
  --pr-data "$PR_DATA" \
  --diff "$PR_DIFF" \
  --agents "security,performance,style,architecture,accessibility" \
  --depth comprehensive

gh pr comment "$PR" --body "Multi-agent code review initiated"
```

## Workflow

1. **Fetch PR context** with `gh pr view --json` and `gh pr diff`
2. **Pick topology** based on PR size (ring < 100 LOC, mesh 100–500, hierarchical > 500) — see [`references/swarm-management.md`](references/swarm-management.md)
3. **Dispatch agents in parallel** — one per review dimension; see [`references/review-agents.md`](references/review-agents.md)
4. **Aggregate findings**, post inline comments via the GitHub API; see [`references/comments-and-gates.md`](references/comments-and-gates.md)
5. **Apply quality gates** — block merge on critical security findings, warn on performance regressions, suggest on style
6. **Verify** (see below)

## Verification

After a review run, confirm:

- [ ] Each requested agent posted at least one finding (or an explicit "no issues found")
- [ ] Inline comments resolve to actual lines in the diff (no stale `commit_id`)
- [ ] PR status reflects the outcome — `--approve`, `--request-changes`, or labelled
- [ ] Critical security findings blocked the merge (test by injecting a known-bad pattern, e.g. an obvious eval)
- [ ] Rate-limit budget after the run — `gh api rate_limit` — is not exhausted

If a gate misfires, see [`references/troubleshooting.md`](references/troubleshooting.md).

## References

- [`references/review-agents.md`](references/review-agents.md) — security / performance / architecture / style agent commands and templates
- [`references/swarm-management.md`](references/swarm-management.md) — swarm creation, label routing, topology, comment commands, webhook handler
- [`references/configuration.md`](references/configuration.md) — `review-swarm.yml`, custom triggers, GitHub Actions, auto-merge
- [`references/comments-and-gates.md`](references/comments-and-gates.md) — inline comment generation, batch management, quality gates, metrics
- [`references/advanced-features.md`](references/advanced-features.md) — context-aware review, learning, cross-PR analysis, custom agents
- [`references/workflow-examples.md`](references/workflow-examples.md) — five worked examples + Claude Code integration pattern
- [`references/troubleshooting.md`](references/troubleshooting.md) — agents not spawning, comments not posting, slow reviews, security checklist
