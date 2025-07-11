---
description: Helpful when using the jira CLI (ankitpokhrel/jira-cli) for issue management and automation
globs: 
alwaysApply: false
---
# Jira CLI Commands

This document provides a quick reference for common operations using the `jira` CLI tool (ankitpokhrel/jira-cli). This is an interactive command-line interface for Atlassian Jira.

### Configuration Management
```bash
# Use specific config file
jira --config /path/to/custom/.config.yml

# Check current user
jira me

# Test server connectivity
jira serverinfo

# Default config location
# ~/.config/.jira/.config.yml
```

## Issue Management

### Listing Issues
```bash
# Basic listing
jira issue list

# Filter by assignee (use email or display name)
jira issue list -a "john.doe@company.com"
jira issue list -a "John Doe"

# Filter by type, status, priority
jira issue list -t Bug -s "In Progress" -y High

# Filter by labels and created date
jira issue list -l backend -l urgent --created month

# Filter by component and reporter
jira issue list -C "Backend Team" -r "jane.doe@company.com"

# Use JQL (Jira Query Language)
jira issue list -q "project = PROJ AND assignee = currentUser()"
jira issue list -q "project IS NOT EMPTY"

# Recently accessed or watching
jira issue list --history
jira issue list --watching

# Date filters
jira issue list --created today
jira issue list --updated week
jira issue list --created-after 2024-01-01
jira issue list --updated-before 2024-12-31

# Output formatting
jira issue list --plain
jira issue list --plain --no-headers
jira issue list --plain --no-truncate
jira issue list --plain --columns key,assignee,status

# Pagination
jira issue list --paginate 20
jira issue list --paginate 10:50

# Ordering
jira issue list --order-by updated --reverse
```

### Creating Issues
```bash
# Interactive creation
jira issue create

# Create with specific parameters
jira issue create -t Bug -s "Bug summary" -y High -l bug -l urgent

# Create with description and assignee
jira issue create -t Story -s "New feature" -b "Detailed description" \
  -a "john.doe@company.com"

# Create with components and custom fields
jira issue create -t Bug -s "Component bug" -C "Backend" -C "API" \
  --custom story-points=3

# Create from template file
jira issue create --template /path/to/template.tmpl

# Create with stdin template
echo "Description from stdin" | jira issue create -s "Summary" -t Task

# Create and open in browser
jira issue create -t Bug -s "Browser bug" --web

# Create sub-task (requires parent)
jira issue create -t Sub-task -s "Sub-task summary" -P ISSUE-123

# Create with versions
jira issue create -t Bug -s "Version bug" --fix-version "v1.2.0" \
  --affects-version "v1.1.0"

# Non-interactive mode
jira issue create -t Bug -s "Auto bug" --no-input
```

### Viewing and Editing Issues
```bash
# View issue details
jira issue view ISSUE-123

# View with comments
jira issue view ISSUE-123 --comments 5

# Plain text output
jira issue view ISSUE-123 --plain

# Raw API response
jira issue view ISSUE-123 --raw

# Edit issue interactively
jira issue edit ISSUE-123

# Update specific fields
jira issue edit ISSUE-123 -s "Updated summary"
jira issue edit ISSUE-123 -y Critical
jira issue edit ISSUE-123 -b "Updated description"
jira issue edit ISSUE-123 -a "new.assignee@company.com"

# Update labels and components
jira issue edit ISSUE-123 -l bug -l urgent
jira issue edit ISSUE-123 -C "Backend" -C "API"

# Update custom fields
jira issue edit ISSUE-123 --custom story-points=5

# Edit and open in browser
jira issue edit ISSUE-123 -s "Updated" --web

# Non-interactive edit
jira issue edit ISSUE-123 -s "Quick update" --no-input
```

### Issue Operations
```bash
# Assign issue (use email or display name)
jira issue assign ISSUE-123 "john.doe@company.com"
jira issue assign ISSUE-123 "John Doe"

# Clone/duplicate issue
jira issue clone ISSUE-123

# Transition issue
jira issue move ISSUE-123 "In Progress"
jira issue move ISSUE-123 "Done" --comment "Work completed"
jira issue move ISSUE-123 "Done" --assignee "jane.doe@company.com" \
  --resolution "Fixed"

# Transition and open in browser
jira issue move ISSUE-123 "In Progress" --web

# Delete issue
jira issue delete ISSUE-123

# Link issues
jira issue link ISSUE-123 "blocks" ISSUE-456
jira issue link ISSUE-123 "relates to" ISSUE-789

# Unlink issues
jira issue unlink ISSUE-123 ISSUE-456

# Watch/unwatch issue
jira issue watch ISSUE-123 "user@company.com"

# Comments
jira issue comment add ISSUE-123 "Progress update"
jira issue comment list ISSUE-123

# Worklog
jira issue worklog add ISSUE-123 --time-spent "2h" --comment "Development work"
jira issue worklog list ISSUE-123
```

## Project Management

### Projects
```bash
# List all accessible projects
jira project list
jira projects list  # Alias
jira project ls     # Alias

# With debug output
jira project list --debug

# Using custom config
jira project list -c /path/to/custom/config.yml
```

### Boards and Sprints
```bash
# List sprints in table view
jira sprint list --table

# List specific sprint issues
jira sprint list SPRINT-ID --table

# Current/previous/next sprint issues
jira sprint list --current
jira sprint list --prev
jira sprint list --next

# Filter by sprint state
jira sprint list --state active,future
jira sprint list --state closed

# Sprint list with custom output
jira sprint list --table --plain --columns name,start,end
jira sprint list SPRINT-ID --plain --columns type,key,summary,status

# Show all sprint fields
jira sprint list --table --plain --no-truncate
jira sprint list SPRINT-ID --plain --no-truncate

# Add issues to sprint
jira sprint add SPRINT-ID ISSUE-123,ISSUE-456

# Close sprint
jira sprint close SPRINT-ID
```

### Epic Management
```bash
# Epic commands (available subcommands)
jira epic list
jira epic create
jira epic add    # Add issues to epic
jira epic remove # Remove issues from epic
```

## Utility Commands

### User Information
```bash
# Get current user info
jira me

# Check with custom config
jira me --config /path/to/config.yml

# Debug user info
jira me --debug
```

### Server Information
```bash
# Get Jira instance info
jira serverinfo
jira systeminfo  # Alias

# With debug output
jira serverinfo --debug
```

### Version Information
```bash
# Show CLI version
jira version
```

## Advanced Operations

### Complex JQL Queries
```bash
# Complex JQL filtering
jira issue list -q "project = PROJ AND status = 'In Progress' AND assignee = currentUser()"

# Search with custom fields
jira issue list -q "cf[10001] = 'Custom Value'"

# Date-based searches
jira issue list -q "created >= -1w"
jira issue list -q "updated >= startOfDay()"

# Show issues from all projects
jira issue list -q "project IS NOT EMPTY"

# Complex status filtering
jira issue list -s ~Open  # Status NOT equal to Open
jira issue list -a x      # Unassigned issues
```

### Output Formatting
```bash
# Plain text output
jira issue list --plain
jira issue list --plain --no-headers
jira issue list --plain --no-truncate

# Custom columns
jira issue list --plain --columns key,assignee,status,priority

# Fixed columns in interactive mode
jira issue list --fixed-columns 2
```

## Configuration Management

```bash
# Multiple configurations
jira --config work-config.yml issue list
jira --config personal-config.yml issue list

# Debug with custom config
jira --debug --config /path/to/config.yml issue list

# Project-specific operations
jira -p PROJECT_KEY issue list
```

## Browser Integration

```bash
# Open issue in browser
jira open ISSUE-123

# Create and open in browser
jira issue create -t Bug -s "Browser bug" --web

# Edit and open in browser
jira issue edit ISSUE-123 --web

# Move and open in browser
jira issue move ISSUE-123 "Done" --web
```

## Shell Integration

```bash
# Generate shell completion
jira completion bash    # Output completion for bash
jira completion zsh     # Output completion for zsh
jira completion fish    # Output completion for fish
jira completion powershell  # Output completion for PowerShell

# Install completion
# Bash
source <(jira completion bash)
jira completion bash > /etc/bash_completion.d/jira

# Zsh
jira completion zsh > "${fpath[1]}/_jira"

# Fish
jira completion fish > ~/.config/fish/completions/_jira.fish

# Generate man pages
jira man --generate --output /path/to/man/directory
```

## Tips and Gotchas

### Security
1. **API Tokens**: Always use API tokens for Jira Cloud, never passwords
2. **Token Storage**: Store tokens securely using environment variables
3. **Permissions**: You'll only see data you have access to in Jira

### Performance
1. **Caching**: CLI caches responses for better performance
2. **Pagination**: Large result sets are paginated (default 100 items)
3. **Rate Limits**: Be aware of Jira API rate limits when scripting

### Common Issues
1. **Authentication Errors**: 
   - Verify API token is current and has correct permissions
   - Check if your Jira instance URL is correct
   
2. **Missing Issues**: 
   - Confirm you have view permissions for the project
   - Check if issues are in the correct status/state

3. **Config File Conflicts**: 
   - Use `--config` flag to specify exact config file
   - Multiple configs can conflict if not properly isolated

### Best Practices
1. **Use Aliases**: Set up shell aliases for frequently used commands
2. **Templates**: Create issue templates for consistent formatting
3. **JQL Mastery**: Learn JQL for powerful issue filtering
4. **Automation**: Combine with shell scripts for workflow automation
5. **Multiple Configs**: Use separate configs for different Jira instances

### Global Flags
```bash
# Available on all commands
-c, --config string    # Config file (default: ~/.config/.jira/.config.yml)
    --debug            # Turn on debug output
-p, --project string   # Jira project to look into
-h, --help             # Help for command
```

### Command Aliases
Most commands have convenient aliases:
- `jira issue` → `jira issues`
- `jira project` → `jira projects`
- `jira sprint` → `jira sprints`
- `jira issue list` → `jira issue ls`
- `jira issue assign` → `jira issue asg`
- `jira issue move` → `jira issue mv`
- `jira issue view` → `jira issue show`

### Scripting Examples
```bash
# Daily standup script
#!/bin/bash
echo "My issues for today:"
jira issue list -a "$(jira me | cut -d' ' -f1)" -s "In Progress"

# List all high priority bugs
#!/bin/bash
jira issue list -t Bug -y High --plain --columns key,summary,assignee

# Create issue from template with error handling
#!/bin/bash
if ! jira issue create -t Bug -s "Automated bug report" -b "$(cat error.log)"; then
    echo "Failed to create issue" >&2
    exit 1
fi

# Check sprint progress
#!/bin/bash
echo "Current sprint progress:"
jira sprint list --current --plain --columns key,summary,status
```