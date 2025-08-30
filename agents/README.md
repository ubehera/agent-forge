# Claude Code Agent Collection - ubehera

A curated collection of specialized Claude Code subagents for professional software engineering. Each agent follows official Claude Code specifications with YAML frontmatter and comprehensive domain expertise.

## Agent Capability Matrix

| Agent | Primary Domain | Security Level | Performance Focus | Best For | Tool Set |
|-------|---------------|----------------|-------------------|----------|----------|
| **api-platform-engineer** | API Design & Governance | OAuth/JWT, Rate Limiting | Gateway optimization, Caching | REST/GraphQL APIs, Developer portals | Read, Write, MultiEdit, Bash, Grep, WebFetch, Task |
| **aws-cloud-architect** | Cloud Infrastructure | IAM, KMS, WAF | Auto-scaling, Cost optimization | AWS deployments, Well-Architected | Read, Write, MultiEdit, Bash, Task, WebSearch |
| **data-pipeline-engineer** | ETL/Streaming | Data privacy | Spark optimization, Parallel processing | Data lakes, Real-time processing | Read, Write, MultiEdit, Bash, Task |
| **devops-automation-expert** | CI/CD & Automation | Security scanning, Secrets mgmt | Pipeline efficiency | GitOps, IaC, Monitoring | Read, Write, MultiEdit, Bash, Task, Grep |
| **full-stack-architect** | Web Applications | OWASP compliance | Core Web Vitals, Bundle optimization | Modern web apps, React/Next.js | Read, Write, MultiEdit, Bash, Task, WebSearch |
| **machine-learning-engineer** | ML/AI Systems | Model security | Distributed training, Inference optimization | MLOps, Model serving | Read, Write, MultiEdit, Bash, Task, WebSearch |
| **performance-optimization-specialist** | All-domain Performance | Performance-security balance | Expert optimization | Bottleneck resolution, Monitoring | Read, Write, MultiEdit, Bash, Grep, Task |
| **security-architect** | Security & Compliance | Expert all domains | Security-performance tradeoffs | Threat modeling, Compliance | Read, Write, MultiEdit, Bash, Grep, WebSearch |
| **system-design-specialist** | Distributed Systems | Security patterns | Scalability, Reliability | Large-scale architecture | Read, Write, MultiEdit, WebSearch, Task |
| **research-librarian** | Research & Discovery | Trusted sources | Efficient retrieval | Unknown URLs, literature surveys | Read, Write, MultiEdit, WebSearch |

## Invocation Guide

### Automatic Invocation Triggers
Agents are automatically selected when your request matches their description keywords:

- **API-related**: "REST API", "GraphQL", "OpenAPI", "API gateway", "developer portal" → `api-platform-engineer`
- **AWS/Cloud**: "AWS", "CloudFormation", "CDK", "cloud architecture", "serverless" → `aws-cloud-architect`
- **Data processing**: "ETL", "data pipeline", "Spark", "streaming", "Airflow", "Kafka" → `data-pipeline-engineer`
- **Automation**: "CI/CD", "pipeline", "GitOps", "automation", "deployment" → `devops-automation-expert`
- **Web development**: "React", "Next.js", "frontend", "full-stack", "web app" → `full-stack-architect`
- **ML/AI**: "machine learning", "model training", "MLOps", "neural network" → `machine-learning-engineer`
- **Performance**: "optimization", "slow", "performance", "Core Web Vitals", "bottleneck" → `performance-optimization-specialist`
- **Security**: "security", "threat", "vulnerability", "compliance", "authentication" → `security-architect`
- **Architecture**: "system design", "distributed", "scalability", "microservices" → `system-design-specialist`
- **Research**: "find docs", "RFC", "compare", "which standard/library", "best practice" → `research-librarian`

### Agent Specialization Levels

**🔴 Expert Level (9-10 rating):**
- `devops-automation-expert` - Gold standard for CI/CD and automation
- `performance-optimization-specialist` - Comprehensive performance optimization
- `machine-learning-engineer` - Production-ready MLOps patterns

**🟡 Strong Level (7-8 rating):**
- `api-platform-engineer` - Solid API governance and platform patterns
- `data-pipeline-engineer` - Advanced data processing and streaming
- `system-design-specialist` - Excellent distributed systems knowledge
- `aws-cloud-architect` - Strong cloud architecture foundations

**🔵 Good Level (6-7 rating):**
- `security-architect` - Comprehensive security knowledge
- `full-stack-architect` - Modern web application patterns

## Common Use Case Combinations

### Building Secure APIs
1. `api-platform-engineer` - API design and specification
2. `research-librarian` - Source discovery for specs and vendor docs
2. `security-architect` - Security patterns and threat modeling  
3. `performance-optimization-specialist` - API performance tuning
4. `devops-automation-expert` - CI/CD and deployment automation

### ML Platform Development
1. `machine-learning-engineer` - ML pipeline and model serving
2. `data-pipeline-engineer` - Feature engineering and data processing
3. `aws-cloud-architect` - Cloud infrastructure for ML
4. `security-architect` - ML model security and data privacy

### Production Web Application
1. `full-stack-architect` - Application architecture and implementation
2. `devops-automation-expert` - CI/CD and deployment pipelines
3. `security-architect` - Security implementation and compliance
4. `performance-optimization-specialist` - Frontend and backend optimization

### Distributed System Design
1. `system-design-specialist` - Overall architecture and scalability
2. `performance-optimization-specialist` - Performance requirements
3. `security-architect` - Security architecture and threat modeling
4. `devops-automation-expert` - Deployment and operations strategy

### Cloud Migration Project
1. `aws-cloud-architect` - Cloud architecture and migration strategy
2. `devops-automation-expert` - Automation and CI/CD setup
3. `security-architect` - Cloud security and compliance
4. `performance-optimization-specialist` - Performance optimization

## Agent Quality Standards

### All agents include:
- ✅ **Claude Code Compliance**: Proper YAML frontmatter with markdown body
- ✅ **Tool Restrictions**: Optimized tool sets for performance and security
- ✅ **Practical Examples**: Working code implementations
- ✅ **Success Metrics**: Measurable KPIs and deliverables
- ✅ **Quality Checklists**: Comprehensive validation criteria
- ✅ **Documentation Standards**: Architecture diagrams and specifications

### Recent Expert Review Scores:
- **Security Architecture**: 5.8/10 (improvements planned)
- **Performance Optimization**: 8.2/10 (excellent coverage)
- **ML Engineering**: 7.5/10 (strong MLOps foundation)
- **System Design**: 8.2/10 (exceptional patterns)
- **DevOps Automation**: 7.2/10 (strong technical foundation)

## MCP Tool Compatibility

**Note**: MCP tool availability depends on your Claude Code configuration. Agents will use available MCP tools when present:

- **mcp__memory**: State management and knowledge persistence
- **mcp__fetch**: External API testing and validation
- **mcp__sequential-thinking**: Complex problem decomposition
- **mcp__ide**: Code execution and diagnostics (if configured)

Agents function fully without MCP tools but leverage them when available for enhanced capabilities.

## Installation & Usage

### For Current User:
```bash
cp agents/*.md ~/.claude/agents/
```

### For Project Only:
```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

### Verify Installation:
```bash
ls ~/.claude/agents/ | grep -E "(api-platform|aws-cloud|system-design)"
```

**Important**: Restart Claude Code after installing or modifying agents.

## Development Philosophy

This collection prioritizes:
1. **Production-ready patterns** over academic examples
2. **Practical implementation** over theoretical knowledge
3. **Security by default** across all domains
4. **Performance awareness** in all recommendations
5. **DevOps integration** throughout the development lifecycle

## Contributing

When enhancing agents:
- Follow official Claude Code subagent specifications
- Include practical code examples
- Add measurable success criteria
- Test invocation accuracy with sample requests
- Maintain tool restriction optimizations

## Changelog

- **v1.0**: Initial collection with 9 specialized agents
- **v1.1**: Added capability matrix, invocation guide, and collaboration patterns
- **v1.2**: Enhanced descriptions for better automatic invocation (planned)
- **v1.3**: Integrated security and DevOps context across all agents (planned)

---

**Maintained by**: Umank Behera  
**Compatibility**: Claude Code Official Specifications  
**Last Updated**: 2025-01-26
