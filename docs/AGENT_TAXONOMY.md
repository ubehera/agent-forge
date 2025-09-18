# Agent Taxonomy & Classification System

## Overview

The ubehera agent-forge system organizes 60+ specialized agents into a hierarchical taxonomy based on expertise level, domain focus, and collaboration patterns. This classification enables optimal task routing, quality assurance, and systematic capability expansion.

## Hierarchical Structure

### Tier 0: Meta-Orchestration (4 agents)
**Purpose**: System coordination and intelligent workflow management
**Quality Threshold**: 9.0+
**Characteristics**: Multi-agent coordination, complex decision making, system optimization

| Agent | Primary Function | Activation Patterns |
|-------|------------------|-------------------|
| `agent-coordinator` | Multi-agent workflow orchestration | "orchestrate", "coordinate", "multi-agent", "complex workflow" |
| `context-manager` | Context optimization and memory management | "optimize context", "manage memory", "information synthesis" |
| `task-distributor` | Intelligent task routing and load balancing | "distribute tasks", "route to expert", "load balance" |
| `workflow-orchestrator` | Complex multi-step process management | "manage workflow", "process automation", "step coordination" |

**Tool Access**: Task, Read, Write, MultiEdit (minimal for performance)
**Delegation Authority**: Can delegate to any agent in the system

### Tier 1: Foundation (9 agents) ✅ Existing
**Purpose**: Core architectural competencies and system-wide expertise
**Quality Threshold**: 8.5+
**Characteristics**: Broad expertise, high-quality output, frequent collaboration

| Agent | Domain | Quality Score | Primary Technologies |
|-------|--------|---------------|---------------------|
| `system-design-specialist` | Distributed Systems | 8.2 | Architecture, Scalability, Microservices |
| `api-platform-engineer` | API Design | 8.0 | REST, GraphQL, OpenAPI, Gateways |
| `security-architect` | Security | 5.8→8.5 | Zero-trust, OWASP, Threat modeling |
| `devops-automation-expert` | DevOps | 7.2→8.5 | CI/CD, Kubernetes, Infrastructure |
| `aws-cloud-architect` | Cloud Platforms | 8.1 | AWS, Multi-cloud, Serverless |
| `performance-optimization-specialist` | Performance | 8.2 | Optimization, Monitoring, Tuning |
| `data-pipeline-engineer` | Data Engineering | 7.8 | ETL, Streaming, Data architecture |
| `machine-learning-engineer` | ML/AI | 7.5→8.5 | MLOps, Model deployment, AI systems |
| `full-stack-architect` | Full-stack | 8.0 | End-to-end architecture, Integration |

**Tool Access**: Varies by agent, typically includes Task for coordination
**Delegation Authority**: Can delegate to specialist and expert tiers

### Tier 2: Development Specialists (6 agents)
**Purpose**: Specialized development domains with cross-cutting expertise
**Quality Threshold**: 8.0+
**Characteristics**: Deep domain knowledge, practical implementation focus

| Agent | Domain | Primary Technologies | Tool Set |
|-------|--------|---------------------|----------|
| `frontend-expert` | Frontend Development | React 18+, Vue 3, Angular 17+, TypeScript | Read, Write, MultiEdit, WebFetch |
| `backend-expert` | Backend Development | Server architecture, APIs, Microservices | Read, Write, MultiEdit, Bash |
| `mobile-architect` | Mobile Development | React Native, Flutter, iOS, Android | Read, Write, MultiEdit, Task |
| `database-expert` | Database Systems | SQL/NoSQL, Optimization, Migrations | Read, Write, MultiEdit, Bash |
| `microservices-architect` | Microservices | Service mesh, Communication, Orchestration | Read, Write, MultiEdit, Task |
| `integration-specialist` | System Integration | APIs, Message queues, ETL, Webhooks | Read, Write, MultiEdit, WebFetch |

**Activation Patterns**: Domain-specific keywords combined with implementation terms
**Collaboration**: Heavy integration with foundation and language tiers

### Tier 3: Language Specialists (6 agents)
**Purpose**: Deep language and framework expertise
**Quality Threshold**: 7.5+
**Characteristics**: Language mastery, framework specialization, ecosystem knowledge

| Agent | Language/Runtime | Frameworks | Performance Focus |
|-------|-----------------|------------|------------------|
| `python-master` | Python 3.12+ | FastAPI, Django, Flask, Pandas | Async patterns, Data processing |
| `typescript-expert` | TypeScript 5+ | Node.js, Deno, Bun, Express | Type safety, Runtime optimization |
| `rust-systems-engineer` | Rust | Actix, Tokio, WebAssembly | Systems programming, Performance |
| `go-specialist` | Go | Gin, Fiber, gRPC, Kubernetes | Concurrency, Cloud-native |
| `java-architect` | Java 21+ | Spring Boot, Hibernate, Maven | Enterprise patterns, JVM optimization |
| `kotlin-developer` | Kotlin | Android, Spring Boot, Ktor | Multiplatform, Coroutines |

**Tool Access**: Read, Write, MultiEdit, Bash (language-appropriate)
**Specialization**: Version-specific features, performance optimization, ecosystem integration

### Tier 4: Infrastructure (5 agents)
**Purpose**: Infrastructure and operations expertise
**Quality Threshold**: 7.2+
**Characteristics**: Operational focus, automation, reliability

| Agent | Domain | Technologies | Operational Focus |
|-------|--------|--------------|------------------|
| `kubernetes-expert` | Container Orchestration | K8s, Helm, Operators, Service mesh | Scaling, Management, Security |
| `terraform-engineer` | Infrastructure as Code | Terraform, Pulumi, CloudFormation | Provisioning, State management |
| `docker-specialist` | Containerization | Docker, Podman, BuildKit | Optimization, Multi-stage builds |
| `monitoring-engineer` | Observability | Prometheus, Grafana, ELK, Jaeger | Metrics, Logging, Tracing |
| `sre-specialist` | Site Reliability | SLOs, Error budgets, Chaos engineering | Reliability, Incident response |

**Tool Access**: Read, Write, MultiEdit, Bash (infrastructure commands)
**Focus Areas**: Automation, reliability, scalability, monitoring

### Tier 5: Quality & Testing (5 agents)
**Purpose**: Quality assurance, testing, and compliance
**Quality Threshold**: 7.0+
**Characteristics**: Quality focus, standards enforcement, validation

| Agent | Domain | Specialization | Validation Focus |
|-------|--------|----------------|------------------|
| `test-architect` | Testing Strategy | Framework design, Test planning | Coverage, Strategy |
| `qa-automation-expert` | Test Automation | Selenium, Cypress, Jest, TestNG | Automation, CI/CD integration |
| `code-reviewer` | Code Quality | Static analysis, Standards | Quality gates, Best practices |
| `accessibility-specialist` | A11y Compliance | WCAG 2.1, Screen readers, Testing | Inclusive design, Compliance |
| `compliance-auditor` | Regulatory Compliance | SOC2, HIPAA, GDPR, PCI | Audit trails, Risk assessment |

**Tool Access**: Read, Write, MultiEdit, WebFetch (for standards verification)
**Quality Focus**: Standards enforcement, risk mitigation, compliance validation

### Tier 6: Data & AI (5 agents)
**Purpose**: Data engineering and artificial intelligence
**Quality Threshold**: 7.0+
**Characteristics**: Data focus, analytics, machine learning

| Agent | Domain | Technologies | Data Focus |
|-------|--------|--------------|------------|
| `data-architect` | Data Architecture | Data lakes, Warehouses, Modeling | Schema design, Governance |
| `analytics-engineer` | Data Analytics | dbt, Spark, Snowflake, BigQuery | Transformation, Visualization |
| `ai-researcher` | AI Research | LangChain, Transformers, PyTorch | Model development, Research |
| `nlp-specialist` | Natural Language | spaCy, NLTK, Transformers | Text processing, Understanding |
| `computer-vision-expert` | Computer Vision | OpenCV, TensorFlow, YOLO | Image processing, Recognition |

**Tool Access**: Read, Write, MultiEdit, WebSearch (for research)
**Research Integration**: Heavy use of WebSearch for latest developments

### Tier 7: Specialized Domains (6 agents)
**Purpose**: Industry-specific and specialized technology expertise
**Quality Threshold**: 6.8+
**Characteristics**: Domain specialization, industry knowledge

| Agent | Domain | Industry Focus | Specialized Knowledge |
|-------|--------|----------------|---------------------|
| `fintech-engineer` | Financial Technology | Banking, Payments, Trading | Compliance, Security, Performance |
| `blockchain-developer` | Web3/Crypto | DeFi, Smart contracts, NFTs | Consensus, Cryptography, Gas optimization |
| `game-developer` | Game Development | Unity, Unreal, Game engines | Performance, Physics, Rendering |
| `iot-engineer` | Internet of Things | Embedded, Sensors, Edge computing | Real-time, Power management |
| `embedded-systems-expert` | Embedded Systems | RTOS, Hardware, Firmware | Real-time constraints, Memory |
| `quantum-computing-researcher` | Quantum Computing | Qiskit, Cirq, Quantum algorithms | Quantum mechanics, Algorithms |

**Tool Access**: Read, Write, MultiEdit, WebSearch (domain research)
**Specialization**: Industry-specific patterns, regulatory requirements

### Tier 8: Business & Product (5 agents)
**Purpose**: Product management and business analysis
**Quality Threshold**: 6.5+
**Characteristics**: Business focus, user-centric, strategic

| Agent | Domain | Business Focus | Collaboration Patterns |
|-------|--------|----------------|----------------------|
| `product-manager` | Product Strategy | Roadmapping, Requirements, Metrics | Heavy collaboration with technical teams |
| `business-analyst` | Requirements Analysis | Documentation, Process modeling | Translation between business and technical |
| `technical-writer` | Documentation | API docs, User guides, Tutorials | Integration with all technical agents |
| `ux-researcher` | User Research | User testing, Analytics, Personas | Frontend and design collaboration |
| `project-coordinator` | Project Management | Agile, Scrum, Resource management | Cross-functional coordination |

**Tool Access**: Read, Write, MultiEdit (documentation focus)
**Integration**: High collaboration with technical agents for translation

### Tier 9: Research & Analysis (4 agents)
**Purpose**: Research capabilities and emerging technologies
**Quality Threshold**: 6.5+
**Characteristics**: Research focus, trend analysis, knowledge synthesis

| Agent | Domain | Research Focus | Information Sources |
|-------|--------|----------------|-------------------|
| `research-librarian` | Information Discovery | Sources, Synthesis, Validation | Academic papers, Documentation |
| `trend-analyst` | Technology Trends | Forecasting, Analysis, Impact | Industry reports, Market data |
| `competitive-analyst` | Market Intelligence | Competitor analysis, Positioning | Market research, Product analysis |
| `market-researcher` | User Research | Surveys, Interviews, Market validation | User data, Market studies |

**Tool Access**: Read, Write, MultiEdit, WebSearch (heavy research focus)
**Research Methods**: Systematic information gathering and synthesis

## Agent Selection Algorithm

### Primary Routing Logic
1. **Keyword Matching**: Match request keywords to agent activation patterns
2. **Domain Classification**: Identify primary domain (frontend, backend, security, etc.)
3. **Complexity Assessment**: Determine appropriate tier based on task complexity
4. **Capability Matching**: Ensure agent has required tools and expertise
5. **Load Balancing**: Consider agent availability and performance history

### Fallback Chain
1. **Specialist Fallback**: If specialist unavailable, route to higher tier
2. **Foundation Escalation**: Complex issues escalate to foundation tier
3. **Meta-Orchestration**: Multi-agent workflows route to Tier 0
4. **Default Routing**: Ultimate fallback to `system-design-specialist`

### Quality Gates
- Minimum quality score requirements by tier
- Automatic quality validation for outputs
- Cross-tier review for complex tasks
- Continuous quality monitoring and improvement

## Collaboration Patterns

### Vertical Collaboration (Cross-Tier)
- **Foundation → Specialist**: Architectural guidance to implementation
- **Specialist → Language**: Domain requirements to language-specific implementation
- **Meta → All**: Orchestration and coordination across all tiers

### Horizontal Collaboration (Same-Tier)
- **Cross-domain validation**: Security + Performance + API review
- **Integration patterns**: Frontend + Backend + Database coordination
- **Quality assurance**: Multiple specialists review complex outputs

### Escalation Patterns
- **Complexity Escalation**: Specialist → Foundation → Meta
- **Quality Escalation**: Failed quality gates trigger higher-tier review
- **Error Recovery**: Automatic fallback to more general expertise

## Quality Management

### Quality Scoring Framework
- **Automated Evaluation**: `scripts/quality-scorer.py` for objective metrics
- **Peer Review**: Cross-agent validation for complex outputs
- **User Feedback**: Continuous quality improvement based on usage
- **Performance Monitoring**: Response time and accuracy tracking

### Continuous Improvement
- **Quality Trends**: Track quality scores over time
- **Usage Analytics**: Monitor agent selection patterns and success rates
- **Feedback Integration**: Incorporate user feedback into agent improvements
- **Knowledge Updates**: Regular updates based on technology evolution

## Metadata Management

### Agent Metadata Schema
```json
{
  "name": "agent-name",
  "tier": 0-9,
  "category": "Domain Category",
  "quality_score": 0.0-10.0,
  "activation_patterns": ["keyword1", "keyword2"],
  "dependencies": ["agent1", "agent2"],
  "delegates_to": ["agent1", "agent2"],
  "tools": ["Read", "Write", "MultiEdit"],
  "last_updated": "ISO-8601",
  "maintainer": "username"
}
```

### Routing Configuration
- **Primary Keywords**: Direct routing based on exact matches
- **Semantic Matching**: Fuzzy matching for related concepts
- **Context Awareness**: Previous agent history influences routing
- **Performance Optimization**: Route to best-performing agents

## Success Metrics

### System-Level Metrics
- **Routing Accuracy**: >95% correct agent selection
- **Quality Consistency**: >8.0 average quality score across outputs
- **User Satisfaction**: >4.5/5 rating for agent system
- **Performance**: <30 seconds for agent routing decisions

### Agent-Level Metrics
- **Task Completion Rate**: >98% successful completion
- **Quality Score**: Tier-specific minimum thresholds
- **Response Time**: Task-appropriate response times
- **Collaboration Effectiveness**: Cross-agent integration success

This taxonomy provides a comprehensive framework for organizing and managing a large-scale agent system while maintaining quality, performance, and usability standards.