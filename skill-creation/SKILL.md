---
name: skill-creation
description: Use when creating new skills, agents, or improving existing ones. Provides the 10-step systematic process for high-quality skill development.
---

# Skill Creation Methodology

## When This Skill Activates

- Creating a new Claude Code skill or agent
- "How do I make a skill for X?"
- "Create a skill that does Y"
- Systematizing a repetitive workflow
- Improving existing skills

## The 10-Step Process

| Step | Name | Output |
|------|------|--------|
| 1 | UNDERSTAND | Problem statement (1-2 paragraphs) |
| 2 | EXPLORE | 3-5 failure modes without guidance |
| 3 | RESEARCH | Notes with sources |
| 4 | SYNTHESIZE | 5-10 core principles |
| 5 | DRAFT | First SKILL.md |
| 6 | SELF-CRITIQUE | Gap list |
| 7 | ITERATE | Improved draft |
| 8 | TEST | Before/after comparison |
| 9 | FINALIZE | Production-ready file |
| 10 | DOCUMENT | Ecosystem integration |

## Quick Start Template

```yaml
---
name: <skill-name>
description: <When to activate - be precise!>
---

# <Skill Name>

## When This Skill Activates
- <Trigger condition 1>
- <Trigger condition 2>

## Methodology

### Step 1: <First Step>
<What to do>

### Step 2: <Second Step>
<What to do>

## Examples

<Concrete examples>

## Quality Checklist
- [ ] Criteria 1
- [ ] Criteria 2
```

## Quality Checklist

Every skill MUST:
- [ ] Address documented failure modes
- [ ] Be actionable, not theoretical
- [ ] Have concrete examples
- [ ] Have precise trigger conditions
- [ ] Integrate with relevant agents

## Skill vs Agent Decision

| Need | Solution |
|------|----------|
| Methodology guidance | Skill |
| Autonomous execution | Agent |
| Both | Skill + Agent pair |

## File Locations

```
~/.claude/skills/<name>/SKILL.md    # Skill file
~/.claude/agents/<name>.md          # Agent file
```

## Integration

**Agent:** skill-architect (for autonomous execution of this methodology)

**Delegate to skill-architect when:**
- Complex skill requiring deep research
- Full 10-step process needed
- User wants hands-off skill creation
