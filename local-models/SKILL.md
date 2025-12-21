---
name: local-models
description: Use when needing free, private, or fast AI assistance for support tasks like explaining code, analyzing logs, research, or drafts. Routes to local Ollama models (devstral, qwen3-coder, llama4, llama3.2) for zero-cost operations. NOT for writing/editing code - Claude handles all coding.
---

# Local Model Integration (Ollama) - December 2025

## When This Skill Activates
- User asks to "use local model" or "use ollama"
- Privacy-sensitive analysis needed (credentials, internal code)
- High-volume repetitive tasks (many quick queries)
- Offline work required
- User wants free/zero-cost assistance
- Research or explanation tasks
- Draft generation before Claude refinement

## Critical Rule: Claude Does ALL Coding

**Local models = Support tasks ONLY**
**Claude (Opus/Sonnet) = ALL code writing/editing**

Local models assist with understanding, not implementation.

## Available Models (M3 Max 64GB)

| Model | Size | Best For | Alias |
|-------|------|----------|-------|
| **gpt-oss:120b** | 65GB | Deep reasoning, architecture | `reason` |
| **llama4:scout** | 67GB | Multimodal, images | `vision` |
| **qwen3-coder:30b** | 18GB | Long-context (256K) | `deep` |
| **devstral:24b** | 14GB | Code review (68% SWE-Bench) | `code` |
| **gpt-oss:20b** | 13GB | Quick reasoning | `think` |
| **llama3.2** | 2GB | Ultra-fast Q&A (<2s) | `ask` |

## Performance Optimizations (Active)

Environment variables configured in `~/.zshrc`:
```bash
OLLAMA_FLASH_ATTENTION=1    # Faster inference
OLLAMA_KV_CACHE_TYPE=q8_0   # 47% memory savings
OLLAMA_METAL=1              # Apple Silicon GPU
OLLAMA_MAX_LOADED_MODELS=3  # Keep models hot
OLLAMA_NUM_PARALLEL=4       # Parallel requests
OLLAMA_KEEP_ALIVE="10m"     # Avoid cold starts
```

## Task Routing

### Use Local Models For:
| Task | Model | Alias |
|------|-------|-------|
| Explain this code | llama3.2 | `ask` |
| Analyze logs (large) | qwen3-coder:30b | `deep` |
| What does this error mean | llama3.2 | `ask` |
| Research architecture | gpt-oss:20b | `think` |
| Review image/screenshot | llama4:scout | `vision` |
| Draft documentation | llama3.2 | `ask` |
| Code understanding | devstral:24b | `code` |

### Claude Handles (NOT Local):
- Writing new code
- Editing existing code
- Bug fixes
- Test generation
- Refactoring
- Any file modifications

## Quick Aliases (Terminal)

```bash
# Direct aliases
ask "What is dependency injection?"       # llama3.2 (<2s)
code "Explain this function"              # devstral:24b (68% SWE-Bench)
think "Quick comparison"                  # gpt-oss:20b
deep "Analyze this large codebase"        # qwen3-coder:30b (256K)
reason "Design a caching architecture"    # gpt-oss:120b (best reasoning)
vision                                    # llama4:scout (multimodal)

# Functions
ask_ai "Quick question"                   # Pipe to llama3.2
code_ai "Code explanation"                # Pipe to devstral
think_ai "Reasoning task"                 # Pipe to gpt-oss:20b
analyze_ai file.py "Review this"          # File + qwen3-coder

# Smart Router (auto-selects model)
ollama-router.py "your query"             # Routes to optimal model
```

## Within Claude Conversation

Say: "Use local model to explain this" or "Ask ollama about..."

Claude will:
1. Route to appropriate local model via Bash
2. Get response
3. Integrate into conversation

## Advanced: Intelligent Routing

For automatic model selection based on task complexity:

```bash
# Install RouteLLM (optional)
pip install routellm

# Routes simple→local, complex→cloud automatically
# 85% cost reduction while maintaining quality
```

## Advanced: Semantic Caching

For repeated similar queries:

```bash
# Install GPTCache (optional)
pip install gptcache

# 10x cost reduction, 100x speed on cache hits
```

## Cost Comparison

| Approach | Cost per 1K queries |
|----------|---------------------|
| Cloud API (Sonnet) | ~$15 |
| Cloud API (Opus) | ~$75 |
| Local Models | $0 |
| With RouteLLM | ~$2.25 (85% savings) |
| With GPTCache | ~$0.10 (99% savings) |

## Model Selection Guide

```
Need speed?        → llama3.2 (2GB, <1s response)
Need context?      → qwen3-coder:30b (256K tokens)
Need code insight? → devstral:24b (68% SWE-Bench)
Need reasoning?    → gpt-oss:20b
Need vision?       → llama4:scout
```

## Privacy Benefits

Local models keep sensitive data on your machine:
- API keys and credentials
- Internal business logic
- Proprietary algorithms
- Customer data analysis

## Cloud Models via Ollama (Optional)

Access cloud-scale models through Ollama:
```bash
ollama run deepseek-v3.1:671b-cloud    # Best reasoning
ollama run qwen3-coder:480b-cloud      # Best coding
```

## Anti-Patterns

- Using local models to write production code (quality risk)
- Skipping local for simple explanations (cost waste)
- Using llama3.2 for complex reasoning (wrong tool)
- Using large models for simple Q&A (slow, wasteful)
- Not using aliases (slower workflow)

## Verification

```bash
# Check models
ollama list

# Check running models
ollama ps

# Test quick response
ask "Hello"

# Test code model
code "def fib(n): pass"
```

## Monitoring

```bash
# Memory usage
ollama ps

# Model details
ollama show devstral:24b

# GPU utilization (Activity Monitor → GPU History)
```

## Detailed Model Guide

See `~/.claude/skills/local-models/MODEL_GUIDE.md` for:
- Detailed use cases per model
- Performance overlap zones
- When to use which model
- Chaining strategies
- Decision flowchart
