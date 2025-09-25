---
description: Comprehensive security audit of agents and infrastructure
args: [--scope agents|scripts|configs|all] [--level basic|advanced|comprehensive] [--fix-issues]
tools: Task, Grep, Read
model: claude-sonnet-4-20250514
---

## Objective
Perform thorough security auditing of agent configurations, scripts, and infrastructure with automated vulnerability detection and remediation.

## Before You Run
- Ensure you have appropriate permissions for security scanning
- Update vulnerability databases if applicable
- Review current security policies and compliance requirements
- Backup current configurations before applying fixes

## Execution
Run security audit with different scopes:

```bash
# Comprehensive security audit
!/security-audit --scope all --level comprehensive

# Quick agent security check
!/security-audit --scope agents --level basic

# Advanced audit with auto-fix
!/security-audit --scope all --level advanced --fix-issues
```

## Security Audit Scope

### Agent Security Analysis
- **Tool Permissions**: Verify minimal privilege principle
- **Input Validation**: Check for injection vulnerabilities
- **Output Sanitization**: Prevent information disclosure
- **Access Controls**: Validate permission boundaries
- **Dependency Analysis**: Check for vulnerable dependencies

### Script Security Review
- **Shell Injection**: Scan for command injection risks
- **Path Traversal**: Verify file access restrictions
- **Privilege Escalation**: Check for unsafe privilege usage
- **Input Sanitization**: Validate user input handling
- **Error Handling**: Prevent information leakage

### Configuration Security
- **Credential Management**: Identify hardcoded secrets
- **File Permissions**: Verify secure file access
- **Network Security**: Check communication protocols
- **Encryption Usage**: Validate data protection
- **Audit Logging**: Ensure comprehensive logging

## Vulnerability Categories

### Critical Vulnerabilities
- **Remote Code Execution**: Command injection, unsafe eval
- **Privilege Escalation**: Sudo misuse, setuid issues
- **Data Exfiltration**: Unauthorized data access
- **Authentication Bypass**: Weak access controls

### High Priority Issues
- **Information Disclosure**: Sensitive data exposure
- **Denial of Service**: Resource exhaustion vulnerabilities
- **Cross-Site Scripting**: Output sanitization issues
- **Insecure Defaults**: Weak default configurations

### Medium Priority Issues
- **Insecure Communications**: Unencrypted channels
- **Weak Cryptography**: Outdated encryption methods
- **Session Management**: Poor session handling
- **Input Validation**: Insufficient input checks

## Automated Security Checks

### Static Analysis
```bash
# Check for hardcoded secrets
grep -r -i "password\|secret\|key\|token" --include="*.md" --include="*.sh" .

# Find world-writable files
find . -type f -perm -002 -ls

# Check for unsafe shell patterns
grep -r "eval\|exec\|system" --include="*.sh" .

# Validate file permissions
find . -type f -name "*.sh" ! -perm 755 -ls
```

### Configuration Validation
```bash
# Check SSH configuration
if [ -f ~/.ssh/config ]; then
    grep -E "(PasswordAuthentication|PermitRootLogin)" ~/.ssh/config
fi

# Validate Git configuration
git config --list | grep -E "(user\.email|user\.name)"

# Check environment variables
env | grep -v "^_" | sort
```

### Dependency Security
```bash
# Check for outdated packages
npm audit || pip audit || bundle audit

# Verify GPG signatures
git verify-commit HEAD 2>/dev/null || echo "Unsigned commit detected"
```

## Compliance Frameworks

### OWASP Top 10 Compliance
- [ ] A01: Broken Access Control
- [ ] A02: Cryptographic Failures
- [ ] A03: Injection Vulnerabilities
- [ ] A04: Insecure Design
- [ ] A05: Security Misconfiguration
- [ ] A06: Vulnerable Components
- [ ] A07: Authentication Failures
- [ ] A08: Software Integrity Failures
- [ ] A09: Logging/Monitoring Failures
- [ ] A10: Server-Side Request Forgery

### CIS Controls
- **Inventory Management**: Asset discovery and tracking
- **Software Management**: Secure software deployment
- **Configuration Management**: Secure configurations
- **Access Control**: Principle of least privilege
- **Logging and Monitoring**: Security event tracking

## Security Hardening

### Agent Hardening
- **Tool Restriction**: Remove unnecessary tool permissions
- **Input Validation**: Strengthen input sanitization
- **Output Filtering**: Prevent data leakage
- **Error Handling**: Secure error management
- **Timeout Enforcement**: Prevent resource exhaustion

### Script Hardening
```bash
# Secure shell script patterns
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Input validation example
if [[ ! "$input" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Invalid input" >&2
    exit 1
fi

# Secure temporary files
TMP_FILE=$(mktemp) || exit 1
trap 'rm -f "$TMP_FILE"' EXIT
```

### Configuration Hardening
- **File Permissions**: Restrict access to sensitive files
- **Network Policies**: Implement network segmentation
- **Encryption**: Enable encryption in transit and at rest
- **Monitoring**: Comprehensive security logging

## Incident Response

### Automated Response
- **Quarantine**: Isolate compromised components
- **Alerting**: Notify security team immediately
- **Logging**: Capture detailed forensic information
- **Rollback**: Revert to last known good state

### Manual Response Procedures
1. **Assessment**: Evaluate scope and impact
2. **Containment**: Prevent further damage
3. **Investigation**: Root cause analysis
4. **Recovery**: Restore secure operations
5. **Lessons Learned**: Update security measures

## Security Reporting

### Vulnerability Report Format
```json
{
  "scan_id": "audit-2024-01-15-001",
  "timestamp": "2024-01-15T10:30:00Z",
  "scope": "comprehensive",
  "summary": {
    "critical": 0,
    "high": 2,
    "medium": 5,
    "low": 12
  },
  "vulnerabilities": [
    {
      "severity": "high",
      "category": "injection",
      "description": "Potential command injection in script",
      "file": "scripts/install-agents.sh:127",
      "remediation": "Add input validation and sanitization"
    }
  ],
  "recommendations": [
    "Implement input validation framework",
    "Enable security logging",
    "Regular dependency updates"
  ]
}
```

### Compliance Dashboard
- **Security Score**: Overall security posture (0-100)
- **Vulnerability Trends**: Issues over time
- **Remediation Status**: Fix implementation progress
- **Compliance Status**: Framework adherence levels

## Continuous Security

### Automated Security Pipeline
- **Pre-commit Hooks**: Security checks before commits
- **CI/CD Integration**: Security gates in deployment
- **Regular Scanning**: Scheduled vulnerability assessments
- **Dependency Monitoring**: Automated dependency updates

### Security Metrics
- **Mean Time to Detection (MTTD)**: < 24 hours
- **Mean Time to Response (MTTR)**: < 4 hours
- **Vulnerability Fix Rate**: > 95% within SLA
- **Security Test Coverage**: > 80% of codebase

## Follow Up
- Review security audit findings with team
- Prioritize vulnerability remediation
- Update security policies and procedures
- Schedule regular security training
- Implement continuous monitoring
- Document security improvements

## Emergency Contacts
- **Security Team**: security@company.com
- **Incident Response**: incident-response@company.com
- **On-call Engineer**: +1-555-SECURITY
- **External Security Firm**: vendor-security@partner.com
