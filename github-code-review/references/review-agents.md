# Specialized Review Agents

Each agent focuses on one review dimension. Run them in parallel via the swarm.

## Security Agent

Identifies vulnerabilities and suggests fixes.

```bash
CHANGED_FILES=$(gh pr view 123 --json files --jq '.files[].path')

SECURITY_RESULTS=$(npx ruv-swarm github review-security \
  --pr 123 \
  --files "$CHANGED_FILES" \
  --check "owasp,cve,secrets,permissions" \
  --suggest-fixes)

if echo "$SECURITY_RESULTS" | grep -q "critical"; then
  gh pr review 123 --request-changes --body "$SECURITY_RESULTS"
  gh pr edit 123 --add-label "security-review-required"
else
  gh pr comment 123 --body "$SECURITY_RESULTS"
fi
```

**Checks:** SQL injection, XSS, auth bypasses, authorization flaws, cryptographic weaknesses, dependency CVEs, secret exposure, CORS misconfiguration.

**Comment template for security findings:**

```markdown
🔒 **Security Issue: [Type]**

**Severity**: Critical / High / Low

**Description**: [Clear explanation]
**Impact**: [Consequences if not addressed]

**Suggested Fix**:
\`\`\`language
[Code example]
\`\`\`

**References**: [OWASP link], [Best practice link]
```

## Performance Agent

Analyses performance impact and optimisation opportunities.

```bash
npx ruv-swarm github review-performance \
  --pr 123 \
  --profile "cpu,memory,io" \
  --benchmark-against main \
  --suggest-optimizations
```

**Metrics:** Big-O complexity, query efficiency, memory allocation, cache utilisation, network requests, bundle size, render performance.

**Benchmarks:** baseline comparison, load-test simulations, memory-leak detection, bottleneck identification.

## Architecture Agent

Evaluates design patterns and architectural decisions.

```bash
npx ruv-swarm github review-architecture \
  --pr 123 \
  --check "patterns,coupling,cohesion,solid" \
  --visualize-impact \
  --suggest-refactoring
```

**Checks:** SOLID adherence, DRY violations, separation of concerns, dependency injection, layer violations, circular dependencies.

**Metrics:** coupling, cohesion, cyclomatic complexity, maintainability index.

## Style Agent

Enforces coding standards and best practices, with auto-fix for safe changes.

```bash
npx ruv-swarm github review-style \
  --pr 123 \
  --check "formatting,naming,docs,tests" \
  --auto-fix "formatting,imports,whitespace"
```

**Checks:** formatting, naming conventions, documentation, comment quality, test coverage, error handling, logging.

**Auto-fix:** formatting, import organisation, trailing whitespace, simple naming issues.
