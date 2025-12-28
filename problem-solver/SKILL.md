# Problem Solver Skill

## Description
Sophisticated methodology for diagnosing, researching, and solving any problem through systematic investigation, hypothesis testing, and iterative refinement.

## Activation
Auto-activates when:
- Something "not working", "broken", "failing", "unexpected"
- Error messages or stack traces appear
- User asks "why", "how to fix", "what's wrong"
- Debugging or troubleshooting needed

## Core Philosophy
**Don't guess. Investigate. Prove. Verify.**

---

## Methodology: DIQRS-ITVF

### Phase 1: DISCOVER

#### D - Diagnose
- What exactly is the problem? (verbatim errors)
- What's expected vs actual behavior?
- When did it start? What changed recently?
- Is it reproducible? Under what conditions?

#### I - Intersect
- Cross-reference multiple data sources
- Compare logs, configs, code, and behavior
- Find where symptoms converge
- Identify common threads

#### Q - Question
Formulate precise questions:
- "Why does X happen when Y?"
- "What controls Z behavior?"
- "Where is this value coming from?"
- Challenge assumptions with questions

### Phase 2: RESEARCH

#### R - Research
- Read all relevant logs and configs
- Search codebase for related patterns
- Check documentation and changelogs
- Look for similar issues (GitHub, forums)

#### S - Synthesize
- Combine findings into coherent picture
- Identify root cause vs symptoms
- Map the causal chain
- Formulate hypotheses ranked by likelihood

### Phase 3: ITERATE

#### I - Iterate
- Test hypotheses one at a time
- Start with most likely cause
- Make minimal changes
- Document each attempt and result

#### T - Test
- Verify hypothesis with concrete test
- Reproduce the problem first
- Apply fix and test again
- Check for regressions

#### V - Verify
- Confirm fix addresses root cause
- Test edge cases
- Ensure no side effects
- Get user confirmation

#### F - Finalize
- Document the solution
- Update relevant configs/code
- Add safeguards if appropriate
- Share learnings (update CLAUDE.md, create hooks)

---

## Diagnostic Toolkit

### Log Analysis
```bash
# Claude Code decision audit
tail -100 ~/.claude/logs/decision-audit.jsonl | jq -s 'group_by(.decision) | map({decision: .[0].decision, count: length})'

# Recent errors
grep -i "error\|fail\|denied" ~/.claude/logs/*.json | tail -20

# Session context
cat ~/.claude/logs/session_start.json | jq '.context'
```

### Config Validation
```bash
# Validate JSON syntax
cat ~/.claude/settings.local.json | jq . > /dev/null && echo "Valid" || echo "Invalid JSON"

# Check effective settings
cat ~/.claude/settings.local.json | jq '.permissions'

# Find all settings files
find ~/.claude -name "settings*.json" -o -name "*.local.json" 2>/dev/null
```

### System State
```bash
# Environment
env | grep -i claude
which claude && claude --version

# Processes
ps aux | grep -E "claude|node|python" | grep -v grep

# Network
lsof -i -P | grep LISTEN | head -10
```

---

## Problem Pattern Library

| Pattern | Symptoms | Root Cause | Fix |
|---------|----------|------------|-----|
| Permission loop | "auto-denied in dontAsk mode" | Pattern not matching allow list | Add tool to allow list without parens |
| Hook failure | Operation blocked unexpectedly | Hook returning deny | Check hook script, run manually |
| MCP timeout | Tool hangs or fails | Server not responding | Restart MCP server |
| Context overflow | Slow, truncated, or confused | Too much context | /compact or /clear |
| Config not applied | Changes don't take effect | Cached or wrong file | Restart Claude Code |

---

## Sophisticated Techniques

### Multi-Source Triangulation
Don't trust single source. Verify with:
1. Logs (what happened)
2. Config (what should happen)
3. Code (what's implemented)
4. Behavior (what actually happens)

### Hypothesis Ranking
Score each hypothesis:
- **Evidence strength**: How much supports it?
- **Explanatory power**: Does it explain all symptoms?
- **Falsifiability**: Can we disprove it easily?
- **Simplicity**: Occam's razor

### Bisection Debugging
When cause unclear:
1. Identify working state and broken state
2. Find midpoint (time, commit, config change)
3. Test midpoint
4. Narrow range by half
5. Repeat until root cause found

### Rubber Duck Protocol
Before asking for help:
1. State the problem out loud
2. Explain what you've tried
3. Describe expected vs actual
4. Often solution becomes obvious

---

## Anti-Patterns

- **Shotgun debugging**: Changing random things hoping something works
- **Symptom fixing**: Treating symptoms, not root cause
- **Assumption blindness**: "It can't be X" without checking
- **Documentation trust**: Assuming docs match reality
- **Single hypothesis**: Not considering alternatives
- **Skipping verification**: Assuming fix worked without testing
