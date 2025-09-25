---
description: Invoke api-platform-engineer for API design, governance, and platform work
args: [task-description] [api-context] [--spec=openapi|graphql] [--gateway=kong|apigee]
tools: Task, Read
model: claude-sonnet-4-20250514
---

## Purpose
Direct invocation of the `api-platform-engineer` for API design, governance, developer portal, and platform architecture tasks.

## Usage Examples

```bash
# API Design & Specification
/agent-api "design user management REST API" ./src/users --spec=openapi
/agent-api "create GraphQL schema for products" ./src/products --spec=graphql
/agent-api "design event-driven API for notifications" ./src/events --spec=asyncapi

# API Gateway Configuration  
/agent-api "configure rate limiting policies" ./config/kong --policy=tiered
/agent-api "setup API authentication" ./config/gateway --auth=oauth2
/agent-api "implement circuit breakers" ./config/resilience --pattern=bulkhead

# Developer Experience
/agent-api "setup developer portal" ./docs/api --features=try-it-out,sdk-gen
/agent-api "generate API documentation" ./api-specs --format=interactive
/agent-api "create API usage examples" ./examples --languages=typescript,python

# Governance & Standards
/agent-api "review API standards compliance" ./apis --report=detailed
/agent-api "validate OpenAPI specifications" ./specs --lint=strict
/agent-api "assess API security posture" ./apis --framework=owasp
```

## Input Validation

```bash
# Validate required task description
if [ -z "$1" ]; then
  echo "❌ Error: Task description required"
  echo "💡 Usage: /agent-api [task] [context] [--options]"
  echo "📚 Examples:"
  echo "  /agent-api 'design REST endpoints' ./src/api --spec=openapi"
  echo "  /agent-api 'review API security' ./apis --owasp-top10"
  echo "  /agent-api 'setup developer portal' ./docs --interactive"
  exit 1
fi

# Validate API context if provided
if [ -n "$2" ] && [ "$2" != "--"* ] && [ ! -e "$2" ]; then
  echo "⚠️ Warning: API context path not found: $2"
  echo "💡 Will proceed with current directory context"
fi
```

## Agent Delegation

Delegate to `api-platform-engineer` with structured context:

**Task**: $1
**API Context**: ${2:-.}
**Options**: $3

**Instructions for api-platform-engineer**:
You are being invoked for API platform engineering work. Focus on:

1. **Primary Task**: "$1"
2. **Working Context**: ${2:-.}
3. **Technical Requirements**: Apply API platform engineering best practices including:
   - OpenAPI 3.0/GraphQL/AsyncAPI specification design
   - API gateway configuration and policy management
   - Developer experience optimization
   - API governance and standards compliance
   - Authentication/authorization patterns (OAuth 2.0, JWT, API keys)
   - Rate limiting, throttling, and resilience patterns
   - API lifecycle management and versioning strategies

4. **Quality Standards**:
   - Follow RESTful design principles and industry standards
   - Ensure security by default (authentication, encryption, validation)
   - Design for scalability and performance (caching, pagination)
   - Provide comprehensive documentation and examples
   - Consider developer experience and self-service capabilities

5. **Deliverables**:
   - Concrete specifications, configurations, or implementations
   - File paths for all created/modified artifacts  
   - Technical decisions and rationale
   - Integration requirements and dependencies
   - Testing and validation approaches
   - Next steps and follow-up recommendations

**Project Context**: This is part of the ubehera agent-forge ecosystem. Maintain compatibility with existing patterns and follow established conventions.

## Expected Outputs

- **API Specifications**: OpenAPI/GraphQL schemas with examples
- **Gateway Configurations**: Policy definitions and routing rules
- **Documentation**: Developer-friendly API documentation
- **Security Implementations**: Authentication and authorization patterns
- **Integration Guides**: SDK generation and client library setup
- **Governance Frameworks**: API standards and compliance reports

## Error Handling

If the api-platform-engineer agent is unavailable:

1. **Alternative Approaches**:
   - Use `/agent-backend` for service-level API design
   - Use `/agent-security` for API security-focused tasks
   - Use `/workflow-api-development` for comprehensive API workflows

2. **Manual Steps**:
   - Review existing API specifications in `./api-specs/`
   - Consult API governance documentation in `./docs/api/`
   - Check gateway configurations in `./config/`

3. **Related Commands**:
   - `/quality-api` - API quality assessment
   - `/setup-api-project` - Initialize new API project
   - `/docs-generate` - Generate API documentation

4. **Documentation References**:
   - `agents/01-foundation/api-platform-engineer.md`
   - `docs/patterns/api-design-patterns.md`
   - `templates/api-specifications/`