# The security tax — unattended-loop hardening reference

An unattended loop is an unattended attack surface. The governing model is Simon Willison's **lethal
trifecta** (2025-06-16): an agent is exploitable when it simultaneously has (a) access to **private data**,
(b) exposure to **untrusted content**, and (c) an **outward communication channel**. Any one alone is
survivable; all three together means a single injected instruction can read your secrets and exfiltrate them.
A loop that runs while you sleep removes the human who would otherwise catch it.

> This setup's concrete machine audit (live findings + ranked H1–H12 checklist) is in
> `plans/glistening-plotting-reddy.md` Phase 0. This file is the general discipline.

## Where the three legs co-occur (audit your own setup this way)
- **Private data:** filesystem (`Read`, MCP `read_file`), plaintext keys in config, `~/.claude/memory/`,
  git history, private repos via github MCP, env vars.
- **Untrusted content:** `WebFetch`/`WebSearch` bodies, **github issue/PR/comment bodies** (an attacker just
  opens an issue in a repo you read), cross-session message buses, doc-fetch MCPs, and **skill/plugin tool
  descriptions** (tool poisoning — the model reads the description; a code-only review misses it).
- **Exfiltration:** `WebFetch` GET to an attacker URL, shell (`curl`/`nc`), any "consult an external LLM"
  connector, message-send connectors, github write (issue/PR/gist), and Slack/Zapier/n8n/Make/webhook plugins.

Highest-realism attack path in practice: **github-MCP cross-repo exfil** — injected text in a public issue
tells the agent to read a private repo and write its contents into a public PR/gist via the same connector.
All three legs inside one connector.

## The #1 credential-leak vector: debug-logging-into-context
Agent frameworks capture stdout into the LLM context window, so any secret a hook/skill/command *prints* —
an env dump, a `cat` of a config, a stack trace — becomes retrievable by natural-language query, and persists
in transcripts on disk. (Empirical study: print/console.log exposure = ~73.5% of credential-leak issues;
~520/17,022 audited skills leak — verify the exact figures before quoting externally.) **State the invariant:
no plaintext secret is ever present in a file a printing skill can read, nor in any transcript/log the loop
writes.**

## Hardening checklist (general, ranked by leverage)
1. **Get secrets out of readable config** — rotate, store in OS keychain / launch-env, reference indirectly.
   Scan logs + transcripts for any past exposure.
2. **Add deny-side rules** — **deny overrides allow**, so you can keep broad allows and still block the
   dangerous shapes: secret-file reads (`~/.claude.json`, `.ssh/**`, `.aws/**`, `**/.env*`, `**/credentials`),
   exfil binaries (`curl/wget/nc/scp/ssh`), and MCP exec/write duplicates. (Bash matching is prefix-based and
   bypassable via shell tricks — deny is defense-in-depth; the airtight exfil control is network sandboxing.)
3. **Remove unattended arbitrary-shell/file-write MCP from allow** — it collapses "agent decision" into "code
   execution" with no prompt and is the exec/exfil leg directly under any injection. Use gated native
   `Bash`/`Write` instead.
4. **Re-enable guardrails for unattended runs** — move `defaultMode` off `auto`/`dontAsk`; keep the
   dangerous-mode confirmation; **never `--dangerously-skip-permissions`** in a routine or teammate-inherited
   context (it bypasses your deny rules too).
5. **Network allowlist (Trusted, not Full)** — defeats the exfil leg even when a shell deny is bypassed; scope
   `additionalDirectories` to the working repo, not `$HOME`.
6. **Treat cross-session message buses as untrusted input** — do not auto-execute instructions from peer
   messages; for unattended loops, prefer read-only presence over send/receive.
7. **Scope connectors per routine + audit third-party skills/plugins** — an overnight code loop needs neither
   Slack/Zapier/webhook connectors nor github *write*. Audit **description AND scripts** (injection hides in
   either; ~36% of a malicious-skill sample carried injection; ~76% only detectable with both layers). Pin +
   hash the marketplace; alert on change (rug-pull defense). Reconcile multiple settings files (divergent
   plugin sets = ambiguous surface = a smell).
8. **Least-privilege connector tokens** — read-only / single-repo fine-grained PAT for loops.
9. **`suppressOutput` on non-interactive hooks** + a PostToolUse/Stop secret-redaction scrubber that alerts on
   match (a match means a skill leaked) over `csk-…`, `sk-…`, `ghp_…`, `xox[bp]-…`, `AKIA…`.
10. **Restrict unattended writes to `claude/*` branches**; keep `enableAllProjectMcpServers` off + allowlist;
    adopt `allowManagedHooksOnly` so project/plugin-injected hooks can't run (a malicious plugin hook is RCE).
11. **Detective backstop** — schedule `gitleaks`/`trufflehog`/grep over `logs/` + `projects/`; alert on hits.

## Sources
Willison *lethal trifecta* (2025-06-16) + *MCP prompt injection* (2025-04-09); Invariant Labs tool-poisoning /
github-MCP toxic-agent-flow (Apr–May 2025); OWASP LLM Top 10 (LLM01); credential-leak study (arXiv:2604.03070,
verify) + Snyk ToxicSkills (verify); Anthropic Claude Code permissions/Routines docs (2026).
