# CLAUDE.md

This file provides guidance to Claude Code when working with this repository (agent-forge).

## Project Overview
- Workspace for building and maintaining Claude Code subagents.
- Agents live under `agents/` as Markdown files with YAML frontmatter.

## Agent Format (Required)
Each agent is a Markdown file with YAML frontmatter followed by the system prompt body:

```markdown
---
name: agent-name
description: When and why this agent should be invoked
tools: Read, Write, MultiEdit, Bash # optional, use minimal set
---

Agent system prompt content...
```

### Frontmatter Rules
- `name`: unique, `kebab-case`.
- `description`: specific, action‑oriented; drives automatic routing.
- `tools` (optional): declare only what’s required to reduce permissions and latency.

## Locations
- Agents: `agents/*.md`
- Docs: `AGENTS.md`, `CONTRIBUTING.md`, `agents/AGENT_CHECKLIST.md`

## Install & Test
```bash
# Install agents (current user)
cp agents/*.md ~/.claude/agents/

# Or install for project only
mkdir -p .claude/agents && cp agents/*.md .claude/agents/

# Verify
ls ~/.claude/agents | rg '(api-platform|aws-cloud|system-design)'
```
- Restart Claude Code after installation.
- Validate auto‑routing with prompts matching each agent’s description.

## Tool Selection Guidelines
- Read/Write/Edit: file operations
- MultiEdit: coordinated multi-file changes
- Bash: shell commands
- Grep/Glob: search helpers (if available)
- WebFetch/WebSearch: external info (use only when needed)

Keep tools minimal per agent for performance and security.

## MCP Notes
- If using MCP, configure servers in project `.mcp.json` or user-level `~/.mcp.json`.
- Agents automatically inherit available MCP tools when Claude Code is configured.

## Maintenance
- Keep descriptions up to date for accurate routing.
- Prefer concise, practical examples over long narratives.
- Update `agents/README.md` when adding or renaming agents.

