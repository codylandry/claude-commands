#!/usr/bin/env python3
"""
Intelligent text-to-speech notification hook for Claude Code.

Features:
- Context-aware messages extracted from conversation transcripts
- Specific file names and command details in notifications
- OpenAI TTS with macOS fallback
- Smart permission request handling
- Dynamic message generation using OpenAI API
"""

import json
import sys
import os

from utils.message_generator import generate_enhanced_notification_message
from utils.tts_manager import speak_text
from utils.error_handler import log_error


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
        
        # Generate dynamic message
        message = generate_enhanced_notification_message(data)
        
        # Speak the message using improved TTS manager
        speak_text(message)
        
        # Return success response
        response = {"continue": True}
        json.dump(response, sys.stdout)
        
    except Exception as e:
        # Log error and continue
        log_error(f"Notification hook error: {str(e)}", data)
        response = {"continue": True}
        json.dump(response, sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()