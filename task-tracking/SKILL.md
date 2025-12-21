---
description: Automatic todo list creation and tracking for complex tasks. Activates when tasks have 3+ steps, user provides multiple items, or work requires careful planning. Ensures progress visibility and prevents forgotten steps.
triggers:
  - complex task
  - multiple steps
  - build feature
  - implement
  - create system
  - refactor
  - numbered list
  - several things
  - todo
  - track progress
---

# Task Tracking Skill

## Purpose

Ensure Claude proactively uses TodoWrite for complex tasks, maintaining visible progress and preventing forgotten steps.

## When to Activate (Automatic)

**ALWAYS create a todo list when:**

1. **Complex Tasks** - 3+ distinct steps or actions required
2. **Multi-Item Requests** - User provides numbered/comma-separated lists
3. **Feature Implementation** - Building new functionality
4. **Refactoring** - Code restructuring affecting multiple files
5. **Bug Fixing** - When investigation + fix + verification needed
6. **System Changes** - Infrastructure, config, or architectural work

**Skip todo lists for:**
- Single-line fixes (typos, obvious bugs)
- Pure questions/explanations
- Tasks completable in <3 trivial steps

## Task State Management

```
┌─────────────┐     ┌──────────────┐     ┌───────────────┐
│   pending   │ ──► │ in_progress  │ ──► │   completed   │
└─────────────┘     └──────────────┘     └───────────────┘
                           │
                           ▼ (if blocked)
                    Create new task for blocker
```

### Rules

1. **One in_progress at a time** - Focus on single task
2. **Mark complete IMMEDIATELY** - Don't batch completions
3. **Never mark incomplete work done** - Keep in_progress if blocked
4. **Create blockers as new tasks** - When stuck, add investigation task

## Todo List Format

Each todo item requires TWO forms:

```json
{
  "content": "Implement user authentication",      // Imperative (what to do)
  "activeForm": "Implementing user authentication", // Present continuous (doing)
  "status": "pending"
}
```

## Workflow Pattern

### 1. Task Reception
When receiving a complex request:

```
User: "Add dark mode with persistence and system preference detection"

Claude thinks: This has 3+ steps → Create todo list
```

### 2. Immediate Planning
```
TodoWrite([
  {"content": "Add dark mode toggle component", "activeForm": "Adding dark mode toggle", "status": "pending"},
  {"content": "Implement theme context/state", "activeForm": "Implementing theme state", "status": "pending"},
  {"content": "Add system preference detection", "activeForm": "Adding system preference detection", "status": "pending"},
  {"content": "Persist theme choice to localStorage", "activeForm": "Persisting theme choice", "status": "pending"},
  {"content": "Update components to use theme", "activeForm": "Updating components", "status": "pending"}
])
```

### 3. Progress Updates
```
// Starting first task
TodoWrite([
  {"content": "Add dark mode toggle component", "activeForm": "Adding dark mode toggle", "status": "in_progress"},
  ...rest pending
])

// After completing first task
TodoWrite([
  {"content": "Add dark mode toggle component", "activeForm": "Adding dark mode toggle", "status": "completed"},
  {"content": "Implement theme context/state", "activeForm": "Implementing theme state", "status": "in_progress"},
  ...rest pending
])
```

### 4. Handling Blockers
If stuck on a task:
```
// Don't mark complete! Add blocker task
TodoWrite([
  {"content": "Investigate localStorage API issue", "activeForm": "Investigating localStorage issue", "status": "in_progress"},
  {"content": "Persist theme choice to localStorage", "activeForm": "Persisting theme choice", "status": "pending"},  // stays pending
  ...
])
```

## Completion Requirements

**Only mark completed when ALL true:**
- ✅ Implementation is complete (not partial)
- ✅ No errors or test failures
- ✅ All acceptance criteria met
- ✅ Can demonstrate/verify success

**Keep in_progress if ANY true:**
- ❌ Tests are failing
- ❌ Implementation is partial
- ❌ Encountered unresolved errors
- ❌ Missing dependencies

## Task Breakdown Guidelines

### Good Tasks (Specific & Actionable)
```
✅ "Create UserService with CRUD methods"
✅ "Add input validation for email field"
✅ "Write unit tests for authentication flow"
✅ "Fix null pointer in getUser endpoint"
```

### Bad Tasks (Vague & Unmeasurable)
```
❌ "Improve code quality"
❌ "Make it better"
❌ "Handle errors"
❌ "Do the backend stuff"
```

## Integration with Other Skills

| Situation | Skill Synergy |
|-----------|---------------|
| Bug fix | task-tracking + systematic-debugging |
| New API | task-tracking + api-design-patterns |
| Complex problem | task-tracking + escalation-reasoning |
| Claiming done | task-tracking + quality-gates |

## Examples

### Example 1: Feature Request
```
User: "Implement user registration with email verification"

→ Create todos:
1. Create registration form component
2. Add form validation (email, password strength)
3. Create registration API endpoint
4. Implement email service integration
5. Create verification token system
6. Add verification endpoint
7. Write tests for registration flow
8. Test email delivery
```

### Example 2: Bug Report
```
User: "Users can't log in after password reset"

→ Create todos:
1. Reproduce the issue locally
2. Investigate password reset flow
3. Check token generation/validation
4. Identify root cause
5. Implement fix
6. Add regression test
7. Verify fix in staging
```

### Example 3: Refactoring
```
User: "Refactor the API to use async/await instead of callbacks"

→ Create todos:
1. Identify all callback-based functions
2. Refactor auth module to async/await
3. Refactor user module to async/await
4. Refactor data module to async/await
5. Update error handling patterns
6. Run existing tests
7. Fix any failing tests
```

## Anti-Patterns to Avoid

1. **Forgetting to update status** - Always mark in_progress before starting
2. **Batching completions** - Mark done immediately, not all at end
3. **Marking blocked tasks complete** - Keep trying or add blocker task
4. **Too granular** - "Write line 1", "Write line 2" is too much
5. **Too vague** - "Do the thing" is not actionable
6. **No todos for complex work** - If 3+ steps, always create list

## Memory Integration

After completing a complex task set, consider using memory-keeper to persist:
- Patterns discovered
- Decisions made
- User preferences observed

This ensures learnings survive context compaction.
