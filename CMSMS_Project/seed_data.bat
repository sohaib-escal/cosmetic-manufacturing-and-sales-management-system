@echo off
echo ========================================
echo Seeding Sample Data
echo ========================================
echo.

echo Step 1: Activating virtual environment...
call venv\Scripts\activate

echo Step 2: Running data seeding script...
python simple_seed_data.py

echo.
echo Data seeding completed!
pause
