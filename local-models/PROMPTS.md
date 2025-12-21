# Optimized Prompt Templates

## Why Templates Matter

Each model responds best to specific prompt structures. These templates are optimized for:
- Maximum accuracy
- Consistent output format
- Faster inference
- Better reasoning chains

---

## llama3.2 Templates (Speed Focus)

### Quick Answer
```
Answer in 1-2 sentences: {question}
```

### Syntax Lookup
```
Show only the code syntax for: {concept}
No explanation needed.
```

### Error Decode
```
What does this error mean in plain English?
Error: {error_message}
One sentence answer.
```

### Yes/No Decision
```
Yes or No only: {question}
```

### List Generation
```
List 5 {items} without explanation:
```

---

## devstral:24b Templates (Code Focus)

### Code Explanation
```
Explain this code's purpose and logic:

```{language}
{code}
```

Focus on:
1. What it does
2. How it works
3. Key patterns used
```

### Bug Finder
```
Find bugs or issues in this code:

```{language}
{code}
```

List each issue with:
- Line/location
- Problem
- Suggested fix
```

### Code Review
```
Review this code for:
- Correctness
- Performance
- Security
- Best practices

```{language}
{code}
```

Format: Issue → Severity (High/Medium/Low) → Fix
```

### Refactor Suggestions
```
Suggest refactoring improvements for:

```{language}
{code}
```

Keep the same functionality. Focus on:
- Readability
- Maintainability
- Performance
```

### Test Cases
```
Generate test cases for this function:

```{language}
{code}
```

Include:
- Happy path
- Edge cases
- Error cases
```

---

## gpt-oss:20b Templates (Quick Reasoning)

### Comparison
```
Compare {option_a} vs {option_b} for {use_case}:

| Aspect | {option_a} | {option_b} |
|--------|------------|------------|

Recommendation: [one sentence]
```

### Pros/Cons
```
{topic} - Pros and Cons:

Pros:
1.
2.
3.

Cons:
1.
2.
3.

Bottom line: [one sentence]
```

### Quick Decision
```
I need to choose between:
A) {option_a}
B) {option_b}

Context: {context}

Which should I pick and why? (3 sentences max)
```

### Trade-off Analysis
```
Analyze trade-offs for: {decision}

Consider:
- Performance
- Complexity
- Maintainability
- Cost

Quick recommendation:
```

---

## gpt-oss:120b Templates (Deep Reasoning)

### System Design
```
Design a system for: {requirement}

Include:
1. High-level architecture
2. Component breakdown
3. Data flow
4. Key trade-offs
5. Scaling considerations

Constraints: {constraints}
```

### Architecture Review
```
Review this architecture for:

{architecture_description}

Analyze:
1. Strengths
2. Weaknesses
3. Potential failure modes
4. Scaling bottlenecks
5. Security concerns
6. Recommendations

Be thorough and critical.
```

### Complex Problem Solving
```
Problem: {problem_description}

Requirements:
{requirements}

Constraints:
{constraints}

Provide:
1. Problem analysis
2. Possible approaches (at least 3)
3. Trade-off comparison
4. Recommended approach with justification
5. Implementation considerations
```

### Security Analysis
```
Perform security analysis on:

{system_or_code_description}

Check for:
1. Authentication vulnerabilities
2. Authorization issues
3. Data exposure risks
4. Injection vectors
5. OWASP Top 10 concerns

Rate each: Critical/High/Medium/Low
Provide remediation for Critical/High.
```

### Migration Planning
```
Plan migration from: {current_state}
To: {target_state}

Consider:
1. Risk assessment
2. Phased approach
3. Rollback strategy
4. Data migration
5. Downtime estimation
6. Testing strategy
```

---

## qwen3-coder:30b Templates (Long Context)

### Codebase Analysis
```
Analyze this codebase:

{large_code_dump}

Provide:
1. Overall architecture
2. Main components and their responsibilities
3. Data flow between components
4. External dependencies
5. Potential issues or tech debt
```

### Log Analysis
```
Analyze these logs for issues:

{log_content}

Find:
1. Error patterns
2. Performance anomalies
3. Suspicious activities
4. Root cause analysis
5. Recommended actions
```

### Documentation Generation
```
Generate documentation for:

{code}

Include:
1. Overview
2. API reference (if applicable)
3. Usage examples
4. Configuration options
5. Error handling
```

### Multi-File Review
```
Review these related files:

File 1: {filename1}
{content1}

File 2: {filename2}
{content2}

[... more files ...]

Analyze:
1. How they interact
2. Consistency issues
3. Potential bugs across boundaries
4. Refactoring opportunities
```

### Repository Summary
```
Summarize this repository structure:

{file_tree_and_key_files}

Provide:
1. Project purpose
2. Technology stack
3. Architecture pattern
4. Key entry points
5. How to get started
```

---

## llama4:scout Templates (Multimodal)

### Screenshot Analysis
```
[Image attached]

Analyze this screenshot:
1. What is shown
2. Any errors or issues visible
3. UI/UX observations
4. Suggested improvements
```

### Diagram Interpretation
```
[Image attached]

Interpret this diagram:
1. What it represents
2. Key components
3. Relationships/flows
4. Missing elements (if any)
```

### Error Screenshot Debug
```
[Image attached]

Debug this error:
1. What went wrong
2. Likely cause
3. How to fix it
```

### UI Review
```
[Image attached]

Review this UI:
1. Usability issues
2. Accessibility concerns
3. Visual hierarchy
4. Improvement suggestions
```

---

## Template Usage Scripts

### Bash Functions (add to ~/.zshrc)

```bash
# Code review template
review_code() {
    echo "Review this code for correctness, performance, security, best practices:

\`\`\`
$(cat "$1")
\`\`\`

Format: Issue → Severity → Fix" | ollama run devstral:24b
}

# Quick comparison
compare() {
    echo "Compare $1 vs $2:
| Aspect | $1 | $2 |
|--------|-----|-----|
Recommendation:" | ollama run gpt-oss:20b
}

# System design
design() {
    echo "Design a system for: $1
Include: architecture, components, data flow, trade-offs, scaling" | ollama run gpt-oss:120b
}

# Log analysis
analyze_logs() {
    cat "$1" | ollama run qwen3-coder:30b "Analyze these logs for errors, patterns, root causes"
}
```

---

## Anti-Patterns

### Don't Do This:

```bash
# Too vague
ask "help with code"

# Too much for fast model
ask "Design a microservices architecture for e-commerce"

# Too little context for reasoning model
reason "which is better"

# Wrong model for task
code "what is the meaning of life"  # Use ask instead
```

### Do This Instead:

```bash
# Specific
ask "Python dict comprehension syntax"

# Right model for complexity
reason "Design a microservices architecture for e-commerce"

# Sufficient context
reason "Redis vs Memcached for session storage in a stateless API"

# Right model for task
ask "what is dependency injection"
```
