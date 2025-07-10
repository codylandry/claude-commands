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


def generate_dynamic_message(data):
    """Generate a dynamic message using OpenAI based on the transcript."""
    api_key = os.getenv("OPENAI_API_KEY")
    transcript_path = data.get("transcript_path")
    base_message = data.get("message", "")
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})
    
    # For permission requests, try to extract specific details from transcript
    if "permission" in base_message.lower():
        try:
            # Try to get specific details from recent transcript
            if transcript_path and os.path.exists(transcript_path):
                messages = []
                with open(transcript_path, 'r') as f:
                    for line in f:
                        if line.strip():
                            messages.append(json.loads(line))
                
                # Look for recent tool_use calls in the last few messages
                for msg in messages[-3:]:
                    content = msg.get('message', {}).get('content', [])
                    if isinstance(content, list):
                        for item in content:
                            if item.get('type') == 'tool_use':
                                tool_name = item.get('name', '')
                                tool_input = item.get('input', {})
                                
                                if "Write" in base_message and tool_name == "Write":
                                    file_path = tool_input.get('file_path', '')
                                    if file_path:
                                        filename = os.path.basename(file_path)
                                        return f"Claude wants to create {filename}"
                                elif "Edit" in base_message and tool_name == "Edit":
                                    file_path = tool_input.get('file_path', '')
                                    if file_path:
                                        filename = os.path.basename(file_path)
                                        return f"Claude wants to edit {filename}"
                                elif "Bash" in base_message and tool_name == "Bash":
                                    command = tool_input.get('command', '')
                                    description = tool_input.get('description', '')
                                    if description:
                                        return f"Claude wants to {description.lower()}"
                                    elif command:
                                        main_cmd = command.split()[0] if command else ""
                                        return f"Claude wants to run {main_cmd}"
                                elif "Read" in base_message and tool_name == "Read":
                                    file_path = tool_input.get('file_path', '')
                                    if file_path:
                                        filename = os.path.basename(file_path)
                                        return f"Claude wants to read {filename}"
        except:
            pass
        
        # Fallback if we couldn't extract specifics
        if "Write" in base_message:
            return "Claude wants to create a file"
        elif "Edit" in base_message or "Update" in base_message:
            return "Claude wants to edit a file"
        elif "Bash" in base_message:
            return "Claude wants to run a command"
        elif "Read" in base_message:
            return "Claude wants to read a file"
        else:
            return "Claude needs permission for an action"
    
    # For non-permission requests, try OpenAI if available
    if not api_key or not transcript_path:
        # Fallback logic for other cases
        if "approval" in base_message.lower() or "confirm" in base_message.lower():
            return "Claude needs your approval to continue"
        elif "error" in base_message.lower() or "failed" in base_message.lower():
            return "Claude encountered an error and needs assistance"
        elif base_message:
            return f"Claude says: {base_message}"
        else:
            return "Claude needs your attention"
    
    try:
        # Read the transcript (JSONL format - each line is a JSON object)
        messages = []
        with open(transcript_path, 'r') as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
        
        # Get the last few messages for context, filtering out system messages
        recent_messages = [msg for msg in messages[-5:] if msg.get('role') in ['user', 'assistant']]
        context = "\n".join([f"{msg.get('role', 'unknown')}: {msg.get('content', '')[:300]}" 
                           for msg in recent_messages])
        
        # Build comprehensive context with detailed tool information
        enhanced_context = f"Recent conversation context:\n{context}\n\nCurrent notification: {base_message}"
        
        # Extract detailed tool information from recent messages
        tool_details = ""
        if "permission" in base_message.lower():
            # Look for the most recent tool_use in the transcript
            for msg in reversed(messages[-10:]):  # Check more messages
                msg_content = msg.get('message', {}).get('content', [])
                if isinstance(msg_content, list):
                    for item in msg_content:
                        if item.get('type') == 'tool_use':
                            tool_name = item.get('name', '')
                            tool_input = item.get('input', {})
                            
                            if tool_name == "Write":
                                file_path = tool_input.get('file_path', '')
                                content_preview = tool_input.get('content', '')[:100]
                                tool_details = f"\nTool: Writing file '{file_path}'\nContent preview: {content_preview}..."
                                break
                            elif tool_name == "Edit":
                                file_path = tool_input.get('file_path', '')
                                old_string = tool_input.get('old_string', '')[:50]
                                new_string = tool_input.get('new_string', '')[:50]
                                tool_details = f"\nTool: Editing file '{file_path}'\nChanging: '{old_string}...' to '{new_string}...'"
                                break
                            elif tool_name == "Bash":
                                command = tool_input.get('command', '')
                                description = tool_input.get('description', '')
                                tool_details = f"\nTool: Running bash command\nCommand: {command}\nDescription: {description}"
                                break
                            elif tool_name == "Read":
                                file_path = tool_input.get('file_path', '')
                                tool_details = f"\nTool: Reading file '{file_path}'"
                                break
                if tool_details:
                    break
        
        enhanced_context += tool_details
        
        
        if tool_name:
            enhanced_context += f"\nTool: {tool_name}"
        if tool_input:
            if tool_name == "Bash":
                command = tool_input.get("command", "")
                description = tool_input.get("description", "")
                if command:
                    enhanced_context += f"\nCommand: {command}"
                if description:
                    enhanced_context += f"\nPurpose: {description}"
            elif "file_path" in tool_input:
                enhanced_context += f"\nFile: {tool_input.get('file_path', '')}"
        
        # Generate dynamic message using OpenAI
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
                        "content": "You create VERY brief, specific audio notifications for a developer. Your job is to extract the key action from the context and announce it clearly.\n\nFor PERMISSION requests:\n- Say exactly what Claude wants to do\n- Include specific filenames when available\n- Include command names for bash\n- Examples: 'Claude wants to create package.json', 'Claude wants to edit config.yaml', 'Claude wants to run find command'\n\nFor COMPLETION messages:\n- Say what specific work was just finished\n- Focus on the actual files/commands involved\n- Examples: 'Claude finished creating test files', 'Claude completed the search', 'Claude updated the configuration'\n\nRules:\n- Maximum 12 words\n- Always start with 'Claude wants to' or 'Claude finished'\n- Use specific filenames when provided\n- Never mention conversations, participants, or summaries\n- Be direct and actionable"
                    },
                    {
                        "role": "user",
                        "content": f"Context and tool details:\n{enhanced_context}\n\nCreate a specific audio notification:"
                    }
                ],
                "max_tokens": 60,
                "temperature": 0.2
            },
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_message = result["choices"][0]["message"]["content"].strip()
            
            
            # If OpenAI gives us a bad response, use our fallback logic
            if (not generated_message or 
                "conversation" in generated_message.lower() or 
                "participants" in generated_message.lower() or
                len(generated_message) < 5):
                fallback_message = ""
                if "permission" in base_message.lower():
                    if "Write" in base_message:
                        fallback_message = "Claude wants to create a file"
                    elif "Edit" in base_message:
                        fallback_message = "Claude wants to edit a file"
                    elif "Bash" in base_message:
                        fallback_message = "Claude wants to run a command"
                    elif "Read" in base_message:
                        fallback_message = "Claude wants to read a file"
                    else:
                        fallback_message = "Claude needs permission for an action"
                else:
                    fallback_message = f"Claude says: {base_message}" if base_message else "Claude needs your attention"
                
                
                return fallback_message
            
            
            return generated_message
        else:
            return f"Claude says: {base_message}" if base_message else "Claude needs your attention"
            
    except Exception as e:
        # Write error to debug file for troubleshooting
        try:
            with open("/tmp/hook_error.txt", "a") as f:
                f.write(f"Notification hook error: {str(e)}\n")
                f.write(f"API key present: {bool(api_key)}\n")
                f.write(f"Transcript path: {transcript_path}\n")
                f.write(f"Base message: {base_message}\n")
                f.write(f"Tool name: {tool_name}\n")
                f.write(f"Tool input: {tool_input}\n\n")
        except:
            pass
        return f"Claude says: {base_message}" if base_message else "Claude needs your attention"


def main():
    try:
        # Read input from stdin
        data = json.load(sys.stdin)
        
        
        # Generate dynamic message
        message = generate_dynamic_message(data)
        
        # Try OpenAI TTS first, fallback to macOS TTS
        if not speak_with_openai(message):
            speak_with_macos(message)
        
        # Return success response
        response = {"continue": True}
        json.dump(response, sys.stdout)
        
    except Exception as e:
        # Silent failure - don't break the hook chain
        response = {"continue": True}
        json.dump(response, sys.stdout)
        sys.exit(0)


if __name__ == "__main__":
    main()