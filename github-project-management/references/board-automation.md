# Project Board Automation

## Initialise Board & Connect Swarm

```bash
PROJECT_ID=$(gh project list --owner @me --format json | \
  jq -r '.projects[] | select(.title == "Development Board") | .id')

npx ruv-swarm github board-init \
  --project-id "$PROJECT_ID" \
  --sync-mode "bidirectional" \
  --create-views "swarm-status,agent-workload,priority"

gh project field-create "$PROJECT_ID" --owner @me \
  --name "Swarm Status" \
  --data-type "SINGLE_SELECT" \
  --single-select-options "pending,in_progress,completed"
```

## `.github/board-sync.yml`

```yaml
version: 1
project:
  name: "AI Development Board"
  number: 1

mapping:
  status:
    pending:     "Backlog"
    assigned:    "Ready"
    in_progress: "In Progress"
    review:      "Review"
    completed:   "Done"
    blocked:     "Blocked"

  agents:
    coder:     "Development"
    tester:    "Testing"
    analyst:   "Analysis"
    designer:  "Design"
    architect: "Architecture"

  priority:
    critical: "Critical"
    high:     "High"
    medium:   "Medium"
    low:      "Low"

  fields:
    - name: "Agent Count"
      type: number
      source: task.agents.length
    - name: "Complexity"
      type: select
      source: task.complexity
    - name: "ETA"
      type: date
      source: task.estimatedCompletion
```

## Real-Time Sync

```bash
npx ruv-swarm github board-sync \
  --map-status '{
    "todo":        "To Do",
    "in_progress": "In Progress",
    "review":      "Review",
    "done":        "Done"
  }' \
  --auto-move-cards \
  --update-metadata

npx ruv-swarm github board-realtime \
  --webhook-endpoint "https://api.example.com/github-sync" \
  --update-frequency "immediate" \
  --batch-updates false
```

## Issues → Project Cards

```bash
ISSUES=$(gh issue list --label "enhancement" --json number,title,body)

echo "$ISSUES" | jq -r '.[].number' | while read -r issue; do
  gh project item-add "$PROJECT_ID" --owner @me \
    --url "https://github.com/$GITHUB_REPOSITORY/issues/$issue"
done

npx ruv-swarm github board-import-issues \
  --issues "$ISSUES" \
  --add-to-column "Backlog" \
  --parse-checklist \
  --assign-agents
```

## Smart Card Management

```bash
# Auto-assign by load and expertise
npx ruv-swarm github board-auto-assign \
  --strategy "load-balanced" \
  --consider "expertise,workload,availability" \
  --update-cards

# Rule-based card transitions
npx ruv-swarm github board-smart-move \
  --rules '{
    "auto-progress": "when:all-subtasks-done",
    "auto-review":   "when:tests-pass",
    "auto-done":     "when:pr-merged"
  }'

# Bulk operations
npx ruv-swarm github board-bulk \
  --filter "status:blocked" \
  --action "add-label:needs-attention" \
  --notify-assignees
```

## Custom Views

```javascript
{
  "views": [
    { "name": "Swarm Overview",  "type": "board",   "groupBy": "status",         "filters": ["is:open"], "sort": "priority:desc" },
    { "name": "Agent Workload",  "type": "table",   "groupBy": "assignedAgent",  "columns": ["title","status","priority","eta"], "sort": "eta:asc" },
    { "name": "Sprint Progress", "type": "roadmap", "dateField": "eta",          "groupBy": "milestone" }
  ]
}
```

## Dashboard Widgets

```javascript
{
  "dashboard": {
    "widgets": [
      { "type": "chart",   "title": "Task Completion Rate", "data": "completed-per-day",   "visualization": "line" },
      { "type": "gauge",   "title": "Sprint Progress",      "data": "sprint-completion",   "target": 100 },
      { "type": "heatmap", "title": "Agent Activity",       "data": "agent-tasks-per-day" }
    ]
  }
}
```
