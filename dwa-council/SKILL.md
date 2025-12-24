---
name: dwa-council
description: Debate-Weighted Aggregation council for critical multi-agent decisions. Automatically triggers for security, architectural, and high-risk operations requiring expert deliberation.
tags: [decision-making, multi-agent, voting, deliberation]
---

# DWA Council Methodology

Multi-agent deliberation system using Debate-Weighted Aggregation for critical decisions.

## When Council Convenes

Council automatically triggers for 8 conditions:

1. **Architectural Decisions** - Design choices, tech stack, migrations
2. **Security/Risk Decisions** - Auth, secrets, vulnerabilities
3. **Agent Disagreements** - Multiple conflicting approaches
4. **Quality Gate Failures** - TDD violations, linting errors
5. **Ethical Flags** - Privacy, bias, GDPR concerns
6. **Low Aggregate Confidence** - Uncertainty < 0.75
7. **External Commitments** - Deploys, API calls, publishing
8. **Novel/OOD Queries** - Unfamiliar technology decisions

## DWA Voting Formula

```
Score = Σ (Vote × Confidence × Expertise Weight)
```

Where:
- **Vote**: 1.0 for APPROVE, 0.0 for REJECT/ABSTAIN
- **Confidence**: Agent's confidence in their recommendation (0-1)
- **Expertise Weight**: Agent's domain expertise (0-1, from YAML frontmatter)

## Council Workflow

```
1. TRIGGER DETECTION
   └─> Pattern matching or risk-level check
       └─> Infer domain (security, architecture, api_design, etc.)

2. AGENT SELECTION
   └─> Query expertise registry for relevant agents
       └─> Filter by min_expertise >= 0.5
           └─> Select top N agents (default: 5)

3. PROPOSAL GENERATION
   └─> Each agent generates independent proposal
       ├─> Recommendation (what to do)
       ├─> Reasoning chain (step-by-step logic)
       ├─> Confidence score (0-1)
       └─> Domain relevance (0-1)

4. DEBATE (Optional - only if needed)
   └─> Check: Low consensus OR low confidence?
       └─> Round 1: Agents critique each other's proposals
           └─> Round 2 (if needed): Refine based on critiques

5. VOTING AGGREGATION
   └─> Each agent votes (typically for own proposal)
       └─> Apply DWA formula
           └─> Winner = highest weighted score

6. ESCALATION CHECK
   └─> Aggregate confidence < 0.7? → Escalate
   └─> Tie vote (within 5%)? → Escalate
   └─> High disagreement (HHI < 0.3)? → Escalate
       └─> Consult o3/Gemini/DeepSeek for expert opinion

7. DECISION FINALIZATION
   └─> Persist session to memory-keeper
       └─> Audit trail for compliance
           └─> Return decision to user
```

## Escalation Triggers

Council may escalate to external models (o3, Gemini, DeepSeek) when:

- **Low Confidence**: Aggregate confidence < 0.7
- **Tie Vote**: Top two proposals within 5% score
- **High Disagreement**: Herfindahl-Hirschman Index < 0.3

## Example: Security Decision

```
Trigger: "Design JWT authentication system"
Domain: security
Agents: security-auditor (1.0), code-reviewer (0.9), backend-developer (0.7)

Proposals:
  1. security-auditor: "Use RS256 with public key verification"
     - Confidence: 0.90
     - Reasoning: Asymmetric signing prevents forgery

  2. code-reviewer: "Use RS256 with public key verification"
     - Confidence: 0.85
     - Reasoning: Industry standard, better security

  3. backend-developer: "Use HS256 for simplicity"
     - Confidence: 0.70
     - Reasoning: Easier implementation

Voting (DWA):
  Proposal 1 (RS256): (0.90 × 1.0) + (0.85 × 0.9) = 1.665
  Proposal 2 (HS256): (0.70 × 0.7) = 0.490

Winner: RS256 approach (Proposal 1) with 77% confidence
Decision: "Use JWT with RS256 signing for enhanced security"
```

## Configuration

### Agent Expertise Weights

Agents declare expertise in YAML frontmatter:

```yaml
---
name: security-auditor
expertise_weights:
  security: 1.0      # Primary domain
  architecture: 0.7
  api_design: 0.5
  performance: 0.4
council_role: proposer  # proposer | reviewer | abstainer
---
```

### Hook Integration

Council hook runs after `intelligent_gate.py`:

```json
{
  "PreToolUse": [
    {"type": "command", "command": "python3 ~/.claude/hooks/intelligent_gate.py"},
    {"type": "command", "command": "python3 ~/.claude/hooks/council_hook.py"}
  ]
}
```

## Performance Characteristics

- **Token Overhead**: ~12,000 tokens for full council (5 agents + debate)
- **Latency**: 30-60 seconds (parallel proposal generation)
- **Cost Optimization**: Local Ollama models for proposals ($0), Claude Opus only for critical domains
- **Escalation Cost**: $0.016-$0.06 per external model consultation

## Audit Trail

All council sessions persisted to memory-keeper MCP:

- **Channel**: `council:sessions` - Full session data
- **Channel**: `council:audit` - Audit trail entries
- **Channel**: `council:decisions` - Decision index

Query with:
```python
from council.state_manager import list_sessions

# Recent security decisions
sessions = list_sessions(domain="security", limit=10)

# High-confidence decisions only
sessions = list_sessions(min_confidence=0.85)
```

## Phase 2 Status (Current)

✅ **Implemented:**
- Trigger detection (8 conditions)
- Expertise registry (YAML frontmatter parsing)
- Voting aggregation (DWA formula + HHI)
- Debate manager (consensus checks)
- State manager (persistence framework)
- Council hook (PreToolUse integration)

⏳ **Phase 3 TODO:**
- Actual Ollama proposal generation (currently simulated)
- External model escalation (o3/Gemini integration)
- Message bus integration
- Performance metrics

## Usage

Council convenes automatically via hook when triggers detected.

Manual convocation (for testing):

```python
from council.trigger_detector import detect_trigger
from council.orchestrator import convene_council

# Detect trigger
trigger = detect_trigger(
    tool_name="Bash",
    operation_text="Deploy authentication system to production",
    risk_level="HIGH"
)

# Convene council
if trigger:
    session = convene_council(trigger, context="Production deployment")
    print(f"Decision: {session.decision}")
    print(f"Confidence: {session.decision_confidence}")
```

## References

- **Plan**: `/Users/mac/.claude/plans/synthetic-soaring-quill.md`
- **Implementation**: `/Users/mac/.claude/council/`
- **Tests**: `/Users/mac/.claude/council/test_phase1.py`
- **Hooks**: `/Users/mac/.claude/hooks/council_hook.py`

---

**DWA Council: Making critical decisions through expert deliberation.**
