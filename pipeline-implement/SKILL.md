---
name: pipeline-implement
description: TDD-driven implementation pipeline stage (Design → Code)
trigger: After architecture review, when ready to code
---

# Implementation Pipeline Stage

**Pipeline Position:** Third stage (Design → Code)
**Previous Stage:** `pipeline-arch-review`
**Next Stage:** `pipeline-test-verify`

## Methodology

Implement architecture using Test-Driven Development (TDD) and best practices.

### Process (RED-GREEN-REFACTOR)

1. **RED: Write Failing Test First**
   - Read architecture design and acceptance criteria
   - Write test for smallest behavior unit
   - Run test (should fail)
   - Verify test fails for right reason

2. **GREEN: Implement Minimum Code**
   - Write simplest code to make test pass
   - No premature optimization
   - No extra features
   - Run test (should pass)

3. **REFACTOR: Improve Code Quality**
   - Clean up duplication
   - Improve names and structure
   - Optimize if needed
   - Run tests (should still pass)

4. **REPEAT: Next Behavior**
   - Pick next acceptance criterion
   - Write failing test
   - Implement → Refactor
   - Continue until feature complete

### Implementation Checklist

**Before Writing Code:**
- [ ] Read architecture design (ADR)
- [ ] Review acceptance criteria
- [ ] Identify first testable behavior
- [ ] Check existing patterns in codebase

**During Implementation:**
- [ ] Write test first (RED)
- [ ] Implement minimal code (GREEN)
- [ ] Refactor for quality
- [ ] Run full test suite
- [ ] Add integration tests for critical paths
- [ ] Handle error cases
- [ ] Add logging/observability

**After Implementation:**
- [ ] All tests pass
- [ ] Code coverage >80% on new code
- [ ] No hardcoded values (use config)
- [ ] Documentation updated
- [ ] Migration scripts created (if DB changes)

### Code Quality Standards

**Functions:**
- Single responsibility
- < 50 lines
- < 4 parameters
- Pure when possible (no side effects)

**Naming:**
- Descriptive, searchable names
- Verbs for functions (`getUserById`)
- Nouns for variables/classes (`user`)
- Constants in UPPER_CASE

**Error Handling:**
- Validate inputs
- Fail fast with clear messages
- Don't swallow exceptions
- Use domain-specific errors

**Performance:**
- No premature optimization
- Profile before optimizing
- O(n) or better for critical paths
- Cache strategically

### Output Format

```markdown
## Implementation Summary: [Feature Name]

### Files Created/Modified
- `src/module/feature.ts` - [Purpose]
- `tests/module/feature.test.ts` - [Test coverage]
- `src/types/feature.ts` - [Type definitions]

### Test Coverage
**Unit Tests:** X/Y behaviors covered (Z%)
**Integration Tests:** X critical paths tested
**Edge Cases:** [List edge cases covered]

### Implementation Details

#### Core Components
[Brief description of main implementations]

#### Test Results
```bash
✓ All tests passing (XX tests, XX assertions)
✓ Coverage: XX% statements, XX% branches
```

#### API Surface
```typescript
// Public interfaces implemented
export interface ...
```

### Security Considerations Addressed
- [Input validation implemented]
- [Authentication checks added]
- [Secrets management]

### Performance Notes
- [Any performance considerations]
- [Optimization decisions]

### Known Limitations
- [Acknowledged edge cases or future work]

### Next Step
→ Use `pipeline-test-verify` for comprehensive testing
```

### TDD Best Practices

- **Test Names:** Describe behavior, not implementation
  - Good: `test_user_login_fails_with_invalid_password`
  - Bad: `test_check_password_method`

- **Arrange-Act-Assert:** Structure every test clearly
```python
def test_behavior():
    # Arrange: Set up test data
    user = User(email="test@example.com")

    # Act: Execute behavior
    result = user.validate_email()

    # Assert: Verify outcome
    assert result is True
```

- **No Mocks in TDD:** Test real behavior when possible
  - Mock external services (APIs, DB) only
  - Don't mock internal code
  - Favor integration tests

- **Red-Green-Refactor Cycle:** Never skip RED
  - Watch test fail first
  - Ensures test actually tests something
  - Prevents false positives

### Anti-Patterns to Avoid

- ❌ Writing code before tests
- ❌ Testing implementation details
- ❌ Over-mocking (mocking everything)
- ❌ Large test files (split by module)
- ❌ Skipping refactor step
- ❌ Premature abstraction

### Integration with Agents

**Automatically delegate:**
- Python code → `python-pro` agent
- Backend API → `backend-developer` agent
- Frontend → `frontend-expert` agent
- Database → `database-architect` agent

### Handoff to Testing

After implementation complete, suggest:
```
Use pipeline-test-verify for comprehensive testing and quality checks.
```
