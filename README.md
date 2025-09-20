# agent-forge

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

Production-ready Claude Code agents with checklists and MCP integrations—build, test, and maintain in one workspace.

## Structure
- `agents/`: Claude Code subagents (`.md` with YAML frontmatter) grouped by tiered directories
- `commands/`, `scripts/`: Optional helpers and maintenance utilities (installation, verification, scoring)

See `../AGENTS.md` for contributor guidelines and `agents/AGENT_CHECKLIST.md` for additions/updates.

## Quick Start
```bash
# Clone and enter the repository
git clone https://github.com/ubehera/agent-forge.git
cd agent-forge

# Install every agent (user scope)
./scripts/install-agents.sh --user

# Validate frontmatter/tooling before opening a PR
./scripts/verify-agents.sh

# (Optional) Manual copy fallback
find agents -mindepth 2 -maxdepth 2 -name '*.md' -print0 \
  | xargs -0 cp -t ~/.claude/agents/
```

## Documentation Map
- `SYSTEM_OVERVIEW.md`: Tier breakdown, workflow lifecycle, and hand-off patterns
- `docs/IMPLEMENTATION_ROADMAP.md`: Delivered milestones and upcoming specialist backlog
- `agents/README.md`: Current agent catalog with triggers, tiers, and toolsets
- `../AGENTS.md`: Contributor guide for the entire workspace
- `agents/AGENT_CHECKLIST.md`: Pre-flight verification for new or updated agents
- `prompts/CLAUDE.md`: Operating instructions used by Claude Code when working in this repo
- `docs/README.md`: Index of project documentation for quick navigation

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
