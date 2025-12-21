# Local Model Use Case Guide

## Quick Reference Matrix

| Use Case | Primary | Alternative | Why |
|----------|---------|-------------|-----|
| **Quick Q&A** | llama3.2 | gpt-oss:20b | Speed vs depth |
| **Explain code** | devstral:24b | llama3.2 | Accuracy vs speed |
| **Debug errors** | devstral:24b | qwen3-coder | Code focus vs context |
| **Architecture** | gpt-oss:120b | gpt-oss:20b | Deep vs quick |
| **Code review** | devstral:24b | gpt-oss:120b | Code vs reasoning |
| **Log analysis** | qwen3-coder:30b | devstral:24b | Context vs code |
| **Documentation** | llama3.2 | qwen3-coder | Speed vs quality |
| **Research** | gpt-oss:120b | qwen3-coder | Reasoning vs context |
| **Image analysis** | llama4:scout | - | Only multimodal |
| **Refactor ideas** | gpt-oss:120b | devstral:24b | Design vs code |
| **API design** | gpt-oss:120b | devstral:24b | Architecture vs impl |
| **Test strategy** | gpt-oss:20b | devstral:24b | Quick vs detailed |
| **Performance** | qwen3-coder:30b | gpt-oss:120b | Code vs design |
| **Security review** | gpt-oss:120b | devstral:24b | Thorough vs quick |

---

## Model Profiles

### llama3.2 (2GB) - "The Speedster"
**Alias:** `ask`
**Response time:** <2 seconds
**Best for:**
- Quick factual questions
- Simple explanations
- Syntax lookups
- Error message decoding
- Documentation lookups
- Brainstorming keywords
- Quick translations

**Example queries:**
```bash
ask "What does ECONNREFUSED mean?"
ask "Python list comprehension syntax"
ask "Difference between POST and PUT"
ask "What is dependency injection in one sentence"
ask "Convert this to async: def fetch(): return data"
```

**Limitations:**
- Shallow reasoning
- May miss nuance
- Short context window

---

### devstral:24b (14GB) - "The Coder"
**Alias:** `code`
**SWE-Bench:** 68% (best local)
**Best for:**
- Code explanations
- Function analysis
- Bug identification
- Code review feedback
- Pattern recognition
- Refactoring suggestions
- Test case ideas

**Example queries:**
```bash
code "Explain this authentication flow"
code "What's wrong with this SQL query"
code "How would you refactor this function"
code "Identify potential bugs in this code"
code "What design pattern is this using"
cat src/auth.py | code "Review this for security issues"
```

**Overlaps with:**
- gpt-oss:120b (when deep reasoning about code needed)
- qwen3-coder (when analyzing large codebases)

---

### gpt-oss:20b (13GB) - "The Quick Thinker"
**Alias:** `think`
**Best for:**
- Quick comparisons
- Trade-off analysis
- Decision support
- Pros/cons lists
- Simple architecture questions
- Technology selection
- Quick estimates

**Example queries:**
```bash
think "Redis vs Memcached for session storage"
think "Should I use REST or GraphQL here"
think "Pros and cons of microservices"
think "Estimate complexity of adding auth"
think "Which database for time-series data"
think "Monorepo vs polyrepo tradeoffs"
```

**Overlaps with:**
- gpt-oss:120b (use 120b for deeper analysis)
- llama3.2 (use llama3.2 for simpler questions)

---

### gpt-oss:120b (65GB) - "The Architect"
**Alias:** `reason`
**Best for:**
- System design
- Architecture decisions
- Complex trade-offs
- Security analysis
- Performance strategy
- Migration planning
- Technical debt analysis
- Novel problem solving

**Example queries:**
```bash
reason "Design a caching strategy for this e-commerce site"
reason "How should we migrate from monolith to microservices"
reason "Analyze security implications of this auth flow"
reason "What's the best approach for real-time notifications"
reason "Design a rate limiting system"
reason "How to handle eventual consistency here"
```

**Overlaps with:**
- gpt-oss:20b (use 20b for quicker, simpler analysis)
- devstral:24b (use devstral for code-specific analysis)

---

### qwen3-coder:30b (18GB) - "The Context King"
**Alias:** `deep`
**Context:** 256K tokens (largest)
**Best for:**
- Large file analysis
- Log file parsing
- Codebase understanding
- Multi-file relationships
- Documentation generation
- Long conversation context
- Repository analysis

**Example queries:**
```bash
cat app.log | deep "Find error patterns and root causes"
cat src/*.py | deep "Explain the architecture"
deep "Summarize all API endpoints in this codebase"
cat large_file.py | deep "Document all functions"
deep "How do these 5 services interact"
git diff HEAD~10 | deep "Summarize all changes"
```

**Overlaps with:**
- devstral:24b (use devstral for code-specific, smaller context)
- gpt-oss:120b (use 120b for reasoning, not just context)

---

### llama4:scout (67GB) - "The Vision"
**Alias:** `vision`
**Capabilities:** Multimodal (images + text)
**Best for:**
- Screenshot analysis
- Diagram interpretation
- UI/UX feedback
- Error screenshot debugging
- Architecture diagram review
- Chart/graph analysis
- Design mockup review

**Example queries:**
```bash
vision  # Then paste/describe image
# "What's wrong in this error screenshot"
# "Analyze this architecture diagram"
# "Review this UI mockup"
# "What does this chart show"
# "Identify issues in this network diagram"
```

**Unique capability:** Only model with vision

---

## Overlap Decision Guide

### "Should I use devstral or gpt-oss:120b?"

| Scenario | Use devstral:24b | Use gpt-oss:120b |
|----------|------------------|------------------|
| "Explain this function" | ✅ | |
| "Design this system" | | ✅ |
| "Find bugs in this code" | ✅ | |
| "Should we use X pattern" | | ✅ |
| "Refactor this specific function" | ✅ | |
| "Refactor the entire architecture" | | ✅ |
| "What does this code do" | ✅ | |
| "Why did they design it this way" | | ✅ |

### "Should I use qwen3-coder or devstral?"

| Scenario | Use qwen3-coder:30b | Use devstral:24b |
|----------|---------------------|------------------|
| Single file analysis | | ✅ (faster) |
| Multi-file analysis | ✅ | |
| Large log files | ✅ | |
| Quick code review | | ✅ |
| Codebase documentation | ✅ | |
| Specific function help | | ✅ |
| Understanding repo structure | ✅ | |

### "Should I use gpt-oss:20b or gpt-oss:120b?"

| Scenario | Use gpt-oss:20b | Use gpt-oss:120b |
|----------|-----------------|------------------|
| Quick comparison | ✅ | |
| Deep architecture | | ✅ |
| Simple trade-offs | ✅ | |
| Complex trade-offs | | ✅ |
| Time-sensitive | ✅ | |
| Quality-critical | | ✅ |
| Brainstorming | ✅ | |
| Final decision | | ✅ |

### "Should I use llama3.2 or something else?"

**Use llama3.2 when:**
- Response time matters (<2s)
- Question is straightforward
- Just need a quick answer
- Looking up syntax/facts

**Use something else when:**
- Need reasoning (→ gpt-oss)
- Need code analysis (→ devstral)
- Have large input (→ qwen3-coder)
- Have images (→ llama4:scout)

---

## Chaining Models

For complex tasks, chain models:

```bash
# Quick brainstorm → Deep analysis
ask "List 5 caching strategies" | reason "Analyze which is best for e-commerce"

# Code review → Architecture feedback
cat auth.py | code "Review this" | reason "Suggest architectural improvements"

# Log analysis → Root cause
cat app.log | deep "Find errors" | reason "What's the root cause"
```

---

## Cost-Benefit Summary

| Model | Load Time | Response | Quality | Use When |
|-------|-----------|----------|---------|----------|
| llama3.2 | 1s | <2s | Good | Speed matters |
| gpt-oss:20b | 3s | 5-10s | Better | Quick reasoning |
| devstral:24b | 3s | 5-15s | Best code | Code tasks |
| qwen3-coder | 5s | 10-30s | Great | Large context |
| gpt-oss:120b | 10s | 20-60s | Best | Critical decisions |
| llama4:scout | 10s | 15-45s | Great | Images |

**All models: $0 cost, unlimited usage**

---

## Performance Overlap Zones

### Zone 1: General Q&A (Compete on Speed vs Quality)

```
         SPEED                                    QUALITY
    ◄──────────────────────────────────────────────────────►

    llama3.2          gpt-oss:20b              gpt-oss:120b
    [████████]        [████████████]           [████████████████]
    <2s               5-10s                    20-60s

    Use llama3.2:     Use gpt-oss:20b:         Use gpt-oss:120b:
    - "What is X"     - "Compare X vs Y"       - "Design X system"
    - "Syntax for"    - "Pros/cons of"         - "Analyze X deeply"
    - "Quick help"    - "Should I use"         - "Critical decision"
```

### Zone 2: Code Understanding (Compete on Context vs Specialization)

```
         SPECIALIZATION                         CONTEXT SIZE
    ◄──────────────────────────────────────────────────────►

    devstral:24b                               qwen3-coder:30b
    [████████████████]                         [████████████████]
    Best SWE-Bench (68%)                       256K tokens

    OVERLAP ZONE: Medium-sized code analysis
    ┌─────────────────────────────────────────────────────┐
    │  Both work well for:                                │
    │  - Single file review (devstral slightly better)    │
    │  - Function explanations (tie)                      │
    │  - Bug identification (devstral better)             │
    │  - Code documentation (qwen3 better for large)      │
    └─────────────────────────────────────────────────────┘

    Clear winners:
    devstral:24b → Specific code tasks, smaller files
    qwen3-coder → Multi-file, logs, large context
```

### Zone 3: Reasoning Tasks (Compete on Depth)

```
         QUICK                                  THOROUGH
    ◄──────────────────────────────────────────────────────►

    gpt-oss:20b                                gpt-oss:120b
    [████████████]                             [████████████████████]

    OVERLAP ZONE: Architecture & Design Questions
    ┌─────────────────────────────────────────────────────┐
    │  Question: "How should I structure auth?"           │
    │                                                     │
    │  gpt-oss:20b response:                              │
    │  - JWT vs sessions comparison                       │
    │  - Basic recommendation                             │
    │  - 5-10 seconds                                     │
    │                                                     │
    │  gpt-oss:120b response:                             │
    │  - Detailed threat model                            │
    │  - Multiple architecture options                    │
    │  - Trade-off analysis                               │
    │  - Implementation considerations                    │
    │  - 30-60 seconds                                    │
    └─────────────────────────────────────────────────────┘
```

### Zone 4: Code + Reasoning (Triple Overlap)

```
                    devstral:24b
                    (Code Expert)
                         ▲
                        /│\
                       / │ \
                      /  │  \
                     /   │   \
                    /    │    \
    gpt-oss:120b ◄──────┼──────► qwen3-coder:30b
    (Reasoning)    OVERLAP      (Context)
                    ZONE

    Triple Overlap Tasks:
    ┌─────────────────────────────────────────────────────┐
    │  "Review this codebase architecture"                │
    │                                                     │
    │  Option 1: devstral:24b                             │
    │  → Best for: Code-level issues, patterns           │
    │  → Weakness: May miss big picture                   │
    │                                                     │
    │  Option 2: gpt-oss:120b                             │
    │  → Best for: Architectural concerns, design         │
    │  → Weakness: Less code-specific                     │
    │                                                     │
    │  Option 3: qwen3-coder:30b                          │
    │  → Best for: Understanding full codebase            │
    │  → Weakness: Less deep on specific issues           │
    │                                                     │
    │  BEST APPROACH: Chain them                          │
    │  qwen3 (understand) → devstral (review) → gpt-oss   │
    └─────────────────────────────────────────────────────┘
```

### Performance Benchmark Estimates

| Task Type | llama3.2 | gpt-oss:20b | devstral | qwen3 | gpt-oss:120b |
|-----------|----------|-------------|----------|-------|--------------|
| Simple Q&A | 95% | 97% | 90% | 92% | 99% |
| Code explain | 70% | 80% | **95%** | 90% | 88% |
| Debug code | 60% | 75% | **92%** | 88% | 85% |
| Architecture | 50% | 82% | 75% | 78% | **95%** |
| Long context | 40% | 60% | 70% | **95%** | 80% |
| Reasoning | 55% | 80% | 70% | 75% | **96%** |
| Speed (tok/s) | **120** | 45 | 40 | 35 | 15 |

**Bold = Best in category**

### When Models Produce Similar Results

These scenarios have significant overlap - pick based on what matters:

| Scenario | All These Work | Pick Based On |
|----------|----------------|---------------|
| "Explain this error" | llama3.2, devstral, gpt-oss:20b | Speed vs depth |
| "Review this function" | devstral, qwen3, gpt-oss:120b | Code vs reasoning |
| "Compare X vs Y" | gpt-oss:20b, gpt-oss:120b | Quick vs thorough |
| "Summarize this file" | llama3.2, devstral, qwen3 | Size of file |
| "What pattern is this" | devstral, gpt-oss:20b, gpt-oss:120b | Recognition vs analysis |

### Decision Flowchart

```
START
  │
  ▼
┌─────────────────┐
│ Is it an image? │──YES──► llama4:scout
└────────┬────────┘
         │ NO
         ▼
┌─────────────────┐
│ Need speed <5s? │──YES──► llama3.2
└────────┬────────┘
         │ NO
         ▼
┌─────────────────┐
│ Large context?  │──YES──► qwen3-coder:30b
│ (>10K tokens)   │
└────────┬────────┘
         │ NO
         ▼
┌─────────────────┐
│ Code-specific?  │──YES──► devstral:24b
└────────┬────────┘
         │ NO
         ▼
┌─────────────────┐
│ Critical/Deep?  │──YES──► gpt-oss:120b
└────────┬────────┘
         │ NO
         ▼
      gpt-oss:20b (default reasoning)
```
