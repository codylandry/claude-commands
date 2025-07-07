---
description: "Continue existing flow workflows from where they left off"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, TodoWrite, TodoRead]
---

# Continue Flow Command

Resume interrupted flow workflows by analyzing current state and continuing directly.

## Command Process

### Step 1: Find Workspace
**If workspace provided by user:** Use that workspace path
**If no workspace provided:** 
1. Check `.ai-workspace/` for available workflows
2. Show user available options with current status  
3. Ask user to select which workflow to continue

### Step 2: Load State and Context
**Read existing documents:**
1. `.ai-workspace/{workspace}/flow-state.json` - Get current phase and progress
2. `.ai-workspace/{workspace}/working-doc.md` - Load implementation plan
3. `@~/.claude/flow/feedback.md` - Apply user feedback preferences

**Determine current status:**
- What phase: understanding/planning/execution/integration
- Last completed step
- Next step to execute
- Any blockers or errors

### Step 3: Continue Workflow Directly

**Based on current phase, continue the work:**

**Understanding Phase:** 
- Read research progress, continue research analysis
- Update research findings with new discoveries
- Move to planning when research complete

**Planning Phase:**
- Read planning progress, continue step breakdown
- Update working document with remaining steps
- Move to execution when plan complete

**Execution Phase:**
- Read last completed step from working document
- Execute next step in the implementation plan
- Update progress and run validations
- Create commits at checkpoint steps

**Integration Phase:**
- Complete final validations and testing
- Prepare for merge/deployment
- Create final commit

### Step 4: Update State
Update `.ai-workspace/{workspace}/flow-state.json`:
- Add continuation timestamp
- Update current phase and progress
- Log continuation action in agent history

## Flow State Structure
```json
{
  "current_phase": "execution",
  "last_step_completed": 3,
  "next_step": 4,
  "total_steps": 8,
  "agent_history": [
    {"agent": "research", "completed_at": "...", "status": "completed"},
    {"agent": "planning", "completed_at": "...", "status": "completed"},
    {"agent": "execution", "completed_at": "...", "status": "in_progress"}
  ],
  "blockers": [],
  "user_checkpoints": {
    "planning_approved": true,
    "execution_in_progress": true
  }
}
```

## Error Recovery

**If workspace doesn't exist:** List available workspaces or suggest creating new flow
**If state file corrupted:** Ask user how to proceed (restart vs manual fix)
**If execution blocked:** Report specific blockers and ask for guidance

## Continuation Examples

**Mid-execution continuation:**
"Continuing execution of step 4/8: Implement user authentication. Last completed: Database schema setup."

**Between-phase continuation:**  
"Planning phase complete. Ready to start execution phase with 6 implementation steps."

## Quality Checks
- [ ] Workspace exists and is readable
- [ ] Flow state contains valid phase information  
- [ ] Working document has clear next steps
- [ ] No unresolved blockers

Start by discovering available workflows or asking which workspace to continue.