# agent-forge

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

Production-ready Claude Code agents with checklists and MCP integrations—build, test, and maintain in one workspace.

## Structure
- `agents/`: Claude Code subagents (`.md` with YAML frontmatter)
- `commands/`, `scripts/`: Optional helpers and maintenance utilities

See `AGENTS.md` for contributor guidelines and `agents/AGENT_CHECKLIST.md` for additions/updates.

## Quick Start
```bash
# Clone and enter the repository
git clone https://github.com/ubehera/agent-forge.git
cd agent-forge

# Install agents for current user (or project)
cp agents/*.md ~/.claude/agents/ \
  || (mkdir -p .claude/agents && cp agents/*.md .claude/agents/)
# Restart Claude Code, then test prompts matching the agent description
```

## License
- Code, documentation, and agents are licensed under Apache License 2.0. See `LICENSE`.

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
