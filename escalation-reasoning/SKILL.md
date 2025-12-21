---
name: escalation-reasoning
description: Use when stuck on hard problems, need deeper reasoning, standard approaches fail, or facing architecture decisions. Implements 5-tier escalation from standard reasoning to external expert models.
---

# Escalation-Aware Reasoning

## When This Skill Activates
- Stuck on a problem after 2+ attempts
- Architecture or design decisions needed
- Novel algorithms or complex logic
- Security-critical code review
- User explicitly asks to "think harder"

## The 5-Tier Escalation System

| Tier | Method | Reasoning Depth | Best For |
|------|--------|-----------------|----------|
| 1 | Standard | Default | Routine tasks, simple fixes |
| 2 | `/think` | 4K tokens | Debugging, code reviews |
| 3 | `/megathink` | 10K tokens | Architecture decisions |
| 4 | `/ultrathink` | 32K tokens | Hard problems, novel approaches |
| 5 | External | Expert models | True blockers, breakthroughs |

## Auto-Escalation Triggers

### Escalate to Tier 2 (`/think`)
- First debugging attempt failed
- Code review needed
- Comparing implementation options

### Escalate to Tier 3 (`/megathink`)
- Architecture decisions
- Database schema design
- API design trade-offs
- Multi-component interactions

### Escalate to Tier 4 (`/ultrathink`)
- 2+ failed attempts at same problem
- Security-critical analysis
- Performance optimization
- Complex algorithm design

### Escalate to Tier 5 (External)
- Truly blocked after tier 4
- Need second opinion
- Novel research-level problems
- Critical production issues

## External Model Options (Tier 5)

| Model | Strength | Cost | Best For |
|-------|----------|------|----------|
| o3 | Reasoning | $$$$ | Hard math/logic |
| Gemini 2.5 Pro | Context | $$$ | Large codebases |
| DeepSeek-R1 | Value | $ | Cost-effective reasoning |
| Codex | Code | $$ | Pure implementation |

## Cost Awareness

**DeepSeek is 97% cheaper** than equivalent Claude reasoning.

Before escalating, ask:
1. Have I tried simpler approaches?
2. Is the cost justified by the problem?
3. Can I break this into smaller problems?

## How to Escalate

```
# Tier 2
/think: [your question]

# Tier 3
/megathink: [your question]

# Tier 4
/ultrathink: [your question]

# Tier 5 - Use consult-llm tool
Consult o3 about: [your question]
```

## Anti-Patterns

- Jumping to tier 4 for simple problems (wasteful)
- Not escalating after repeated failures (stubborn)
- Using external models for routine tasks (expensive)
- Skipping intermediate tiers (miss simpler solutions)
