#!/bin/bash
# GitHub Repository Creation Script
# For Burp Suite Laboratory Exercise

set -e  # Exit on any error

echo "🎯 GitHub Repository Setup for Burp Suite Laboratory"
echo "📚 Master's Degree in Cybersecurity Exercise"
echo "================================================================"
echo

# Configuration
REPO_NAME="burp-suite-laboratory"
REPO_DESCRIPTION="Educational race condition attack scripts for Burp Suite laboratories - Master's Degree in Cybersecurity exercise"
REPO_TOPICS="cybersecurity,burp-suite,race-condition,educational,python,security-testing,portswigger,web-security"

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "📦 Install it with: brew install gh"
    echo "🔗 Or visit: https://cli.github.com/"
    echo
    echo "📋 Manual steps after installing gh:"
    echo "   1. gh auth login"
    echo "   2. Run this script again"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo "🔐 You need to authenticate with GitHub first."
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI detected and authenticated"
echo

# Get user confirmation
echo "📋 Repository Configuration:"
echo "   Name: $REPO_NAME"
echo "   Description: $REPO_DESCRIPTION"
echo "   Visibility: Public (educational purpose)"
echo "   Topics: $REPO_TOPICS"
echo

read -p "🤔 Do you want to create this repository? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Repository creation cancelled."
    exit 0
fi

echo "🚀 Creating GitHub repository..."

# Create the repository
gh repo create "$REPO_NAME" \
    --description "$REPO_DESCRIPTION" \
    --public \
    --clone=false \
    --add-readme=false

echo "✅ Repository created successfully!"
echo

# Add remote origin
echo "🔗 Adding remote origin..."
GITHUB_USERNAME=$(gh api user --jq '.login')
REMOTE_URL="https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

git remote add origin "$REMOTE_URL"
echo "✅ Remote origin added: $REMOTE_URL"
echo

# Push to GitHub
echo "📤 Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "✅ Code pushed successfully!"
echo

# Add topics
echo "🏷️  Adding repository topics..."
gh repo edit --add-topic "cybersecurity,burp-suite,race-condition,educational,python,security-testing,portswigger,web-security"

echo "✅ Topics added successfully!"
echo

# Final information
echo "🎉 Repository setup complete!"
echo "================================================================"
echo "📍 Repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo "🌟 Repository features:"
echo "   ✅ Comprehensive README with badges"
echo "   ✅ Educational documentation"
echo "   ✅ MIT License"
echo "   ✅ Proper .gitignore"
echo "   ✅ Example configurations"
echo "   ✅ Contributing guidelines"
echo "   ✅ Setup instructions"
echo
echo "📝 Next steps:"
echo "   1. Star your repository if you want"
echo "   2. Share with classmates (if allowed)"
echo "   3. Update configuration for your specific labs"
echo "   4. Document your learning progress"
echo
echo "🎓 Happy learning and ethical hacking!"
echo "================================================================"

# Open repository in browser (optional)
read -p "🌐 Open repository in browser? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    gh repo view --web
fi

echo "👋 Setup complete!"

