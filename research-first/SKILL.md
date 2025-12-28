# Research-First Skill

## Description
Enforces research and validation before making significant changes to configuration files, system settings, or unfamiliar code.

## When This Activates
- Editing configuration files (settings.json, .env, hooks, etc.)
- Making changes to unfamiliar systems
- User asks to "enhance", "upgrade", "fix" something you haven't researched
- Before deleting or significantly modifying existing code

## Methodology

### STOP Before Acting
Before editing ANY configuration or system file:

1. **ASK**: Do I understand what this does?
2. **RESEARCH**: Use research-oracle agent to find best practices
3. **VALIDATE**: Use code-reviewer to check proposed changes
4. **CONFIRM**: Show user the plan before executing

### Required Steps for Config Changes

```
1. READ current config completely
2. RESEARCH community best practices (use research-oracle)
3. COMPARE current vs best practices
4. PROPOSE changes (show diff to user)
5. WAIT for approval
6. IMPLEMENT incrementally
7. VERIFY with code-reviewer
```

### Agents to Use Proactively

| Situation | Agent | Why |
|-----------|-------|-----|
| Unfamiliar system | research-oracle | Learn before touching |
| Config changes | code-reviewer | Validate before/after |
| Complex edits | error-detective | Catch issues early |
| Architecture | architectural-cognition-engine | Understand impact |

### Anti-Patterns (DON'T DO)

- Deleting large sections without understanding why they exist
- Making "simplifications" that remove functionality
- Acting on assumptions without verification
- Editing files before reading them completely
- Proposing changes without researching alternatives

### Trigger Phrases

When user says any of these, ACTIVATE THIS SKILL:
- "enhance", "upgrade", "improve", "optimize"
- "fix", "clean up", "simplify"
- "make it better", "best practice"
- Any config file editing

## Example Workflow

```
User: "Enhance the settings.local.json"

WRONG:
→ Immediately edit file based on assumptions

RIGHT:
1. Read current file completely
2. Launch research-oracle: "Research Claude Code settings best practices"
3. Wait for research results
4. Compare current config vs recommendations
5. Show user: "Based on research, here are suggested changes..."
6. Wait for approval
7. Make incremental changes
8. Verify with code-reviewer
```

## Integration with CLAUDE.md

Add to delegation rules:
```
### Before Config/System Changes (→ research-oracle FIRST)
- Any settings.json, settings.local.json edits
- Hook modifications
- System configuration changes
- When user asks to "enhance" or "upgrade"
- **ALWAYS research before modifying**
```
