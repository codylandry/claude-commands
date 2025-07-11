"""
Hook logging utilities for Claude Code hooks.

Provides centralized logging functionality for hook input/output data.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional


class HookLogger:
    """Centralized logging for Claude Code hooks."""
    
    def __init__(self, log_dir: str = "~/.claude/.hook-logs", enabled: bool = True):
        """
        Initialize the hook logger.
        
        Args:
            log_dir: Directory for logging files (supports ~ expansion)
            enabled: Whether logging is enabled
        """
        self.log_dir = Path(log_dir).expanduser()
        self.enabled = enabled
    
    def log_hook_input(self, hook_name: str, data: Dict[str, Any]) -> None:
        """
        Log hook input data to a JSONL file.
        
        Args:
            hook_name: Name of the hook (e.g., 'notification', 'stop')
            data: Input data to log
        """
        if not self.enabled:
            return
            
        try:
            # Create log directory if it doesn't exist
            self.log_dir.mkdir(parents=True, exist_ok=True)
            
            # Write to hook-specific log file
            log_file = self.log_dir / f"{hook_name}.jsonl"
            with open(log_file, "a") as f:
                json.dump(data, f)
                f.write("\n")
        except Exception:
            # Silently ignore logging errors to avoid breaking hooks
            pass
    
    def log_hook_output(self, hook_name: str, response: Dict[str, Any]) -> None:
        """
        Log hook output/response data.
        
        Args:
            hook_name: Name of the hook
            response: Response data to log
        """
        if not self.enabled:
            return
            
        try:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            
            log_file = self.log_dir / f"{hook_name}_responses.jsonl"
            with open(log_file, "a") as f:
                json.dump(response, f)
                f.write("\n")
        except Exception:
            pass
    
    def log_hook_error(self, hook_name: str, error: str, data: Optional[Dict[str, Any]] = None) -> None:
        """
        Log hook errors with context.
        
        Args:
            hook_name: Name of the hook
            error: Error message or description
            data: Optional context data
        """
        if not self.enabled:
            return
            
        try:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            
            error_entry = {
                "hook": hook_name,
                "error": error,
                "context": data
            }
            
            log_file = self.log_dir / "hook_errors.jsonl"
            with open(log_file, "a") as f:
                json.dump(error_entry, f)
                f.write("\n")
        except Exception:
            pass


# Global logger instance with default configuration
default_logger = HookLogger()


def log_hook_input(hook_name: str, data: Dict[str, Any]) -> None:
    """Convenience function for logging hook inputs."""
    default_logger.log_hook_input(hook_name, data)


def log_hook_output(hook_name: str, response: Dict[str, Any]) -> None:
    """Convenience function for logging hook outputs."""
    default_logger.log_hook_output(hook_name, response)


def log_hook_error(hook_name: str, error: str, data: Optional[Dict[str, Any]] = None) -> None:
    """Convenience function for logging hook errors."""
    default_logger.log_hook_error(hook_name, error, data)