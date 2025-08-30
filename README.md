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
- Code (commands, scripts): PolyForm Small Business 1.0.0. Free for orgs ≤ $250k trailing‑12‑months revenue. Commercial use above the cap requires a paid license. See `LICENSE` and `COMMERCIAL_LICENSE.md`.
- Documentation and agents: CC BY‑NC‑SA 4.0 (noncommercial, share alike, with attribution). See `LICENSE-CC`.
- Commercial licensing: message @ubehera on GitHub to request terms and pricing.

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
