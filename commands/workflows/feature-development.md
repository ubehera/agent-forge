---
description: Execute complete feature development workflow with DDD and quality gates
args: [feature-context] [--stage=all|requirements|design|api|implementation|testing] [--ddd] [--parallel]
tools: Task, TodoWrite, Read, Write
model: claude-sonnet-4-5
---

## Purpose
Complete feature development workflow using Domain-Driven Design principles with automated agent coordination, quality gates, and progress tracking.

## Workflow Stages

### Stage 1: Requirements Analysis (Quality Gate: 90%)
**Agents**: `agent-coordinator` → `system-design-specialist`
**Duration**: 1-2 hours
**Deliverables**:
- Business requirements specification
- User journey mapping
- Acceptance criteria definition
- Risk assessment and mitigation

### Stage 2: Domain Modeling (Quality Gate: 85%)
**Agents**: `domain-modeling-expert` (strategic DDD), `system-design-specialist` (architecture implications)
**Command**: `/domain-model` for event storming and context mapping
**Duration**: 2-4 hours
**Deliverables**:
- Bounded contexts identification
- Domain model with aggregates
- Event storming results
- Ubiquitous language definition

### Stage 3: API Design (Quality Gate: 95%)
**Agents**: `api-platform-engineer`
**Duration**: 1-3 hours
**Deliverables**:
- OpenAPI/GraphQL specifications
- API contract definitions
- Authentication/authorization patterns
- Error handling strategies

### Stage 4: Implementation (Quality Gate: 80%)
**Agents**: Technology-specific agents based on stack
**Duration**: 4-16 hours
**Deliverables**:
- Core domain logic implementation
- API layer with validation
- Unit tests (>80% coverage)
- Integration tests

### Stage 5: Testing & Validation (Quality Gate: 90%)
**Agents**: `test-engineer`, `security-architect`, `performance-optimization-specialist`
**Duration**: 2-6 hours
**Deliverables**:
- End-to-end test suite
- Security scan results
- Performance benchmarks
- Quality metrics report

## Usage Examples

```bash
# Full feature development workflow
/workflow-feature-development ./features/user-management

# Execute specific stage
/workflow-feature-development ./features/payments --stage=api

# DDD-focused approach with domain modeling
/workflow-feature-development ./features/inventory --ddd --stage=design

# Parallel execution where possible
/workflow-feature-development ./features/notifications --parallel --stage=implementation

# Skip to implementation (development mode)
/workflow-feature-development ./features/search --stage=implementation --skip-gates
```

## Input Validation

```bash
# Validate feature context
FEATURE_CONTEXT=$1
STAGE=${2#--stage=}
FLAGS="$3 $4 $5"

if [ -z "$FEATURE_CONTEXT" ]; then
  echo "❌ Error: Feature context required"
  echo "💡 Usage: /workflow-feature-development [feature-path] [--stage] [--options]"
  echo "📚 Examples:"
  echo "  /workflow-feature-development ./features/user-auth"
  echo "  /workflow-feature-development ./src/payments --stage=api"
  echo "  /workflow-feature-development ./modules/inventory --ddd"
  exit 1
fi

# Create feature directory if it doesn't exist
if [ ! -d "$FEATURE_CONTEXT" ]; then
  echo "📏 Creating feature directory: $FEATURE_CONTEXT"
  mkdir -p "$FEATURE_CONTEXT"
fi

# Validate stage parameter
case "$STAGE" in
  "all"|"")
    STAGE="all"
    echo "🚀 Executing full feature development workflow"
    ;;
  "requirements"|"design"|"api"|"implementation"|"testing")
    echo "🎨 Executing stage: $STAGE"
    ;;
  *)
    echo "❌ Error: Invalid stage: $STAGE"
    echo "💡 Available stages: all, requirements, design, api, implementation, testing"
    exit 1
    ;;
esac
```

## Workflow Implementation

### Progress Tracking Setup

Create comprehensive TodoWrite tracking for the feature:

**Feature Development: $FEATURE_CONTEXT**
- [ ] Stage 1: Requirements Analysis (Target: 90% quality gate)
- [ ] Stage 2: Domain Modeling (Target: 85% quality gate)
- [ ] Stage 3: API Design (Target: 95% quality gate)
- [ ] Stage 4: Implementation (Target: 80% quality gate)
- [ ] Stage 5: Testing & Validation (Target: 90% quality gate)

**Quality Gate Metrics**:
- Requirements completeness and stakeholder alignment
- Domain model clarity and bounded context definition
- API specification completeness and standards compliance
- Code coverage, test quality, and implementation completeness
- Security compliance, performance benchmarks, and E2E validation

### Stage Execution Logic

```bash
# Execute workflow based on stage selection
case "$STAGE" in
  "all")
    execute_full_workflow "$FEATURE_CONTEXT" "$FLAGS"
    ;;
  "requirements")
    execute_requirements_stage "$FEATURE_CONTEXT" "$FLAGS"
    ;;
  "design")
    execute_design_stage "$FEATURE_CONTEXT" "$FLAGS"
    ;;
  "api")
    execute_api_stage "$FEATURE_CONTEXT" "$FLAGS"
    ;;
  "implementation")
    execute_implementation_stage "$FEATURE_CONTEXT" "$FLAGS"
    ;;
  "testing")
    execute_testing_stage "$FEATURE_CONTEXT" "$FLAGS"
    ;;
esac

# Quality gate validation
validate_quality_gate() {
  local stage=$1
  local threshold=$2
  local context=$3
  
  echo "🔍 Quality Gate: $stage (threshold: $threshold%)"
  
  case "$stage" in
    "requirements")
      # Validate requirements completeness
      check_requirements_quality "$context" "$threshold"
      ;;
    "design")
      # Validate domain model and architecture
      check_design_quality "$context" "$threshold"
      ;;
    "api")
      # Validate API specifications
      check_api_quality "$context" "$threshold"
      ;;
    "implementation")
      # Validate code quality and tests
      check_implementation_quality "$context" "$threshold"
      ;;
    "testing")
      # Validate comprehensive testing
      check_testing_quality "$context" "$threshold"
      ;;
  esac
}
```

### Agent Coordination Sequence

#### Stage 1: Requirements Analysis
Delegate to `agent-coordinator` for requirements extraction:

**Task**: Requirements analysis and business context extraction for feature: $FEATURE_CONTEXT

**Instructions**: 
1. Analyze business requirements and user needs
2. Define acceptance criteria and success metrics
3. Identify stakeholders and constraints
4. Create user journey mapping
5. Assess risks and define mitigation strategies
6. Prepare context for domain modeling stage

**Quality Gate**: 90% requirements completeness and stakeholder alignment

#### Stage 2: Domain Modeling (DDD)
Delegate to `domain-modeling-expert` for strategic DDD analysis:

**Task**: Domain-driven design analysis for feature: $FEATURE_CONTEXT

**Instructions**:
1. Apply Domain-Driven Design principles with event storming
2. Identify bounded contexts and their relationships using context mapping
3. Define domain model with aggregates, entities, and value objects
4. Establish ubiquitous language and domain glossary
5. Model domain events and command flows
6. Define integration patterns between contexts (ACL, OHS, etc.)
7. Coordinate with `system-design-specialist` for architectural implications

**Command**: Use `/domain-model $FEATURE_CONTEXT --technique event-storming` for facilitation

**Quality Gate**: 85% domain model clarity and bounded context definition

#### Stage 3: API Design
Delegate to `api-platform-engineer` for contract specification:

**Task**: API design and contract specification for feature: $FEATURE_CONTEXT

**Instructions**:
1. Design RESTful APIs following OpenAPI 3.0 standards
2. Define authentication and authorization patterns
3. Specify error handling and validation rules
4. Design event-driven APIs for domain events
5. Create API documentation and examples
6. Ensure API governance compliance

**Quality Gate**: 95% API specification completeness and standards compliance

#### Stage 4: Implementation
Delegate to technology-specific agents based on project stack:

**Task**: Implementation of feature: $FEATURE_CONTEXT

**Technology Selection**:
- TypeScript/Node.js: `typescript-architect`
- Python: `python-expert`
- Frontend: `frontend-expert`
- Backend Services: `backend-architect`

**Instructions**:
1. Implement core domain logic with proper separation
2. Build API layer with validation and error handling
3. Create unit tests with >80% coverage
4. Implement integration tests for API contracts
5. Follow project coding standards and patterns
6. Document implementation decisions and trade-offs

**Quality Gate**: 80% implementation completeness and test coverage

#### Stage 5: Testing & Validation
Delegate to quality specialists for comprehensive validation:

**Testing**: `test-engineer`
**Security**: `security-architect` 
**Performance**: `performance-optimization-specialist`

**Instructions**:
1. Create end-to-end test suite covering critical paths
2. Execute security scanning and vulnerability assessment
3. Run performance benchmarks and load testing
4. Validate compliance with quality standards
5. Generate comprehensive quality metrics report
6. Provide recommendations for production readiness

**Quality Gate**: 90% comprehensive validation and security compliance

## Feature Flags & Options

### DDD Flag (`--ddd`)
When `--ddd` flag is provided:
- Enhanced domain modeling with event storming
- Deeper bounded context analysis
- More thorough ubiquitous language development
- Extended design stage duration

### Parallel Flag (`--parallel`)
When `--parallel` flag is provided:
- Execute independent tasks simultaneously
- Coordinate parallel agent execution
- Merge results with conflict resolution
- Faster overall workflow completion

### Skip Gates Flag (`--skip-gates`)
Development mode option:
- Skip quality gate validation
- Faster iteration cycles
- Still track progress and metrics
- Warning about skipped validation

## Success Metrics & Reporting

### Quality Metrics Tracking
- **Requirements**: Completeness score, stakeholder approval
- **Design**: Domain model coverage, context clarity
- **API**: Specification completeness, standards compliance
- **Implementation**: Code coverage, test quality, complexity metrics
- **Testing**: E2E coverage, security score, performance benchmarks

### Workflow Completion Report
```
🏁 Feature Development Complete: [feature-name]
⏱️ Duration: [total-time]
📋 Stages: [completed-stages]
📈 Quality Gates: [passed/total]
📊 Overall Score: [aggregate-quality-score]%

📝 Deliverables:
- Requirements Specification: [file-path]
- Domain Model: [file-path]
- API Specifications: [file-path]
- Implementation: [file-paths]
- Test Suite: [file-path]
- Quality Report: [file-path]

🚀 Next Steps:
- Deploy to staging environment
- Execute user acceptance testing
- Plan production release
- Monitor feature usage and performance
```

## Error Recovery

If any stage fails:
1. **Identify Failure Point**: Log detailed error information
2. **Quality Gate Analysis**: Determine if threshold can be adjusted
3. **Agent Retry**: Attempt stage re-execution with refined context
4. **Manual Intervention**: Provide specific remediation steps
5. **Workflow Resumption**: Continue from last successful stage

### Common Failure Scenarios
- **Requirements Unclear**: Request stakeholder clarification
- **Domain Complexity**: Break into smaller bounded contexts
- **API Conflicts**: Review existing API standards and patterns
- **Implementation Blocks**: Suggest alternative approaches or patterns
- **Quality Issues**: Provide specific improvement recommendations