---
allowed-tools: [Bash, Read, mcp__zapier__jira_software_cloud_find_issues_]
description: Generate comprehensive merge request descriptions with dynamic analysis
---

# MR Description Generator

Generate professional merge request description for: $ARGUMENTS

## Current Branch Analysis
!git branch --show-current
!git log --oneline origin/main..HEAD
!git diff --name-only origin/main..HEAD

## GitLab Template Check
@.gitlab/merge_request_templates/Default.md

## Jira Integration (if applicable)
Extract ticket key from branch name and fetch details using Jira MCP tools if available.

## Analysis & Generation Workflow

1. **Analyze Changes**: Review git diff, commits, and modified files
2. **Extract Context**: Get Jira ticket details from branch name if present
3. **Use Template**: Apply GitLab template if exists, otherwise use standard format
4. **Generate Description**: Create comprehensive MR description
5. **Copy to Clipboard**: Use `echo "description" | pbcopy` for immediate use

## Standard MR Template

```markdown
## Summary
Brief overview of changes and business value.

## Changes Made
### Features
- New functionality added

### Bug Fixes  
- Issues resolved

### Technical Changes
- Refactoring, performance, technical debt

## Jira Ticket
KEY-123: Ticket Title
Description of ticket requirements and implementation approach.

## Testing
### Automated Tests
- Test coverage details

### Manual Testing
1. Setup requirements
2. Test steps with specific commands
3. Expected outcomes

**Provide executable commands when possible:**
- API changes: `curl -X GET "https://gitlab-preview.company.com/api/v1/endpoint"`
- Frontend changes: `npm run dev` then visit `http://localhost:3000/feature-path`
- Script execution: `npm run test:integration` or `python scripts/validate_feature.py`
- Database changes: `npm run db:migrate && npm run db:seed`

## Breaking Changes
- Migration steps if applicable

## Deployment Notes
- Special considerations
- Environment configurations

## Checklist
- [ ] Code follows project standards
- [ ] Tests added for new functionality  
- [ ] Documentation updated
- [ ] Manual testing completed
```

## Implementation Instructions

Execute these steps to generate a comprehensive MR description:

1. **Extract branch context**: Parse branch name for Jira ticket keys (ABC-123, XYZ-456 patterns)
2. **Analyze all changes**: Review commits, file modifications, and scope of changes  
3. **Categorize changes**: Identify features, bug fixes, technical debt, infrastructure updates
4. **Fetch Jira details**: Use MCP tools to get ticket information if ticket key found
5. **Apply template**: Use GitLab template if available, otherwise standard format
6. **Generate description**: Create comprehensive, reviewer-friendly description
7. **Add executable commands**: Include specific commands reviewers can run to test changes
8. **Copy to clipboard**: Execute `echo "description" | pbcopy` for immediate use

**Key Focus**: Reduce reviewer friction by providing specific, executable commands for testing changes.
Examples: curl commands for API changes, npm scripts for features, database migration commands.