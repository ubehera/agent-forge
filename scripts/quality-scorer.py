#!/usr/bin/env python3
"""
Agent Quality Scoring System
Evaluates agents against comprehensive quality metrics
"""

import json
import yaml
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class QualityMetrics:
    """Quality scoring metrics for agents"""
    completeness: float = 0.0      # 25% - Content coverage and thoroughness
    accuracy: float = 0.0          # 25% - Technical accuracy and correctness
    usability: float = 0.0         # 20% - Ease of use and clear instructions
    performance: float = 0.0       # 15% - Tool usage and efficiency
    maintainability: float = 0.0   # 15% - Code quality and documentation

    @property
    def overall_score(self) -> float:
        """Calculate weighted overall score"""
        weights = {
            'completeness': 0.25,
            'accuracy': 0.25,
            'usability': 0.20,
            'performance': 0.15,
            'maintainability': 0.15
        }

        return (
            self.completeness * weights['completeness'] +
            self.accuracy * weights['accuracy'] +
            self.usability * weights['usability'] +
            self.performance * weights['performance'] +
            self.maintainability * weights['maintainability']
        )

class AgentQualityScorer:
    """Comprehensive agent quality assessment"""

    def __init__(self, agents_dir: str = "agents"):
        self.agents_dir = Path(agents_dir)
        self.quality_standards = self._load_quality_standards()

    def _load_quality_standards(self) -> Dict:
        """Load quality standards configuration"""
        return {
            'required_sections': [
                'Core Expertise',
                'Approach & Philosophy',
                'Technical Implementation',
                'Quality Standards',
                'Deliverables'
            ],
            'min_word_count': 1500,
            'required_frontmatter': ['name', 'description'],
            'tool_optimization_threshold': 7,  # Max recommended tools
            'code_example_requirement': True,
            'mcp_integration_bonus': 0.2,
            'collaboration_section_bonus': 0.1
        }

    def evaluate_agent(self, agent_file: Path) -> Tuple[QualityMetrics, Dict]:
        """Evaluate a single agent file"""
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse frontmatter and body
            frontmatter, body = self._parse_agent_file(content)

            # Evaluate each metric
            completeness = self._evaluate_completeness(frontmatter, body)
            accuracy = self._evaluate_accuracy(frontmatter, body)
            usability = self._evaluate_usability(frontmatter, body)
            performance = self._evaluate_performance(frontmatter, body)
            maintainability = self._evaluate_maintainability(frontmatter, body)

            metrics = QualityMetrics(
                completeness=completeness,
                accuracy=accuracy,
                usability=usability,
                performance=performance,
                maintainability=maintainability
            )

            # Detailed analysis
            analysis = self._generate_detailed_analysis(
                agent_file.name, frontmatter, body, metrics
            )

            return metrics, analysis

        except Exception as e:
            return QualityMetrics(), {'error': str(e)}

    def _parse_agent_file(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML frontmatter and markdown body"""
        if not content.startswith('---'):
            return {}, content

        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content

        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter or {}, body
        except yaml.YAMLError:
            return {}, content

    def _evaluate_completeness(self, frontmatter: Dict, body: str) -> float:
        """Evaluate content completeness (25%)"""
        score = 0.0

        # Required frontmatter fields (20%)
        required_fields = self.quality_standards['required_frontmatter']
        field_score = sum(1 for field in required_fields if field in frontmatter) / len(required_fields)
        score += field_score * 0.20

        # Required sections (30%)
        required_sections = self.quality_standards['required_sections']
        section_score = sum(1 for section in required_sections if section in body) / len(required_sections)
        score += section_score * 0.30

        # Content depth - word count (25%)
        word_count = len(body.split())
        min_words = self.quality_standards['min_word_count']
        word_score = min(word_count / min_words, 1.0)
        score += word_score * 0.25

        # Code examples (15%)
        code_blocks = len(re.findall(r'```[\s\S]*?```', body))
        code_score = min(code_blocks / 3, 1.0)  # Target: 3+ code examples
        score += code_score * 0.15

        # Documentation links and references (10%)
        links = len(re.findall(r'\[.*?\]\(.*?\)', body))
        link_score = min(links / 5, 1.0)  # Target: 5+ links
        score += link_score * 0.10

        return min(score, 1.0)

    def _evaluate_accuracy(self, frontmatter: Dict, body: str) -> float:
        """Evaluate technical accuracy (25%)"""
        score = 0.0

        # Proper YAML structure (30%)
        yaml_score = 1.0 if self._validate_yaml_structure(frontmatter) else 0.5
        score += yaml_score * 0.30

        # Technical terminology usage (25%)
        tech_terms = self._count_technical_terms(body)
        tech_score = min(tech_terms / 20, 1.0)  # Target: 20+ technical terms
        score += tech_score * 0.25

        # Realistic examples and patterns (25%)
        realistic_score = self._evaluate_realism(body)
        score += realistic_score * 0.25

        # Consistency with domain expertise (20%)
        consistency_score = self._evaluate_domain_consistency(frontmatter, body)
        score += consistency_score * 0.20

        return min(score, 1.0)

    def _evaluate_usability(self, frontmatter: Dict, body: str) -> float:
        """Evaluate usability and clarity (20%)"""
        score = 0.0

        # Clear description for routing (35%)
        description = frontmatter.get('description', '')
        desc_score = self._evaluate_description_quality(description)
        score += desc_score * 0.35

        # Structured content organization (25%)
        structure_score = self._evaluate_content_structure(body)
        score += structure_score * 0.25

        # Actionable instructions (25%)
        actionable_score = self._count_actionable_elements(body)
        score += actionable_score * 0.25

        # Examples and code snippets (15%)
        example_score = self._evaluate_example_quality(body)
        score += example_score * 0.15

        return min(score, 1.0)

    def _evaluate_performance(self, frontmatter: Dict, body: str) -> float:
        """Evaluate performance considerations (15%)"""
        score = 0.0

        # Tool optimization (40%)
        tools = frontmatter.get('tools', [])
        if isinstance(tools, str):
            tools = [t.strip() for t in tools.split(',')]

        tool_count = len(tools) if tools else 0
        optimal_tools = self.quality_standards['tool_optimization_threshold']

        if tool_count == 0:
            tool_score = 0.8  # No tools specified = inherit all (slight penalty)
        elif tool_count <= optimal_tools:
            tool_score = 1.0  # Optimal tool selection
        else:
            tool_score = max(0.5, 1.0 - (tool_count - optimal_tools) * 0.1)

        score += tool_score * 0.40

        # MCP tool integration (30%)
        mcp_integration = 'mcp__' in body or 'MCP' in body
        mcp_score = 1.0 if mcp_integration else 0.6
        score += mcp_score * 0.30

        # Efficiency patterns (30%)
        efficiency_keywords = ['optimization', 'performance', 'efficient', 'scalable']
        efficiency_count = sum(1 for keyword in efficiency_keywords if keyword.lower() in body.lower())
        efficiency_score = min(efficiency_count / 4, 1.0)
        score += efficiency_score * 0.30

        return min(score, 1.0)

    def _evaluate_maintainability(self, frontmatter: Dict, body: str) -> float:
        """Evaluate maintainability (15%)"""
        score = 0.0

        # Clear naming convention (25%)
        name = frontmatter.get('name', '')
        naming_score = 1.0 if re.match(r'^[a-z][a-z0-9-]*[a-z0-9]$', name) else 0.5
        score += naming_score * 0.25

        # Collaboration patterns (25%)
        collaboration_keywords = ['collaborative', 'integration', 'workflow', 'coordinate']
        collab_count = sum(1 for keyword in collaboration_keywords if keyword.lower() in body.lower())
        collab_score = min(collab_count / 3, 1.0)
        score += collab_score * 0.25

        # Version control indicators (20%)
        version_indicators = ['Licensed under', 'Apache-2.0', 'last_updated']
        version_score = sum(1 for indicator in version_indicators if indicator in body) / len(version_indicators)
        score += version_score * 0.20

        # Update frequency potential (15%)
        update_score = 1.0 if 'Enhanced Capabilities' in body else 0.8
        score += update_score * 0.15

        # Documentation clarity (15%)
        doc_sections = ['##', '###', '####']
        doc_count = sum(body.count(section) for section in doc_sections)
        doc_score = min(doc_count / 15, 1.0)  # Target: 15+ headings
        score += doc_score * 0.15

        return min(score, 1.0)

    def _validate_yaml_structure(self, frontmatter: Dict) -> bool:
        """Validate YAML frontmatter structure"""
        required_fields = ['name', 'description']
        return all(field in frontmatter for field in required_fields)

    def _count_technical_terms(self, body: str) -> int:
        """Count technical terms and concepts"""
        tech_patterns = [
            r'\b(API|REST|GraphQL|HTTP|HTTPS|JSON|XML|YAML)\b',
            r'\b(database|SQL|NoSQL|PostgreSQL|MongoDB|Redis)\b',
            r'\b(Docker|Kubernetes|AWS|GCP|Azure|terraform)\b',
            r'\b(React|Vue|Angular|Node\.js|Python|Java|TypeScript)\b',
            r'\b(microservices|architecture|scalability|performance)\b'
        ]

        count = 0
        for pattern in tech_patterns:
            count += len(re.findall(pattern, body, re.IGNORECASE))

        return count

    def _evaluate_realism(self, body: str) -> float:
        """Evaluate realism of examples and patterns"""
        # Check for realistic code examples, proper syntax, real-world patterns
        code_blocks = re.findall(r'```[\s\S]*?```', body)

        if not code_blocks:
            return 0.5

        realistic_indicators = 0
        total_blocks = len(code_blocks)

        for block in code_blocks:
            # Check for realistic patterns
            if any(indicator in block for indicator in [
                'import ', 'from ', 'def ', 'class ', 'function',
                ':', '{', '}', ';', '//', '#', 'const ', 'let ', 'var '
            ]):
                realistic_indicators += 1

        return min(realistic_indicators / total_blocks, 1.0) if total_blocks > 0 else 0.5

    def _evaluate_domain_consistency(self, frontmatter: Dict, body: str) -> float:
        """Evaluate consistency between claimed expertise and content"""
        name = frontmatter.get('name', '').lower()
        description = frontmatter.get('description', '').lower()

        # Extract domain keywords from name and description
        domain_keywords = []
        if 'api' in name or 'api' in description:
            domain_keywords.extend(['REST', 'GraphQL', 'OpenAPI', 'endpoint'])
        if 'security' in name or 'security' in description:
            domain_keywords.extend(['authentication', 'authorization', 'encryption', 'vulnerability'])
        if 'performance' in name or 'performance' in description:
            domain_keywords.extend(['optimization', 'caching', 'latency', 'throughput'])

        if not domain_keywords:
            return 0.8  # Neutral score for unclear domain

        # Count domain keyword usage in body
        found_keywords = sum(1 for keyword in domain_keywords if keyword.lower() in body.lower())
        consistency_score = min(found_keywords / len(domain_keywords), 1.0)

        return max(consistency_score, 0.6)  # Minimum 60% for basic consistency

    def _evaluate_description_quality(self, description: str) -> float:
        """Evaluate quality of agent description for routing"""
        if not description or len(description) < 50:
            return 0.3

        quality_indicators = [
            len(description.split()) >= 20,  # Sufficient detail
            'expert' in description.lower() or 'specialist' in description.lower(),
            any(keyword in description.lower() for keyword in ['design', 'implement', 'optimize', 'manage']),
            '.' in description,  # Proper sentences
            description.count(',') >= 2  # Multiple capabilities listed
        ]

        return sum(quality_indicators) / len(quality_indicators)

    def _evaluate_content_structure(self, body: str) -> float:
        """Evaluate content organization and structure"""
        structure_indicators = [
            '## ' in body,  # Main sections
            '### ' in body,  # Subsections
            '```' in body,  # Code examples
            '- ' in body or '* ' in body,  # Lists
            body.count('\n\n') >= 10  # Proper paragraph breaks
        ]

        return sum(structure_indicators) / len(structure_indicators)

    def _count_actionable_elements(self, body: str) -> float:
        """Count actionable instructions and patterns"""
        actionable_patterns = [
            r'\b(implement|configure|setup|install|deploy|execute)\b',
            r'\b(step \d+|first|second|third|next|then|finally)\b',
            r'```[\s\S]*?```',  # Code blocks
            r'- \[.*?\]',  # Checklists
        ]

        total_actionable = 0
        for pattern in actionable_patterns:
            total_actionable += len(re.findall(pattern, body, re.IGNORECASE))

        return min(total_actionable / 15, 1.0)  # Target: 15+ actionable elements

    def _evaluate_example_quality(self, body: str) -> float:
        """Evaluate quality and usefulness of examples"""
        code_blocks = re.findall(r'```[\s\S]*?```', body)

        if not code_blocks:
            return 0.4

        quality_score = 0.0
        for block in code_blocks:
            # Check for comprehensive examples
            if len(block) > 100:  # Substantial code
                quality_score += 0.3
            if '# ' in block or '//' in block:  # Comments
                quality_score += 0.2
            if any(keyword in block for keyword in ['function', 'class', 'def', 'const']):  # Real code
                quality_score += 0.3

        return min(quality_score, 1.0)

    def _generate_detailed_analysis(self, filename: str, frontmatter: Dict, body: str, metrics: QualityMetrics) -> Dict:
        """Generate detailed quality analysis"""
        return {
            'filename': filename,
            'overall_score': round(metrics.overall_score, 2),
            'metrics': {
                'completeness': round(metrics.completeness, 2),
                'accuracy': round(metrics.accuracy, 2),
                'usability': round(metrics.usability, 2),
                'performance': round(metrics.performance, 2),
                'maintainability': round(metrics.maintainability, 2)
            },
            'analysis': {
                'word_count': len(body.split()),
                'code_blocks': len(re.findall(r'```[\s\S]*?```', body)),
                'sections': body.count('## '),
                'tools_specified': len(frontmatter.get('tools', [])) if frontmatter.get('tools') else 0,
                'mcp_integration': 'mcp__' in body.lower() or 'mcp' in body.lower(),
                'collaboration_section': 'collaborative' in body.lower()
            },
            'recommendations': self._generate_recommendations(metrics, frontmatter, body),
            'tier_classification': self._classify_tier(metrics.overall_score),
            'timestamp': datetime.now().isoformat()
        }

    def _generate_recommendations(self, metrics: QualityMetrics, frontmatter: Dict, body: str) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []

        if metrics.completeness < 0.8:
            recommendations.append("Add missing required sections (Core Expertise, Approach, etc.)")

        if metrics.accuracy < 0.8:
            recommendations.append("Improve technical accuracy and add more domain-specific terminology")

        if metrics.usability < 0.8:
            recommendations.append("Enhance description clarity and add more actionable instructions")

        if metrics.performance < 0.8:
            recommendations.append("Optimize tool selection and add MCP integration patterns")

        if metrics.maintainability < 0.8:
            recommendations.append("Improve documentation structure and add collaboration patterns")

        return recommendations

    def _classify_tier(self, score: float) -> str:
        """Classify agent tier based on quality score"""
        if score >= 9.0:
            return "Tier 0 - Meta (Orchestration)"
        elif score >= 8.0:
            return "Tier 1 - Foundation"
        elif score >= 7.5:
            return "Tier 2 - Specialist"
        elif score >= 7.0:
            return "Tier 3 - Expert"
        elif score >= 6.5:
            return "Tier 4 - Professional"
        else:
            return "Tier 5 - Developing"

    def evaluate_all_agents(self) -> Dict:
        """Evaluate all agents in the agents directory"""
        results = {}

        for agent_file in self.agents_dir.rglob("*.md"):
            if agent_file.name.startswith('.'):
                continue

            metrics, analysis = self.evaluate_agent(agent_file)
            results[str(agent_file.relative_to(self.agents_dir))] = {
                'metrics': metrics,
                'analysis': analysis
            }

        return results

    def generate_quality_report(self, output_file: str = "quality-report.json"):
        """Generate comprehensive quality report"""
        results = self.evaluate_all_agents()

        # Calculate summary statistics
        all_scores = [r['metrics'].overall_score for r in results.values() if hasattr(r['metrics'], 'overall_score')]

        summary = {
            'total_agents': len(results),
            'average_score': sum(all_scores) / len(all_scores) if all_scores else 0,
            'highest_score': max(all_scores) if all_scores else 0,
            'lowest_score': min(all_scores) if all_scores else 0,
            'tier_distribution': self._calculate_tier_distribution(all_scores),
            'evaluation_timestamp': datetime.now().isoformat()
        }

        report = {
            'summary': summary,
            'agents': results
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)

        return report

    def _calculate_tier_distribution(self, scores: List[float]) -> Dict[str, int]:
        """Calculate distribution of agents across quality tiers"""
        distribution = {
            'Tier 0 - Meta': 0,
            'Tier 1 - Foundation': 0,
            'Tier 2 - Specialist': 0,
            'Tier 3 - Expert': 0,
            'Tier 4 - Professional': 0,
            'Tier 5 - Developing': 0
        }

        for score in scores:
            tier = self._classify_tier(score)
            distribution[tier] += 1

        return distribution

def main():
    """Main execution function"""
    import argparse

    parser = argparse.ArgumentParser(description="Agent Quality Scoring System")
    parser.add_argument("--agents-dir", default="agents", help="Directory containing agent files")
    parser.add_argument("--output", default="quality-report.json", help="Output report file")
    parser.add_argument("--agent", help="Evaluate specific agent file")

    args = parser.parse_args()

    scorer = AgentQualityScorer(args.agents_dir)

    if args.agent:
        # Evaluate single agent
        agent_path = Path(args.agent)
        metrics, analysis = scorer.evaluate_agent(agent_path)
        print(f"Quality Score: {metrics.overall_score:.2f}")
        print(f"Tier: {analysis.get('tier_classification', 'Unknown')}")
        print("\nDetailed Metrics:")
        for metric, value in analysis['metrics'].items():
            print(f"  {metric.capitalize()}: {value}")

        if analysis.get('recommendations'):
            print("\nRecommendations:")
            for rec in analysis['recommendations']:
                print(f"  - {rec}")
    else:
        # Evaluate all agents
        report = scorer.generate_quality_report(args.output)
        print(f"Quality report generated: {args.output}")
        print(f"Total agents evaluated: {report['summary']['total_agents']}")
        print(f"Average quality score: {report['summary']['average_score']:.2f}")

if __name__ == "__main__":
    main()