# agent-forge

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

Production-ready Claude Code agents with checklists and MCP integrations—build, test, and maintain in one workspace.

## System Architecture

### 🎯 Core Components
- **22 Specialized Agents**: Tiered collection from orchestration to domain experts
- **37 Slash Commands**: Quick access workflows using latest Claude models (Opus 4.1, Sonnet 4)
- **Automation Scripts**: Install, verify, and score agent quality
- **MCP Integration**: Memory persistence and advanced reasoning capabilities

### 📊 Agent Tiers (22 Total)
- **Tier 0 (Meta)**: `agent-coordinator` - Multi-agent orchestration
- **Tier 1 (Foundation)**: 6 agents - Core engineering (API, testing, review, debugging)
- **Tier 2 (Development)**: 4 agents - Language/platform specialists
- **Tier 3 (Specialists)**: 8 agents - Domain experts (cloud, backend, database, DevOps)
- **Tier 4 (Experts)**: 1 agent - Machine learning/MLOps
- **Tier 6 (Integration)**: 1 agent - Research and documentation
- **Tier 7 (Security)**: 1 agent - Security architecture and compliance

## Quick Start
```bash
# Clone and enter the repository
git clone https://github.com/ubehera/agent-forge.git
cd agent-forge

# Install every agent (user scope)
./scripts/install-agents.sh --user

# Validate frontmatter/tooling before opening a PR
./scripts/verify-agents.sh

# Test agent quality scoring
python3 scripts/quality-scorer.py --agents-dir agents

# Restart Claude Code to load agents
```

## Workflow Patterns

### 🔄 Agent Orchestration
1. **Discovery**: `agent-coordinator` decomposes problems and selects specialists
2. **Implementation**: Foundation/specialist tiers execute domain work
3. **Quality Gates**: Review agents validate readiness (test, security, performance)
4. **Operations**: DevOps agents finalize deployment and monitoring

### 🎯 Common Workflows
- **Feature Development**: `/workflow` → DDD workflow with quality gates
- **API Design**: `/api` → `api-platform-engineer` with OpenAPI/GraphQL
- **Security Review**: `/security-audit` → `security-architect` assessment
- **Performance**: `/performance` → `performance-optimization-specialist`
- **Incident Response**: `sre-incident-responder` → diagnosis → mitigation

## Key Documentation
- `agents/README.md`: Complete agent catalog with invocation triggers
- `agents/AGENT_CHECKLIST.md`: Pre-flight checklist for agent updates
- `agents/TESTING.md`: Comprehensive testing procedures
- `commands/README.md`: Slash command catalog and usage
- `patterns/orchestration/`: Multi-agent coordination patterns
- `prompts/CLAUDE.md`: Operating instructions for Claude Code

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
