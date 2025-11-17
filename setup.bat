@echo off
REM Blood Donation Camp - Windows Setup Script

echo.
echo ====================================
echo Blood Donation Camp Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/6] Python found
echo.

REM Create virtual environment
echo [2/6] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists
) else (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install dependencies
echo [4/6] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Create .env file if it doesn't exist
echo [5/6] Checking environment configuration...
if exist .env (
    echo .env file already exists
) else (
    echo Creating .env from .env.example...
    copy .env.example .env
    echo Please edit .env if you have custom MySQL credentials
)

REM Run migrations
echo [6/6] Running database migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo Error: Failed to run migrations
    echo Make sure XAMPP MySQL is running!
    pause
    exit /b 1
)

echo.
echo ====================================
echo Setup complete!
echo ====================================
echo.
echo Next steps:
echo 1. Start XAMPP MySQL (if not already running)
echo 2. Run: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/
echo.
pause
