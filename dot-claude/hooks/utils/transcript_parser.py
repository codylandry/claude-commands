#!/usr/bin/env python3
"""
Transcript parsing utilities for Claude Code hooks.
"""

import json
import os
from typing import List, Dict, Any, Optional


def parse_transcript(transcript_path: str) -> List[Dict[str, Any]]:
    """
    Parse a JSONL transcript file and return all messages.
    
    Args:
        transcript_path: Path to the JSONL transcript file
        
    Returns:
        List of message dictionaries
    """
    messages = []
    
    if not transcript_path or not os.path.exists(transcript_path):
        return messages
    
    try:
        with open(transcript_path, 'r') as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
    except Exception:
        pass
    
    return messages


def get_recent_messages(messages: List[Dict[str, Any]], count: int = 10, 
                       roles: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Get the most recent messages, optionally filtered by roles.
    
    Args:
        messages: List of message dictionaries
        count: Maximum number of messages to return
        roles: List of roles to filter by (e.g., ['user', 'assistant'])
        
    Returns:
        List of recent messages
    """
    if roles:
        filtered_messages = [msg for msg in messages if msg.get('role') in roles]
    else:
        filtered_messages = messages
    
    return filtered_messages[-count:] if filtered_messages else []


def get_recent_user_assistant_messages(messages: List[Dict[str, Any]], 
                                     count: int = 5) -> List[Dict[str, Any]]:
    """
    Get recent user and assistant messages, excluding system messages.
    
    Args:
        messages: List of message dictionaries
        count: Maximum number of messages to return
        
    Returns:
        List of recent user/assistant messages
    """
    return get_recent_messages(messages, count, ['user', 'assistant'])


def format_messages_for_context(messages: List[Dict[str, Any]], 
                               max_content_length: int = 300) -> str:
    """
    Format messages into a readable context string.
    
    Args:
        messages: List of message dictionaries
        max_content_length: Maximum length of content to include per message
        
    Returns:
        Formatted context string
    """
    context_lines = []
    
    for msg in messages:
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        
        if isinstance(content, str):
            content_preview = content[:max_content_length]
        else:
            content_preview = str(content)[:max_content_length]
        
        context_lines.append(f"{role}: {content_preview}")
    
    return "\n".join(context_lines)