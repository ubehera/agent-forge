# Agent System Implementation Roadmap

Roadmap for evolving the agent-forge workspace while maintaining production readiness.

## Completed
- Tiered directory layout (`00-meta` … `07-quality`) with 22 active agents migrated.
- Automation tooling: `install-agents.sh`, `verify-agents.sh`, and `quality-scorer.py` wired into the workflow.
- Foundational coverage: system design, API, testing, performance, security, language runtime, cloud, data, MLOps, DevOps, observability, and research.
- Delivered backlog items: `python-expert`, `backend-architect`, `database-architect`, `observability-engineer`, `mobile-specialist`, `typescript-architect`, `sre-incident-responder`.

## In Progress
- Refresh metadata (`configs/agent-metadata.json`, taxonomy docs) whenever agents change.
- Harden quality scoring heuristics to cover collaboration signals and invocation accuracy.
- Expand documentation with concrete invocation transcripts for critical personas.

## Near-Term Additions
1. **Domain specialists** – start with a fintech/compliance expert.
2. **Analytics & BI lead** – warehouse governance, dashboards, self-service data.
3. **AI safety reviewer** – responsible AI assessments, guardrails, audit trails.

Each addition should include:
- Updated tier placement and routing rules.
- Fresh tests in `agents/TESTING.md`.
- Quality score ≥ 8.0 using `quality-scorer.py`.

## Quality Gates
- Scripts must pass `./scripts/verify-agents.sh` in CI.
- Coverage of invocation scenarios documented in `agents/TESTING.md`.
- Metadata and taxonomy must list every active agent exactly once.

## Collaboration Protocol
- Use `agent-coordinator` for cross-agent deliverables and to enforce quality gates.
- Document significant architectural decisions as ADRs (see `docs/` if new files are added).
- Store reusable orchestration stories under `patterns/` to keep best practices discoverable.
