#!/Users/codylandry/.claude/.venv/bin/python
"""
Standalone text-to-speech tool for Claude Code.

Usage:
    speak.py "Text to speak"
    echo "Text to speak" | speak.py
    speak.py --voice nova "Text with specific voice"
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.tts_manager import speak_text


def main():
    parser = argparse.ArgumentParser(
        description="Speak text using TTS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    speak.py "Hello world"
    speak.py --voice nova "Hello with Nova voice"
    echo "Hello from pipe" | speak.py
    speak.py --macos-only "Use only macOS TTS"
        """
    )
    
    parser.add_argument(
        'text', 
        nargs='?', 
        help='Text to speak (if not provided, reads from stdin)'
    )
    parser.add_argument(
        '--voice', 
        default='alloy',
        choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'],
        help='Voice to use for OpenAI TTS (default: alloy)'
    )
    parser.add_argument(
        '--macos-only', 
        action='store_true',
        help='Use only macOS TTS (skip OpenAI)'
    )
    
    args = parser.parse_args()
    
    # Get text from argument or stdin
    if args.text:
        text = args.text
    else:
        if sys.stdin.isatty():
            parser.error("No text provided. Use argument or pipe text to stdin.")
        text = sys.stdin.read().strip()
    
    if not text:
        parser.error("No text to speak")
    
    # Speak the text
    prefer_openai = not args.macos_only
    success = speak_text(text, voice=args.voice, prefer_openai=prefer_openai)
    
    if not success:
        print("Failed to speak text", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()