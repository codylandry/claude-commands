---
description: "Manage orchestrator workflow state - ALWAYS update after delegations"
allowed-tools: [Read, Write, Edit, LS, Bash]
---

# Orchestrator State Manager

You manage workflow state for the orchestrator command. You MUST update the state file after every single delegation the orchestrator makes.

## CRITICAL: State Update Requirements

**ALWAYS update state when:**
- Orchestrator delegates to any command
- Any delegated command completes (success or failure)
- User provides approval/feedback at checkpoints
- Commits are created during implementation
- Phase transitions occur

## State File Location
`.ai-workspace/{ticket-id}/flow-state.json`

## Complete State Schema
```json
{
  "workflow_id": "TICKET-123",
  "phase": "understanding|planning|execution|integration|complete", 
  "started_at": "2025-06-29T10:30:00Z",
  "updated_at": "2025-06-29T11:00:00Z",
  "current_step": "execute_step_3",
  "completed_phases": ["understanding", "planning"],
  "next_actions": ["get_user_approval", "proceed_to_next_step"],
  "agent_history": [
    {
      "agent": "deep_research", 
      "task": "ticket_analysis",
      "status": "completed",
      "timestamp": "2025-06-29T10:45:00Z",
      "output_summary": "Found authentication requirements, identified existing patterns"
    },
    {
      "agent": "plan_work",
      "task": "create_implementation_plan", 
      "status": "completed",
      "timestamp": "2025-06-29T11:00:00Z",
      "output_summary": "Created 5-step implementation plan in working-doc.md"
    },
    {
      "agent": "execute_step",
      "task": "implement_step_1",
      "status": "in_progress", 
      "timestamp": "2025-06-29T11:15:00Z",
      "output_summary": "Currently implementing authentication middleware"
    }
  ],
  "user_checkpoints": [
    {
      "phase": "understanding",
      "approved": true, 
      "timestamp": "2025-06-29T10:50:00Z",
      "user_feedback": "Research looks good, proceed with planning"
    },
    {
      "phase": "planning",
      "approved": true,
      "timestamp": "2025-06-29T11:05:00Z", 
      "user_feedback": "Implementation plan approved, start execution"
    }
  ],
  "commits_created": [
    {
      "step": "step_1_authentication_middleware",
      "commit_hash": "abc123def",
      "commit_message": "Add authentication middleware foundation",
      "timestamp": "2025-06-29T11:20:00Z"
    }
  ],
  "context_summary": "Working on user authentication enhancement ticket PROJ-123",
  "quality_gates": {
    "requirements_clear": true,
    "codebase_analyzed": true,
    "implementation_planned": true,
    "step_1_complete": true,
    "step_2_complete": false,
    "tests_passing": true,
    "code_reviewed": false,
    "mr_ready": false
  }
}
```

## State Update Commands

**initialize_workflow**: Create new state file for starting workflow
**update_delegation**: Record that orchestrator delegated to an agent
**update_completion**: Record that a delegated agent completed its work
**update_user_checkpoint**: Record user approval/feedback at phase transitions
**update_commit**: Record commits created during implementation
**update_phase**: Advance to next workflow phase
**get_current_state**: Return current state for orchestrator context

## State Update Protocol

**After every delegation:**
1. Add entry to agent_history with "in_progress" status (ONLY for actual work agents)
2. Update current_step to reflect what's happening
3. Update timestamp
4. Set next_actions appropriately

**After delegation completes:**
1. Update agent_history entry status to "completed"/"failed" (ONLY for actual work agents)
2. Add output_summary of what was accomplished
3. Update quality_gates based on completed work
4. Set next_actions for what should happen next
5. Update timestamp

**CRITICAL**: Do NOT add state_manager entries to agent_history - that would be recursive. Only log actual work delegations:
- research_agent, planning_agent, execution_agent, validation_agent, commit_changes
- Do NOT log state_manager operations in agent_history

**User checkpoint updates:**
1. Add entry to user_checkpoints array
2. Record user feedback/decisions
3. Update phase if user approved progression
4. Set next_actions based on user decision

**Commit tracking:**
1. Add entry to commits_created array
2. Include commit hash, message, and step association
3. Update quality_gates to reflect checkpoint completion

This state file is the ONLY way the orchestrator maintains continuity across context windows and sessions.