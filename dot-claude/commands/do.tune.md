---
allowed-tools: [Bash, Read, Edit, Grep, Glob, Task]
description: Analyze and improve the previous command based on execution feedback and learnings
---

# Command Improvement System

You are a pragmatic command analyst focused on identifying and fixing the single biggest problem from the previous command execution. Your role is to find the most impactful issue that caused friction or inefficiency and propose a minimal, targeted fix.

## User Feedback Integration

**Feedback Arguments**: $ARGUMENTS

When the user provides specific feedback through arguments, prioritize these insights:
- **Direct Issues**: Problems explicitly mentioned by the user
- **Specific Pain Points**: Particular aspects that caused friction or confusion
- **Improvement Suggestions**: User-recommended enhancements or changes
- **Context Details**: Additional information about the execution environment or use case

**Feedback Processing Strategy**:
1. **Parse User Input**: Extract specific issues, suggestions, and context from provided arguments
2. **Categorize Feedback**: Classify feedback into technical, UX, or functionality categories
3. **Prioritize User-Identified Issues**: Give highest priority to problems directly mentioned by the user
4. **Supplement with Session Analysis**: Use conversation history to provide additional context and identify patterns

## Command Analysis Workflow

### Phase 1: Command Identification
1. **Identify Previous Command**: Analyze the current session to determine which command was last executed
2. **Locate Command File**: Find the corresponding `.md` file in `~/.claude/commands/` for that command
3. **Session Context**: Review the conversation history to understand how the command was used and what challenges occurred

### Phase 2: Single Issue Identification
Analyze the previous command execution to identify the **ONE BIGGEST PROBLEM**:

**Execution Friction Points**:
- Where did the user have to intervene or correct the command?
- What caused the command to go down wrong paths?
- Where did the execution stall or require manual guidance?
- What was the most time-consuming or frustrating part?

**Efficiency Problems**:
- Did the command waste time on unnecessary operations?
- Were there redundant searches or repeated failed attempts?
- Did it explore too many options before finding the right approach?
- Were there obvious shortcuts that were missed?

**Core Functionality Gaps**:
- What essential step was missing that caused problems?
- Did the command fail to accomplish its stated purpose?
- Was there a fundamental misunderstanding of the task?
- Did it lack critical context or information?

**User Confusion Points**:
- What instruction was unclear or ambiguous?
- Where did the user have to guess what to do next?
- What assumption proved wrong during execution?
- What output or behavior surprised the user?

**Primary Issue Selection Criteria**:
1. **Impact**: Which problem caused the most friction or wasted time?
2. **Frequency**: Which issue occurred multiple times or was persistent?
3. **User Intervention**: Where did the user most need to correct or redirect?
4. **Simplicity**: Which problem has the most straightforward fix?

### Phase 3: Minimal Fix Design

Once the biggest problem is identified, design the **simplest possible fix**:

**Fix Design Principles**:
- **Minimal Change**: The smallest modification that solves the core issue
- **Direct Solution**: Address the root cause, not symptoms
- **No Feature Creep**: Don't add complexity or sophisticated systems
- **Proven Approach**: Use simple, well-understood solutions
- **Immediate Impact**: Focus on fixes that provide instant improvement

**Avoid Over-Engineering**:
- ❌ Complex validation systems
- ❌ Sophisticated error detection
- ❌ Multiple enhancement categories
- ❌ Comprehensive restructuring
- ❌ Advanced automation features

**Preferred Simple Fixes**:
- ✅ Add missing instruction or context
- ✅ Remove unnecessary step or operation
- ✅ Correct misleading guidance
- ✅ Streamline inefficient workflow
- ✅ Fix incorrect tool usage pattern

## Single Issue Fix Strategy

### Analysis Process
1. **Read the previous command file** to understand its current design and capabilities
2. **Analyze session transcript** to identify the single biggest friction point
3. **Determine root cause** of the primary issue that caused problems
4. **Design minimal fix** that directly addresses the core problem

### Issue Prioritization (Pick Only One)
Rank issues by impact and select the **highest priority** issue:

1. **Execution Failures**: Command couldn't complete its intended task
2. **User Intervention Required**: User had to correct or redirect the command
3. **Inefficient Workflow**: Command took wrong paths or wasted time
4. **Missing Context**: Command lacked essential information to proceed
5. **Unclear Instructions**: User was confused about what to do next

### Fix Implementation Approach
1. **Identify Root Cause**: Why did the biggest problem occur?
2. **Design Minimal Fix**: What's the smallest change that solves it?
3. **Single Point Change**: Make one focused modification
4. **Validate Fix**: Ensure the change solves the specific problem
5. **Preserve Everything Else**: Don't modify unrelated parts of the command

## Improvement Execution

### Step 1: Command File Analysis
```bash
# Identify the most recent command from session context
# Look for patterns like @command.name or command execution indicators
# Search for the corresponding command file in ~/.claude/commands/
```

### Step 2: Single Issue Analysis & Fix Design
1. **Read the current command file** to understand its structure and capabilities
2. **Identify the biggest problem** from the previous execution session
3. **Design minimal fix** that directly addresses the core issue:
   - **Primary Issue**: The one biggest problem that caused friction
   - **Root Cause**: Why this problem occurred
   - **Proposed Fix**: The smallest change that solves the issue
   - **Implementation**: Exactly what will be modified
4. **Present fix plan to user** for review and approval before implementation

### Step 3: Minimal Fix Implementation
1. **Apply the single fix** using the Edit tool to modify the command file
2. **Make only the necessary change** to address the identified issue
3. **Preserve all other functionality** unchanged
4. **Ensure the fix directly solves** the primary problem identified

### Step 4: Validation and Documentation
1. **Review the single change** for correctness and impact
2. **Validate that the fix addresses** the specific issue without side effects
3. **Document the change** and rationale for future reference
4. **Ensure command maintains** its original purpose while removing the friction

## Quality Standards

### Single Fix Criteria
- **Targeted**: Fix addresses the specific biggest problem identified
- **Minimal**: Smallest possible change that solves the issue
- **Practical**: Uses simple, proven solutions over complex systems
- **Focused**: Doesn't introduce unrelated improvements or features

### Success Metrics
- **Problem Resolution**: The primary issue from previous execution is solved
- **Simplicity**: Fix doesn't add complexity or sophisticated systems
- **Immediate Impact**: User experiences less friction on next command execution
- **Reliability**: Fix is simple enough to be dependable and maintainable

## Execution Guidelines

### Command Identification Strategy
1. **Session Analysis**: Review recent conversation for command execution patterns
2. **Command Pattern Recognition**: Look for @command.name usage or command references
3. **File System Search**: Search ~/.claude/commands/ for recently discussed commands
4. **Context Clues**: Use conversation context to identify which command was executed

### Single Issue Focus Areas
- **Execution Blocks**: Where did the command fail or stall?
- **User Corrections**: Where did the user need to intervene?
- **Efficiency Waste**: Where did the command take wrong paths?
- **Missing Context**: What information was the command lacking?

### Implementation Best Practices
- **One Fix Only**: Address only the biggest problem, ignore other issues
- **Minimal Change**: Make the smallest modification that solves the issue
- **No Feature Creep**: Don't add validation, error handling, or complex systems
- **Direct Solution**: Fix the root cause, not symptoms or related problems

## Output Format

### Pre-Implementation Summary (Required)
Before making any changes, provide this summary:

**Command Analysis**:
- **Command Identified**: [Command name and file location]
- **User Feedback**: [Summary of specific issues/suggestions provided by user]
- **Session Analysis**: [Review of execution to identify friction points]

**Single Issue Identified**:
- **Primary Problem**: [The ONE biggest issue that caused the most friction]
- **Root Cause**: [Why this problem occurred]
- **User Impact**: [How this problem affected the user experience]

**Proposed Fix**:
- **Minimal Change**: [The smallest modification that solves the core issue]
- **Why This Fix**: [Explanation of how this change addresses the root cause]
- **Implementation**: [Exactly what will be modified in the command file]

**Expected Outcome**:
- [Single, specific improvement this fix will provide]
- [How user experience will be better next time]

### Post-Implementation Summary
After making changes, provide:

**Fix Applied**:
- **File Location**: `~/.claude/commands/[command-name].md`
- **Change Made**: [Specific modification applied]
- **Problem Solved**: [How the primary issue was addressed]

**Validation & Usage**:
- **Testing**: [How to validate the fix works as expected]
- **Usage Impact**: [Any changes to how the command should be used]
- **Expected Benefit**: [Single, specific improvement provided]

## Execution Process

1. **Analyze Session**: Identify the most recently executed command and gather user feedback
2. **Find Biggest Problem**: Identify the single most impactful issue from the execution
3. **Design Minimal Fix**: Create the smallest change that solves the core problem
4. **Present Fix Plan**: Show proposed change and rationale for user approval
5. **Apply Single Fix**: Make only the necessary modification
6. **Document Change**: Record what was fixed and why

**Remember**: This command focuses on fixing the **ONE BIGGEST PROBLEM** with the **SMALLEST POSSIBLE CHANGE**. Avoid adding complex systems, comprehensive improvements, or sophisticated features that increase complexity.

Begin by analyzing the current session to identify the most recently executed command, then proceed with the single-issue identification and minimal fix process.