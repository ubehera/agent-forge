# Contributing

Thanks for improving this repository. Please read this short guide before opening a PR.

## Scope
- Primary contributions target `ubehera/` (agents, commands, scripts).

## Start Here
- Read: `AGENTS.md` (repo guidelines)
- Standards: `CLAUDE.md` (agent spec and workflows)
- Agent checklist: `agents/AGENT_CHECKLIST.md`

## Local Validation
```bash
# Install agents for current user (or project)
cp ubehera/agents/*.md ~/.claude/agents/ \
  || (mkdir -p .claude/agents && cp ubehera/agents/*.md .claude/agents/)
# Restart Claude Code, then test prompts matching the agent description
```

## Pull Requests
- Use the PR template in `.github/PULL_REQUEST_TEMPLATE.md`.
- Write clear, imperative commit messages (e.g., `agents(api): refine description`).
- Include what changed, why, and verification steps.

## Documentation Updates
- When adding/renaming agents, update:
  - `agents/README.md` (matrix and triggers)
  - `AGENTS.md` (stays accurate and concise)
  - `CLAUDE.md` (if standards/workflows change)

## Security & Configuration
- Review `.mcp.json` changes carefully; never commit secrets. Prefer env vars.
- Keep `tools` minimal per agent to reduce permissions and improve performance.

