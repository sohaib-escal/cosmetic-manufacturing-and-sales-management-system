@echo off
echo ========================================
echo Cosmetic Manufacturing System Setup
echo ========================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo Step 2: Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Step 3: Installing dependencies...
pip install django django-filter django-crispy-forms pillow django-mathfilters
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo Step 4: Running database migrations...
python manage.py makemigrations
python manage.py migrate

echo Step 5: Creating superuser...
echo Please create an admin account when prompted:
python manage.py createsuperuser

echo Step 6: Starting the development server...
echo.
echo The system will be available at: http://127.0.0.1:8000/
echo Admin panel: http://127.0.0.1:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver

pause
