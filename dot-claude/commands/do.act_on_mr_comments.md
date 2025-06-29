---
allowed-tools: [Bash, Read, Edit, Write, Grep, Glob, Task]
description: Analyze MR comments and implement requested changes with comprehensive workflow
---

# MR Comments Implementation Assistant

Analyze merge request comments and implement requested changes systematically: $ARGUMENTS

## Your Analysis and Implementation Process

## Current Context
**Branch:** !git branch --show-current
**Project:** @CLAUDE.md
**Working Document:** @.ai-workspace/$(git branch --show-current)/working-doc.md

## MR Information
!glab mr view --comments

## Recent Changes
!git log --oneline -5
!git diff main...HEAD --name-only

## Implementation Workflow

### 1. Analyze Comments
- Categorize feedback: bugs, improvements, questions, style
- Identify actionable vs. informational comments
- Assess priority and complexity

### 2. Create Implementation Plan
- Break down actionable comments into specific tasks
- Reference working document patterns
- Consider dependencies and conflicts
- Estimate scope and complexity

### 3. Get User Approval
Present comprehensive plan with:
- Summary of actionable comments
- Proposed implementation steps
- Potential conflicts or concerns
- Request explicit approval before proceeding

### 4. Execute Implementation
- Follow working document patterns
- Implement incrementally with testing
- Run quality checks after each change
- Update documentation and commit changes

## Success Criteria
- [ ] All actionable comments addressed
- [ ] Code quality maintained
- [ ] Tests passing
- [ ] Working document updated
- [ ] Changes committed with clear messages

## Quick Reference

### Essential Commands
```bash
# MR Operations
glab mr view --comments                    # Get MR with comments
glab mr note --message "Response"         # Add response note

# Context Gathering  
jira issue view <key>                     # Get ticket context
git log --oneline -5                      # Recent commits
git diff main...HEAD                      # Branch changes

# Quality Checks
npm run test                              # Run tests
npm run lint                              # Check linting
npm run type-check                        # Type checking
```

### Comment Types
**Actionable:** Code changes, bug fixes, tests, documentation
**Informational:** Questions, praise, future considerations

Follow project patterns and maintain code quality standards.