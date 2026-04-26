# Issue Management & Triage

## Single Issue with Swarm Coordination

```javascript
// Initialize issue management swarm
mcp__claude-flow__swarm_init { topology: "star", maxAgents: 3 }
mcp__claude-flow__agent_spawn { type: "coordinator", name: "Issue Coordinator" }
mcp__claude-flow__agent_spawn { type: "researcher",  name: "Requirements Analyst" }
mcp__claude-flow__agent_spawn { type: "coder",       name: "Implementation Planner" }

mcp__github__create_issue {
  owner: "org",
  repo: "repository",
  title: "Integration Review: Complete system integration",
  body: `## Integration Review

  ### Overview
  Comprehensive review and integration between components.

  ### Objectives
  - [ ] Verify dependencies and imports
  - [ ] Ensure API integration
  - [ ] Check hook system integration
  - [ ] Validate data systems alignment`,
  labels: ["integration", "review", "enhancement"],
  assignees: ["username"]
}

mcp__claude-flow__task_orchestrate {
  task: "Monitor and coordinate issue progress with automated updates",
  strategy: "adaptive",
  priority: "medium"
}
```

## Batch Issue Creation

```bash
gh issue create --title "Feature: Advanced GitHub Integration" \
  --body "Implement comprehensive GitHub workflow automation..." \
  --label "feature,github,high-priority"

gh issue create --title "Bug: Merge conflicts in integration branch" \
  --body "Resolve merge conflicts..." \
  --label "bug,integration,urgent"

gh issue create --title "Documentation: Update integration guides" \
  --body "Update all documentation..." \
  --label "documentation,integration"
```

## Issue → Swarm Conversion

```bash
ISSUE_DATA=$(gh issue view 456 --json title,body,labels,assignees,comments)

npx ruv-swarm github issue-to-swarm 456 \
  --issue-data "$ISSUE_DATA" \
  --auto-decompose \
  --assign-agents

# Batch
ISSUES=$(gh issue list --label "swarm-ready" --json number,title,body,labels)
npx ruv-swarm github issues-batch --issues "$ISSUES" --parallel

echo "$ISSUES" | jq -r '.[].number' | while read -r num; do
  gh issue edit "$num" --add-label "swarm-processing"
done
```

### Issue Comment Commands

```markdown
/swarm analyze
/swarm decompose 5
/swarm assign @agent-coder
/swarm estimate
/swarm start
```

## Auto-Triage

`.github/swarm-labels.json`:

```json
{
  "rules": [
    { "keywords": ["bug", "error", "broken"],
      "labels": ["bug", "swarm-debugger"],
      "agents": ["debugger", "tester"] },
    { "keywords": ["feature", "implement", "add"],
      "labels": ["enhancement", "swarm-feature"],
      "agents": ["architect", "coder", "tester"] },
    { "keywords": ["slow", "performance", "optimize"],
      "labels": ["performance", "swarm-optimizer"],
      "agents": ["analyst", "optimizer"] }
  ]
}
```

```bash
npx ruv-swarm github triage --unlabeled --analyze-content --suggest-labels --assign-priority
npx ruv-swarm github find-duplicates --threshold 0.8 --link-related --close-duplicates
```

## Decomposition & Progress

```bash
ISSUE_BODY=$(gh issue view 456 --json body --jq '.body')

SUBTASKS=$(npx ruv-swarm github issue-decompose 456 \
  --body "$ISSUE_BODY" \
  --max-subtasks 10 \
  --assign-priorities)

CHECKLIST=$(echo "$SUBTASKS" | jq -r '.tasks[] | "- [ ] " + .description')
UPDATED_BODY="$ISSUE_BODY

## Subtasks
$CHECKLIST"

gh issue edit 456 --body "$UPDATED_BODY"

# Spawn linked sub-issues for high-priority items
echo "$SUBTASKS" | jq -c '.tasks[] | select(.priority == "high")' | while read -r task; do
  TITLE=$(echo "$task" | jq -r '.title')
  BODY=$(echo "$task" | jq -r '.description')
  gh issue create --title "$TITLE" --body "$BODY

Parent issue: #456" --label "subtask"
done
```

### Automated Progress Updates

```bash
CURRENT=$(gh issue view 456 --json body,labels)
PROGRESS=$(npx ruv-swarm github issue-progress 456)

UPDATED_BODY=$(echo "$CURRENT" | jq -r '.body' \
  | npx ruv-swarm github update-checklist --progress "$PROGRESS")

gh issue edit 456 --body "$UPDATED_BODY"

SUMMARY=$(echo "$PROGRESS" | jq -r '
"## Progress Update

**Completion**: \(.completion)%
**ETA**: \(.eta)

### Completed
\(.completed | map("- " + .) | join("\n"))

### In Progress
\(.in_progress | map("- " + .) | join("\n"))

### Remaining
\(.remaining | map("- " + .) | join("\n"))"')

gh issue comment 456 --body "$SUMMARY"

if [[ $(echo "$PROGRESS" | jq -r '.completion') -eq 100 ]]; then
  gh issue edit 456 --add-label "ready-for-review" --remove-label "in-progress"
fi
```

## Stale Issue Management

```bash
STALE_DATE=$(date -d '30 days ago' --iso-8601)
STALE_ISSUES=$(gh issue list --state open --json number,title,updatedAt,labels \
  --jq ".[] | select(.updatedAt < \"$STALE_DATE\")")

echo "$STALE_ISSUES" | jq -r '.number' | while read -r num; do
  ISSUE=$(gh issue view "$num" --json title,body,comments,labels)
  ACTION=$(npx ruv-swarm github analyze-stale --issue "$ISSUE" --suggest-action)

  case "$ACTION" in
    close)
      gh issue comment "$num" --body "Inactive for 30 days; closing in 7 days without further activity."
      gh issue edit "$num" --add-label "stale"
      ;;
    keep)
      gh issue edit "$num" --remove-label "stale" 2>/dev/null || true
      ;;
    needs-info)
      gh issue comment "$num" --body "More information needed; may be closed as stale otherwise."
      gh issue edit "$num" --add-label "needs-info"
      ;;
  esac
done

# Hard-close after 37 days
gh issue list --label stale --state open --json number,updatedAt \
  --jq ".[] | select(.updatedAt < \"$(date -d '37 days ago' --iso-8601)\") | .number" \
  | while read -r num; do
      gh issue close "$num" --comment "Closing due to inactivity. Reopen if still relevant."
    done
```
