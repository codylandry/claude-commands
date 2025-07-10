#!/bin/bash
# Setup script for Claude hooks virtual environment

set -e  # Exit on any error

HOOKS_DIR="$HOME/.claude/hooks"
VENV_DIR="$HOOKS_DIR/.venv"

echo "Setting up Claude hooks virtual environment..."

# Change to hooks directory
cd "$HOOKS_DIR"

# Source asdf if available
if [ -f "$HOME/.asdf/asdf.sh" ]; then
    source "$HOME/.asdf/asdf.sh"
fi

# Remove existing venv if it exists
if [ -d "$VENV_DIR" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$VENV_DIR"
fi

# Create new virtual environment using system python or asdf
echo "Creating virtual environment..."
if command -v python3 &> /dev/null; then
    python3 -m venv "$VENV_DIR"
else
    /usr/bin/python3 -m venv "$VENV_DIR"
fi

# Activate and install dependencies
echo "Installing dependencies..."
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r requirements.txt

echo "Setup complete! Virtual environment created at: $VENV_DIR"
echo "Dependencies installed:"
"$VENV_DIR/bin/pip" list