---
name: pipeline-arch-review
description: Architecture design and ADR creation pipeline stage (Spec → Design)
trigger: After PM spec, when technical design is needed
---

# Architecture Review Pipeline Stage

**Pipeline Position:** Second stage (Spec → Design)
**Previous Stage:** `pipeline-pm-spec`
**Next Stage:** `pipeline-implement`

## Methodology

Transform user stories into technical architecture with Architecture Decision Records (ADRs).

### Process

1. **Research Existing Patterns**
   - Read current codebase architecture
   - Identify existing patterns and conventions
   - Review similar features for consistency

2. **Design Alternatives**
   - Generate 2-3 architectural approaches
   - Evaluate tradeoffs for each
   - Consider scalability, maintainability, performance

3. **Architecture Decision Record (ADR)**
   - Document decision context
   - List alternatives considered
   - Explain chosen approach and rationale
   - Note consequences (positive and negative)

4. **Component Design**
   - Define modules/services/components
   - Specify interfaces and contracts
   - Identify data models and schemas
   - Plan error handling strategy

5. **Review Criteria**
   - Scalability: Can it handle 10x growth?
   - Security: What are the attack vectors?
   - Performance: What are the bottlenecks?
   - Maintainability: Can team understand it?
   - Testing: How will we test it?

### Output Format

```markdown
# Architecture Design: [Feature Name]

## Context
[User stories being addressed, from PM spec]

## Goals & Constraints
**Goals:**
- [What we're optimizing for]

**Constraints:**
- [Technical limitations, deadlines, resources]

## Architecture Decision Record

### Status
Proposed | Accepted | Deprecated

### Decision
[Clear statement of the architectural decision]

### Alternatives Considered

#### Option 1: [Name]
**Pros:**
- [Benefits]

**Cons:**
- [Drawbacks]

#### Option 2: [Name]
**Pros:**
- [Benefits]

**Cons:**
- [Drawbacks]

#### Option 3 (Chosen): [Name]
**Pros:**
- [Why this is best]

**Cons:**
- [Acknowledged tradeoffs]

**Rationale:**
[Why we chose this approach]

## System Design

### Components
```
[Component diagram or description]
```

### Data Models
```typescript
// Core entities
interface Entity {
  // ...
}
```

### API Contracts
```typescript
// Public interfaces
interface API {
  // ...
}
```

### Dependencies
- [External services]
- [Libraries/frameworks]
- [Infrastructure requirements]

## Security Considerations
- [Authentication/authorization approach]
- [Data encryption requirements]
- [Input validation strategy]

## Performance Considerations
- [Expected load]
- [Caching strategy]
- [Database optimization]

## Testing Strategy
- Unit: [What and how]
- Integration: [What and how]
- E2E: [Critical paths]

## Migration Plan
[If modifying existing systems]

## Rollback Strategy
[How to undo if needed]

## Consequences

**Positive:**
- [Benefits of this approach]

**Negative:**
- [Costs or limitations]

**Neutral:**
- [Changes that are neither good nor bad]

## Next Step
→ Use `pipeline-implement` to build this architecture
```

### Best Practices

- **Research First:** Read existing code before designing
- **Document Decisions:** Every significant choice needs rationale
- **Consider Alternatives:** Explore at least 2-3 options
- **Think Long-Term:** Design for change, not just current needs
- **Security By Design:** Bake security in from the start

### Anti-Patterns to Avoid

- ❌ Copy-paste architecture without understanding
- ❌ Over-engineering for hypothetical requirements
- ❌ Under-documenting key decisions
- ❌ Ignoring existing patterns (NIH syndrome)
- ❌ Missing rollback/migration plans

### Handoff to Implementation

After architecture approval, suggest:
```
Use pipeline-implement to build this architecture with TDD.
```
