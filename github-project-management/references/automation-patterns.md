# Automation Patterns

## GitHub Actions: Issue Handler

```yaml
# .github/workflows/issue-swarm.yml
name: Issue Swarm Handler
on:
  issues:
    types: [opened, labeled, commented]

jobs:
  swarm-process:
    runs-on: ubuntu-latest
    steps:
      - name: Process Issue
        uses: ruvnet/swarm-action@v1
        with:
          command: |
            if [[ "${{ github.event.label.name }}" == "swarm-ready" ]]; then
              npx ruv-swarm github issue-init ${{ github.event.issue.number }}
            fi
```

## Board Sync Workflow

```bash
npx ruv-swarm github issue-board-sync \
  --project "Development" \
  --column-mapping '{
    "To Do":       "pending",
    "In Progress": "active",
    "Done":        "completed"
  }'
```

## Specialised Issue Strategies

### Bug investigation

```bash
npx ruv-swarm github bug-swarm 456 \
  --reproduce \
  --isolate \
  --fix \
  --test
```

### Feature implementation

```bash
npx ruv-swarm github feature-swarm 456 \
  --design \
  --implement \
  --document \
  --demo
```

### Technical debt refactoring

```bash
npx ruv-swarm github debt-swarm 456 \
  --analyze-impact \
  --plan-migration \
  --execute \
  --validate
```

## Complete Workflow Example

End-to-end: feature issue → swarm decomposition → board → automated tracking → progress monitoring.

```bash
# 1. Create feature issue with swarm coordination
gh issue create \
  --title "Feature: Real-time Collaboration" \
  --body "$(cat <<'EOF'
## Feature: Real-time Collaboration

### Overview
Implement real-time collaboration features using WebSockets.

### Objectives
- [ ] WebSocket server setup
- [ ] Client-side integration
- [ ] Presence tracking
- [ ] Conflict resolution
- [ ] Testing and documentation

### Swarm Coordination
This feature will use mesh topology for parallel development.
EOF
)" \
  --label "enhancement,swarm-ready,high-priority"

# 2. Initialise swarm and decompose tasks
ISSUE_NUM=$(gh issue list --label "swarm-ready" --limit 1 --json number --jq '.[0].number')
npx ruv-swarm github issue-init "$ISSUE_NUM" \
  --topology mesh \
  --auto-decompose \
  --assign-agents "architect,coder,tester"

# 3. Add to project board
PROJECT_ID=$(gh project list --owner @me --format json | jq -r '.projects[0].id')
gh project item-add "$PROJECT_ID" --owner @me \
  --url "https://github.com/$GITHUB_REPOSITORY/issues/$ISSUE_NUM"

# 4. Set up automated tracking
npx ruv-swarm github board-sync --auto-move-cards --update-metadata

# 5. Monitor progress
npx ruv-swarm github issue-progress "$ISSUE_NUM" \
  --auto-update-comments \
  --notify-on-completion
```

## Operational guidance

A few decisions worth making once per project, not per issue:

- **Initialise the swarm only for issues large enough to need decomposition.** A 5-line bug fix doesn't need a swarm; a multi-component epic does. The cost of swarm coordination is wasted on trivial work.
- **Use the swarm's memory store for progress coordination across long-running issues.** Don't re-derive state from issue comments on every poll — write to memory once, read many times. See the `mcp__claude-flow__task_orchestrate` calls in [`issue-management.md`](issue-management.md).
- **Validate bidirectional sync at least once after `board-init`.** Create a test card, move it on the board, confirm the linked issue picks up the new status. Sync misconfigurations silently drift state until you notice cards in the wrong column at the next standup.

## Quick Reference

```bash
# Issue management
gh issue create --title "..." --body "..." --label "..."
npx ruv-swarm github issue-init <number>
npx ruv-swarm github issue-decompose <number>
npx ruv-swarm github triage --unlabeled

# Project boards
npx ruv-swarm github board-init --project-id <id>
npx ruv-swarm github board-sync
npx ruv-swarm github board-analytics

# Sprint management
npx ruv-swarm github sprint-manage --sprint "Sprint X"
npx ruv-swarm github milestone-track --milestone "vX.X"

# Analytics
npx ruv-swarm github issue-metrics --issue <number>
npx ruv-swarm github board-kpis
```
