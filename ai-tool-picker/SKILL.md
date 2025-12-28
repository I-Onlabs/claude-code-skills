---
name: ai-tool-picker
description: Guide for choosing the right AI coding tool for the task. Use when user asks "which AI should I use", "should I use Claude or Cursor", "what's the best tool for X", or when helping decide between Claude Code, Cursor, Windsurf, VSCode + Copilot, Gemini, Grok, Codex, Qwen, or this Claude interface.
---

# AI Tool Picker

Quick reference for vibecoders juggling multiple AI tools.

## Decision Tree

**What are you trying to do?**

### Writing/Editing Code in a File
→ **Cursor** or **Windsurf** (in-editor, sees your files)
→ **Claude Code** (terminal-based, good for refactors across many files)

### Quick Question or Concept
→ **Grok** (fast, real-time info)
→ **This Claude** (if you're already here)
→ **ChatGPT** (familiar, broad knowledge)

### Long Codebase or Big Context
→ **Gemini** (huge context window — 1M+ tokens)
→ **Claude Code** (can navigate and read files itself)

### Creating Files, Docs, Diagrams, Presentations
→ **This Claude** (creates downloadable files, artifacts, browser control)

### Debugging Error Messages
→ Paste into **Cursor/Windsurf** (sees your code)
→ Or paste into **This Claude** with the file

### Agentic Tasks (multi-step, autonomous)
→ **Claude Code** (runs commands, edits files, loops until done)
→ **Codex CLI** (OpenAI's agent)
→ **Aider** (open source, git-aware)

### Research + Code
→ **This Claude** (web search + file creation)
→ **Gemini** (good at research, massive context)
→ **Perplexity** (research-first, then code)

### Image Generation / Vision
→ **ChatGPT/DALL-E** (image generation)
→ **Claude** (vision analysis, can see images)
→ **Gemini** (vision + generation)

---

## Tool Profiles

| Tool | Best For | Limitations |
|------|----------|-------------|
| **Cursor** | In-editor coding, tab completion, inline edits | Needs IDE open, per-file focus |
| **Windsurf** | Similar to Cursor, Cascade flow | Same as Cursor |
| **Claude Code** | Terminal agent, multi-file refactors, autonomous | Command line only |
| **This Claude** | Files, research, browser control, conversations | Not in your IDE |
| **Gemini** | Huge context (2M tokens), research | Can be verbose |
| **Grok** | Fast answers, real-time X/Twitter data | Less depth |
| **ChatGPT/GPT-4** | Familiarity, DALL-E, plugins | Rate limits |
| **Codex CLI** | OpenAI's terminal agent | Newer, less mature |
| **Qwen** | Free/open, good at code | Less polish |
| **Aider** | Open source, git-integrated | Setup required |
| **Copilot** | VSCode integration, autocomplete | Less agentic |

---

## Common Scenarios

**"I need to refactor authentication across 20 files"**
→ Claude Code — it can navigate, plan, and execute

**"Help me understand this error in my React component"**
→ Cursor/Windsurf — sees your code context

**"Create a presentation about my project"**
→ This Claude — makes PowerPoint files

**"What's the best way to structure a Next.js app?"**
→ Any of them, but Gemini/Claude for long explanations

**"I'm stuck and don't know what's wrong"**
→ Start with Cursor (sees your files), escalate to Claude Code if complex

**"Build me a landing page from scratch"**
→ Cursor/Windsurf for iterative coding, or This Claude for a complete artifact

**"Analyze this 500-page PDF"**
→ Gemini (massive context) or This Claude (can read PDFs)

**"What's happening in the news about X?"**
→ Grok (real-time) or This Claude (web search)

**"Generate an image for my app"**
→ ChatGPT/DALL-E, Midjourney, or dedicated image tools

---

## Pro Tips

1. **Stay in one tool per task** — context switching loses context
2. **Cursor/Windsurf for flow** — stay in editor, stay in zone
3. **Claude Code for big jobs** — let it run while you do other things
4. **This Claude for output** — when you need actual files to download
5. **Gemini for massive context** — paste entire repos
6. **Match the tool to the output** — need a file? Use something that makes files
7. **Use MCP servers** — extend Claude Code with custom tools

---

## Model Selection Within Tools

**When you can choose the model:**

| Task | Best Model |
|------|------------|
| Complex reasoning | Claude Opus, GPT-4, Gemini Pro |
| Fast iteration | Claude Sonnet, GPT-4o-mini |
| Long context | Gemini 1.5 Pro (2M tokens) |
| Cost-sensitive | Claude Haiku, GPT-4o-mini |
| Code generation | Claude Sonnet, GPT-4 |

---

## When Tools Hit Limits

| Problem | Solution |
|---------|----------|
| Cursor slowing down | Break into smaller files/tasks |
| Claude Code looping | Be more specific, or take over manually |
| Context too long | Summarize, or switch to Gemini |
| Rate limited | Switch tools temporarily |
| AI hallucinates | Ask for sources, or verify with another AI |
| Need real-time data | Use Grok or Claude with web search |
| Tool doesn't support feature | Chain tools — generate in one, edit in another |

---

## Tool Combos That Work Well

1. **Research → Implement**: This Claude (research + plan) → Cursor (code it)
2. **Prototype → Polish**: This Claude (quick artifact) → Cursor (refine)
3. **Debug → Fix**: Paste error in Claude → Apply fix in Cursor
4. **Big Refactor**: Claude Code (autonomous) → Cursor (review/tweak)
5. **Learn → Build**: Gemini (explain concepts) → Cursor (practice)
