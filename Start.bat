@echo off

rem Get the path to the folder containing the .bat file
set "SCRIPT_PATH=%~dp0"

rem Change to the specified directory
cd /d "%SCRIPT_PATH%"

rem Run the Python script using pipenv
echo Starting bot...
pipenv run python bot.py

rem Pause to keep the console window open (optional)
pause