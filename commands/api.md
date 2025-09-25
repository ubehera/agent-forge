---
description: Design comprehensive API with contracts and documentation
args: <service-name> [--spec openapi|graphql|asyncapi] [--version v1]
tools: Task, Write, Read
model: claude-sonnet-4-20250514
---

# API Design Orchestration

Design comprehensive API for: **$ARGUMENTS**

## API Strategy

### Service Analysis
Parse the service requirements from the arguments:
- Extract service name from first argument
- Determine specification format (default: OpenAPI 3.1)
- Set version strategy (default: v1)

### Design Delegation

Invoke api-platform-engineer via Task tool with:
- **Context**: Business requirements and constraints
- **Deliverables**:
  - API specification document
  - Request/response examples
  - Error handling patterns
  - Authentication schemes
  - Rate limiting strategy
  - Versioning approach

## Quality Standards

### API Design Principles
- RESTful conventions or GraphQL best practices
- Consistent naming and structure
- Comprehensive error codes
- Security by design
- Performance optimization
- Developer experience focus

### Specification Requirements
- Complete endpoint documentation
- Schema definitions with validation rules
- Example requests and responses
- Authentication/authorization details
- Rate limiting and quotas
- Deprecation strategy

## Integration Points

Consider these integrations:
1. **API Gateway Configuration**
   - Route definitions
   - Security policies
   - Rate limiting rules
   - Caching strategies

2. **Client SDK Generation**
   - TypeScript/JavaScript
   - Python
   - Go/Java as needed

3. **Documentation Portal**
   - Interactive API explorer
   - Code examples
   - Tutorials

4. **Monitoring & Analytics**
   - Endpoint metrics
   - Error tracking
   - Usage patterns

## Deliverables

Generate these artifacts:
1. API specification file (OpenAPI/GraphQL/AsyncAPI)
2. Postman/Insomnia collection
3. Mock server configuration
4. Integration test suite
5. Client SDK templates
6. Documentation site

## Examples

```
/api user-management
/api payment-service --spec openapi --version v2
/api notification-hub --spec asyncapi
/api analytics --spec graphql
```

## Follow-up Actions

After API design:
1. Use `/test` to generate API tests
2. Use `/agent backend-architect` for implementation
3. Configure CI/CD with API validation
4. Set up API monitoring dashboard