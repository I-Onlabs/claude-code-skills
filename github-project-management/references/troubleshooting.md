# Troubleshooting & Constraints

## Sync Issues

```bash
npx ruv-swarm github board-diagnose \
  --check "permissions,webhooks,rate-limits" \
  --test-sync \
  --show-conflicts
```

## Performance Optimisation

```bash
npx ruv-swarm github board-optimize \
  --analyze-size \
  --archive-completed \
  --index-fields \
  --cache-views
```

## Data Recovery

```bash
npx ruv-swarm github board-recover \
  --backup-id "2024-01-15" \
  --restore-cards \
  --preserve-current \
  --merge-conflicts
```

## GitHub Constraints to Watch

| Limit | Default | Workaround |
|---|---|---|
| REST API rate limit (authenticated) | 5,000 req/hr | Batch comment operations; cache `gh` responses; use GraphQL where possible |
| GraphQL points / hour | 5,000 | Reduce field selection in queries; rely on webhooks for real-time |
| Project items per project | 1,200 (Projects v2) | Archive completed; split by quarter or product area |
| Issue body length | 65,536 chars | Move long checklists into linked sub-issues |
| Labels per issue | 100 | Most rules cap well below this; flag if your label scheme creeps near the limit |
| Webhook delivery retries | 8 attempts over ~30 min | Make handler idempotent; reconcile via periodic full sync |

## Required Permissions

| Operation | Token scope |
|---|---|
| Read issues, view PRs | `repo:read` (or `public_repo` for public) |
| Create / edit issues, post comments | `repo` |
| Manage Projects v2 | `project` (`read:project` for read-only) |
| Webhook subscription | `admin:repo_hook` |
| Cross-organisation sync | `read:org`, `repo` on both orgs |

## Tool Prerequisites

- `gh` CLI ≥ 2.40 — `gh auth status` should show "Logged in"
- `jq` ≥ 1.6 — required by every JSON-piping example
- Node.js ≥ 18 — required by `npx ruv-swarm`
- One of: `ruv-swarm` MCP server **or** `claude-flow` MCP server configured. See [ruv-swarm](https://github.com/ruvnet/ruv-swarm) and [claude-flow](https://github.com/ruvnet/claude-flow) for install. Several commands work without these (the plain `gh` examples), but `swarm-` commands require the MCP server to be running.

## Security Checklist

The original skill called these out as six categories — Command Authorization, Rate Limiting, Audit Logging, Data Privacy, Access Control, Webhook Security. Restated as concrete checks:

- [ ] **Command Authorization** — validate user permissions before running issue-comment commands (`/swarm assign`, `/swarm decompose`, etc.)
- [ ] **Rate Limiting** — cap comment-command handler invocations per user/hour to prevent spam
- [ ] **Audit Logging** — log all swarm mutations (issue edits, board moves) with actor + timestamp
- [ ] **Data Privacy** — respect private-repo scoping; never leak private-repo data through cross-repo / cross-org workflows
- [ ] **Access Control** — project-board API tokens scoped to read+write only on the boards in use, not org-wide; review on a schedule
- [ ] **Webhook Security** — verify `x-hub-signature-256`; rotate `GITHUB_WEBHOOK_SECRET` periodically; reject events from unverified senders
