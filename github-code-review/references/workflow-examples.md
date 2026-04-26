# Workflow Examples

## Security-Critical PR

```bash
npx ruv-swarm github review-init \
  --pr 456 \
  --agents "security,authentication,audit" \
  --depth "maximum" \
  --require-security-approval \
  --penetration-test
```

## Performance-Sensitive PR

```bash
npx ruv-swarm github review-init \
  --pr 789 \
  --agents "performance,database,caching" \
  --benchmark \
  --profile \
  --load-test
```

## UI Component PR

```bash
npx ruv-swarm github review-init \
  --pr 321 \
  --agents "accessibility,style,i18n,docs" \
  --visual-regression \
  --component-tests \
  --responsive-check
```

## Feature Development PR

```bash
gh pr view 456 --json body,labels,files | \
  npx ruv-swarm github pr-init 456 \
    --topology hierarchical \
    --agents "architect,coder,tester,security" \
    --auto-assign-tasks
```

## Bug Fix PR

```bash
npx ruv-swarm github pr-init 789 \
  --topology mesh \
  --agents "debugger,analyst,tester" \
  --priority high \
  --regression-test
```

## Monitoring & Reporting

Real-time dashboard:

```bash
npx ruv-swarm github review-dashboard \
  --real-time \
  --show "agent-activity,issue-trends,fix-rates,coverage"
```

Comprehensive review report:

```bash
npx ruv-swarm github review-report \
  --format "markdown" \
  --include "summary,details,trends,recommendations" \
  --email-stakeholders \
  --export-pdf
```

PR-specific analytics:

```bash
npx ruv-swarm github pr-report 123 \
  --metrics "completion-time,agent-efficiency,token-usage,issue-density" \
  --format markdown \
  --compare-baseline
```

## Claude Code Integration Pattern

In a single message, dispatch swarm coordination, agent spawning, gh CLI, tests, and todo tracking concurrently:

```javascript
[Single Message - Parallel Execution]:
  // Initialize coordination
  mcp__claude-flow__swarm_init { topology: "hierarchical", maxAgents: 5 }
  mcp__claude-flow__agent_spawn { type: "reviewer",    name: "Senior Reviewer" }
  mcp__claude-flow__agent_spawn { type: "tester",      name: "QA Engineer" }
  mcp__claude-flow__agent_spawn { type: "coordinator", name: "Merge Coordinator" }

  // PR operations via gh CLI
  Bash("gh pr create --title 'Feature: Add authentication' --base main")
  Bash("gh pr view 54 --json files,diff")
  Bash("gh pr review 54 --approve --body 'LGTM after automated review'")

  // Validation
  Bash("npm test")
  Bash("npm run lint")
  Bash("npm run build")

  // Track progress
  TodoWrite { todos: [
    { content: "Complete code review", status: "completed", activeForm: "Completing code review" },
    { content: "Run test suite",       status: "completed", activeForm: "Running test suite" },
    { content: "Validate security",    status: "completed", activeForm: "Validating security" },
    { content: "Merge when ready",     status: "pending",   activeForm: "Merging when ready" }
  ]}
```
