# Sprint Planning & Analytics

## What gets tracked

Across the commands in this file, the skill captures:

- **Per-issue:** time-to-close, agent efficiency, subtask completion rate
- **Per-sprint:** velocity (story points / issues per sprint), burndown, blockers
- **Per-board:** average cycle time, throughput, work-in-progress counts, blocked-time percentage, first-time-pass rate
- **Per-team / per-member:** velocity, quality, collaboration signals (anonymous mode supported)
- **Cross-cutting:** integration success rates between linked PRs/issues, defect density

These are produced by `board-analytics`, `board-progress`, `board-kpis`, `team-metrics`, `issue-metrics`, and `effectiveness` — each documented below with its specific flag set.

## Sprint Management

```bash
npx ruv-swarm github sprint-manage \
  --sprint "Sprint 23" \
  --auto-populate \
  --capacity-planning \
  --track-velocity

npx ruv-swarm github milestone-track \
  --milestone "v2.0 Release" \
  --update-board \
  --show-dependencies \
  --predict-completion
```

### Agile (Scrum) Board

```bash
npx ruv-swarm github agile-board \
  --methodology "scrum" \
  --sprint-length "2w" \
  --ceremonies "planning,review,retro" \
  --metrics "velocity,burndown"
```

### Kanban Flow

```bash
npx ruv-swarm github kanban-board \
  --wip-limits '{
    "In Progress": 5,
    "Review":      3
  }' \
  --cycle-time-tracking \
  --continuous-flow
```

## Board Analytics

```bash
PROJECT_DATA=$(gh project item-list "$PROJECT_ID" --owner @me --format json)

ISSUE_METRICS=$(echo "$PROJECT_DATA" | jq -c '.items[] | select(.content.type == "Issue")' | \
  while read -r item; do
    ISSUE_NUM=$(echo "$item" | jq -r '.content.number')
    gh issue view "$ISSUE_NUM" --json createdAt,closedAt,labels,assignees
  done)

npx ruv-swarm github board-analytics \
  --project-data "$PROJECT_DATA" \
  --issue-metrics "$ISSUE_METRICS" \
  --metrics "throughput,cycle-time,wip" \
  --group-by "agent,priority,type" \
  --time-range "30d" \
  --export "dashboard"
```

## Performance Reports

```bash
npx ruv-swarm github board-progress \
  --show "burndown,velocity,cycle-time" \
  --time-period "sprint" \
  --export-metrics

npx ruv-swarm github board-report \
  --type "sprint-summary" \
  --format "markdown" \
  --include "velocity,burndown,blockers" \
  --distribute "slack,email"
```

## KPI Tracking

```bash
npx ruv-swarm github board-kpis \
  --metrics '[
    "average-cycle-time",
    "throughput-per-sprint",
    "blocked-time-percentage",
    "first-time-pass-rate"
  ]' \
  --dashboard-url

npx ruv-swarm github team-metrics \
  --board "Development" \
  --per-member \
  --include "velocity,quality,collaboration" \
  --anonymous-option
```

## Release Planning

```bash
npx ruv-swarm github release-plan-board \
  --analyze-velocity \
  --estimate-completion \
  --identify-risks \
  --optimize-scope
```

## Per-Issue Metrics

```bash
npx ruv-swarm github issue-metrics \
  --issue 456 \
  --metrics "time-to-close,agent-efficiency,subtask-completion"

npx ruv-swarm github effectiveness \
  --issues "closed:>2024-01-01" \
  --compare "with-swarm,without-swarm"
```
