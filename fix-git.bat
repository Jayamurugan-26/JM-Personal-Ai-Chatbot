@echo off
echo Fixing Git branch issue...

REM Rename master to main
git branch -m master main

REM Push to remote
git push -u origin main

echo Done! Your code has been pushed to main branch.
pause
