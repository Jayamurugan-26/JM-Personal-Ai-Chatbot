@echo off
echo Searching for Git...

REM Try to find git.exe in common locations
set GITPATH=

if exist "C:\Program Files\Git\bin\git.exe" set GITPATH=C:\Program Files\Git\bin
if exist "C:\Program Files (x86)\Git\bin\git.exe" set GITPATH=C:\Program Files (x86)\Git\bin

if "%GITPATH%"=="" (
    echo Git not found in default locations.
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Found Git at: %GITPATH%

REM Add Git to PATH temporarily and run commands
set PATH=%GITPATH%;%PATH%

echo Renaming branch to main...
git branch -m master main

echo Pushing to GitHub...
git push -u origin main

echo Done!
pause
