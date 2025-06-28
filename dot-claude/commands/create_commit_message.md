---
allowed-tools: [Bash, Read, Grep]
description: Generate contextual commit messages by analyzing git changes and project context
---

# Create Commit Message Command

You are an expert at creating meaningful, contextual commit messages by analyzing changes and understanding the work being done. Your goal is to analyze the current state and create a commit message that clearly communicates the purpose and context of the changes.

**IMPORTANT: You should ONLY generate the commit message text. Do NOT attempt to `git add` or `git commit` anything. Your sole responsibility is to craft the message and copy it to the clipboard using `pbcopy`.**

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
- @WORKING_ON.md
- @TODO.md
- @CLAUDE.md

**Recent Commit Style:**
!git log --oneline -5 --pretty=format:"%s"

**Project Configuration:**
@package.json
@pyproject.toml

### 3. Efficient Context Gathering Strategy
- Extract ticket number from branch name: !git branch --show-current | grep -o '[A-Z]\+-[0-9]\+'
- **Smart Context Gathering**: If working documentation already contains comprehensive ticket details and context, use that information instead of fetching ticket directly
- Only fetch Jira ticket information if working docs are missing or lack sufficient context
- Only look for parent/linked tickets if current context is insufficient to understand the change purpose

### 4. Intent Analysis
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

## Implementation Workflow

### Step 1: Automatic Context Collection
Execute all dynamic content commands to gather comprehensive context:
- Git state analysis (branch, status, diffs)
- Working documentation review
- Recent commit pattern analysis
- Project configuration inspection

### Step 2: Smart Analysis
- Parse ticket number from branch: !git branch --show-current | grep -o '[A-Z]\+-[0-9]\+'
- Determine if additional ticket lookup is needed based on working docs
- Identify change scope: feature/fix/refactor/docs/test
- Assess business impact and technical significance

### Step 3: Message Generation
Generate commit message following this priority:
1. **Ticket Context** (if available): `[TICKET-123] Description`
2. **Change Type** classification (feat/fix/docs/refactor/test)
3. **Business Impact** explanation in body
4. **Technical Details** if complex changes

### Step 4: Delivery
Copy final message to clipboard: `echo "commit message" | pbcopy`

**Quality Checklist:**
- [ ] Ticket number included (if applicable)
- [ ] Clear, imperative description (50-72 chars)
- [ ] Business context explained
- [ ] Technical details noted (if complex)
- [ ] Follows project conventions

## Context Sources Priority (Efficient Approach)

1. **Direct Code Changes** - What actually changed in the diff
2. **Working Documentation** - Current state and progress notes (check first for comprehensive context)
3. **Ticket Information** - Only if working docs lack sufficient detail
4. **Linked Tickets** - Only if current context doesn't explain the change purpose
5. **Recent Commits** - Project patterns and style consistency
6. **User Clarification** - When intent cannot be determined from above sources

**Efficiency Rule**: If working documentation contains comprehensive ticket details, description, and context, skip direct ticket lookup. Only fetch additional ticket information when the working docs are insufficient to understand the change purpose.

## Real-World Examples

### Feature Implementation
```
[PROJ-123] Add user preference toggle for dark mode

Implements the dark mode toggle requested in the user settings mockups.
Toggle state is persisted to localStorage and applied on page load.

- Added DarkModeToggle component with persistent state
- Updated theme provider to support dynamic switching
- Included accessibility features for screen readers
```

### Bug Fix with Context
```
[PROJ-456] Fix memory leak in WebSocket connection handling

Resolves issue where WebSocket connections weren't properly cleaned up
on component unmount, causing memory usage to grow over time in the
chat feature during extended sessions.

- Added proper cleanup in useEffect return function
- Implemented connection pooling to prevent duplicate connections
- Added debug logging for connection lifecycle tracking
```

### Strategic Refactoring
```
[PROJ-789] Extract payment processing into separate service

Refactors payment logic from checkout component into dedicated service
to prepare for upcoming multi-payment-provider feature work in Q2.

- Moved payment validation to PaymentService class
- Created abstract PaymentProvider interface
- Updated checkout flow to use new service layer
- Maintained backward compatibility for existing integrations
```

### Documentation Update
```
[PROJ-101] Update API documentation for new authentication flow

Documents the OAuth 2.0 + PKCE authentication changes implemented
in PROJ-95, including migration guide for existing integrations.

- Added authentication flow diagrams
- Included code samples for common frameworks
- Created migration checklist for existing users
```

## Usage Instructions

This command automatically:

1. **Gathers Context** - Executes all dynamic content commands to collect git state, working documentation, and project context
2. **Analyzes Changes** - Reviews diffs and identifies the purpose and scope of modifications
3. **Generates Message** - Creates a structured commit message following project conventions
4. **Delivers Result** - Copies the final message to clipboard using `pbcopy`

**When to Ask User for Clarification:**
- Intent of changes cannot be determined from diffs and documentation
- Multiple possible interpretations of the change purpose
- Complex architectural decisions need business context
- Working documentation is missing or incomplete

