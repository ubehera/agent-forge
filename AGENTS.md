# Repository Guidelines

## Project Structure & Module Organization
- Primary development lives in this repository.
- `agents/`: Claude Code subagents (`.md` with YAML frontmatter).
- `commands/`, `scripts/`: Optional helpers and maintenance utilities.
- Project MCP config is managed at the repo root (`.mcp.json`) when applicable.

## Build, Test, and Development Commands
- Install all local agents (current user):
  ```bash
  cp agents/*.md ~/.claude/agents/
  ```
- Install for this project only:
  ```bash
  mkdir -p .claude/agents && cp agents/*.md .claude/agents/
  ```
- Verify installed agents:
  ```bash
  ls ~/.claude/agents | rg '(api-platform|aws-cloud|system-design)'
  ```
- Restart Claude Code after installing or modifying agents.

## Coding Style & Naming Conventions
- Markdown + YAML frontmatter at top.
- YAML: 2‑space indentation; `kebab-case` for names.
- File names: `kebab-case.md` (e.g., `api-platform-engineer.md`).
- Frontmatter: required `name`, `description`; optional `tools` for minimal, intentional access.

## Testing Guidelines
- Validate automatic routing using prompts matching the agent’s description.
- Check tool restrictions, links, and code block rendering.
- Prefer concise, actionable examples over long narratives.

## Commit & Pull Request Guidelines
- Commits: imperative subject; optional scope (e.g., `agents(api): refine description`).
- PRs: summary, rationale, affected files, and verification steps.
- When adding/renaming agents, update `agents/README.md` and, if standards change, `CLAUDE.md`.

## Security & Configuration Tips
- Review `.mcp.json` before enabling servers; never commit secrets.
- Keep `tools` minimal to reduce permissions and improve performance.
