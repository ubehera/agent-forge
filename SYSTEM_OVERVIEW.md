# Agent Forge System Overview

Agent Forge is a tiered collection of Claude Code agents built for production engineering workflows. Each agent follows the official sub-agent specification (YAML frontmatter + Markdown body) and is optimized for least-privilege tool access.

## Architecture Summary
- **Tiered layout** (`agents/00-meta` → `agents/07-quality`) keeps ownership and escalation paths explicit.
- **15 active agents** cover orchestration, system design, quality, DevOps, data/ML, security, and research.
- **Automation scripts** (`scripts/install-agents.sh`, `scripts/verify-agents.sh`, `scripts/quality-scorer.py`) provide install, validation, and scoring loops.
- **Metadata** (`configs/agent-metadata.json`) mirrors the directory structure for routing and reporting.

## Tier Breakdown
- **Meta (Tier 0)** — `agent-coordinator` manages delegation, dependency ordering, and quality gates across agents.
- **Foundation (Tier 1)** — `api-platform-engineer`, `code-reviewer`, `error-diagnostician`, `performance-optimization-specialist`, `system-design-specialist`, `test-engineer`.
- **Development (Tier 2)** — `frontend-expert` covers modern UI; `mobile-specialist` delivers native/cross-platform apps; `python-expert` and `typescript-architect` provide language-idiomatic services.
- **Specialists (Tier 3)** — `aws-cloud-architect`, `backend-architect`, `data-pipeline-engineer`, `database-architect`, `devops-automation-expert`, `full-stack-architect`, `observability-engineer`, `sre-incident-responder`.
- **Experts (Tier 4)** — `machine-learning-engineer` provides MLOps patterns and model lifecycle guidance.
- **Integration (Tier 6)** — `research-librarian` sources authoritative references and standards.
- **Quality & Security (Tier 7)** — `security-architect` owns threat models, compliance overlays, and secure design reviews.

## Workflow Pattern
1. **Discovery & Orchestration** — `agent-coordinator` decomposes problem statements, selects specialists, and ensures context sharing.
2. **Implementation** — Foundation and Specialist tiers execute domain work, delegating research to `research-librarian` and security considerations to `security-architect` as needed.
3. **Quality Gate** — `test-engineer`, `code-reviewer`, and `performance-optimization-specialist` confirm readiness before delivery.
4. **Operations** — `devops-automation-expert`, `observability-engineer`, `sre-incident-responder`, and `aws-cloud-architect` finalize deployment, telemetry, and resiliency.

## Tooling Integration
- Each agent declares only the tools it needs (e.g., `frontend-expert` avoids Bash for safety; `devops-automation-expert` keeps Grep for log triage).
- MCP servers are configured via `.mcp.json`; agents automatically adopt whichever servers the host environment exposes.

## Maintenance Checklist
- Run `./scripts/verify-agents.sh` on every change to catch frontmatter drift.
- Keep `configs/agent-metadata.json`, `agents/README.md`, and `docs/IMPLEMENTATION_ROADMAP.md` synchronized with the live roster.
- Record major changes in `docs/IMPLEMENTATION_ROADMAP.md` and add orchestration recipes to `patterns/` when new collaboration flows emerge.
- Use `python3 scripts/quality-scorer.py --agent <path>` to spot regressions before review.

Agent Forge aims for production-ready clarity: a predictable structure, explicit hand-offs, and automation that enforces quality without slowing delivery.
