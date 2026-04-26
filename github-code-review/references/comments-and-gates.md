# Comments & Quality Gates

## Generate Inline Review Comments

```bash
PR_DIFF=$(gh pr diff 123 --color never)
PR_FILES=$(gh pr view 123 --json files)

COMMENTS=$(npx ruv-swarm github review-comment \
  --pr 123 \
  --diff "$PR_DIFF" \
  --files "$PR_FILES" \
  --style "constructive" \
  --include-examples \
  --suggest-fixes)

echo "$COMMENTS" | jq -c '.[]' | while read -r comment; do
  FILE=$(echo "$comment" | jq -r '.path')
  LINE=$(echo "$comment" | jq -r '.line')
  BODY=$(echo "$comment" | jq -r '.body')
  COMMIT_ID=$(gh pr view 123 --json headRefOid -q .headRefOid)

  gh api \
    --method POST \
    /repos/:owner/:repo/pulls/123/comments \
    -f path="$FILE" \
    -f line="$LINE" \
    -f body="$BODY" \
    -f commit_id="$COMMIT_ID"
done
```

## Batch Comment Management

```bash
npx ruv-swarm github review-comments \
  --pr 123 \
  --group-by "agent,severity" \
  --summarize \
  --resolve-outdated
```

## Required Status Checks

```yaml
protection_rules:
  required_status_checks:
    strict: true
    contexts:
      - "review-swarm/security"
      - "review-swarm/performance"
      - "review-swarm/architecture"
      - "review-swarm/tests"
```

## Quality Gate Thresholds

```bash
npx ruv-swarm github quality-gates \
  --define '{
    "security":     {"threshold": "no-critical"},
    "performance":  {"regression": "<5%"},
    "coverage":     {"minimum": "80%"},
    "architecture": {"complexity": "<10"},
    "duplication":  {"maximum": "5%"}
  }'
```

## Track Review Metrics

```bash
npx ruv-swarm github review-metrics \
  --period 30d \
  --metrics "issues-found,false-positives,fix-rate,time-to-review" \
  --export-dashboard \
  --format json
```

## Progress Updates to PR

```bash
PROGRESS=$(npx ruv-swarm github pr-progress 123 --format markdown)
gh pr comment 123 --body "$PROGRESS"

if [[ $(echo "$PROGRESS" | grep -o '[0-9]\+%' | sed 's/%//') -gt 90 ]]; then
  gh pr edit 123 --add-label "ready-for-review"
fi
```
