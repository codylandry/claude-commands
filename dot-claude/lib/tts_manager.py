#!/usr/bin/env python3
"""
Text-to-Speech manager utilities for Claude Code hooks.
"""

import os
import subprocess
import tempfile
import requests
from typing import Optional


def speak_with_openai(text: str, voice: str = "alloy") -> bool:
    """
    Use OpenAI TTS API to generate and play speech.
    
    Args:
        text: Text to speak
        voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)
        
    Returns:
        True if successful, False otherwise
    """
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


def speak_with_macos(text: str) -> bool:
    """
    Use macOS built-in TTS as fallback.
    
    Args:
        text: Text to speak
        
    Returns:
        True if successful, False otherwise
    """
    try:
        subprocess.run(["say", text], check=True)
        return True
    except Exception:
        return False


def speak_text(text: str, voice: str = "alloy", 
               prefer_openai: bool = True) -> bool:
    """
    Speak text using the best available TTS method.
    
    Args:
        text: Text to speak
        voice: Voice to use for OpenAI TTS
        prefer_openai: Whether to try OpenAI first
        
    Returns:
        True if successful, False otherwise
    """
    if prefer_openai:
        if speak_with_openai(text, voice):
            return True
        return speak_with_macos(text)
    else:
        if speak_with_macos(text):
            return True
        return speak_with_openai(text, voice)


def is_openai_available() -> bool:
    """
    Check if OpenAI TTS is available (API key present).
    
    Returns:
        True if OpenAI API key is available
    """
    return bool(os.getenv("OPENAI_API_KEY"))


def is_macos_tts_available() -> bool:
    """
    Check if macOS TTS is available.
    
    Returns:
        True if 'say' command is available
    """
    try:
        subprocess.run(["which", "say"], capture_output=True, check=True)
        return True
    except Exception:
        return False