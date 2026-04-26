# Configuration & Workflows

## `.github/review-swarm.yml`

```yaml
version: 1
review:
  auto-trigger: true
  required-agents:
    - security
    - performance
    - style
  optional-agents:
    - architecture
    - accessibility
    - i18n

  thresholds:
    security: block      # Block merge on security issues
    performance: warn    # Warn on performance issues
    style: suggest       # Suggest style improvements

  rules:
    security:
      - no-eval
      - no-hardcoded-secrets
      - proper-auth-checks
      - validate-input
    performance:
      - no-n-plus-one
      - efficient-queries
      - proper-caching
      - optimize-loops
    architecture:
      - max-coupling: 5
      - min-cohesion: 0.7
      - follow-patterns
      - avoid-circular-deps
```

## Custom Triggers

```javascript
{
  "triggers": {
    "high-risk-files": {
      "paths": ["**/auth/**", "**/payment/**", "**/admin/**"],
      "agents": ["security", "architecture"],
      "depth": "comprehensive",
      "require-approval": true
    },
    "performance-critical": {
      "paths": ["**/api/**", "**/database/**", "**/cache/**"],
      "agents": ["performance", "database"],
      "benchmarks": true,
      "regression-threshold": "5%"
    },
    "ui-changes": {
      "paths": ["**/components/**", "**/styles/**", "**/pages/**"],
      "agents": ["accessibility", "style", "i18n"],
      "visual-tests": true,
      "responsive-check": true
    }
  }
}
```

## `.github/workflows/auto-review.yml`

```yaml
name: Automated Code Review
on:
  pull_request:
    types: [opened, synchronize]
  issue_comment:
    types: [created]

jobs:
  swarm-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup GitHub CLI
        run: echo "${{ secrets.GITHUB_TOKEN }}" | gh auth login --with-token

      - name: Run Review Swarm
        run: |
          PR_NUM=${{ github.event.pull_request.number }}
          PR_DATA=$(gh pr view "$PR_NUM" --json files,title,body,labels)
          PR_DIFF=$(gh pr diff "$PR_NUM")

          REVIEW_OUTPUT=$(npx ruv-swarm github review-all \
            --pr "$PR_NUM" \
            --pr-data "$PR_DATA" \
            --diff "$PR_DIFF" \
            --agents "security,performance,style,architecture")

          echo "$REVIEW_OUTPUT" | gh pr review "$PR_NUM" --comment -F -

          if echo "$REVIEW_OUTPUT" | grep -q "approved"; then
            gh pr review "$PR_NUM" --approve
          elif echo "$REVIEW_OUTPUT" | grep -q "changes-requested"; then
            gh pr review "$PR_NUM" --request-changes -b "See review comments above"
          fi

      - name: Update Labels
        run: |
          if echo "$REVIEW_OUTPUT" | grep -q "security"; then
            gh pr edit "$PR_NUM" --add-label "security-review"
          fi
          if echo "$REVIEW_OUTPUT" | grep -q "performance"; then
            gh pr edit "$PR_NUM" --add-label "performance-review"
          fi
```

## CI/CD Integration

```yaml
# .github/workflows/build-and-review.yml
name: Build and Review
on: [pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install
      - run: npm test
      - run: npm run build

  swarm-review:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Run Swarm Review
        run: |
          npx ruv-swarm github review-all \
            --pr ${{ github.event.pull_request.number }} \
            --include-build-results
```

## PR Description Template

For repos that want every PR to declare its review intent up-front, drop this template at `.github/pull_request_template.md`. The swarm reads `Topology`, `Max Agents`, and `Review Focus Areas` directly from the PR body.

```markdown
<!-- .github/pull_request_template.md -->
## Swarm Configuration
- Topology: [mesh/hierarchical/ring/star]
- Max Agents: [number]
- Auto-spawn: [yes/no]
- Priority: [high/medium/low]

## Tasks for Swarm
- [ ] Task 1 description
- [ ] Task 2 description
- [ ] Task 3 description

## Review Focus Areas
- [ ] Security review
- [ ] Performance analysis
- [ ] Architecture validation
- [ ] Accessibility check
```

## Auto-Merge When Ready

```bash
SWARM_STATUS=$(npx ruv-swarm github pr-status 123)

if [[ "$SWARM_STATUS" == "complete" ]]; then
  REVIEWS=$(gh pr view 123 --json reviews --jq '.reviews | length')
  if [[ $REVIEWS -ge 2 ]]; then
    gh pr merge 123 --auto --squash
  fi
fi
```
