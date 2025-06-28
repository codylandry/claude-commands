---
allowed-tools: [Bash, Read, Grep, Glob]
description: Comprehensive code review with security analysis and scope validation
---

# Code Review Command

Conduct a thorough code review of changes in the current branch, identifying areas for improvement across multiple dimensions of code quality.

## Current Branch Context
!git branch --show-current
!git log --oneline -5
!git diff --name-only HEAD~1..HEAD

## Project Context
@CLAUDE.md
@package.json
@.eslintrc.json || @eslint.config.js
@tsconfig.json

## Review Scope

Analyze all changes in the current branch against the base branch (typically main/master), focusing on:

### Code Quality
- **Code smells**: Identify duplicated code, long methods, large classes, inappropriate comments
- **Design patterns**: Check for anti-patterns, missing design patterns where beneficial
- **SOLID principles**: Evaluate adherence to single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **Clean code**: Assess readability, naming conventions, function/class size, complexity

### Security Analysis
- **Input validation**: Check for proper sanitization and validation of user inputs
- **Authentication/Authorization**: Review access controls and permission checks
- **Data exposure**: Look for potential information leakage, hardcoded secrets
- **Injection vulnerabilities**: SQL injection, XSS, command injection risks
- **Cryptographic practices**: Proper use of encryption, hashing, random number generation
- **Error handling**: Ensure errors don't expose sensitive information

### Logic & Behavior Analysis
- **Logical inconsistencies**: Check for contradictory logic, unreachable code, or conflicting conditions
- **Scope creep**: Identify functionality that goes beyond the stated requirements
- **Unnecessary complexity**: Flag over-engineered solutions or excessive abstractions
- **Feature bloat**: Spot additions that weren't requested or needed
- **AI agent overreach**: Look for signs of excessive automation or functionality added without explicit requirement

### Performance & Efficiency
- **Algorithmic complexity**: Identify inefficient algorithms or data structures
- **Resource usage**: Memory leaks, excessive memory allocation, blocking operations
- **Database queries**: N+1 problems, missing indexes, inefficient queries
- **Caching opportunities**: Identify areas where caching could improve performance

### Testing & Documentation
- **Test coverage**: Assess completeness of unit, integration, and end-to-end tests
- **Test quality**: Check for meaningful assertions, proper mocking, edge case coverage
- **Documentation**: Evaluate code comments, API documentation, README updates
- **Maintainability**: Consider how easy the code will be to modify and extend

## Automated Analysis Steps

1. **Changed Files Analysis**
   !git diff --stat HEAD~1..HEAD
   !git diff HEAD~1..HEAD --name-only | head -20

2. **Dependency Changes**
   !git diff HEAD~1..HEAD package.json || echo "No package.json changes"
   !git diff HEAD~1..HEAD requirements.txt || echo "No requirements.txt changes"

3. **Configuration Changes**
   !git diff HEAD~1..HEAD --name-only | grep -E '\.(json|yaml|yml|env|config)$' || echo "No config file changes"

4. **Test Coverage Assessment**
   !find . -name "*test*" -o -name "*spec*" | grep -E '\.(js|ts|py|rb|go)$' | wc -l | awk '{print "Test files found: " $1}'

## Detailed Review Process

1. **Code Quality Analysis**: Examine each changed file for design patterns, SOLID principles, and clean code practices
2. **Security Review**: Check for vulnerabilities, input validation, and secure coding practices  
3. **Logic Validation**: Verify the implementation matches requirements without scope creep
4. **Performance Assessment**: Identify potential bottlenecks and optimization opportunities
5. **Testing Evaluation**: Ensure adequate test coverage for new and modified functionality

## Review Output Format

Structure your review as follows:

### Executive Summary
- **Files Changed**: [Number] files modified/added/deleted
- **Risk Level**: LOW/MEDIUM/HIGH based on security and stability concerns
- **Scope Assessment**: Implementation alignment with stated requirements
- **Overall Quality**: Brief assessment of code quality and maintainability

### Priority Findings

#### 🔴 Critical Issues (Block Merge)
- Security vulnerabilities requiring immediate attention
- Breaking changes that affect API compatibility  
- Major bugs or logic errors causing incorrect behavior
- Data integrity or corruption risks

#### 🟡 Important Issues (Fix Before Merge)
- Performance bottlenecks or resource leaks
- Code smells affecting maintainability
- Missing error handling for critical paths
- Inadequate test coverage for new functionality

#### 🟠 Scope & Architecture Concerns
- Features exceeding stated requirements
- Over-engineered solutions where simpler approaches exist
- Missing business logic validation
- Architectural inconsistencies with existing patterns

#### 🟢 Optimization Opportunities  
- Code style and formatting improvements
- Documentation enhancements
- Performance optimizations (non-critical)
- Refactoring opportunities for better readability

### Implementation Analysis

#### Security Review
- Input validation and sanitization
- Authentication and authorization checks
- Sensitive data handling
- Cryptographic implementations

#### Code Quality Assessment
- Adherence to project conventions
- Design pattern usage
- SOLID principle compliance
- Clean code practices

#### Testing Coverage
- Unit test adequacy for new code
- Integration test requirements
- Edge case handling
- Mock usage and test quality

### Action Items
1. **Immediate**: Critical security and stability fixes
2. **Pre-merge**: Important quality and functionality issues  
3. **Follow-up**: Optimization and enhancement opportunities
4. **Documentation**: Update requirements if scope questions arise

## Review Guidelines

### Analysis Approach
- Reference specific files and line numbers for all findings
- Provide concrete code examples for suggested improvements
- Consider existing project patterns and conventions
- Balance thoroughness with practical actionability
- Focus on meaningful issues rather than stylistic preferences
- **Analyze and document only** - do not attempt to fix identified issues
- Question scope creep and unnecessary feature additions

### Quality Standards
- Verify alignment with business requirements
- Check for proper error handling and edge cases
- Evaluate security implications of all changes
- Assess performance impact on existing functionality
- Ensure adequate test coverage for reliability

### Success Criteria
✅ **Comprehensive**: All changed files reviewed systematically  
✅ **Actionable**: Clear priority and specific remediation steps  
✅ **Balanced**: Highlights both issues and good practices  
✅ **Scoped**: Validates requirements alignment and necessity  

## Execution Workflow

The command will automatically:
1. Gather git context and project configuration
2. Analyze all changed files systematically  
3. Cross-reference with tests and documentation
4. Generate prioritized findings with actionable recommendations
5. Validate scope alignment with stated requirements

Begin the review by running the automated analysis steps above, then proceed with detailed examination of each changed file.