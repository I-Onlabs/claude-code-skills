# Troubleshooting

## Review agents not spawning

```bash
npx ruv-swarm swarm-status                              # check swarm
gh auth status                                          # verify gh auth
npx ruv-swarm github review-init --pr 123 --force       # re-init
```

## Comments not posting to PR

```bash
gh auth status                                          # token still valid?
gh api rate_limit                                       # over the limit?
npx ruv-swarm github review-comments --pr 123 --batch   # batch instead of per-comment
```

## Review taking too long

```bash
# Incremental on large PRs
npx ruv-swarm github review-init --pr 123 --incremental

# Reduce agent count
npx ruv-swarm github review-init --pr 123 --agents "security,style" --max-agents 3

# Parallelise + cache
npx ruv-swarm github review-init --pr 123 --parallel --cache-results
```

## Performance tips for large reviews

Concrete optimisations beyond the troubleshooting commands above:

- **Cache analysis results** between runs so unchanged files aren't re-reviewed (`--cache-results`)
- **Incremental review** for PRs over a few hundred lines (`--incremental` reviews only the diff since the last run)
- **Parallel agent execution** — agents within a single PR review are independent; the swarm topology should be `mesh` or `hierarchical`, not `ring`
- **Batch comment posting** instead of per-finding API calls — see [`comments-and-gates.md`](comments-and-gates.md) `--batch` flag

## Webhook security caveats

Beyond the `swarm-management.md` HMAC verification:

- The numeric PR validation in the webhook handler **does not block PRs from forks**. Fork PRs can send arbitrary content. If your repo accepts fork PRs, add a `event.pull_request.head.repo.fork` check before invoking the swarm.
- Rotate the `GITHUB_WEBHOOK_SECRET` periodically; treat it like a production credential.

## Security checklist

Before enabling automated review on a public repo:

- [ ] GitHub token scoped to a single repository
- [ ] Webhook signatures verified (`x-hub-signature-256`, see `swarm-management.md`)
- [ ] `GITHUB_WEBHOOK_SECRET` from environment, not committed to repo
- [ ] Command-injection protection — never interpolate PR content into shell strings
- [ ] Fork-PR handling explicit (block, sandbox, or accept with reduced agent set)
- [ ] Rate limiting configured for webhook endpoint
- [ ] Audit logging enabled for all swarm operations
- [ ] Secret scanning active in branch protection
- [ ] Branch protection rules enforced (required status checks)
