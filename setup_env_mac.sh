#!/bin/bash

echo "🛠️ Setting up your Python virtual environment on macOS..."

# Step 1: Check for existing venv
if [ -d "venv" ]; then
    echo "✅ 'venv/' directory already exists. Skipping creation."
else
    echo "📁 Creating a new virtual environment in 'venv/'..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment. Make sure Python 3 is installed."
        exit 1
    fi
fi

# Step 2: Activate the venv
echo "⚙️ Activating the virtual environment..."
source venv/bin/activate

# Step 3: Upgrade pip inside venv
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Step 4: Install from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ No requirements.txt found. Skipping dependency installation."
fi

echo "✅ Setup complete. Your virtual environment is ready."
echo "To activate it in the future, run:"
echo "    source venv/bin/activate"
