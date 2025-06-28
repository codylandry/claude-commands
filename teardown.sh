#!/bin/bash

# Claude Commands GNU Stow Teardown Script
# This script removes the GNU Stow symlinks and restores direct file management

set -e  # Exit on any error

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
COMMANDS_DIR="$CLAUDE_DIR/commands"

echo "🔧 Tearing down Claude Commands GNU Stow setup..."

# Check if GNU Stow is installed
if ! command -v stow &> /dev/null; then
    echo "❌ Error: GNU Stow is not installed"
    echo "   Install with: brew install stow (macOS) or apt install stow (Ubuntu)"
    exit 1
fi

# Check if commands directory is currently a symlink managed by stow
if [ ! -L "$COMMANDS_DIR" ]; then
    echo "❌ Error: Commands directory is not a symlink"
    echo "   It appears GNU Stow is not currently managing the commands directory"
    echo "   Current state: $(ls -la "$COMMANDS_DIR" 2>/dev/null || echo "does not exist")"
    exit 1
fi

# Verify the symlink points to our repository
CURRENT_TARGET=$(readlink "$COMMANDS_DIR")
EXPECTED_TARGET="$REPO_DIR/dot-claude/commands"

if [ "$CURRENT_TARGET" != "$EXPECTED_TARGET" ]; then
    echo "⚠️  Warning: Commands directory symlink doesn't point to this repository"
    echo "   Current target: $CURRENT_TARGET"
    echo "   Expected target: $EXPECTED_TARGET"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

# Remove the stow-managed symlinks
echo "🗑️  Removing GNU Stow symlinks..."
stow -d "$REPO_DIR" -t "$CLAUDE_DIR" -D dot-claude

# Copy files back to a regular directory
echo "📁 Creating regular commands directory..."
mkdir -p "$COMMANDS_DIR"

echo "📝 Copying command files..."
cp -r "$REPO_DIR/dot-claude/commands/"* "$COMMANDS_DIR/"

# Verify teardown
if [ -d "$COMMANDS_DIR" ] && [ ! -L "$COMMANDS_DIR" ]; then
    echo "✅ Success! GNU Stow teardown complete"
    echo "   Commands directory is now a regular directory: $COMMANDS_DIR"
    echo "   Files copied from repository: $REPO_DIR/dot-claude/commands/"
else
    echo "❌ Error: Teardown failed"
    exit 1
fi

echo ""
echo "🎉 Teardown complete! Claude commands are now managed directly."
echo "   Commands directory: $COMMANDS_DIR"
echo "   Repository remains at: $REPO_DIR"
echo ""
echo "Note: Changes made to files in $COMMANDS_DIR will NOT be version controlled."
echo "To resume version control, run: $REPO_DIR/setup.sh"