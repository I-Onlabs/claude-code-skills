# Advanced Coordination

## Multi-Board Synchronisation

```bash
npx ruv-swarm github multi-board-sync \
  --boards "Development,QA,Release" \
  --sync-rules '{
    "Development->QA": "when:ready-for-test",
    "QA->Release":     "when:tests-pass"
  }'

npx ruv-swarm github cross-org-sync \
  --source "org1/Project-A" \
  --target "org2/Project-B" \
  --field-mapping "custom" \
  --conflict-resolution "source-wins"
```

## Issue Dependencies & Epics

```bash
npx ruv-swarm github issue-deps 456 \
  --resolve-order \
  --parallel-safe \
  --update-blocking

npx ruv-swarm github epic-swarm \
  --epic 123 \
  --child-issues "456,457,458" \
  --orchestrate
```

## Cross-Repository Coordination

```bash
npx ruv-swarm github cross-repo \
  --issue "org/repo#456" \
  --related "org/other-repo#123" \
  --coordinate
```

## Team Collaboration

### Work Distribution

```bash
npx ruv-swarm github board-distribute \
  --strategy "skills-based" \
  --balance-workload \
  --respect-preferences \
  --notify-assignments
```

### Standup Automation

```bash
npx ruv-swarm github standup-report \
  --team "frontend" \
  --include "yesterday,today,blockers" \
  --format "slack" \
  --schedule "daily-9am"
```

### Review Coordination

```bash
npx ruv-swarm github review-coordinate \
  --board "Code Review" \
  --assign-reviewers \
  --track-feedback \
  --ensure-coverage
```

## Topology Selection Guide

| Scenario | Topology | Why |
|---|---|---|
| Sequential dependencies (Epic → child issues) | hierarchical | Clear parent / child reporting |
| Independent parallel work (3+ unrelated issues) | mesh | Agents share findings without bottleneck |
| Single-coordinator triage / standup | star | One hub aggregates from many spokes |
| Pipeline (issue → review → release) | ring | Hand-off between fixed stages |
