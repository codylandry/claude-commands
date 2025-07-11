# GitLab CLI (glab) Commands

This document provides a quick reference for common operations using the GitLab CLI (`glab`) tool.

## Merge Requests

### Checking MR Status
```bash
# View a specific merge request by ID
glab mr view 123

# View a specific merge request by branch name
glab mr view branch-name

# View merge request with comments
glab mr view 123 --comments

# Open merge request in browser
glab mr view 123 --web

# List all open merge requests
glab mr list

# List merged merge requests
glab mr list --state merged

# List closed merge requests
glab mr list --state closed
```

### Creating and Managing MRs
```bash
# Create a new merge request (will open editor for details)
glab mr create

# Create MR with title and description
glab mr create --title "Fix bug in login flow" --description "This fixes issue #42"

# Create MR with auto-fill from current branch
glab mr create --fill

# Create MR for a specific issue
glab mr for 42

# Update a merge request
glab mr update 123 --title "Updated title" --description "New description"

# Add labels to a merge request
glab mr update 123 --label bug,urgent

# Checkout branch for a merge request
glab mr checkout 123

# Merge/accept a merge request
glab mr merge 123

# Close a merge request
glab mr close 123

# Reopen a merge request
glab mr reopen 123
```

### MR Approvals and Reviews
```bash
# Approve a merge request
glab mr approve 123

# Revoke approval for a merge request
glab mr revoke 123

# List eligible approvers for a merge request
glab mr approvers 123

# Add a comment/note to a merge request
glab mr note 123 -m "This looks good to me"
```

## CI/CD Pipelines

### Checking Pipeline Status
```bash
# View current pipeline status on your branch
glab ci status

# List all pipelines
glab ci list

# List failed pipelines
glab ci list --status=failed

# List pipelines for a specific branch
glab ci list --ref branch-name

# Get JSON details of a pipeline
glab ci get

# View pipeline details interactively (with options to run, trace, cancel)
glab ci view
```

### Managing Pipelines
```bash
# Run a new pipeline on current branch
glab ci run

# Run a pipeline on a specific branch
glab ci run --ref branch-name

# Run a pipeline with variables
glab ci run --variable KEY=VALUE --variable ANOTHER=VALUE

# Run a pipeline with variables from a file
glab ci run --variables-file path/to/vars.json

# Cancel a running pipeline
glab ci cancel

# Retry a failed pipeline
glab ci retry
```

### Jobs and Artifacts
```bash
# Trace/follow a job log in real time
glab ci trace JOB_ID

# Download artifacts from the latest pipeline
glab ci artifact
```


## Tips

1. Most commands accept a `-R` or `--repo` flag to specify a repository: 
   `glab mr list -R owner/repo-name`

2. Use `--help` with any command to see all available options:
   `glab mr create --help`

3. Output can be formatted as JSON for scripting:
   `glab mr view 123 --output json`

4. For viewing in a browser, add the `--web` flag to most commands:
   `glab issue view 42 --web` 
