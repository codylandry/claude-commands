#!/usr/bin/env python3
"""
Simplified message generation utilities for Claude Code hooks.
"""

from typing import Dict, Any


# Tool descriptions for generating notifications
TOOL_DESCRIPTIONS = {
    "Bash": "run a command",
    "Write": "create a file", 
    "Edit": "edit a file",
    "MultiEdit": "edit a file",
    "Read": "read a file",
    "WebFetch": "fetch a URL",
    "Glob": "search for files",
    "Grep": "search file contents",
    "Task": "perform a task",
    "LS": "list directory contents",
    "NotebookRead": "read a notebook",
    "NotebookEdit": "edit a notebook",
    "TodoWrite": "update tasks",
    "WebSearch": "search the web"
}


def generate_notification_message(data: Dict[str, Any]) -> str:
    """
    Generate a simple notification message.
    
    Args:
        data: Hook data containing message, etc.
        
    Returns:
        Generated notification message
    """
    base_message = data.get("message", "")
    
    # Handle permission requests
    if "permission" in base_message.lower():
        return _generate_permission_message(base_message)
    
    # Generic notifications for everything else
    if "error" in base_message.lower() or "failed" in base_message.lower():
        return "Claude encountered an error"
    elif "waiting" in base_message.lower():
        return "Claude is waiting for input"
    elif "approval" in base_message.lower() or "confirm" in base_message.lower():
        return "Claude needs your approval"
    else:
        return "Claude needs your attention"


def _generate_permission_message(base_message: str) -> str:
    """Generate a permission message using static tool descriptions."""
    # Extract tool name from the permission message
    # Messages look like: "Claude needs your permission to use Write"
    if "permission to use" in base_message:
        requested_tool = base_message.split("permission to use")[-1].strip()
        
        # Use static tool descriptions
        if requested_tool in TOOL_DESCRIPTIONS:
            description = TOOL_DESCRIPTIONS[requested_tool]
            return f"Claude wants to {description}"
    
    return "Claude needs permission"


def generate_completion_message(data: Dict[str, Any]) -> str:
    """
    Generate a completion message for stop hooks.
    
    Returns:
        Completion message
    """
    return "Claude finished its task"


# Keep these functions for backward compatibility
def generate_enhanced_notification_message(data: Dict[str, Any]) -> str:
    """Simplified version of enhanced notification."""
    return generate_notification_message(data)


def generate_bash_notification_message(data: Dict[str, Any]) -> str:
    """Simplified version of bash notification."""
    return generate_notification_message(data)


def generate_fallback_message(base_message: str, tool_name: str = "") -> str:
    """Simple fallback message."""
    if "permission" in base_message.lower():
        return "Claude needs permission"
    elif "error" in base_message.lower():
        return "Claude encountered an error"
    else:
        return "Claude needs your attention"