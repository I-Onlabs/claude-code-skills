# Claude Code Skills Collection

**154+ methodology skills organized by function and domain.**

## Overview

Skills provide **methodology** (HOW to approach problems), not execution:
- Auto-activate based on context/triggers
- Guide Claude's approach to tasks
- No model/tool assignments needed
- Already optimally structured

## Quick Install

```bash
# Install all skills
cp -r */ ~/.claude/skills/

# Install specific category
cp -r workflow/* ~/.claude/skills/
cp -r patterns/* ~/.claude/skills/
```

## Skills by Category

### 🔄 Workflow Skills (Core Methodology)

**Systematic processes for development workflows**

- **systematic-debugging** - 4-phase debugging framework
  - Phase 1: Root Cause Investigation
  - Phase 2: Pattern Analysis
  - Phase 3: Hypothesis Testing
  - Phase 4: Implementation

- **test-driven-development** - RED-GREEN-REFACTOR cycle
  - Write failing test first
  - Make it pass
  - Refactor for quality

- **pipeline-pm-spec** - INVEST user stories
- **pipeline-arch-review** - Architecture Decision Records
- **pipeline-implement** - TDD-driven implementation
- **pipeline-test-verify** - Comprehensive quality gates

- **task-tracking** - Auto todo lists for 3+ step tasks
- **project-context** - Load project conventions
- **quality-gates** - Pre-completion verification
- **verification-before-completion** - Prove success before claiming done

### 📐 Pattern Libraries

**Design patterns and best practices**

- **api-design-patterns** - 5-layer API pattern (Models/Services/Routers/Tests/Docs)
- **python-best-practices** - Modern Python 3.11+ patterns
- **code-refactor** - Bulk refactoring operations
- **defense-in-depth** - Multi-layer validation
- **intelligent-gate** - Decision framework for risky operations
- **token-optimization** - Efficiency patterns

### 🏗️ Frameworks & Platforms

**Framework-specific guidance**

**AWS:**
- aws-agentic-ai - Bedrock AgentCore
- aws-cdk-development - Infrastructure as Code
- aws-cost-operations - Cost optimization
- aws-serverless-eda - Serverless patterns

**Web Frameworks:**
- react-patterns - React 18+ patterns
- nextjs-patterns - Next.js 14+ App Router
- vue-patterns - Vue 3 composition

**Others:**
- kubernetes-patterns - K8s best practices
- docker-patterns - Container optimization

### 💻 Language-Specific

**Language best practices and idioms**

- **python-pro** - Python 3.11+ (type hints, async, data science)
- **typescript-expert** - TypeScript patterns
- **go-expert** - Go idioms
- **rust-expert** - Rust ownership patterns
- **java-expert** - Modern Java

### 🤖 Automation & Productivity

**Task automation and efficiency**

- **task-tracking** - Auto todo management
- **code-execution** - Local Python execution
- **local-models** - Ollama integration guide
- **escalation-reasoning** - 5-tier reasoning escalation (/think, /megathink, etc.)
- **intelligent-decision-making** - Multi-model consensus

### 🎯 Domain-Specific

**Specialized domain expertise**

**Security:**
- senior-security - Security expert methodology
- security-patterns - OWASP compliance

**Performance:**
- performance-analysis - Profiling and optimization
- token-optimization - Cost efficiency

**Data:**
- agentdb-* - Vector search, memory patterns
- data-engineering - ETL pipelines

**DevOps:**
- devops-patterns - CI/CD best practices
- kubernetes-patterns - Container orchestration

**Quality:**
- code-reviewer - Review methodology
- qa-expert - Testing strategies

### 🔧 Tools & Integrations

**Tool-specific guidance**

- **local-models** - Ollama integration (gpt-oss, qwen3-coder, etc.)
- **github-code-review** - GitHub PR workflows
- **playwright-skill** - Browser automation
- **chrome-devtools** - Web debugging

### 🎨 Creative & Content

**Content creation and design**

- **content-creator** - SEO-optimized marketing
- **algorithmic-art** - Generative art with p5.js
- **canvas-design** - Visual design
- **architecture-diagram-creator** - System diagrams

### 📊 Data & Analytics

**Data processing and analysis**

- **agentdb-vector-search** - Semantic search
- **agentdb-memory-patterns** - Persistent memory
- **csv-data-summarizer** - Quick data analysis
- **dashboard-creator** - KPI dashboards

### 🚀 Advanced Workflows

**Complex multi-step workflows**

- **vibe-coding-coordinator** - 15-20min preparation phases
- **bootstrap-orchestrator** - Project initialization
- **task-orchestrator** - Multi-task coordination
- **hoa-orchestrator** - Quality-gated workflows (G0→G1→S→G2→G3→G4→M)

## Skill Structure

Each skill has this format:

```yaml
---
name: skill-name
description: When and how to use this skill
triggers:                # Auto-activation keywords
  - keyword1
  - keyword2
---

# Skill methodology content
```

## How Skills Work

### Auto-Activation

Skills activate automatically based on:
- **Triggers**: Keywords in your request
- **Context**: Type of task being performed
- **Description**: Matching task patterns

**Example:**
```
You: "Fix this bug"
→ systematic-debugging auto-activates
→ Guides Claude through 4-phase framework
```

### No Model Assignment

Skills guide the **current Claude model**, they don't execute independently:
- Agents = WHO executes (use models/tools)
- Skills = HOW to approach (methodology only)

### Already Optimal

Skills don't need the agent enhancements because:
- Workflow skills already have systematic patterns
- Pattern skills are reference libraries
- Tool skills are decision frameworks
- No execution = no model/tool needs

## Skill Categories Explained

### Workflow vs Patterns

**Workflow Skills:**
- Sequential processes
- Quality gates
- Already have ReAct-like patterns
- Examples: systematic-debugging, TDD, pipelines

**Pattern Skills:**
- Reference libraries
- Best practices collections
- No workflow needed
- Examples: api-design-patterns, python-best-practices

### When to Use Which

| Your Task | Skill Activates | Why |
|-----------|-----------------|-----|
| Fix bug | systematic-debugging | 4-phase root cause framework |
| New feature | pipeline-pm-spec → pipeline-implement | Sequential development workflow |
| Write test | test-driven-development | RED-GREEN-REFACTOR cycle |
| API design | api-design-patterns | 5-layer reference pattern |
| Python code | python-best-practices | Pythonic idioms guide |
| Complex task | task-tracking | Auto todo management |

## Best Practices

### Skill Organization

1. **Workflow first** - Process-oriented skills
2. **Patterns second** - Reference libraries
3. **Domain third** - Specialized expertise
4. **Tools last** - Integration guides

### Naming Conventions

- **Workflow**: `systematic-*`, `pipeline-*`, `*-workflow`
- **Patterns**: `*-patterns`, `*-best-practices`
- **Domain**: `*-expert`, `senior-*`
- **Tools**: `*-skill`, `*-integration`

## Sync from Local

```bash
# Update from your active skills
./sync-from-local.sh

# This copies from ~/.claude/skills/ to here
```

## Creating New Skills

1. Create `my-skill/SKILL.md`
2. Add YAML frontmatter with triggers
3. Document methodology (not implementation)
4. Test auto-activation
5. Submit PR

Template:
```yaml
---
name: my-skill
description: Brief description of when/how to use
triggers:
  - keyword1
  - keyword2
---

# My Skill

## Purpose
What this skill helps with

## When to Activate
Specific scenarios

## Methodology
Step-by-step approach
```

## Contributing

1. Skills provide methodology, not execution
2. Use clear triggers for auto-activation
3. Document when/how to use
4. Test with real scenarios
5. Keep skills focused (single responsibility)

## License

MIT License - Free to use, modify, and distribute

---

**Status:** Production-ready skill library
**Skills:** 154+ organized by category
**Auto-Activation:** Based on triggers and context
**Purpose:** Methodology guidance (not execution)
**Quality:** Workflow skills have systematic patterns
