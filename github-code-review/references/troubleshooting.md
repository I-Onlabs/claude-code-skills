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

## Security checklist

Before enabling automated review on a public repo:

- [ ] GitHub token scoped to a single repository
- [ ] Webhook signatures verified (`x-hub-signature-256`, see `swarm-management.md`)
- [ ] Command-injection protection — never interpolate PR content into shell strings
- [ ] Rate limiting configured for webhook endpoint
- [ ] Audit logging enabled for all swarm operations
- [ ] Secret scanning active in branch protection
- [ ] Branch protection rules enforced (required status checks)
