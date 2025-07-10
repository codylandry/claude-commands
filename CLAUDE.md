# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository manages version-controlled Claude CLI commands using GNU Stow for symlink management. It provides a sophisticated flow-based development system with specialized agents for orchestrating complete development workflows.

## Core Architecture

### Command Management System
- **Primary Directory**: `dot-claude/` contains all Claude CLI configuration files
- **Symlink Management**: GNU Stow creates symlinks from `dot-claude/` to `~/.claude/`
- **Command Structure**: Commands are organized in `dot-claude/commands/` with YAML frontmatter defining allowed tools and descriptions

### Flow-Based Agent System
The repository implements a multi-agent workflow system:
- **Supervisor Agent**: Orchestrates development workflows through defined phases
- **Research Agent**: Analyzes tickets and codebases to understand requirements
- **Planning Agent**: Creates detailed implementation plans from research findings
- **Execution Agent**: Implements steps systematically with commit checkpoints
- **Validation Agent**: Performs quality assurance and prepares for integration
- **Commit Agent**: Creates commits at logical workflow checkpoints

### Hook System
- **Notification Hook**: Python-based system for voice notifications during Claude sessions
- **Stop Hook**: Cleanup and logging when Claude sessions end
- **Utilities**: Shared utilities for error handling, message generation, and context extraction

## Common Development Commands

### Setup and Management
```bash
# Initial setup (creates symlinks)
./setup.sh

# Remove symlinks and restore direct file management
./teardown.sh

# Verify symlink status
ls -la ~/.claude/commands/
```

### Flow Commands (Available in Claude)
```bash
# Start new development workflows
@flow.start

# Resume existing workflows
@flow.continue

# Collect system improvement feedback
@flow.tune
```

### Generation Commands (Available in Claude)
```bash
# Generate contextual commit messages
@gen.commit_message

# Generate merge request descriptions
@gen.mr_description
```

### Action Commands (Available in Claude)
```bash
# Comprehensive code review with security analysis
@do.code_review

# Handle merge request comments and feedback
@do.act_on_mr_comments

# Conduct comprehensive research with multiple agents
@do.research

# Copy files with intelligent handling
@do.copy
```

## Directory Structure and Key Files

### Command Files
- `dot-claude/commands/` - All Claude commands with YAML frontmatter
- `dot-claude/commands/flow/` - Flow orchestration commands
- `dot-claude/agents/flow/` - Specialized agent definitions with process diagrams

### Configuration
- `dot-claude/settings.json` - Permissions and hook configuration
- `dot-claude/CLAUDE.md` - Global Claude configuration (separate from this project-specific file)

### Hook System
- `dot-claude/hooks/` - Python-based notification and cleanup hooks
- `dot-claude/hooks/utils/` - Shared utilities for transcript parsing, TTS, and error handling

## Workflow Management

### .ai-workspace Convention
The system uses `.ai-workspace/` directories for ticket-based development:
```
.ai-workspace/
├── TICKET-123/
│   ├── working-doc.md          # Progress tracking and implementation plan
│   └── research-findings.md    # Technical analysis and architectural decisions
```

### Flow Phases
1. **Understanding Phase**: Research agent analyzes requirements and codebase
2. **Planning Phase**: Planning agent creates detailed implementation steps
3. **Execution Phase**: Execution agent implements steps with commit checkpoints
4. **Integration Phase**: Validation agent ensures quality and prepares for merge

### Working Document Structure
Each workflow maintains state in `working-doc.md` with:
- Current phase and progress tracking
- Milestone completion status
- Implementation steps with checkboxes
- Blocker documentation
- Quality indicators (tests, linting)
- Commit history with hashes

## Technical Implementation Notes

### Agent Delegation Protocol
When using flow commands, agents are invoked using the Task tool with:
- Agent path: `agents/flow/{agent_name}`
- Specific task description with context
- Expected deliverable format
- Feedback preferences for instruction detail level

### Hook System Requirements
- Python virtual environment at `~/.claude/hooks/.venv/`
- Dependencies managed via `requirements.txt`
- Setup script creates and configures environment
- Utilities provide shared functionality across hooks

### Command Development
When creating new commands:
1. Add `.md` file to `dot-claude/commands/`
2. Include YAML frontmatter with description and allowed-tools
3. Follow existing command patterns for consistency
4. Commands become immediately available after file creation (via symlinks)

## Quality and Testing

### Code Quality Standards
- All workflow phases include quality checkpoints
- Validation agent performs comprehensive security and quality analysis
- Commit agent ensures proper commit message formatting
- Flow system includes automated error recovery and user checkpoints

### Error Handling
- Working documents track blockers with detailed descriptions
- Each phase includes error recovery paths
- User approval required for phase transitions
- Clear escalation paths for unresolvable issues

## Security Considerations

The repository includes defensive security tooling:
- Code review commands include security analysis
- Hook system isolates execution in virtual environments
- Permission system restricts file access to appropriate directories
- Agent system prevents direct code execution, requiring delegation

## Development Guidelines

### Adding New Commands
1. Create command file in `dot-claude/commands/` with proper frontmatter
2. Test command functionality through Claude CLI
3. Commit changes to version control
4. Commands are immediately available due to symlink management

### Modifying Flow Agents
1. Edit agent files in `dot-claude/agents/flow/`
2. Agents are read dynamically by flow commands
3. Follow existing agent patterns and process diagrams
4. Update supervision preferences in feedback files as needed

### Hook Development
1. Add Python scripts to `dot-claude/hooks/`
2. Use shared utilities from `utils/` directory
3. Test with hook setup script
4. Configure in `settings.json` with appropriate matchers