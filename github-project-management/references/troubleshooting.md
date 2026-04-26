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

- [ ] Validate user permissions before running issue-comment commands
- [ ] Rate-limit comment-command handlers to prevent spam
- [ ] Audit-log all swarm operations (issue + board mutations)
- [ ] Respect private-repo scoping in cross-repo / cross-org workflows
- [ ] Verify webhook signatures (`x-hub-signature-256`) for real-time sync
