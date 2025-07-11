# Context Resources Guide

This document helps Claude understand where to find different types of contextual information and how to use available resources effectively.

## Local Context Files

### `glab`: ~/.claude/context/glab.md
- **Purpose**: GitLab CLI usage patterns and commands
- **When to use**: Working with GitLab repositories, merge requests, issues
- **Contains**: Command examples, workflow patterns, API usage

### `jira`: ~/.claude/context/jira.md
- **Purpose**: Jira integration and ticket management
- **When to use**: Working with tickets, understanding requirements, project tracking
- **Contains**: Jira CLI commands, ticket analysis patterns, workflow integration

## MCP Server Resources

### Engineering Index MCP
- **Purpose**: Zapier company policies, guides, architecture docs, best practices, zinnia design system documentation
- **When to use**: Understanding Zapier engineering standards, architectural decisions, company-wide practices
- **Contains**: Engineering guidelines, coding standards, infrastructure documentation

### Coda MCP
- **Purpose**: Zapier's primary documentation hub
- **When to use**: Project briefs, team documentation, organizational docs, ADRs, RFCs
- **Contains**: 
  - Project specifications and briefs
  - Team and zone documentation
  - Architectural Decision Records (ADRs)
  - Request for Comments (RFCs)
  - Process documentation

### Zapier MCP
- **Purpose**: Zapier Slack conversations and internal communications
- **When to use**: Understanding context around feature development, team discussions, decision rationale
- **Contains**: Slack conversations, team communications, development discussions

## Context Gathering Strategy

1. **Start Local**: Check relevant context files in this directory first
2. **Expand to Documentation**: Use Coda MCP for formal documentation and project specs
3. **Understand Standards**: Use Engineering Index MCP for company practices and guidelines
4. **Gather Social Context**: Use Zapier MCP for team discussions and decision context
5. **Technical Implementation**: Use GitLab/Jira context for specific implementation patterns

## Usage Patterns

- **New Feature Development**: Coda (project brief) → Engineering Index (standards) → Zapier MCP (team discussions)
- **Bug Investigation**: Jira (ticket context) → Zapier MCP (related discussions) → GitLab (code patterns)
- **Architecture Decisions**: Engineering Index (standards) → Coda (ADRs/RFCs) → Zapier MCP (team input)
- **Code Review**: Engineering Index (best practices) → GitLab (merge request patterns) → local context files