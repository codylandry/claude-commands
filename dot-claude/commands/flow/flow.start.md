---
description: "Start and coordinate complete development workflows using specialized agents"
allowed-tools: [Task, Read, Write, Edit, Bash, Grep, Glob, TodoWrite, TodoRead]
---

# Flow Start Command

**Start a new development workflow. Follow these steps exactly:**

## Process

1. **Read Feedback**
   - Read @~/.claude/flow/feedback.md
   - Apply supervision preferences

2. **Discover Workspace**
   - Check .ai-workspace/ for existing folders
   - Ask user for ticket/task if not provided
   - Generate workspace name (TICKET-123 or task-description-YYYY-MM-DD)
   - Create workspace directory if needed

3. **Assume Supervisor Role**
   - Read @~/.claude/agents/flow/supervisor.md to assume the supervisor role
   - Begin supervising the workflow for {ticket/task} in workspace {workspace_name}

**That's it.** You now act as the supervisor agent following its process diagram.

## Error Handling
- If workspace setup fails: Ask user for different name
- If supervisor role assumption fails: Report error with details

Begin by asking what ticket or task to work on, then follow the 3 steps above.