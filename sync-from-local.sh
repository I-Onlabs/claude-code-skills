#!/bin/bash
# Sync skills from ~/.claude/skills/ to this repository

set -e

SKILLS_DIR="$HOME/.claude/skills"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "====================================="
echo "Syncing Skills from Local"
echo "====================================="
echo ""

if [ ! -d "$SKILLS_DIR" ]; then
    echo "❌ Error: ~/.claude/skills/ not found"
    exit 1
fi

echo "Source: $SKILLS_DIR"
echo "Target: $REPO_DIR"
echo ""

# Count skills
skill_count=$(ls -1d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')

if [ "$skill_count" -eq 0 ]; then
    echo "❌ No skill directories found in ~/.claude/skills/"
    exit 1
fi

echo "Found $skill_count skill directories"
echo ""

# Sync skills (excluding .git directories)
echo "Syncing skills..."
rsync -av --exclude='.git' --exclude='README.md' "$SKILLS_DIR/" "$REPO_DIR/"

# Verify
synced_count=$(ls -1d "$REPO_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "✅ Synced $synced_count skills successfully"
echo ""
echo "Next steps:"
echo "  1. Review changes: git status"
echo "  2. Commit: git add . && git commit -m 'Update skills'"
echo "  3. Push: git push origin main"
echo ""
