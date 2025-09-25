# Claude Code Custom Slash Commands

> **Production-ready slash commands for the agent-forge ecosystem**

These custom slash commands orchestrate multi-agent workflows, automate development tasks, and ensure quality standards across the ubehera agent-forge project.

## Installation

Commands are automatically available in this project. To install globally:
```bash
# Copy to user commands directory (preserves subdirectories)
cp -r commands/* ~/.claude/commands/

# Or create a symlink for automatic updates
ln -s $(pwd)/commands ~/.claude/commands/ubehera

# Restart Claude Code to load commands
```

## Command Architecture

### Security & Design Principles
- **Least Privilege**: Minimal tool permissions with specific restrictions
- **Agent Delegation**: Complex operations delegated to specialist agents
- **Input Validation**: All user inputs sanitized and validated
- **Quality Gates**: Progressive validation at each workflow stage
- **Error Handling**: Graceful failures with actionable guidance

### Command Structure
```yaml
Frontmatter Fields:
  description: Brief command purpose
  args: <required> [optional] [--flag value]
  tools: Specific tools with restrictions (e.g., Bash(npm test:*))
  model: claude-3-5-haiku-20241022 or claude-3-5-sonnet-20241022
```

## Command Catalog

### 🎯 Core Workflows
- `/workflow` - Execute complete DDD workflow with quality gates
- `/feature` - Full-stack feature development pipeline
- `/api` - Design APIs with api-platform-engineer
- `/deploy` - Review and deployment with safety checks

### 🤖 Agent Orchestration
- `/agent <name> <task>` - Invoke specific agent with context
- `/orchestrate` - Coordinate multi-agent workflows
- `/team` - Form specialized agent teams
- `/parallel-execution` - Run agents in parallel

### ✅ Quality & Testing
- `/test [scope]` - Comprehensive testing with coverage gates
- `/review [scope]` - Code review with multi-level validation
- `/performance [target]` - Performance analysis and optimization
- `/security-audit` - Security assessment and remediation
- `/quality-gates` - Multi-dimensional quality validation

### 🔧 Development Tools
- `/debug <error>` - Intelligent debugging assistance
- `/quick-fix <issue>` - Quick fixes for common issues
- `/docs <library>` - Fetch documentation
- `/search` - Multi-source intelligent search

### 📦 Project Management
- `/install-agents` (`setup/install-agents.md`) - Install repository agents
- `/verify-agents` (`quality/verify-agents.md`) - Validate agent configuration
- `/score-agents` (`quality/score-agents.md`) - Quality scoring for agents
- `/release-prepare` (`ops/release-prepare.md`) - Automated release preparation

### 🚀 Automation & DevOps
- `/deploy-pipeline` (`automation/deploy-pipeline.md`) - CI/CD pipeline setup
- `/health-check` (`automation/health-check.md`) - Infrastructure health monitoring
- `/batch-update` (`automation/batch-update.md`) - Batch operations with rollback
- `/sync-upstream` (`ops/sync-upstream.md`) - Repository synchronization
- `/workflow-automation` (`git/workflow-automation.md`) - Git workflow automation
- `/cleanup-automation` (`maintenance/cleanup-automation.md`) - Repository cleanup

## Usage Examples

### Feature Development
```bash
# Complete feature with DDD workflow
/workflow "user authentication system" --level enterprise

# Quick feature implementation
/feature "payment processing" --api-first

# API-first development
/api payment-service --spec openapi --version v2
```

### Quality Assurance
```bash
# Comprehensive testing
/test src/auth --coverage-target 90 --type all

# Strict code review
/review PR-123 --level strict

# Performance optimization
/performance api/users --metric latency --optimize

# Security audit
/security-audit --comprehensive
```

### Agent Coordination
```bash
# Direct agent invocation
/agent python-expert "Optimize data pipeline"

# Multi-agent orchestration
/orchestrate "microservices migration" --quality enterprise

# Parallel agent execution
/parallel-execution "comprehensive refactoring"
```

### Development Utilities
```bash
# Debug complex issues
/debug "TypeError: Cannot read property 'x' of undefined"

# Quick fixes
/quick-fix "eslint errors" --auto-fix

# Documentation lookup
/docs react hooks
```

## Quality Levels

### MVP (Minimum Viable Product)
- 70% quality gates
- Basic validation and testing
- Fast iteration focus

### Standard (Production Ready)
- 85% quality gates
- Comprehensive testing
- Performance validated
- Security reviewed

### Enterprise (Mission Critical)
- 95% quality gates
- Full compliance audits
- Complete documentation
- Extensive monitoring

## Command Development

### Creating New Commands

1. **Choose appropriate directory**:
   - `workflows/` - Multi-step processes
   - `agents/` - Agent-specific commands
   - `quality/` - Validation and testing
   - `utils/` - Helper utilities

2. **Use standard frontmatter**:
   ```yaml
   ---
   description: Clear, concise description
   args: <required> [optional] [--flag value]
   tools: Task, Read  # Minimal permissions
   model: claude-3-5-haiku-20241022  # Or sonnet for complex tasks
   ---
   ```

3. **Follow security principles**:
   - Validate all inputs
   - Use least privilege for tools
   - Delegate dangerous operations to agents
   - Include error handling

4. **Test thoroughly**:
   ```bash
   # Validate command structure
   ./scripts/verify-commands.sh

   # Test with sample inputs
   /your-command "test input"
   ```

## Integration with Agent Ecosystem

Commands seamlessly integrate with 30+ specialized agents:
- **Foundation Tier**: Core development (API, review, test, debug)
- **Development Tier**: Language specialists (Python, TypeScript, frontend)
- **Specialist Tier**: Domain experts (cloud, database, DevOps)
- **Expert Tier**: Advanced capabilities (ML, security, research)

## Best Practices

1. **Start with `/workflow`** for complex multi-phase features
2. **Use `/agent`** for direct specialist invocation
3. **Run `/test`** and `/review`** before deployments
4. **Leverage `/performance`** for optimization
5. **Apply `/quick-fix`** for common issues

## Troubleshooting

### Command Not Found
- Ensure Claude Code is restarted after adding commands
- Check command file has `.md` extension
- Verify frontmatter is valid YAML

### Permission Errors
- Review `tools` declaration in frontmatter
- Use specific tool restrictions (e.g., `Bash(npm:*)`)
- Delegate privileged operations to agents

### Execution Failures
- Check argument format matches `args` pattern
- Verify required agents are installed
- Review error messages for guidance

## Contributing

When adding or modifying commands:
1. Follow the established patterns
2. Update this README
3. Test with various inputs
4. Run validation scripts
5. Document usage examples
