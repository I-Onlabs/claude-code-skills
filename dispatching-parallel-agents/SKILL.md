---
name: dispatching-parallel-agents
description: Dispatch one focused agent per independent problem domain so investigations run concurrently. Use when facing 2+ independent tasks with no shared state — for example "spawn agents in parallel", "parallel debugging", "fan out tasks", "investigate multiple failures at once", or "distribute independent work across agents".
---

# Dispatching Parallel Agents

## Contents

- [When to Use](#when-to-use)
- [When NOT to Use](#when-not-to-use)
- [The Pattern](#the-pattern)
- [Verification](#verification)
- [References](#references)

## Overview

When you have multiple unrelated failures (different test files, different subsystems, different bugs), investigating them sequentially wastes time. Each investigation is independent and can happen in parallel.

**Core principle:** dispatch one agent per independent problem domain. Let them work concurrently.

## When to Use

- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from the others
- No shared state between investigations

## When NOT to Use

- **Related failures** — fixing one might fix others; investigate together first
- **Need full context** — understanding requires seeing the entire system
- **Exploratory debugging** — root cause is still unknown
- **Shared state** — agents would interfere (editing same files, holding same locks)

See [`references/integration-examples.md`](references/integration-examples.md) for a decision flowchart.

## The Pattern

### 1. Identify independent domains

Group failures by what's broken. If two failures sit in unrelated subsystems and fixing one cannot affect the other, they're independent domains.

### 2. Create focused agent tasks

Each agent gets:

- **Specific scope** — one test file or subsystem
- **Clear goal** — make these tests pass
- **Constraints** — don't change other code
- **Expected output** — summary of what was found and fixed

See [`references/prompt-template.md`](references/prompt-template.md) for the full template and common-mistake patterns.

### 3. Dispatch in parallel

Issue all `Task(...)` calls in a single tool batch so they run concurrently. Sequential dispatches defeat the purpose.

### 4. Review and integrate

When agents return:

- Read each summary
- Verify fixes don't conflict (did any two agents touch the same file?)
- Run the full test suite
- Integrate all changes

## Verification

Confirm success with all of:

- [ ] Every dispatched agent returned a summary (none silently failed)
- [ ] No two agents modified the same file (or if they did, the merges are intentional)
- [ ] Full test suite passes locally
- [ ] Each original failure is now green
- [ ] Spot-check at least one fix manually — agents can make systematic errors

## References

- [`references/prompt-template.md`](references/prompt-template.md) — agent prompt template, common mistakes
- [`references/integration-examples.md`](references/integration-examples.md) — full worked example, decision flowchart, dispatch syntax
