#!/bin/bash

# 🟢 Auto-publish script for initializing and pushing a local folder as a GitHub repo

echo "📦 Initializing local Git repo..."

# Initialize repo
git init

echo "📁 Adding all files..."
git add .

echo "📝 Creating initial commit..."
git commit -m "Initial commit of greyhawk-weather project"

# Prompt for GitHub repo URL
read -p "🌐 Enter GitHub repository URL (e.g. https://github.com/youruser/yourrepo.git): " repo_url

# Set remote and push
echo "🔗 Connecting to GitHub remote..."
git remote add origin "$repo_url"
git branch -M main
git push -u origin main

echo "✅ Repository published successfully!"
