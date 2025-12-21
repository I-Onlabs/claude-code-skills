# Claude Code Skills

**154+ methodology skills providing systematic approaches to development workflows and best practices.**

## Overview

Skills are reusable methodologies that guide how Claude approaches problems. They auto-activate based on context and provide frameworks, patterns, and best practices without executing code directly.

**Key Concept:** Skills provide **methodology** (HOW), Agents provide **execution** (WHO).

## Quick Start

```bash
# Install all skills
git clone https://github.com/I-Onlabs/claude-code-skills.git
cp -r claude-code-skills/*/ ~/.claude/skills/

# Install specific skills
cp -r claude-code-skills/systematic-debugging ~/.claude/skills/
cp -r claude-code-skills/api-design-patterns ~/.claude/skills/
```

## Skills by Category

### 🔄 Workflow Skills

**Systematic processes for development tasks**

| Skill | Purpose | When It Activates |
|-------|---------|------------------|
| **systematic-debugging** | 4-phase debugging framework | Bug fixing, troubleshooting |
| **test-driven-development** | RED-GREEN-REFACTOR cycle | Writing tests, TDD approach |
| **task-tracking** | Auto todo management | Complex multi-step tasks (3+) |
| **quality-gates** | Pre-completion verification | Before claiming work complete |
| **verification-before-completion** | Prove success with evidence | Final validation |
| **pipeline-pm-spec** | INVEST user stories | Feature planning |
| **pipeline-arch-review** | Architecture Decision Records | Design decisions |
| **pipeline-implement** | TDD-driven implementation | Feature development |
| **pipeline-test-verify** | Comprehensive quality gates | Testing workflows |

### 📐 Pattern Libraries

**Design patterns and best practices**

| Skill | Purpose | Use For |
|-------|---------|---------|
| **api-design-patterns** | 5-layer API pattern | REST/GraphQL API structure |
| **python-best-practices** | Modern Python 3.11+ patterns | Pythonic code |
| **defense-in-depth** | Multi-layer validation | Security, data integrity |
| **intelligent-gate** | Risk assessment framework | Risky operations |
| **token-optimization** | Efficiency patterns | Cost optimization |
| **code-refactor** | Bulk refactoring patterns | Large-scale changes |

### 🏗️ Frameworks & Platforms

**Framework-specific guidance**

**AWS:**
- `aws-agentic-ai` - Bedrock AgentCore (Gateway, Runtime, Memory, Identity)
- `aws-cdk-development` - Infrastructure as Code with CDK
- `aws-cost-operations` - Cost optimization and monitoring
- `aws-serverless-eda` - Serverless patterns (Lambda, API Gateway, EventBridge)

**Kubernetes:**
- `kubernetes-patterns` - K8s best practices, deployment patterns

**Web Frameworks:**
- React, Next.js, Vue patterns
- Component architecture, state management

### 💻 Language-Specific

**Language idioms and best practices**

- **Python** - Type hints, async/await, data science
- **TypeScript** - Type safety, modern patterns
- **Go** - Concurrency, interfaces, idiomatic Go
- **Rust** - Ownership, lifetimes, memory safety
- **Java** - Modern Java features

### 🤖 Automation & Tools

**Productivity and integration**

| Skill | Purpose |
|-------|---------|
| **local-models** | Ollama integration guide (gpt-oss, qwen3-coder) |
| **escalation-reasoning** | 5-tier reasoning (/think, /megathink, /ultrathink) |
| **intelligent-decision-making** | Multi-model consensus |
| **code-execution** | Local Python execution for cost savings |
| **github-code-review** | GitHub PR workflows |
| **playwright-skill** | Browser automation |

### 🎯 Domain-Specific

**Specialized expertise by domain**

**Security:**
- Security patterns, OWASP compliance, vulnerability scanning

**Performance:**
- Profiling, optimization, caching strategies

**Data:**
- `agentdb-*` - Vector search, memory patterns, learning algorithms
- Data engineering - ETL pipelines, schema design

**DevOps:**
- CI/CD patterns, container orchestration

**Quality:**
- Code review methodology, testing strategies

### 🎨 Creative & Content

**Content creation and design**

- `content-creator` - SEO-optimized marketing content
- `algorithmic-art` - Generative art with p5.js
- `canvas-design` - Visual design
- `architecture-diagram-creator` - System architecture diagrams
- `dashboard-creator` - KPI dashboards

### 📊 Data & Analytics

**Data processing and visualization**

- `agentdb-vector-search` - Semantic search and embeddings
- `agentdb-memory-patterns` - Persistent memory for agents
- `csv-data-summarizer` - Quick data analysis
- `meeting-insights-analyzer` - Extract insights from transcripts

### 🚀 Advanced Orchestration

**Complex multi-phase workflows**

| Skill | Phases | Use For |
|-------|--------|---------|
| **hoa-orchestrator** | G0→G1→S→G2→G3→G4→M | Quality-gated deliverables with formal verification |
| **vibe-coding-coordinator** | Preparation phase | Understanding vague requests |
| **bootstrap-orchestrator** | Auto-configuration | New project initialization |
| **task-orchestrator** | Task breakdown | Complex multi-task features |

## How Skills Work

### Auto-Activation

Skills activate automatically based on:
- **Keywords** in your request (triggers)
- **Task context** (debugging, testing, API design, etc.)
- **Description matching** (similar task patterns)

**Examples:**

```
You: "Fix this bug"
→ systematic-debugging auto-activates
→ Guides through 4-phase framework

You: "Create an API endpoint"
→ api-design-patterns auto-activates
→ Provides 5-layer structure

You: "This task is complex"
→ task-tracking auto-activates
→ Creates todo list for tracking
```

### Skill Structure

Each skill directory contains:

```
skill-name/
├── SKILL.md          # Methodology and usage
├── CLAUDE.md         # (Optional) Additional context
└── examples/         # (Optional) Example files
```

**SKILL.md frontmatter:**

```yaml
---
name: skill-name
description: Brief description of when/how to use
triggers:
  - keyword1
  - keyword2
  - keyword3
---

# Methodology content...
```

## Commonly Used Skills

### For Debugging
1. **systematic-debugging** - 4-phase root cause analysis
2. **root-cause-tracing** - Deep investigation patterns
3. **error-detective** (agent) - Automated debugging

### For New Features
1. **task-tracking** - Break into steps
2. **pipeline-pm-spec** - Write user stories
3. **pipeline-implement** - TDD implementation
4. **pipeline-test-verify** - Quality verification

### For APIs
1. **api-design-patterns** - 5-layer structure
2. **test-driven-development** - Test-first approach
3. **quality-gates** - Pre-deployment checks

### For Quality
1. **verification-before-completion** - Prove success
2. **quality-gates** - Systematic verification
3. **code-reviewer** (agent) - Automated review

## Keeping Updated

```bash
# Sync latest changes from local skills
cd claude-code-skills/
./sync-from-local.sh

# Commit and push
git add .
git commit -m "Update skills from local"
git push
```

## Creating New Skills

1. Create skill directory: `mkdir my-skill`
2. Create `my-skill/SKILL.md` with YAML frontmatter
3. Document methodology (not implementation)
4. Add clear triggers for auto-activation
5. Test with real scenarios

**Template:**

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

## When to Use
Specific scenarios where this applies

## Methodology
Step-by-step approach to apply
```

## Contributing

Contributions welcome! When adding or modifying skills:

1. Skills provide methodology, not code execution
2. Use clear triggers for auto-activation
3. Document when and how to use
4. Keep focused on single responsibility
5. Test with realistic scenarios

## License

MIT License - See [LICENSE](LICENSE) for details

---

**Repository:** 154+ methodology skills
**Categories:** Workflow • Patterns • Frameworks • Languages • Tools • Domains • Creative • Data • Orchestration
**Activation:** Automatic based on triggers and context
