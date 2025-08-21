@echo off
echo ========================================
echo Resetting Django Migrations
echo ========================================
echo.

echo Step 1: Removing old migration files...
for /d %%d in (*) do (
    if exist "%%d\migrations" (
        echo Cleaning %%d\migrations...
        del /q "%%d\migrations\*.py" 2>nul
        echo. > "%%d\migrations\__init__.py"
    )
)

echo Step 2: Creating fresh migrations...
python manage.py makemigrations

echo Step 3: Applying migrations...
python manage.py migrate

echo Step 4: Creating superuser...
echo Please create an admin account when prompted:
python manage.py createsuperuser

echo Step 5: Starting the development server...
echo.
echo The system will be available at: http://127.0.0.1:8000/
echo Admin panel: http://127.0.0.1:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver

pause
