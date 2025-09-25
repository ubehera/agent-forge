---
description: Execute complete DDD workflow with quality gates for feature development
args: <feature-description> [--level mvp|standard|enterprise]
tools: TodoWrite, Task, Read, Write, MultiEdit
model: claude-opus-4-1-20250805
---

# DDD Workflow Orchestration

Execute the complete Domain-Driven Design workflow for **$ARGUMENTS** with progressive quality gates.

## Workflow Phases

### Phase 1: Requirements Analysis (Quality Gate: 90%)
- Extract business outcomes and success criteria
- Document acceptance criteria and constraints
- Identify risks and propose prototypes
- Use Task tool to delegate to system-design-specialist if complexity is high

### Phase 2: Domain Modeling (Quality Gate: 85%)
- Define bounded contexts and aggregates
- Map domain events and commands
- Establish ubiquitous language
- Delegate to appropriate domain experts via Task

### Phase 3: Architecture Design (Quality Gate: 90%)
- Select architectural style with rationale
- Define data strategy and NFRs
- Specify performance targets (P95 < 200ms, 99.9% SLA)
- Use Task to invoke system-design-specialist for review

### Phase 4: API Specification (Quality Gate: 95%)
- Design REST/GraphQL/Event contracts
- Define authentication and authorization
- Create comprehensive examples
- Delegate to api-platform-engineer via Task

### Phase 5: Implementation (Quality Gate: 80%)
- Build core domain logic with tests
- Implement API layer with validation
- Create UI components if needed
- Use appropriate language specialists (python-expert, typescript-architect, etc.)

### Phase 6: Testing & Validation (Quality Gate: 90%)
- Unit tests (>80% coverage)
- Integration tests (>70% coverage)
- E2E tests for critical paths
- Performance validation (meet P95 targets)
- Security scan with security-architect

### Phase 7: Deployment Preparation
- Review with code-reviewer
- Performance analysis with performance-optimization-specialist
- Security audit if enterprise level
- Documentation and handoff

## Quality Levels

- **MVP**: 70% gates, basic validation, fast iteration
- **Standard**: 85% gates, comprehensive testing, production-ready
- **Enterprise**: 95% gates, full compliance, audit trails

## Progress Tracking

Use TodoWrite throughout to track:
1. Phase completion status
2. Quality gate achievements
3. Blocked items requiring resolution
4. Agent delegation tasks

## Example Usage

```
/workflow "user authentication system" --level enterprise
/workflow "payment processing API" --level standard
/workflow "internal admin dashboard" --level mvp
```

## Next Steps

After workflow completion:
1. Run `/quality-gates` for final validation
2. Use `/review-and-deploy` for deployment
3. Execute `/performance-monitor` for baseline establishment