---
description: "Collect feedback to improve the flow system"
allowed-tools: [Read, Write, Edit, TodoWrite, TodoRead]
---

# Flow Tune Command

Collect and apply user feedback to improve flow system performance.

## Command Usage

**With feedback:** `/flow.tune The execution agent runs too many tests`
**Interactive mode:** `/flow.tune` (no arguments)

## Process

### Step 1: Get Feedback
**If arguments provided:** Use the feedback directly
**If no arguments:** Ask user what they want to improve about the flow system

### Step 2: Understand the Issue  
Ask clarifying questions:
- Which flow phase does this affect? (research/planning/execution/validation)
- What specific scenarios trigger this issue?
- What would you prefer to happen instead?
- How urgent is this improvement?

### Step 3: Apply Immediately (if applicable)
Check for active flow workspaces in `.ai-workspace/`:
- **If research phase active:** Adjust current research approach
- **If planning phase active:** Update current working document approach
- **If execution phase active:** Modify current step execution strategy
- **If validation phase active:** Adjust current validation approach

### Step 4: Save Feedback
Update `~/.claude/flow/feedback.md` with the feedback for future workflows.

## Feedback File Format

**Location:** `~/.claude/flow/feedback.md`

```yaml
feedback:
  - phase: "execution"
    issue: "Running too many tests slows down development"
    solution: "Run only tests related to changed files for faster feedback"
    context: "Large repositories with >100 tests"
    
  - phase: "planning" 
    issue: "Steps are too granular and overwhelming"
    solution: "Create broader steps that can be completed in 20-30 minutes"
    context: "Feature development workflows"
```

## Interactive Mode

When no arguments provided:
1. **Show current feedback:** Display existing feedback by phase
2. **Ask what to do:** "What would you like to improve about the flow system?"
3. **Offer options:** Create new feedback, update existing, or delete outdated feedback

## Examples

**Test performance:**
"The execution agent runs full test suite every step - can it run only relevant tests?"

**Planning granularity:**  
"The planning steps are too detailed - I want bigger chunks I can work on for 30 minutes"

**Research depth:**
"Research phase takes too long - I usually know the codebase well enough to skip detailed analysis"

## Quality Checks
- [ ] Feedback is specific and actionable
- [ ] Phase is clearly identified  
- [ ] Solution addresses the root issue
- [ ] Context helps determine when to apply

Start by asking what the user wants to improve about the flow system.