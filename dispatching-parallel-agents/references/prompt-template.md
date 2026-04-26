# Agent Prompt Template

Good agent prompts are:

1. **Focused** — one clear problem domain
2. **Self-contained** — all context needed to understand the problem
3. **Specific about output** — define what the agent must return

## Template

```markdown
Fix the [N] failing tests in [path/to/file]:

1. "[test name]" — [observed failure]
2. "[test name]" — [observed failure]
3. "[test name]" — [observed failure]

These are [hypothesized failure category, e.g. timing/race condition issues].

Your task:

1. Read the test file and understand what each test verifies
2. Identify root cause — [hypothesis A] or [hypothesis B]?
3. Fix by:
   - [Specific approach #1, e.g. event-based waiting instead of timeouts]
   - [Specific approach #2]
   - [Specific approach #3]

Do NOT [common shortcut to forbid, e.g. just increase timeouts] — find the real issue.

Return: summary of root cause and changes made.
```

## Common Mistakes

| Don't | Do |
|---|---|
| "Fix all the tests" (too broad) | "Fix `agent-tool-abort.test.ts`" (focused scope) |
| "Fix the race condition" (no context) | Paste error messages and test names |
| (no constraints — agent might refactor everything) | "Do NOT change production code" or "Fix tests only" |
| "Fix it" (vague output) | "Return summary of root cause and changes" |
