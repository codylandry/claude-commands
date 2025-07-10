#!/bin/bash

# Claude Commands GNU Stow Setup Script
# This script sets up symbolic links from this repository to ~/.claude/commands/

set -e  # Exit on any error

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
COMMANDS_DIR="$CLAUDE_DIR/commands"
STOW_SOURCE="$REPO_DIR/dot-claude"

echo "🔧 Setting up Claude Commands with GNU Stow..."

# Check if GNU Stow is installed
if ! command -v stow &> /dev/null; then
    echo "❌ Error: GNU Stow is not installed"
    echo "   Install with: brew install stow (macOS) or apt install stow (Ubuntu)"
    exit 1
fi

# Check if ~/.claude directory exists
if [ ! -d "$CLAUDE_DIR" ]; then
    echo "❌ Error: ~/.claude directory does not exist"
    echo "   Please ensure Claude CLI is properly installed"
    exit 1
fi

# Backup existing commands directory if it exists and is not a symlink
if [ -d "$COMMANDS_DIR" ] && [ ! -L "$COMMANDS_DIR" ]; then
    BACKUP_DIR="${COMMANDS_DIR}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "📦 Backing up existing commands directory to: $BACKUP_DIR"
    mv "$COMMANDS_DIR" "$BACKUP_DIR"
fi

# Remove existing symlink if present
if [ -L "$COMMANDS_DIR" ]; then
    echo "🔗 Removing existing symlink: $COMMANDS_DIR"
    rm "$COMMANDS_DIR"
fi

# Use GNU Stow to create symlinks
echo "🔗 Creating symlinks with GNU Stow..."
stow -d "$REPO_DIR" -t "$CLAUDE_DIR" dot-claude

# Verify setup
if [ -L "$COMMANDS_DIR" ]; then
    echo "✅ Success! Claude commands are now managed via GNU Stow"
    echo "   Commands directory: $COMMANDS_DIR"
    echo "   Points to: $(readlink "$COMMANDS_DIR")"
else
    echo "❌ Error: Setup failed - commands directory is not a symlink"
    exit 1
fi

# Setup hooks virtual environment
echo ""
echo "🐍 Setting up hooks virtual environment..."
VENV_DIR="$CLAUDE_DIR/.venv"

# Source asdf if available
if [ -f "$HOME/.asdf/asdf.sh" ]; then
    source "$HOME/.asdf/asdf.sh"
fi

# Remove existing venv if it exists
if [ -d "$VENV_DIR" ]; then
    echo "📦 Removing existing virtual environment..."
    rm -rf "$VENV_DIR"
fi

# Create new virtual environment
echo "🔨 Creating virtual environment..."
if command -v python3 &> /dev/null; then
    python3 -m venv "$VENV_DIR"
else
    /usr/bin/python3 -m venv "$VENV_DIR"
fi

# Install dependencies if requirements.txt exists
REQUIREMENTS_FILE="$REPO_DIR/requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "📦 Installing hook dependencies..."
    "$VENV_DIR/bin/pip" install --upgrade pip > /dev/null 2>&1
    "$VENV_DIR/bin/pip" install -r "$REQUIREMENTS_FILE" > /dev/null 2>&1
    echo "✅ Hook dependencies installed"
else
    echo "⚠️  Warning: No requirements.txt found for hooks"
fi

echo ""
echo "🎉 Setup complete! Your Claude commands are now version controlled."
echo "   Repository: $REPO_DIR"
echo "   Commands: $COMMANDS_DIR"
echo "   Hooks venv: $VENV_DIR"
echo ""
echo "To make changes:"
echo "  1. Edit files in: $REPO_DIR/dot-claude/commands/"
echo "  2. Commit changes: git add . && git commit"
echo "  3. Changes are immediately available to Claude"