---
name: pipeline-test-verify
description: Comprehensive testing and quality verification pipeline stage (Code → Verified)
trigger: After implementation, before commit/PR
---

# Test Verification Pipeline Stage

**Pipeline Position:** Fourth stage (Code → Verified)
**Previous Stage:** `pipeline-implement`
**Next Stage:** Ready for commit/PR

## Methodology

Comprehensive quality verification before considering code complete.

### Verification Layers

1. **Unit Test Verification**
   - All tests pass
   - Coverage >80% on new code
   - Edge cases covered
   - Test names describe behavior

2. **Integration Test Verification**
   - Critical paths tested end-to-end
   - External integrations tested (or mocked)
   - Error scenarios covered
   - Performance benchmarks pass

3. **Code Quality Verification**
   - Linting passes (no warnings)
   - Type checking passes (TypeScript/mypy)
   - Code complexity acceptable
   - No duplicated code

4. **Security Verification**
   - No hardcoded secrets
   - Input validation on all entry points
   - Authentication/authorization checked
   - Dependencies have no known vulnerabilities

5. **Performance Verification**
   - No obvious bottlenecks
   - Database queries optimized (no N+1)
   - Response times acceptable
   - Memory usage reasonable

6. **Documentation Verification**
   - Public APIs documented
   - Complex logic explained
   - README updated (if needed)
   - Migration guides written (if breaking)

### Verification Checklist

```markdown
## Pre-Commit Verification

### ✅ Tests
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] E2E tests pass (if applicable)
- [ ] Coverage >80% on new code
- [ ] No skipped/ignored tests

### ✅ Code Quality
- [ ] Linter passes (zero warnings)
- [ ] Type checker passes (zero errors)
- [ ] No commented-out code
- [ ] Functions < 50 lines
- [ ] Cyclomatic complexity < 10

### ✅ Security
- [ ] No secrets in code
- [ ] Input validation present
- [ ] Auth checks in place
- [ ] Dependencies scanned (npm audit / pip-audit)
- [ ] SQL uses parameterized queries

### ✅ Performance
- [ ] No N+1 queries
- [ ] Database indexes exist
- [ ] Large files streamed (not loaded in memory)
- [ ] API responses < 200ms (or justified)

### ✅ Documentation
- [ ] Public functions have docstrings
- [ ] Complex algorithms explained
- [ ] API docs updated
- [ ] CHANGELOG.md updated
- [ ] Migration guide written (if breaking)

### ✅ Architecture Alignment
- [ ] Follows ADR decisions
- [ ] Consistent with codebase patterns
- [ ] No architectural shortcuts
- [ ] Technical debt documented (if any)
```

### Automated Checks

Run these commands before declaring success:

```bash
# Testing
npm test                    # or: pytest, cargo test, etc.
npm run test:integration
npm run test:coverage

# Code Quality
npm run lint
npm run typecheck
npm run format:check

# Security
npm audit                   # or: pip-audit, cargo audit
npm run security:check

# Performance (if scripts exist)
npm run perf:check
npm run benchmark
```

### Manual Review Triggers

**Invoke code-reviewer agent if:**
- Changes touch security-critical code
- Modifying core architecture
- Large refactoring (>500 lines changed)
- Adding new dependencies
- Performance-sensitive code

**Example:**
```
Use code-reviewer agent to review these changes before commit.
```

### Output Format

```markdown
## Verification Report: [Feature Name]

### Test Results ✅
```
✓ Unit Tests: 45 passed
✓ Integration Tests: 12 passed
✓ Coverage: 87% statements, 82% branches
```

### Code Quality ✅
```
✓ Linting: 0 errors, 0 warnings
✓ Type Check: 0 errors
✓ Complexity: Max 7 (threshold: 10)
```

### Security Scan ✅
```
✓ Secrets: None found
✓ Dependencies: 0 vulnerabilities
✓ Input Validation: All entry points covered
```

### Performance Benchmarks ✅
```
✓ API Response: avg 145ms (threshold: 200ms)
✓ Database Queries: 0 N+1 detected
✓ Memory Usage: 45MB peak (threshold: 100MB)
```

### Documentation ✅
- README.md updated with new feature
- API docs generated
- Migration guide written

### Manual Review
[If code-reviewer agent was used, include summary]

### Approval Status
**STATUS:** ✅ READY FOR COMMIT | ⚠️ NEEDS FIXES | ❌ BLOCKED

**Remaining Issues:**
[List any blockers or required fixes]

### Next Steps
1. [Specific actions needed, if any]
2. Create commit with conventional commit message
3. Push and create PR
```

### Quality Gates

**Must Pass (BLOCKING):**
- All tests pass
- No linting errors
- No type errors
- No security vulnerabilities (high/critical)
- Coverage >80% on new code

**Should Pass (WARNING):**
- No linting warnings
- Documentation complete
- Performance benchmarks met
- Code complexity low

**Nice to Have:**
- 100% test coverage
- Zero technical debt
- Comprehensive E2E tests

### Anti-Patterns to Avoid

- ❌ Skipping tests because "in a hurry"
- ❌ Committing with lint warnings
- ❌ Ignoring security scan results
- ❌ "I'll add tests later"
- ❌ Disabling checks to make things pass

### Integration with Code Review

After all checks pass, automatically suggest:
```
All verification passed. Ready to:
1. Create commit: git add . && git commit -m "feat: [description]"
2. Or invoke code-reviewer agent for manual review first
```

### Failure Recovery

If verification fails:
1. **Identify root cause** (which check failed)
2. **Fix the issue** (don't bypass the check)
3. **Re-run verification**
4. **Only proceed when all green**

### Pipeline Completion

Upon successful verification:
```markdown
✅ Pipeline Complete

Stages Completed:
1. ✅ PM Spec (pipeline-pm-spec)
2. ✅ Architecture Review (pipeline-arch-review)
3. ✅ Implementation (pipeline-implement)
4. ✅ Test Verification (pipeline-test-verify)

Ready for:
- Git commit
- Pull request creation
- Deployment (if CI/CD configured)
```
