# agent-forge

Production-ready Claude Code agents with checklists and MCP integrations—build, test, and maintain in one workspace.

## Structure
- `agents/`: Claude Code subagents (`.md` with YAML frontmatter)
- `commands/`, `scripts/`: Optional helpers and maintenance utilities

See `AGENTS.md` for contributor guidelines and `ubehera/agents/AGENT_CHECKLIST.md` for additions/updates.

## Quick Start
```bash
# Install agents for current user (or project)
cp ubehera/agents/*.md ~/.claude/agents/ \
  || (mkdir -p .claude/agents && cp ubehera/agents/*.md .claude/agents/)
# Restart Claude Code, then test prompts matching the agent description
```

## License
- Code (commands, scripts) is licensed under Apache-2.0. See `LICENSE`.
- Documentation and agents are licensed under CC BY 4.0. See `LICENSE-CC`.

