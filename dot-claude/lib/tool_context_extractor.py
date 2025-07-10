#!/usr/bin/env python3
"""
Tool context extraction utilities for Claude Code hooks.
"""

import os
from typing import Dict, Any, Optional, List, Tuple


def extract_tool_use_from_message(message: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Extract tool use information from a message.
    
    Args:
        message: Message dictionary from transcript
        
    Returns:
        Tool use dictionary or None if not found
    """
    msg_content = message.get('message', {}).get('content', [])
    
    if isinstance(msg_content, list):
        for item in msg_content:
            if item.get('type') == 'tool_use':
                return {
                    'name': item.get('name', ''),
                    'input': item.get('input', {}),
                    'id': item.get('id', '')
                }
    
    return None


def is_internal_tool(tool_name: str) -> bool:
    """
    Check if a tool is considered internal/housekeeping vs user-facing work.
    
    Args:
        tool_name: Name of the tool
        
    Returns:
        True if tool is internal, False if it represents meaningful user work
    """
    internal_tools = {
        'TodoWrite',  # Todo management
        'Task',       # Subagent coordination (usually internal)
        # Add other internal tools as identified
    }
    return tool_name in internal_tools


def find_recent_tool_use(messages: List[Dict[str, Any]], 
                        tool_names: Optional[List[str]] = None,
                        max_messages: int = 10,
                        exclude_internal: bool = False) -> Optional[Dict[str, Any]]:
    """
    Find the most recent tool use in messages.
    
    Args:
        messages: List of message dictionaries
        tool_names: Optional list of tool names to filter by
        max_messages: Maximum number of messages to search
        exclude_internal: Whether to exclude internal tools
        
    Returns:
        Most recent tool use or None
    """
    for msg in reversed(messages[-max_messages:]):
        tool_use = extract_tool_use_from_message(msg)
        if tool_use:
            tool_name = tool_use['name']
            
            # Skip internal tools if requested
            if exclude_internal and is_internal_tool(tool_name):
                continue
                
            if not tool_names or tool_name in tool_names:
                return tool_use
    
    return None


def extract_file_context(tool_input: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract file path and filename from tool input.
    
    Args:
        tool_input: Tool input dictionary
        
    Returns:
        Tuple of (file_path, filename) or (None, None)
    """
    file_path = tool_input.get('file_path', '')
    if file_path:
        filename = os.path.basename(file_path)
        return file_path, filename
    
    return None, None


def extract_command_context(tool_input: Dict[str, Any]) -> Dict[str, str]:
    """
    Extract command information from Bash tool input.
    
    Args:
        tool_input: Tool input dictionary
        
    Returns:
        Dictionary with command details
    """
    command = tool_input.get('command', '')
    description = tool_input.get('description', '')
    
    main_cmd = ''
    if command:
        main_cmd = command.split()[0]
    
    return {
        'command': command,
        'description': description,
        'main_cmd': main_cmd
    }


def extract_url_context(tool_input: Dict[str, Any]) -> Optional[str]:
    """
    Extract URL from WebFetch tool input.
    
    Args:
        tool_input: Tool input dictionary
        
    Returns:
        URL string or None
    """
    return tool_input.get('url', '')


def generate_specific_message_for_tool(tool_name: str, tool_input: Dict[str, Any], 
                                     base_message: str) -> str:
    """
    Generate a specific message based on tool type and input.
    
    Args:
        tool_name: Name of the tool
        tool_input: Tool input dictionary
        base_message: Base message from the hook
        
    Returns:
        Specific message string
    """
    if tool_name == "Write":
        file_path, filename = extract_file_context(tool_input)
        if filename:
            return f"Claude wants to create {filename}"
        return "Claude wants to create a file"
    
    elif tool_name == "Edit":
        file_path, filename = extract_file_context(tool_input)
        if filename:
            return f"Claude wants to edit {filename}"
        return "Claude wants to edit a file"
    
    elif tool_name == "Read":
        file_path, filename = extract_file_context(tool_input)
        if filename:
            return f"Claude wants to read {filename}"
        return "Claude wants to read a file"
    
    elif tool_name == "Bash":
        cmd_info = extract_command_context(tool_input)
        if cmd_info['description']:
            # Use the description directly - they're already well-written
            description = cmd_info['description']
            # Make sure it starts with lowercase for "Claude wants to..."
            if description and not description[0].islower():
                description = description[0].lower() + description[1:]
            return f"Claude wants to {description}"
        elif cmd_info['main_cmd']:
            return f"Claude wants to run {cmd_info['main_cmd']}"
        return "Claude wants to run a command"
    
    elif tool_name == "WebFetch":
        url = extract_url_context(tool_input)
        if url:
            return f"Claude wants to fetch {url}"
        return "Claude wants to fetch a URL"
    
    elif tool_name == "Glob":
        pattern = tool_input.get('pattern', '')
        if pattern:
            return f"Claude wants to search for {pattern}"
        return "Claude wants to search files"
    
    elif tool_name == "Grep":
        pattern = tool_input.get('pattern', '')
        if pattern:
            return f"Claude wants to search for {pattern}"
        return "Claude wants to search file contents"
    
    return f"Claude wants to use {tool_name}"


def extract_tool_details_for_context(tool_use: Dict[str, Any]) -> str:
    """
    Extract detailed tool information for context building.
    
    Args:
        tool_use: Tool use dictionary
        
    Returns:
        Formatted tool details string
    """
    tool_name = tool_use.get('name', '')
    tool_input = tool_use.get('input', {})
    
    details = []
    
    if tool_name == "Write":
        file_path, filename = extract_file_context(tool_input)
        content_preview = tool_input.get('content', '')[:100]
        if file_path:
            details.append(f"Tool: Writing file '{file_path}'")
        if content_preview:
            details.append(f"Content preview: {content_preview}...")
    
    elif tool_name == "Edit":
        file_path, filename = extract_file_context(tool_input)
        old_string = tool_input.get('old_string', '')[:50]
        new_string = tool_input.get('new_string', '')[:50]
        if file_path:
            details.append(f"Tool: Editing file '{file_path}'")
        if old_string and new_string:
            details.append(f"Changing: '{old_string}...' to '{new_string}...'")
    
    elif tool_name == "Bash":
        cmd_info = extract_command_context(tool_input)
        details.append(f"Tool: Running bash command")
        if cmd_info['command']:
            details.append(f"Command: {cmd_info['command']}")
        if cmd_info['description']:
            details.append(f"Description: {cmd_info['description']}")
    
    elif tool_name == "Read":
        file_path, filename = extract_file_context(tool_input)
        if file_path:
            details.append(f"Tool: Reading file '{file_path}'")
    
    elif tool_name == "WebFetch":
        url = extract_url_context(tool_input)
        if url:
            details.append(f"Tool: Fetching URL '{url}'")
    
    return "\n".join(details) if details else f"Tool: {tool_name}"