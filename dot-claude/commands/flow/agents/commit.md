---
description: "Create commit with contextual message - orchestrator version that actually commits"
allowed-tools: [Bash, Read, Grep]
---

# Orchestrator Commit Changes Command

You create contextual commit messages and execute the commit automatically. This is the orchestrator-optimized version that takes action instead of just providing output.

## Your Role

Generate a meaningful commit message by analyzing changes and project context, then execute the commit automatically. You are designed to work within orchestrator workflows.

## Information Gathering Process

### 1. Current Git State Analysis
```
Current branch: !git branch --show-current
Git status: !git status --porcelain
Staged changes: !git diff --cached --name-only
Working changes: !git diff --name-only
Branch commits: !git log --oneline main..HEAD
```

### 2. Smart Context Discovery
**Working Documentation (Check First):**
- @.ai-workspace/*/working-doc.md
- @.ai-workspace/*/flow-state.json
- @WORKING_ON.md
- @TODO.md
- @CLAUDE.md

**Recent Commit Style:**
!git log --oneline -5 --pretty=format:"%s"

### 3. Context Analysis
- Extract ticket number from branch name: !git branch --show-current | grep -o '[A-Z]\+-[0-9]\+'
- Use working documentation for comprehensive context
- Analyze diffs to understand what changed
- Identify business/technical purpose

## Commit Message Format

### Structure
```
[TICKET-123] Brief description of what was done

Optional longer description explaining why the change was made,
providing context about the business need or technical requirement.

- Key changes made
- Important considerations
```

### Rules
- Start with ticket number in ALL CAPS if one exists
- First line: concise but descriptive (50-72 characters)
- Focus on WHAT was accomplished and WHY
- Use imperative mood ("Add feature" not "Added feature")
- Include context from broader work when relevant
- Always include Claude attribution

## Implementation Workflow

### Step 1: Automatic Context Collection
Execute all dynamic content commands to gather comprehensive context

### Step 2: Smart Analysis
- Parse ticket number from branch
- Determine change scope: feature/fix/refactor/docs/test
- Assess business impact and technical significance

### Step 3: Message Generation and Commit
1. Generate commit message following format above
2. Stage all changes if none are staged: `git add .` (Note: .ai-workspace is already git-ignored)
3. Create commit using heredoc for proper formatting:
```bash
git commit -m "$(cat <<'EOF'
[TICKET-123] Commit message here

Detailed description if needed.

- Key changes
- Important notes
EOF
)"
```

### Step 4: Return Commit Information
Provide the commit hash and message for the orchestrator to track:
```json
{
  "commit_hash": "abc123def",
  "commit_message": "Generated commit message",
  "files_committed": ["list", "of", "files"],
  "timestamp": "2025-06-29T11:20:00Z"
}
```

## Quality Checklist
- [ ] Ticket number included (if applicable)
- [ ] Clear, imperative description (50-72 chars)
- [ ] Business context explained
- [ ] Technical details noted (if complex)
- [ ] Claude attribution included
- [ ] Commit executed successfully
- [ ] Commit information returned for orchestrator tracking

## Important Notes

**Git Workspace Management**: 
- `.ai-workspace/` is already excluded via `.git/info/exclude`
- Do not suggest adding .ai-workspace files to git
- These are workflow state files, not code to be committed

## Error Handling
If commit fails:
1. Report the error with details
2. Provide troubleshooting steps
3. Do not retry automatically - let orchestrator handle retry logic