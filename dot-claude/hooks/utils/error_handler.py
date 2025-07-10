#!/usr/bin/env python3
"""
Error handling utilities for Claude Code hooks.
"""

import json
import os
import sys
from typing import Dict, Any, Optional


def log_error(error_msg: str, data: Optional[Dict[str, Any]] = None, 
              error_file: str = "/tmp/hook_error.txt") -> None:
    """
    Log error information to a debug file.
    
    Args:
        error_msg: Error message to log
        data: Optional data dictionary to include in log
        error_file: Path to error log file
    """
    try:
        with open(error_file, "a") as f:
            f.write(f"Hook error: {error_msg}\n")
            
            if data:
                f.write(f"Hook data: {json.dumps(data, indent=2)}\n")
                
                # Log specific context if available
                if "transcript_path" in data:
                    f.write(f"Transcript path: {data['transcript_path']}\n")
                if "message" in data:
                    f.write(f"Base message: {data['message']}\n")
                if "session_id" in data:
                    f.write(f"Session ID: {data['session_id']}\n")
            
            f.write("-" * 50 + "\n")
    except Exception:
        # Silent failure - don't break hook execution
        pass


def safe_hook_execution(hook_function, data: Dict[str, Any], 
                       default_message: str = "Claude needs your attention") -> str:
    """
    Safely execute a hook function with error handling.
    
    Args:
        hook_function: Function to execute
        data: Data to pass to the function
        default_message: Default message if function fails
        
    Returns:
        Message from function or default message
    """
    try:
        return hook_function(data)
    except Exception as e:
        log_error(f"Error in hook function: {str(e)}", data)
        return default_message


def create_success_response() -> Dict[str, Any]:
    """
    Create a success response for hook output.
    
    Returns:
        Success response dictionary
    """
    return {"continue": True}


def handle_hook_main(hook_function, log_file: str, 
                    default_message: str = "Claude needs your attention") -> None:
    """
    Handle the main execution of a hook with proper error handling.
    
    Args:
        hook_function: Function that generates the message
        log_file: File to log hook inputs to
        default_message: Default message if hook fails
    """
    try:
        # Read input from stdin
        data = json.load(sys.stdin)
        
        # Log all raw inputs to debug file
        try:
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            with open(log_file, "a") as f:
                json.dump(data, f)
                f.write("\n")
        except Exception:
            pass
        
        # Generate message using the provided function
        message = safe_hook_execution(hook_function, data, default_message)
        
        # Output the message (hook-specific logic handles TTS)
        # This function just handles the framework
        
        # Return success response
        response = create_success_response()
        json.dump(response, sys.stdout)
        
        return data, message
        
    except Exception as e:
        # Silent failure - don't break the hook chain
        log_error(f"Critical hook error: {str(e)}")
        response = create_success_response()
        json.dump(response, sys.stdout)
        sys.exit(0)


def validate_hook_data(data: Dict[str, Any]) -> bool:
    """
    Validate that hook data contains required fields.
    
    Args:
        data: Hook data dictionary
        
    Returns:
        True if data is valid, False otherwise
    """
    required_fields = ["session_id", "transcript_path", "hook_event_name"]
    
    for field in required_fields:
        if field not in data:
            return False
    
    # Check if transcript path exists
    transcript_path = data.get("transcript_path")
    if transcript_path and not os.path.exists(transcript_path):
        log_error(f"Transcript file not found: {transcript_path}", data)
        return False
    
    return True


def get_api_key_status() -> Dict[str, bool]:
    """
    Get the status of required API keys.
    
    Returns:
        Dictionary with API key availability
    """
    return {
        "openai": bool(os.getenv("OPENAI_API_KEY")),
    }