---
name: quality-gates
description: Use before claiming any task complete. Enforces verification steps, test execution, and proof of success. Prevents premature completion claims and ensures work is actually done.
---

# Quality Gates Before Completion

## Iron Rule

**NEVER claim completion without evidence.**

This skill activates before ANY "done", "complete", "finished", or "ready" statement.

## When This Skill Activates
- About to say "done" or "complete"
- Task appears finished
- User asks "is this done?"
- Before creating a PR
- Before merging code

## Mandatory Quality Checks

### 1. Tests Pass
```bash
# Run relevant tests
pytest tests/
npm test
cargo test
```
**Show the output.** Don't just say "tests pass."

### 2. No Regressions
- Run the FULL test suite, not just new tests
- Existing functionality still works
- No new warnings or errors

### 3. Type Checks (if applicable)
```bash
# Python
mypy src/
pyright src/

# TypeScript
tsc --noEmit
```

### 4. Linting Clean
```bash
# Python
ruff check .

# JavaScript/TypeScript
eslint .

# Rust
cargo clippy
```

### 5. Manual Verification
Actually TEST the feature:
- Run the code
- Check the output
- Verify expected behavior

## Evidence Format

Before claiming "done", provide:

```
## Verification Evidence

### Tests
Command: pytest tests/test_feature.py -v
Result: 5 passed in 0.23s

### Type Check
Command: mypy src/
Result: Success: no issues found

### Manual Test
Action: Called API endpoint with test data
Result: Returned expected response {status: "ok"}
```

## Quick Checklist

```
[ ] Tests written and passing
[ ] Existing tests still pass
[ ] Type checks clean
[ ] Linting clean
[ ] Manually verified behavior
[ ] Showed evidence in response
```

## Integration

This skill combines with:
- `verification-before-completion` (from Superpowers)
- `test-driven-development` (ensures tests exist)
- Project-specific test commands

## Common Excuses (Don't Accept)

- "It should work" → Run it and prove it
- "Tests aren't set up" → Set them up first
- "Minor change, doesn't need tests" → It always needs verification
- "I'll add tests later" → No, add them now

## Anti-Patterns

- Claiming done without running code
- Running only new tests, not regression suite
- Ignoring linting warnings
- Saying "I tested it" without showing output
