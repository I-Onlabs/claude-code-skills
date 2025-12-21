---
name: intelligent-gate
description: Decision-making framework for risky operations. Activates when PreToolUse hook triggers on potentially dangerous commands. Provides methodology for AUDIT → ASSESS → RESEARCH → THINK → DECIDE → ACT workflow.
---

# Intelligent Gate Decision Framework

## When This Skill Activates

This skill provides the decision-making methodology when the PreToolUse hook detects potentially risky operations:
- Destructive commands (rm, delete, reset)
- System modifications (chmod, chown, sudo)
- Sensitive file access (.env, credentials, secrets)
- Configuration changes (package.json, requirements.txt)

## Decision Framework

```
TRIGGER: Risky operation detected by hook
    ↓
AUDIT: What exactly is being attempted?
    ↓
ASSESS: What is the risk level? (low/medium/high/critical)
    ↓
RESEARCH: Check context, constraints, past decisions
    ↓
THINK: Apply escalation reasoning if needed
    ↓
DECIDE: Allow / Modify / Escalate / Deny
    ↓
ACT: Execute with full reasoning logged
```

## Risk Categories

| Level | Examples | Action |
|-------|----------|--------|
| LOW | Read, ls, pwd, grep | Allow silently |
| MEDIUM | Write to project files | Log and allow |
| HIGH | rm -r, chmod, git reset | Audit + Think + Decide |
| CRITICAL | rm -rf /, sudo, .env | Multi-model consultation |

## Audit Questions

When AUDIT phase triggers, ask:
1. **What** is the exact operation being attempted?
2. **Why** is this operation being requested?
3. **Where** will this operation have effect?
4. **What** are the potential consequences?
5. **Is there** a safer alternative?

## Assessment Criteria

### HIGH Risk Indicators
- Recursive deletion (`rm -rf`, `rm -r`)
- Force flags (`-f`, `--force`)
- System paths (`/etc`, `/usr`, `/bin`)
- Root operations (`sudo`, `su`)
- Credential files (`.env`, `secrets`, `credentials`)

### CRITICAL Risk Indicators
- Root filesystem operations (`rm -rf /`)
- Disk formatting (`mkfs`, `dd`)
- Security bypasses (`chmod 777`, `--no-verify`)
- Piping untrusted content to shell (`curl | sh`)

## Escalation Integration

When risk is HIGH or CRITICAL:
1. **First**: Use `/think` to reason through implications
2. **If uncertain**: Use `/megathink` for deeper analysis
3. **For CRITICAL**: Use `/ultrathink` or `consult-llm`
4. **Always**: Log decision with full reasoning

## Output Format

The intelligent gate returns structured decisions:

```json
{
  "decision": "allow|modify|escalate|deny",
  "risk_level": "low|medium|high|critical",
  "reasoning": "Full explanation of decision process",
  "audit_trail": "What was checked and found",
  "alternative": "Safer alternative if available"
}
```

## Integration with Hooks

This skill provides the methodology that the `intelligent_gate.py` hook implements. The hook:
1. Detects risky patterns
2. Assesses risk level
3. Makes decision based on this framework
4. Logs to `~/.claude/logs/decision-audit.jsonl`
5. Returns decision to Claude

## Best Practices

1. **Never block silently** - Always provide reasoning
2. **Suggest alternatives** - Don't just deny, help find safer paths
3. **Log everything** - Audit trail enables learning
4. **Escalate appropriately** - Use thinking levels for uncertainty
5. **Trust but verify** - Most operations are safe, focus on exceptions
