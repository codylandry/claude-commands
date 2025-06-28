# Claude Commands

Version-controlled Claude commands using GNU Stow for symlink management.

## Overview

This repository contains custom Claude commands that can be managed with version control while being automatically available to the Claude CLI. It uses GNU Stow to create symbolic links between this repository and the `~/.claude/commands/` directory.

## Prerequisites

- [Claude CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
- [GNU Stow](https://www.gnu.org/software/stow/) installed:
  - macOS: `brew install stow`
  - Ubuntu/Debian: `apt install stow`
  - Other systems: See [GNU Stow installation guide](https://www.gnu.org/software/stow/)

## Quick Start

1. **Clone and setup:**
   ```bash
   cd ~/repos/personal/claude-commands
   ./setup.sh
   ```

2. **Make changes:**
   ```bash
   # Edit commands in dot-claude/commands/
   vim dot-claude/commands/new_command.md
   
   # Commit changes
   git add .
   git commit -m "Add new command"
   ```

3. **Use in Claude:**
   Commands are immediately available via `@commands/command_name`

## Directory Structure

```
claude-commands/
├── dot-claude/
│   └── commands/           # Command files (symlinked to ~/.claude/commands/)
│       ├── act_on_mr_comments.md
│       ├── code_review.md
│       ├── create_commit_message.md
│       ├── create_mr_description.md
│       ├── deep_research.md
│       ├── execute_step.md
│       └── plan_work.md
├── setup.sh              # Setup GNU Stow symlinks
├── teardown.sh           # Remove GNU Stow setup
└── README.md             # This file
```

## Available Commands

- **`act_on_mr_comments.md`** - Handle merge request comments and feedback
- **`code_review.md`** - Comprehensive code review with security analysis
- **`create_commit_message.md`** - Generate contextual commit messages
- **`create_mr_description.md`** - Generate merge request descriptions
- **`deep_research.md`** - Conduct comprehensive research with multiple agents
- **`execute_step.md`** - Execute implementation steps from working documents  
- **`plan_work.md`** - Create structured implementation plans

## Scripts

### `setup.sh`
Sets up GNU Stow to manage your Claude commands:
- Backs up existing `~/.claude/commands/` directory
- Creates symbolic links from repository to Claude commands directory
- Verifies setup completion

### `teardown.sh`  
Removes GNU Stow management:
- Removes symbolic links
- Copies files back to regular directory structure
- Preserves command functionality without version control

## Usage

### Adding New Commands
1. Create new `.md` file in `dot-claude/commands/`
2. Write your command following Claude command format
3. Commit changes: `git add . && git commit -m "Add new command"`
4. Command immediately available in Claude

### Editing Existing Commands
1. Edit files in `dot-claude/commands/`
2. Changes are immediately reflected in Claude
3. Commit when ready: `git add . && git commit -m "Update command"`

### Managing Versions
```bash
# View command history
git log --oneline

# Revert to previous version
git checkout <commit-hash> dot-claude/commands/command_name.md

# Create branches for experimental commands
git checkout -b experimental-features
```

## Troubleshooting

### Commands not appearing in Claude
- Verify symlinks: `ls -la ~/.claude/commands/`
- Re-run setup: `./setup.sh`
- Check Claude CLI configuration

### Stow conflicts
- Remove existing files: `rm ~/.claude/commands/*`
- Re-run setup: `./setup.sh`

### Backup recovery
- Automatic backups created in `~/.claude/commands.backup.TIMESTAMP/`
- Restore: `cp -r ~/.claude/commands.backup.*/  ~/.claude/commands/`

## Contributing

1. Fork this repository
2. Create feature branch: `git checkout -b feature-name`
3. Add/modify commands in `dot-claude/commands/`
4. Test commands with Claude
5. Commit changes: `git commit -m "Add feature"`
6. Push and create pull request

## License

This repository contains personal Claude commands. Use and modify as needed.