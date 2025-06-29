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
│   ├── research-findings.md    # Detailed research findings and analysis
│   ├── implementation-notes.md # Implementation-specific decisions and patterns
│   ├── analysis.md            # Code analysis and architectural insights
│   └── flow-state.json        # Flow orchestration state and progress tracking
└── TICKET-456/
    ├── working-doc.md
    ├── research-findings.md
    └── flow-state.json
```

#### Usage Guidelines

**Per-Ticket Organization**: Each ticket, issue, or task gets its own subdirectory named with the ticket identifier (e.g., JIRA key, GitHub issue number).

**Document Types**:
- **working-doc.md**: Core planning document with implementation steps, requirements, and progress tracking
- **research-findings.md**: Comprehensive research outputs from the flow research agent
- **implementation-notes.md**: Technical decisions, patterns discovered, and implementation-specific insights
- **analysis.md**: Code analysis, architecture reviews, and system understanding
- **flow-state.json**: Flow orchestration state tracking phases, agent history, and workflow progress

**AI Command Integration**: 
- The `flow:start` command orchestrates complete development workflows using specialized agents
- The `agents/flow/research` agent produces comprehensive research findings and analysis
- The `agents/flow/planning` agent creates detailed implementation plans and working documents
- The `agents/flow/execution` agent executes specific implementation steps from working documents
- The `agents/flow/validation` agent performs quality assurance and validation
- The `agents/flow/commit` agent creates commits at workflow checkpoints
- The `agents/flow/state_manager` agent tracks workflow progress and state

**Flow-Based Workflow Approach**:

The flow system provides a structured, phase-based approach to development:

1. **Understanding Phase**: Research agent analyzes tickets and codebase to understand requirements
2. **Planning Phase**: Planning agent creates detailed implementation plans with step-by-step breakdowns
3. **Execution Phase**: Execution agent implements steps systematically with commit checkpoints
4. **Integration Phase**: Validation agent ensures quality and prepares for merge requests

Each phase includes:
- User checkpoints for approval before proceeding
- State tracking via flow-state.json for workflow continuity
- Specialized agents optimized for specific tasks
- Automatic commit creation at logical checkpoints

**Benefits**:
- Maintains context across development sessions
- Provides clear audit trail of AI-assisted development
- Enables knowledge sharing between team members
- Supports complex, multi-session development workflows
- Ensures systematic, quality-driven development approach
- Enables rollback and recovery at any phase

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