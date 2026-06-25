#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

echo "Setting up Python virtual environment..."
python3 -m venv browserstack

# Activate virtual environment
source browserstack/bin/activate

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Setup completed successfully!"
