@echo off

rem Get the path to the folder containing the .bat file
set "SCRIPT_PATH=%~dp0"

rem Change to the specified directory
cd /d "%SCRIPT_PATH%"

rem Check if pipenv is installed
pipenv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pipenv is needed to run this bot.
    choice /C YN /M "Do you want to install pipenv? (Y/N)"
    if errorlevel 2 (
        echo Pipenv is not installed, the bot can't run.
        pause
        exit /b 1
    ) else (
        echo Installing pipenv...
        pip install pipenv
        rem Check if installation was successful
        if %errorlevel% neq 0 (
            echo Error installing pipenv. Exiting.
            pause
            exit /b 1
        )
    )
)

rem Check if required packages are installed
pipenv run pip show twitchio >nul 2>&1
if %errorlevel% neq 0 (
    echo twitchio is not installed.
    set "MISSING_PACKAGES=true"
)
pipenv run pip show "ahk[binary]" >nul 2>&1
if %errorlevel% neq 0 (
    echo "ahk[binary]" is not installed.
    set "MISSING_PACKAGES=true"
)
pipenv run pip show pyautogui >nul 2>&1
if %errorlevel% neq 0 (
    echo pyautogui is not installed.
    set "MISSING_PACKAGES=true"
)
pipenv run pip show python-dotenv >nul 2>&1
if %errorlevel% neq 0 (
    echo python-dotenv is not installed.
    set "MISSING_PACKAGES=true"
)
pipenv run pip show pathlib >nul 2>&1
if %errorlevel% neq 0 (
    echo pathlib is not installed.
    set "MISSING_PACKAGES=true"
)

rem If any required package is missing, install them
if defined MISSING_PACKAGES (
    echo Installing required packages...
    pipenv install twitchio "ahk[binary]" pyautogui python-dotenv pathlib
    rem Check if installation was successful
    if %errorlevel% neq 0 (
        echo Error installing required packages. Exiting.
        pause
        exit /b 1
    )
)