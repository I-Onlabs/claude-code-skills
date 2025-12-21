---
name: project-context
description: Use when starting work on any project to load project-specific context, conventions, and patterns. Triggers on project initialization, "how does this project work", or before making changes that should follow project conventions.
---

# Project Context Loading

## When This Skill Activates
- Starting a new conversation about a project
- Questions about "how does X work in this project"
- "What are the conventions here"
- Before making changes that should follow project conventions
- When you need to understand project structure

## Process

### 1. Check Project Root
Look for these files in order:
- `.claude/CLAUDE.md` - Project-specific instructions
- `.claude/settings.json` - Project settings
- `CLAUDE.md` - Root-level instructions
- `README.md` - Project documentation

### 2. Check for Project Skills
Look for `.claude/skills/` directory containing project-specific skills.

### 3. Identify Project Type
Detect from files present:
- `package.json` → Node.js/JavaScript
- `pyproject.toml` or `requirements.txt` → Python
- `Cargo.toml` → Rust
- `go.mod` → Go
- `pom.xml` or `build.gradle` → Java

### 4. Load Relevant Context
Based on project type, identify:
- Entry points
- Test locations
- Build commands
- Deployment patterns

## Integration with Your Setup

- **Complements CLAUDE.md auto-delegation rules** - Skills load methodology, agents execute
- **Works with existing agents** - They inherit project context
- **Informs command execution** - Commands know project patterns

## Quick Reference

```
Project context loading checklist:
[ ] Found project root
[ ] Read CLAUDE.md/README.md
[ ] Identified project type
[ ] Located test directory
[ ] Know build/run commands
```
