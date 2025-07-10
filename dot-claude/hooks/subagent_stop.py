#!/usr/bin/env python3
"""
Subagent stop hook for Claude Code - announces when a subagent has completed.
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


def generate_subagent_message(data):
    """Generate a contextual message for subagent completion using OpenAI."""
    api_key = os.getenv("OPENAI_API_KEY")
    transcript_path = data.get("transcript_path")
    
    if not api_key or not transcript_path:
        return "Subagent has completed its assigned work"
    
    try:
        # Read the transcript (JSONL format - each line is a JSON object)
        messages = []
        with open(transcript_path, 'r') as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
        
        # Get the last few messages for context
        recent_messages = messages[-3:]
        context = "\n".join([f"{msg.get('role', 'unknown')}: {msg.get('content', '')[:200]}" 
                           for msg in recent_messages])
        
        # Generate subagent message using OpenAI
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
                        "content": "You are generating a short notification for a user about a subagent completion. Based on the conversation, create a brief message (under 15 words) that tells the user what type of subagent work was just completed."
                    },
                    {
                        "role": "user",
                        "content": f"Recent conversation:\n{context}\n\nGenerate a brief subagent completion notification:"
                    }
                ],
                "max_tokens": 50,
                "temperature": 0.3
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_message = result["choices"][0]["message"]["content"].strip()
            return generated_message
        else:
            return "Subagent has completed its assigned work"
            
    except Exception:
        return "Subagent has completed its assigned work"


def main():
    try:
        # Read input from stdin
        data = json.load(sys.stdin)
        
        # Generate contextual subagent message
        message = generate_subagent_message(data)
        
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