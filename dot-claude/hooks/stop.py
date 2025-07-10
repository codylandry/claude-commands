#!/usr/bin/env python3
"""
Stop hook for Claude Code - announces when Claude has finished its work.
"""

import json
import sys
import os
import subprocess
import tempfile
import requests


def speak_with_openai(text, voice="alloy"):
    """Use OpenAI TTS API to generate and play speech."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return False
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "tts-1",
                "input": text,
                "voice": voice,
                "response_format": "mp3"
            },
            timeout=30
        )
        
        if response.status_code == 200:
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                tmp_file.write(response.content)
                tmp_file_path = tmp_file.name
            
            # Play the audio file using macOS built-in player
            subprocess.run(["afplay", tmp_file_path], check=True)
            
            # Clean up
            os.unlink(tmp_file_path)
            return True
        else:
            return False
            
    except Exception:
        return False


def speak_with_macos(text):
    """Use macOS built-in TTS as fallback."""
    try:
        subprocess.run(["say", text], check=True)
        return True
    except Exception:
        return False


def generate_completion_message(data):
    """Generate a contextual completion message using OpenAI based on the transcript."""
    api_key = os.getenv("OPENAI_API_KEY")
    transcript_path = data.get("transcript_path")
    
    if not api_key or not transcript_path:
        return "Claude has completed your request"
    
    try:
        # Read the transcript (JSONL format - each line is a JSON object)
        messages = []
        with open(transcript_path, 'r') as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
        
        # Get the last few messages for context, filtering out system messages
        recent_messages = [msg for msg in messages[-8:] if msg.get('role') in ['user', 'assistant']]
        context = "\n".join([f"{msg.get('role')}: {msg.get('content', '')[:300]}" 
                           for msg in recent_messages])
        
        # Generate completion message using OpenAI
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "Create a brief completion notification (under 15 words) about what Claude just finished. Examples: 'Claude finished creating test files', 'Claude completed the file analysis', 'Claude finished running commands'. Focus on the actual work done - file operations, commands run, tasks completed. Never mention conversations, participants, or summaries."
                    },
                    {
                        "role": "user",
                        "content": f"Recent conversation:\n{context}\n\nWhat specific task did Claude just complete?"
                    }
                ],
                "max_tokens": 50,
                "temperature": 0.2
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_message = result["choices"][0]["message"]["content"].strip()
            return generated_message
        else:
            return "Claude has completed your request"
            
    except Exception:
        return "Claude has completed your request"


def main():
    try:
        # Read input from stdin
        data = json.load(sys.stdin)
        
        # Generate contextual completion message
        message = generate_completion_message(data)
        
        # Try OpenAI TTS first, fallback to macOS TTS
        if not speak_with_openai(message):
            speak_with_macos(message)
        
        # Return success response
        response = {"continue": True}
        json.dump(response, sys.stdout)
        
    except Exception:
        # Silent failure - don't break the hook chain
        response = {"continue": True}
        json.dump(response, sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()