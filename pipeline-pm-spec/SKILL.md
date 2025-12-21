---
name: pipeline-pm-spec
description: Product requirements to user stories pipeline stage (PM → Spec)
trigger: When user provides high-level requirements or feature requests
---

# PM Specification Pipeline Stage

**Pipeline Position:** First stage (Requirements → User Stories)
**Next Stage:** `pipeline-arch-review`

## Methodology

Transform high-level requirements into actionable user stories following INVEST principles.

### Process

1. **Requirements Gathering**
   - Ask clarifying questions about user needs
   - Identify stakeholders and success criteria
   - Document constraints and assumptions

2. **User Story Creation**
   - Follow format: "As a [role], I want [feature] so that [benefit]"
   - Apply INVEST criteria:
     - **I**ndependent: Can be developed separately
     - **N**egotiable: Details can be discussed
     - **V**aluable: Delivers user value
     - **E**stimable: Can be sized
     - **S**mall: Fits in one iteration
     - **T**estable: Has clear acceptance criteria

3. **Acceptance Criteria**
   - Given/When/Then format
   - Cover happy path and edge cases
   - Measurable and testable

4. **Prioritization**
   - Must-have / Should-have / Nice-to-have
   - Dependencies between stories
   - Risk assessment

### Output Format

```markdown
# Feature: [Feature Name]

## Overview
[Brief description of the feature and its purpose]

## User Stories

### Story 1: [Title]
**As a** [role]
**I want** [capability]
**So that** [benefit]

**Priority:** Must-have | Should-have | Nice-to-have
**Estimate:** S | M | L

**Acceptance Criteria:**
- Given [context]
  When [action]
  Then [outcome]
- Given [context]
  When [action]
  Then [outcome]

### Story 2: [Title]
[Repeat format]

## Success Metrics
- [How we'll measure success]

## Constraints
- [Technical or business constraints]

## Dependencies
- [External dependencies or prerequisites]

## Next Step
→ Use `pipeline-arch-review` to design architecture for these stories
```

### Best Practices

- **User-Centric:** Focus on user value, not implementation
- **Collaborative:** Involve stakeholders in refinement
- **Testable:** Every story must have clear pass/fail criteria
- **Incremental:** Break large features into smaller stories
- **Documented:** Capture decisions and assumptions

### Anti-Patterns to Avoid

- ❌ Technical tasks disguised as user stories
- ❌ Stories without acceptance criteria
- ❌ Vague or unmeasurable criteria
- ❌ Stories too large (>1 sprint)
- ❌ Missing "why" (benefit statement)

### Handoff to Architecture

After completing spec, suggest:
```
Use pipeline-arch-review to design the technical architecture for these user stories.
```

This ensures smooth transition to the next pipeline stage.
