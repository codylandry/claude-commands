# Global Claude Configuration

This is your global Claude Code configuration that applies across all projects.

## AI Behavior Instructions

### Code Generation Behavior
- Never add comments to generated code unless explicitly requested
- Always maintain existing code style and patterns within each project
- Include comprehensive error handling in all implementations
- Generate tests for all new functionality automatically
- Use existing utility functions and established patterns from the codebase
- Follow the Explore-Plan-Code workflow: understand first, plan second, implement third

### Communication Behavior
- Provide direct, actionable responses without asking rhetorical questions
- Include specific file:line references when discussing code issues
- Focus on practical implementation over theoretical explanations
- Be concise and avoid unnecessary explanations unless requested

### Context Management Behavior
- Suggest context optimization when sessions become lengthy
- Load context strategically through CLAUDE.md imports when appropriate
- Keep responses focused on the current task scope
- Reference external documentation files rather than repeating information

### Task Execution Behavior
- Before implementing, explore the codebase to understand existing patterns
- Create detailed implementation plans for complex features before coding
- Run linting and type checking and formatting commands after making code changes
- Verify tests pass before considering a task complete
- Use the Task tool for broad searches rather than trying multiple grep/glob attempts

## Repository Structure Conventions

### .ai-workspace Directory

The `.ai-workspace` directory is used for collaborative AI development work. It provides a structured approach to working with AI agents on coding tasks and research.

#### Directory Structure

```
.ai-workspace/
├── TICKET-123/
│   ├── working-doc.md          # Main implementation plan and progress tracking
│   ├── deep-research.md        # Detailed research findings and analysis
│   ├── implementation-notes.md # Implementation-specific decisions and patterns
│   └── analysis.md            # Code analysis and architectural insights
└── TICKET-456/
    ├── working-doc.md
    └── research-findings.md
```

#### Usage Guidelines

**Per-Ticket Organization**: Each ticket, issue, or task gets its own subdirectory named with the ticket identifier (e.g., JIRA key, GitHub issue number).

**Document Types**:
- **working-doc.md**: Core planning document with implementation steps, requirements, and progress tracking
- **deep-research.md**: Comprehensive research outputs from the deep_research command
- **implementation-notes.md**: Technical decisions, patterns discovered, and implementation-specific insights
- **analysis.md**: Code analysis, architecture reviews, and system understanding

**AI Command Integration**: 
- The `plan_work` command creates working documents in this structure
- The `execute_step` command reads and updates working documents here
- The `deep_research` command outputs detailed findings to research documents
- The `act_on_mr_comments` command references working documents for context

**Benefits**:
- Maintains context across development sessions
- Provides clear audit trail of AI-assisted development
- Enables knowledge sharing between team members
- Supports complex, multi-session development workflows

## Development Context

### Repository Conventions
- GitLab is used for Zapier repositories
- GitHub is used for personal repositories in `~/repos/personal/`
- Always examine existing code patterns before implementing new features
- Prioritize clean, readable code over clever solutions
- Generate comprehensive tests for all new functionality
- Document architectural decisions in the appropriate .ai-workspace files

### Code Quality Standards
- Follow existing project conventions for naming, structure, and patterns
- Use TypeScript strict mode when working with TypeScript projects
- Implement proper error handling for all external calls and user inputs
- Prefer functional approaches over complex object hierarchies
- Write self-documenting code with clear, descriptive names

### Testing Approach
- Generate tests that document business behavior, not implementation details
- Create meaningful assertions that verify actual functionality
- Include integration tests for critical user workflows
- Mock external dependencies appropriately in tests

## Tools and Shortcuts

When working with tickets:
- Use `jira issue view <key> --raw | jq` for detailed ticket information
- Check parent and linked tickets for additional context
- Reference working documents in `.ai-workspace/<ticket-key>/` for implementation context