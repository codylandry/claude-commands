# Global Claude Configuration

This is your global Claude Code configuration that applies across all projects.

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

## Development Preferences

- We use GitLab for Zapier repositories
- We use GitHub for personal repositories in `~/repos/personal/`
- Always reference existing code patterns before implementing new features
- Focus on clean, readable code over clever solutions
- Include comprehensive tests for all new functionality
- Document architectural decisions in the appropriate .ai-workspace files

## Tools and Shortcuts

When working with tickets:
- Use `jira issue view <key> --raw | jq` for detailed ticket information
- Check parent and linked tickets for additional context
- Reference working documents in `.ai-workspace/<ticket-key>/` for implementation context