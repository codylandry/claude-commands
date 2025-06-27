# Create Commit Message Command

You are an expert at creating meaningful, contextual commit messages by analyzing changes and understanding the work being done. Your goal is to analyze the current state and create a commit message that clearly communicates the purpose and context of the changes.

**IMPORTANT: You should ONLY generate the commit message text. Do NOT attempt to `git add` or `git commit` anything. Your sole responsibility is to craft the message and copy it to the clipboard using `pbcopy`.**

## Information Gathering Process

1. **Analyze Current State**
   - Get current branch name (may contain ticket number)
   - Check git status for staged/unstaged changes
   - Generate branch diff (`git diff main...HEAD` or similar)
   - Generate working tree diff (`git diff` and `git diff --staged`)

2. **Gather Context (Efficiently)**
   - Look for current working documentation files (WORKING_ON.md, TODO.md, etc.)
   - Extract ticket number from branch name if present
   - **Smart Context Gathering**: If working documentation already contains comprehensive ticket details and context, use that information instead of fetching ticket directly
   - Only fetch Jira ticket information if working docs are missing or lack sufficient context
   - Only look for parent/linked tickets if current context is insufficient to understand the change purpose
   - Check recent commit messages for patterns and style

3. **Understand Intent**
   - Analyze the diffs to understand what changed
   - Consider the context from documentation and tickets
   - Identify the business/technical purpose behind the changes
   - If intent is unclear, ASK the user to clarify the purpose

## Commit Message Format

### Structure
```
[TICKET-123] Brief description of what was done

Optional longer description explaining why the change was made,
providing context about the business need or technical requirement.
Include relevant details that future developers would find helpful.

- Key changes made
- Important considerations
- Related tickets or dependencies
```

### Rules
- Start with ticket number in ALL CAPS if one exists (e.g., `[PROJ-1234]`)
- First line should be concise but descriptive (50-72 characters)
- Focus on WHAT was accomplished and WHY, not just what files changed
- Use imperative mood ("Add feature" not "Added feature")
- Include context from the broader work when relevant
- Reference related tickets if they provide important context
- **IMPORTANT**: Do NOT mention the current 'step' being worked on or reference internal working process documents (like plan_work.md, execute_step.md) as these are internal workflow tools not shared with others

## Implementation Process

1. **Gather Information (Efficiently)**
   - Run git commands to understand current state
   - Search for working documentation first
   - Extract ticket information only if working docs are insufficient
   - Read recent commits for style guidance

2. **Analyze Changes**
   - Review all diffs comprehensively
   - Identify the core purpose of the changes
   - Consider how changes fit into larger work effort
   - Note any breaking changes or important technical details

3. **Craft Message**
   - Write clear, contextual commit message
   - Include ticket number if available
   - Provide business/technical context
   - Explain the "why" behind the changes
   - Copy the final message to clipboard using `echo "message" | pbcopy`

4. **Validate Understanding**
   - If the intent of changes is unclear from context, ask user
   - Confirm the commit message accurately reflects the work
   - Ensure message follows project conventions

## Context Sources Priority (Efficient Approach)

1. **Direct Code Changes** - What actually changed in the diff
2. **Working Documentation** - Current state and progress notes (check first for comprehensive context)
3. **Ticket Information** - Only if working docs lack sufficient detail
4. **Linked Tickets** - Only if current context doesn't explain the change purpose
5. **Recent Commits** - Project patterns and style consistency
6. **User Clarification** - When intent cannot be determined from above sources

**Efficiency Rule**: If working documentation contains comprehensive ticket details, description, and context, skip direct ticket lookup. Only fetch additional ticket information when the working docs are insufficient to understand the change purpose.

## Examples

### Simple Feature Addition
```
[PROJ-123] Add user preference toggle for dark mode

Implements the dark mode toggle requested in the user settings mockups.
Toggle state is persisted to localStorage and applied on page load.
```

### Bug Fix
```
[PROJ-456] Fix memory leak in WebSocket connection handling

Resolves issue where WebSocket connections weren't properly cleaned up
on component unmount, causing memory usage to grow over time.
```

### Refactoring
```
[PROJ-789] Extract payment processing into separate service

Refactors payment logic from checkout component into dedicated service
to prepare for upcoming multi-payment-provider feature work.
```

## Getting Started

To create a commit message:

1. Analyze the current git state and gather all available context
2. Research any tickets or documentation referenced
3. Understand the intent and purpose of the changes
4. Craft a meaningful commit message that future developers will understand
5. If intent is unclear, ask the user for clarification before proceeding