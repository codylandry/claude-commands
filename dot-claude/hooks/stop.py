#!/usr/bin/env python3
"""
Stop hook for Claude Code - announces when Claude has finished its work.
"""

import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.message_generator import generate_completion_message
from lib.tts_manager import speak_text
from lib.error_handler import log_error

LOG_DIR = "~/.claude/.hook-logs"  # Directory for logging raw inputs
LOG_INPUTS = True  # Set to False to disable logging raw inputs


def main():
    try:
        # Read input from stdin
        data = json.load(sys.stdin)

        if LOG_INPUTS:
            try:
                # Create log directory if it doesn't exist
                os.makedirs(LOG_DIR, exist_ok=True)
                with open(f"{LOG_DIR}/notification.jsonl", "a") as f:
                    json.dump(data, f)
                    f.write("\n")
            except Exception:
                pass

        # Generate contextual completion message
        message = generate_completion_message(data)
        
        # Speak the message using improved TTS manager
        speak_text(message)
        
        # Return success response
        response = {"continue": True}
        json.dump(response, sys.stdout)
        
    except Exception as e:
        # Log error and continue
        log_error(f"Stop hook error: {str(e)}", data)
        response = {"continue": True}
        json.dump(response, sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()