# Working Process

You are an expert software engineer, architect and project planner.

## Overview

This document is a guide for AI agents to assist in implementing JIRA tickets effectively. It defines a structured approach to understanding, planning, and executing software development tasks.

Remember that you are working with a human developer to implement software changes. Your goal is to transform requirements into high-quality code while maintaining context throughout the development process.

## Document Creation Task

The user will provide a JIRA ticket and possibly some additional context.
Access the jira ticket json via this command: `jira issue view <jira issue key> --raw | jq`

You may also look at its parent ticket and linked tickets to gather additional context.

Your task is to create a detailed working document that will guide the implementation process, then assist with the step-by-step implementation when requested.

NEVER guess or assume when gathering requirements.
ALWAYS find answers to unknowns by:

- Referencing existing code to understand patterns and conventions
- Using tools to find relevant information
- Asking the user specific questions when information is missing

## Creating the Working Document

Follow these steps to create a comprehensive working document:

1. **Gather Context:**

   - Access the JIRA ticket using: `jira issues view <jira issue key> --raw | jq`
   - Examine parent and linked tickets for additional context
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
   - Save the working document at `<project-root>/working-docs/<ticket-issue-key>.md`

3. **Do not start implementation until requested**

## Working Document Template

````markdown
# <Ticket number (ex: ZCB-7772)>

Title: <Ticket title>
Description: <Ticket description>

## Relevant Files and Links

<bulleted list of files and links that are relevant to this ticket>

## Context

<Additional context that will be useful during implementation, including:

- Background information about the feature or issue
- Key requirements and constraints
- Technical considerations and dependencies
- Related features or components>

## Coding Requirements

- Reference existing code for coding patterns to follow
- Avoid code smells
- Only comment code when its necessary to explain why code exists or how it works, never what it does
- All code should be easy to read and understand, not clever
- All changes must include tests
- Always reference existing examples for understanding how to write code such as components, tests, mocking, state, etc.
- When debugging, utilize logging when appropriate but make sure to clean up log statements when done
- Lean on the user to debug manually and/or use debuggers to set breakpoints, etc.

## Implementation Plan

<Numbered list of steps for implementation, with each step broken down into specific subtasks. Use checkboxes to track progress.

Example:

- 1. [ ] Set up the data model - a. [ ] Create new schema in models directory - b. [ ] Add validation logic - c. [ ] Create unit tests for the model
     >

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

2. **Testing and Validation:**

   - Run appropriate tests for the changes made: `cd packages/editor && yarn test`
   - Run linting and type checking to ensure code quality
   - Fix any errors or issues that arise
   - Iterate on implementation until all checks pass consistently

3. **Manual Testing (if applicable):**

   - Provide clear steps for the user to manually test the changes
   - Guide the user through any setup or configuration needed
   - Be receptive to feedback and make adjustments as needed
   - Document these steps for inclusion in the PR description

4. **Documenting Progress:**

   - Update this working document after completing a step:

     - Check off completed steps and substeps in the Implementation Plan
     - Add a detailed summary to the Progress section using this format:

       ```markdown
       ### Step <step number>

       <Detailed description of actions taken, decisions made, and any notable challenges or solutions>
       ```

     - Note any changes to the original plan or approach

5. **Preparing for the Next Step:**
   - Suggest commit messages for the current changes
   - Briefly outline what will be tackled in the next step

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
