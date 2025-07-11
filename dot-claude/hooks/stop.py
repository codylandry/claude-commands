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
from lib.hook_logger import log_hook_input, log_hook_error


def main():
    try:
        # Read input from stdin
        data = json.load(sys.stdin)

        # Log hook input using centralized logger
        log_hook_input("stop", data)

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
        log_hook_error("stop", str(e), data)
        response = {"continue": True}
        json.dump(response, sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()