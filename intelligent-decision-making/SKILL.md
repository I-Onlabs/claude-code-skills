---
name: intelligent-decision-making
description: Multi-model consensus and escalation framework for critical decisions. Activates when facing architectural choices, security decisions, or when intelligent-gate recommends escalation. Integrates with consult-llm MCP for multi-model opinions.
---

# Intelligent Decision-Making Framework

## When This Skill Activates

This skill provides methodology for making critical decisions that benefit from:
- Multiple perspectives (multi-model consensus)
- Deep reasoning (escalation tiers)
- Risk assessment (security, architecture, data)
- Audit documentation (decision trail)

## Multi-Model Consensus

For CRITICAL decisions, consult multiple models:

### Available Models via consult-llm
| Model | Strength | Cost | Use For |
|-------|----------|------|---------|
| o3 | Strongest reasoning | High | Complex logic, algorithms |
| gemini-2.5-pro | Multimodal | Medium | Visual, broad knowledge |
| deepseek-reasoner | Cost-effective | Low | Second opinion, validation |
| gpt-5.1-codex-max | Code specialist | High | Implementation details |

### Consensus Pattern
```
1. Frame question neutrally (avoid bias)
2. Query 2-3 models independently
3. Compare responses for agreement
4. Weight by model strength for domain
5. Document reasoning and sources
```

## Escalation Tiers

Integrate with existing escalation system:

```
Level 1: Standard Claude
    ↓ (if uncertain)
Level 2: /think (4K reasoning tokens)
    ↓ (if still uncertain)
Level 3: /megathink (10K reasoning tokens)
    ↓ (if blocked)
Level 4: /ultrathink (32K reasoning tokens)
    ↓ (if critical)
Level 5: Multi-model consultation
```

## Decision Types Requiring This Skill

### Architecture Decisions
- Technology stack choices
- Database schema changes
- API contract modifications
- Service boundaries

### Security Decisions
- Authentication implementation
- Authorization rules
- Secret management
- Input validation

### Data Decisions
- Migration strategies
- Backup policies
- Retention rules
- Privacy compliance

### Operational Decisions
- Deployment strategies
- Scaling approaches
- Monitoring setup
- Incident response

## Decision Documentation

Always document decisions with:

```markdown
## Decision: [Brief Title]

**Date**: YYYY-MM-DD
**Risk Level**: low/medium/high/critical
**Models Consulted**: [list]

### Context
What situation prompted this decision?

### Options Considered
1. Option A: [description]
   - Pros: ...
   - Cons: ...
2. Option B: [description]
   - Pros: ...
   - Cons: ...

### Decision
Which option was chosen and why?

### Reasoning
Full explanation of decision process.

### Risks & Mitigations
What could go wrong and how to handle it?

### Follow-up Actions
What needs to happen next?
```

## Integration Points

### With intelligent-gate Skill
When intelligent-gate determines CRITICAL risk:
1. Gate recommends escalation
2. This skill activates
3. Multi-model consultation begins
4. Decision documented in audit trail

### With consult-llm MCP
```python
# Query multiple models for consensus
mcp__consult_llm__consult_llm(
    prompt="Analyze the security implications of...",
    model="o3",
    files=["src/auth/"]
)
```

### With Audit System
All decisions logged to:
- `~/.claude/logs/decision-audit.jsonl` (structured)
- Conversation context (in-session)

## Best Practices

1. **Ask neutral questions** - Don't bias the analysis
2. **Provide full context** - Include relevant files
3. **Compare independently** - Don't share model responses
4. **Weight appropriately** - Some models are better for certain domains
5. **Document always** - Future you will thank you
6. **Time-box decisions** - Don't overthink routine choices
