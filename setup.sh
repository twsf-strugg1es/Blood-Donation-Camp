#!/bin/bash

# Blood Donation Camp - Unix/Linux/Mac Setup Script

echo ""
echo "===================================="
echo "Blood Donation Camp Setup"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

echo "[1/6] Python found: $(python3 --version)"
echo ""

# Create virtual environment
echo "[2/6] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
else
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "[3/6] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

# Install dependencies
echo "[4/6] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

# Create .env file if it doesn't exist
echo "[5/6] Checking environment configuration..."
if [ -f ".env" ]; then
    echo ".env file already exists"
else
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "Please edit .env if you have custom MySQL credentials"
fi

# Run migrations
echo "[6/6] Running database migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error: Failed to run migrations"
    echo "Make sure XAMPP MySQL is running!"
    exit 1
fi

echo ""
echo "===================================="
echo "Setup complete!"
echo "===================================="
echo ""
echo "Next steps:"
echo "1. Start XAMPP MySQL (if not already running)"
echo "2. Run: python manage.py runserver"
echo "3. Visit: http://127.0.0.1:8000/"
echo ""
