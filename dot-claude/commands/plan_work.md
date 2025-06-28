---
description: Creates comprehensive working documents for JIRA ticket implementation with structured planning
---

# Working Process

You are an expert software engineer, architect and project planner.

## Overview

This document is a guide for AI agents to assist in implementing JIRA tickets effectively. It defines a structured approach to understanding, planning, and executing software development tasks.

Remember that you are working with a human developer to implement software changes. Your goal is to transform requirements into high-quality code while maintaining context throughout the development process.

## Document Creation Task

The user can provide task context in several ways:
1. **JIRA ticket key** (e.g., "ABC-123") - for tickets in your issue tracking system
2. **Task description** as $ARGUMENTS - for ad-hoc development tasks without formal tickets
3. **No arguments** - attempt to infer ticket number from current git branch name

Examples:
- `/plan_work ABC-123` - Uses JIRA ticket ABC-123
- `/plan_work Add user authentication with OAuth2 support` - Creates plan for described task
- `/plan_work` - Extracts ticket from branch name like "feature/ABC-123-user-auth"

## Requirements Gathering

**Step 1: Determine Task Source**
- If $ARGUMENTS contains a ticket pattern (e.g., "ABC-123"), use it as the JIRA ticket key
- If $ARGUMENTS contains descriptive text, treat as an ad-hoc task description
- If no arguments provided, extract ticket from current branch using: `git branch --show-current`

**Step 2: Gather Requirements**
- **For JIRA tickets:** Access ticket data via `jira issue view <jira issue key> --raw | jq`
- **For ad-hoc tasks:** Use the provided description as primary requirements
- **For branch-inferred tickets:** Extract ticket key from branch name and access JIRA

You may also look at parent and linked tickets for additional context when working with JIRA.

Your task is to create a detailed working document that will guide the implementation process, then assist with the step-by-step implementation when requested.

## Validation & Error Handling
NEVER guess or assume when gathering requirements.
ALWAYS find answers to unknowns by:

- Referencing existing code to understand patterns and conventions
- Using tools to find relevant information
- Asking the user specific questions when information is missing

## Creating the Working Document

Follow these steps to create a comprehensive working document:

1. **Gather Context:**

   - **For JIRA tickets:** Access the ticket using `jira issue view <jira issue key> --raw | jq`
   - **For ad-hoc tasks:** Use the provided description and explore related code
   - **For all tasks:** Examine parent and linked tickets when applicable for additional context
   - Identify and explore relevant files and code patterns in the repository
   - Take note of existing approaches, coding styles, and architectural patterns

2. **Create an Implementation Plan:**

   - Use the template below
   - Fill in all fields indicated by `< ... >`
   - Break down complex tasks into smaller, manageable steps
   - For implementation steps, use numbered lists with checkboxes:
     ```markdown
     - 1. [ ] Extract component x from component y
       - a. [ ] Create new x component
       - b. [ ] Update y component to use new x component
       - c. [ ] Verify test/lint/formatting checks pass
     ```
   - Create directory: `<project-root>/.ai-workspace/<ticket-issue-key>/`
   - Save the working document at `<project-root>/.ai-workspace/<ticket-issue-key>/working-doc.md`

3. **Quality Assurance Setup:**
   - Identify testing strategy and frameworks used in the project
   - Determine linting, formatting, and type checking requirements
   - Plan for security and performance considerations
   - Document any project-specific validation requirements

4. **Do not start implementation until requested**

## Working Document Template

````markdown
# <Ticket number (ex: ZCB-7772) or Task Name (ex: User Authentication)>

Title: <Ticket title or task description>
Description: <Ticket description or detailed task requirements>

## Relevant Files and Links

<bulleted list of files and links that are relevant to this ticket>

## Context

<Additional context that will be useful during implementation, including:

- Background information about the feature or issue
- Key requirements and constraints
- Technical considerations and dependencies
- Related features or components>

## Coding Requirements

### Code Quality Standards
- Reference existing code for coding patterns to follow
- Avoid code smells and maintain clean architecture
- Only comment code when necessary to explain why code exists or how it works, never what it does
- All code should be easy to read and understand, not clever
- Follow existing project conventions for naming, structure, and patterns
- Use strict typing and compile-time checks when available in the language

### Testing & Validation
- All changes must include comprehensive tests
- Generate tests that document business behavior, not implementation details
- Include integration tests for critical user workflows
- Always reference existing examples for understanding how to write code, tests, and patterns
- Ensure high test coverage for new functionality
- Follow project-specific testing frameworks and conventions

### Security & Performance
- Implement proper error handling for all external calls and user inputs
- Never introduce code that exposes or logs secrets and keys
- Follow security best practices throughout implementation
- Consider performance implications of all changes

### Development Workflow
- When debugging, utilize logging when appropriate but clean up log statements when done
- Lean on the user to debug manually and/or use debuggers to set breakpoints
- Run linting and type checking commands after making changes
- Verify all tests pass before considering a step complete

## Implementation Plan

<Numbered list of steps for implementation, with each step broken down into specific subtasks. Use checkboxes to track progress.

Example:

- 1. [ ] Set up the data model
  - a. [ ] Create new schema in models directory
  - b. [ ] Add validation logic
  - c. [ ] Create unit tests for the model
  - d. [ ] Verify test/lint/formatting checks pass

## Validation Checklist

### Pre-Implementation
- [ ] Requirements clearly understood and documented
- [ ] Existing code patterns identified and documented
- [ ] Testing strategy defined
- [ ] Security considerations identified

### During Implementation
- [ ] Code follows project conventions
- [ ] Comprehensive tests written
- [ ] Security best practices followed
- [ ] Performance implications considered

### Post-Implementation
- [ ] All tests pass
- [ ] Linting and formatting checks pass
- [ ] Type checking (if applicable) passes
- [ ] Manual testing completed
- [ ] Documentation updated
- [ ] PR/MR description prepared

## Implementation Process

As an AI assistant, follow this process when implementing steps for this ticket:

### Before Starting a Step

- Carefully review this working document to refresh your understanding of the ticket
- Examine the Progress section to understand what has been completed already
- Review relevant code files that will be modified or created

### When Implementing a Step

1. **Implementation Guidelines:**
   - Break down complex tasks into smaller, digestible changes
   - Reference existing code patterns to maintain consistency
   - Provide clear, well-structured code that follows project conventions
   - Explain your approach if it involves important design decisions
   - Use the Explore-Plan-Code workflow: understand first, plan second, implement third

2. **Testing and Validation:**
   - Run appropriate tests for the changes made using project-specific test commands
   - Run linting, formatting, and type/compile checking to ensure code quality
   - Fix any errors or issues that arise
   - Iterate on implementation until all checks pass consistently
   - Generate comprehensive tests for all new functionality

3. **Security and Quality Checks:**
   - Verify no sensitive information is exposed or logged
   - Ensure proper error handling is implemented
   - Validate input sanitization and validation
   - Check for potential performance issues

4. **Manual Testing (if applicable):**
   - Provide clear steps for the user to manually test the changes
   - Guide the user through any setup or configuration needed
   - Be receptive to feedback and make adjustments as needed
   - Document these steps for inclusion in the PR description

5. **Documenting Progress:**
   - Update this working document after completing a step:
     - Check off completed steps and substeps in the Implementation Plan
     - Add a detailed summary to the Progress section using this format:
       ```markdown
       ### Step <step number>
       <Detailed description of actions taken, decisions made, and any notable challenges or solutions>
       ```
     - Note any changes to the original plan or approach
     - Document any technical decisions or patterns discovered

6. **Preparing for the Next Step:**
   - Suggest commit messages following conventional commits format
   - Briefly outline what will be tackled in the next step
   - Identify any potential blockers or dependencies for upcoming work

### When All Steps Are Complete

1. **Final Validation:**

   - Ensure all tests are passing
   - Verify all implementation steps are checked off
   - Confirm with the user that manual testing has been completed successfully

2. **Generate PR Description:**
   - Check if there is a default MR template at `.gitlab/merge_request_templates/Default.md`
   - If present, use that template for the PR description
   - If not, create a concise description summarizing the changes and their purpose, as well as manual testing steps for a reviewer

## Progress

<Step completion summaries added as implementation progresses>

## PR Description

<Use the default gitlab MR template if it exists (`.gitlab/merge_request_templates/Default.md`), otherwise create a summary of the changes, their purpose, and important implementation details. Always include clear manual testing steps for reviewers.>
````
