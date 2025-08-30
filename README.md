# agent-forge

Production-ready Claude Code agents with checklists and MCP integrations—build, test, and maintain in one workspace.

## Structure
- `agents/`: Claude Code subagents (`.md` with YAML frontmatter)
- `commands/`, `scripts/`: Optional helpers and maintenance utilities

See `AGENTS.md` for contributor guidelines and `agents/AGENT_CHECKLIST.md` for additions/updates.

## Quick Start
```bash
# Install agents for current user (or project)
cp agents/*.md ~/.claude/agents/ \
  || (mkdir -p .claude/agents && cp agents/*.md .claude/agents/)
# Restart Claude Code, then test prompts matching the agent description
```

## License
- Code (commands, scripts) is licensed under Apache-2.0. See `LICENSE`.
- Documentation and agents are licensed under CC BY 4.0. See `LICENSE-CC`.

## MCP Config
- Location: `./.mcp.json` (project-level). Claude Code merges this with your user-level `~/.mcp.json`.
- Included by default: `memory` and `sequential-thinking` servers via `npx`.
- Enable more servers by editing `./.mcp.json`. Example (disabled by default):
  ```json
  {
    "mcpServers": {
      "aws-docs": {
        "command": "uvx",
        "args": ["awslabs.aws-documentation-mcp-server@latest"],
        "env": { "AWS_REGION": "us-east-1" },
        "disabled": true
      }
    }
  }
  ```
- Tips: do not commit secrets; use environment variables. Toggle servers with `"disabled": true|false`.
