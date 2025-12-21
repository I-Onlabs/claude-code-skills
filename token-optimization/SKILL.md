---
name: token-optimization
description: Token-aware patterns for efficient context usage. Activates when working on long sessions, large codebases, or when context pressure is detected. Provides strategies for reducing token consumption while maintaining quality.
---

# Token Optimization Skill

## When This Skill Activates

This skill provides methodology for efficient token usage:
- Long-running sessions approaching context limits
- Large codebase exploration
- Multiple file modifications
- Complex multi-step tasks

## Token Awareness

### Context Budget
- Total context: ~200K tokens
- Practical limit: ~160K (leave buffer)
- Compact at: 70% capacity
- Avoid complex work at: >80% capacity

### Token Costs (Approximate)
| Content | Tokens |
|---------|--------|
| 1 line code | ~10-20 |
| 1 page text | ~500 |
| Average file | ~500-2000 |
| CLAUDE.md | ~3000 |
| Full conversation | Grows rapidly |

## Optimization Strategies

### 1. Progressive Disclosure
Instead of loading everything upfront:
```
Bad:  Read all 50 files at once
Good: Read index → identify relevant → read specific
```

### 2. Targeted Search
Use efficient search patterns:
```
Bad:  Read entire directory tree
Good: Glob pattern → Grep specific → Read matches
```

### 3. Minimal Context
Include only what's needed:
```
Bad:  Include entire file for small change
Good: Include function + surrounding context
```

### 4. Structured Summaries
For long outputs:
```
Bad:  Full test output (10K tokens)
Good: Summary + key failures (500 tokens)
```

### 5. Timely Compaction
Monitor and compact proactively:
```
Bad:  Wait for "Context low" warning
Good: Compact at 70% after task completion
```

## MCP Token Management

### Problem: MCP Server Token Drain
MCP tools can consume 30-60K tokens before conversation starts.

### Solution: Selective Loading
- Only enable needed MCP servers per session
- Disable unused servers when not needed
- Use `claude mcp list` to audit

### Memory Server Strategy
| Server | When to Use |
|--------|-------------|
| memory-keeper | Session continuity, compaction recovery |
| server-memory | Long-term key-value storage |
| Neither | Short, focused tasks |

## Compaction Strategy

### Pre-Compaction Checklist
1. ✅ Critical context saved to memory MCP
2. ✅ Important decisions documented
3. ✅ Current task state captured
4. ✅ Key file paths noted

### Post-Compaction Recovery
1. Load context from memory MCP
2. Re-read critical files if needed
3. Check decision-audit.jsonl for context
4. Resume task from documented state

## Code Patterns

### Efficient File Operations
```python
# Bad: Read all then filter
for f in all_files:
    content = read(f)
    if "pattern" in content:
        process(f)

# Good: Search first then read
matches = grep("pattern", all_files)
for f in matches:
    content = read(f)
    process(f)
```

### Efficient Updates
```python
# Bad: Full file replacement
content = read(file)
new_content = content.replace(old, new)
write(file, new_content)

# Good: Targeted edit
edit(file, old_string=old, new_string=new)
```

### Efficient Exploration
```python
# Bad: Deep recursive exploration
explore_all_directories(root)

# Good: Breadth-first with limits
list_top_level(root)
identify_relevant_dirs()
explore_targeted(relevant_only)
```

## Session Management

### Long Session Strategy
1. **Start**: Load minimal context
2. **Work**: Add context as needed
3. **Checkpoint**: Save state periodically
4. **Compact**: At 70% or task completion
5. **Recover**: Restore from checkpoint

### Task Batching
```
Bad:  One massive continuous session
Good: Multiple focused sessions with clear handoffs
```

## Integration with Hooks

### Pre-Compact Hook
Automatically triggered when context low:
- Backs up transcript
- Creates recovery index
- Logs compaction event

### Session Start Hook
Restores context efficiently:
- Loads minimal git status
- Checks for recovery context
- Provides continuation hints

## Metrics to Monitor

Track these for optimization:
- Session length before compaction
- Files read per task
- Tool calls per operation
- Recovery success rate
