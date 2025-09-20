# Agent Testing & Validation Checklist

This document provides comprehensive testing procedures for validating the ubehera agent collection after enhancements and updates.

## Pre-Testing Setup

### Installation Verification
```bash
# Install or refresh all agents locally
./scripts/install-agents.sh --user

# Validate structure and metadata
./scripts/verify-agents.sh

# Confirm expected agents exist in Claude Code's directory
find ~/.claude/agents -maxdepth 1 -type f -name '*.md' \
  | grep -E '(agent-coordinator|api-platform-engineer|code-reviewer|error-diagnostician|performance-optimization-specialist|system-design-specialist|test-engineer|frontend-expert|aws-cloud-architect|data-pipeline-engineer|devops-automation-expert|full-stack-architect|machine-learning-engineer|research-librarian|security-architect)'

# Count should be 22 agents
find ~/.claude/agents -maxdepth 1 -type f -name '*.md' | wc -l
```

### Restart Requirement
- [ ] **Restart Claude Code** after installing or modifying agents
- [ ] **Clear browser cache** if using web interface
- [ ] **Verify agent availability** in Claude Code interface

## Invocation Testing

Test each agent's automatic invocation by using trigger keywords from their enhanced descriptions:

### 1. api-platform-engineer
**Test Phrases:**
- [ ] "Design a REST API for user management"
- [ ] "Create OpenAPI specification for my service"
- [ ] "Set up API gateway with Kong"
- [ ] "Implement GraphQL schema for products"
- [ ] "Build a developer portal for our APIs"

**Expected Result:** Should invoke `api-platform-engineer`

### 2. aws-cloud-architect  
**Test Phrases:**
- [ ] "Design AWS infrastructure for a web application"
- [ ] "Create CloudFormation template for EKS cluster"
- [ ] "Set up serverless architecture with Lambda"
- [ ] "Implement multi-region deployment on AWS"
- [ ] "Design cost-optimized cloud architecture"

**Expected Result:** Should invoke `aws-cloud-architect`

### 3. data-pipeline-engineer
**Test Phrases:**
- [ ] "Build an ETL pipeline with Apache Spark"
- [ ] "Create streaming data pipeline with Kafka"
- [ ] "Set up Airflow for data orchestration"
- [ ] "Design data lake architecture"
- [ ] "Implement real-time analytics pipeline"

**Expected Result:** Should invoke `data-pipeline-engineer`

### 4. devops-automation-expert
**Test Phrases:**
- [ ] "Create CI/CD pipeline with GitHub Actions"
- [ ] "Set up GitOps workflow with ArgoCD"
- [ ] "Implement infrastructure as code with Terraform"
- [ ] "Design deployment automation strategy"
- [ ] "Configure monitoring with Prometheus and Grafana"

**Expected Result:** Should invoke `devops-automation-expert`

### 5. full-stack-architect
**Test Phrases:**
- [ ] "Build a React application with Next.js"
- [ ] "Design full-stack web application architecture"
- [ ] "Implement authentication in a TypeScript app"
- [ ] "Create modern JavaScript frontend"
- [ ] "Set up state management with Redux"

**Expected Result:** Should invoke `full-stack-architect`

### 6. machine-learning-engineer
**Test Phrases:**
- [ ] "Build MLOps pipeline with MLflow"
- [ ] "Train a neural network with PyTorch"
- [ ] "Deploy machine learning model to production"
- [ ] "Implement feature engineering pipeline"
- [ ] "Set up model monitoring and A/B testing"

**Expected Result:** Should invoke `machine-learning-engineer`

### 7. performance-optimization-specialist
**Test Phrases:**
- [ ] "My application is slow, how to optimize it?"
- [ ] "Improve Core Web Vitals for my website"
- [ ] "Optimize database query performance"
- [ ] "Reduce API response time"
- [ ] "Fix performance bottlenecks in my system"

**Expected Result:** Should invoke `performance-optimization-specialist`

### 8. security-architect
**Test Phrases:**
- [ ] "Perform threat modeling for my application"
- [ ] "Implement OWASP security best practices"
- [ ] "Design secure authentication system"
- [ ] "Ensure GDPR compliance in data handling"
- [ ] "Create security architecture for microservices"

**Expected Result:** Should invoke `security-architect`

### 9. system-design-specialist
**Test Phrases:**
- [ ] "Design distributed system for millions of users"
- [ ] "Create scalable microservices architecture"
- [ ] "Implement event-driven architecture"
- [ ] "Design high-availability system"
- [ ] "Handle system scalability challenges"

**Expected Result:** Should invoke `system-design-specialist`

### 10. research-librarian
**Test Phrases:**
- [ ] "Which RFC defines HTTP/2 frame types?"
- [ ] "Compare OpenAPI 3.0 vs 3.1 changes"
- [ ] "Find canonical docs for AWS API Gateway throttling"
- [ ] "Best practices for idempotency keys"
- [ ] "Official spec for JSON Merge Patch"

**Expected Result:** Should invoke `research-librarian`


### 11. agent-coordinator
**Test Phrases:**
- [ ] "Coordinate multiple specialists for a payments launch"
- [ ] "Break this monolith migration into agent-sized tasks"
- [ ] "Design a workflow that routes work between security and devops"
- [ ] "Manage dependencies across frontend, backend, and data teams"
- [ ] "Run a quality gate across all outputs"

**Expected Result:** Should invoke `agent-coordinator`

### 12. code-reviewer
**Test Phrases:**
- [ ] "Review this pull request for security issues"
- [ ] "Identify edge cases in this diff"
- [ ] "Call out missing tests for this feature"
- [ ] "Spot style violations in this Typescript module"
- [ ] "Summarize high-risk findings in this change set"

**Expected Result:** Should invoke `code-reviewer`

### 13. error-diagnostician
**Test Phrases:**
- [ ] "Explain this stack trace from production"
- [ ] "Why is this service returning intermittent 500s?"
- [ ] "Diagnose the root cause for elevated latency"
- [ ] "Help me triage this incident report"
- [ ] "Propose a containment plan for this bug"

**Expected Result:** Should invoke `error-diagnostician`

### 14. test-engineer
**Test Phrases:**
- [ ] "Design an end-to-end test plan for this API"
- [ ] "Recommend regression tests for this feature"
- [ ] "Improve flaky Cypress coverage"
- [ ] "Select frameworks for contract testing"
- [ ] "Explain how to measure test coverage effectively"

**Expected Result:** Should invoke `test-engineer`

### 15. frontend-expert
**Test Phrases:**
- [ ] "Optimize React components for Core Web Vitals"
- [ ] "Design a responsive layout with Tailwind"
- [ ] "Implement an accessible modal in Vue 3"
- [ ] "Debug hydration mismatches in Next.js"
- [ ] "Recommend a state management pattern for complex UI"

**Expected Result:** Should invoke `frontend-expert`

## Agent Quality Testing

### Security & DevOps Integration
Test that each agent includes security and DevOps context:

- [ ] **Security Integration**: Each agent mentions security practices
- [ ] **DevOps Practices**: Each agent includes CI/CD and automation context
- [ ] **Collaborative Workflows**: Each agent references other relevant agents
- [ ] **Integration Patterns**: Each agent describes how it works with others

### Content Validation
- [ ] **Code Examples**: All code examples are syntactically correct
- [ ] **Tool Restrictions**: Each agent uses only allowed Claude Code tools
- [ ] **Frontmatter Format**: YAML frontmatter is properly formatted
- [ ] **Description Quality**: Descriptions include comprehensive trigger keywords

## Cross-Agent Collaboration Testing

Test scenarios that should involve multiple agents:

### 1. Secure API Development
**Request:** "Build a secure REST API with proper authentication and deploy it to AWS"

**Expected Agents:** 
- [ ] `api-platform-engineer` (primary)
- [ ] `security-architect` (for authentication)
- [ ] `aws-cloud-architect` (for deployment)
- [ ] `devops-automation-expert` (for CI/CD)

### 2. ML Platform Development  
**Request:** "Create an end-to-end ML platform with data pipelines and model serving"

**Expected Agents:**
- [ ] `machine-learning-engineer` (primary)
- [ ] `data-pipeline-engineer` (for data processing)
- [ ] `aws-cloud-architect` (for infrastructure)
- [ ] `security-architect` (for data security)

### 3. Performance Optimization
**Request:** "My distributed system is slow and needs optimization for high load"

**Expected Agents:**
- [ ] `performance-optimization-specialist` (primary)
- [ ] `system-design-specialist` (for architecture)
- [ ] `devops-automation-expert` (for monitoring)
- [ ] `security-architect` (for security-performance balance)

## MCP Tool Compatibility Testing

**Note:** These tests only apply if MCP tools are configured in your environment.

### Memory Tools (if available)
- [ ] **mcp__memory__create_entities**: Test with agents that store knowledge
- [ ] **mcp__memory__create_relations**: Test relationship creation
- [ ] **mcp__memory__search_nodes**: Test knowledge retrieval

### IDE Tools (if available)
- [ ] **mcp__ide__getDiagnostics**: Test with performance-optimization-specialist
- [ ] **mcp__ide__executeCode**: Test with machine-learning-engineer

### Fetch Tools (if available)
- [ ] **mcp__fetch**: Test with api-platform-engineer for API validation

### Sequential Thinking (if available)
- [ ] **mcp__sequential-thinking**: Test with system-design-specialist for complex problems

## Performance Testing

### Tool Restriction Validation
- [ ] **api-platform-engineer**: Uses only Read, Write, MultiEdit, Bash, Grep, WebFetch
- [ ] **aws-cloud-architect**: Uses only Read, Write, MultiEdit, Bash, Task, WebSearch
- [ ] **data-pipeline-engineer**: Uses only Read, Write, MultiEdit, Bash, Task
- [ ] **devops-automation-expert**: Uses only Read, Write, MultiEdit, Bash, Task, Grep
- [ ] **full-stack-architect**: Uses only Read, Write, MultiEdit, Bash, Task, WebSearch
- [ ] **machine-learning-engineer**: Uses only Read, Write, MultiEdit, Bash, Task, WebSearch
- [ ] **performance-optimization-specialist**: Uses only Read, Write, MultiEdit, Bash, Grep, Task
- [ ] **security-architect**: Uses only Read, Write, MultiEdit, Bash, Grep, WebSearch
- [ ] **system-design-specialist**: Uses only Read, Write, MultiEdit, WebSearch, Task

### Response Quality
- [ ] **Response Time**: Agents respond within reasonable time
- [ ] **Tool Usage**: Agents use tools efficiently
- [ ] **Code Quality**: Generated code is production-ready
- [ ] **Documentation**: Responses include proper documentation

## Regression Testing

### Original Functionality
Verify that enhancements don't break existing functionality:

- [ ] **Core Expertise**: All original technical knowledge is preserved
- [ ] **Code Examples**: Existing code examples still work correctly
- [ ] **Success Metrics**: Original KPIs and metrics are maintained
- [ ] **Quality Standards**: Original quality checklists are preserved

### Enhancement Validation
- [ ] **Better Invocation**: New descriptions improve automatic selection
- [ ] **Security Context**: Security practices are mentioned appropriately
- [ ] **DevOps Integration**: DevOps practices are included where relevant
- [ ] **Agent Collaboration**: Cross-agent references work as expected

## Test Results Documentation

### Invocation Accuracy
```
Agent Name                     | Test Pass Rate | Issues Found
-------------------------------|----------------|-------------
api-platform-engineer         | __/5          | 
aws-cloud-architect           | __/5          |
data-pipeline-engineer        | __/5          |
devops-automation-expert      | __/5          |
full-stack-architect          | __/5          |
machine-learning-engineer     | __/5          |
performance-optimization-specialist | __/5   |
security-architect            | __/5          |
system-design-specialist      | __/5          |
```

### Overall Assessment
- **Total Test Cases**: 45 individual invocation tests + collaboration tests
- **Pass Threshold**: >90% for production readiness
- **Critical Issues**: Document any agents that fail multiple tests
- **Performance Impact**: Note any significant response time changes

## Troubleshooting

### Common Issues
1. **Agent Not Invoked**: Check description keywords, restart Claude Code
2. **Wrong Agent Selected**: Refine trigger keywords in description
3. **MCP Tools Not Working**: Verify MCP server configuration
4. **Performance Degradation**: Check tool restrictions and complexity

### Resolution Steps
1. **Review agent descriptions** for clarity
2. **Test with more specific keywords**
3. **Check Claude Code logs** for errors
4. **Verify MCP server status** if using MCP tools

---

**Testing Completed Date**: ___________
**Tested By**: ___________
**Overall Status**: [ ] PASS [ ] FAIL [ ] NEEDS IMPROVEMENT
**Notes**: ________________________________________________

### 16. python-expert
**Test Phrases:**
- [ ] "Refactor this FastAPI service using dependency injection"
- [ ] "Optimize this pandas pipeline for 10x more data"
- [ ] "Explain why this asyncio task is blocking the event loop"
- [ ] "Generate a Poetry project scaffold with pytest and mypy configured"
- [ ] "Add OpenTelemetry tracing to this Django REST endpoint"

**Expected Result:** Should invoke `python-expert`

### 17. backend-architect
**Test Phrases:**
- [ ] "Decompose the billing monolith into microservices"
- [ ] "Design REST and event contracts for order fulfillment"
- [ ] "Recommend resilience patterns for this gRPC service"
- [ ] "Plan an AsyncAPI schema for our notification system"
- [ ] "How should we version GraphQL mutations across teams?"

**Expected Result:** Should invoke `backend-architect`

### 18. database-architect
**Test Phrases:**
- [ ] "Design a PostgreSQL schema for multi-tenant billing"
- [ ] "Tune this slow query with EXPLAIN ANALYZE"
- [ ] "Plan DynamoDB single-table modelling for an order system"
- [ ] "Create a migration strategy for zero-downtime column rename"
- [ ] "Set up PITR backups and failover for MySQL 8"

**Expected Result:** Should invoke `database-architect`

### 19. observability-engineer
**Test Phrases:**
- [ ] "Define SLIs and SLOs for checkout latency"
- [ ] "Instrument this Node.js service with OpenTelemetry"
- [ ] "Create Prometheus burn-rate alerts for errors"
- [ ] "Design Grafana dashboards for Kubernetes workloads"
- [ ] "Reduce alert fatigue by consolidating noisy pager rules"

**Expected Result:** Should invoke `observability-engineer`

### 20. mobile-specialist
**Test Phrases:**
- [ ] "Optimize our React Native app for startup speed"
- [ ] "Add biometric authentication to the iOS and Android clients"
- [ ] "Configure Flutter for staged rollouts with Fastlane"
- [ ] "Design an offline-first sync strategy for mobile orders"
- [ ] "Investigate ANR spikes reported in Play Console"

**Expected Result:** Should invoke `mobile-specialist`

### 21. typescript-architect
**Test Phrases:**
- [ ] "Migrate this repo to TypeScript strict mode"
- [ ] "Set up shared API types between Next.js and our Node backend"
- [ ] "Reduce tsc compile time in the Turborepo"
- [ ] "Design a zod-based runtime validation layer for our API"
- [ ] "Fix type errors after upgrading to TypeScript 5.4"

**Expected Result:** Should invoke `typescript-architect`

### 22. sre-incident-responder
**Test Phrases:**
- [ ] "Lead an incident response for elevated checkout errors"
- [ ] "Draft a blameless postmortem template"
- [ ] "Tune PagerDuty alerts to respect SLO burn rates"
- [ ] "Plan a chaos game day for Kubernetes failover"
- [ ] "Improve MTTR for our payments service"

**Expected Result:** Should invoke `sre-incident-responder`
