@echo off

title Auto Install

if exist C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310 (
    goto Install
) else (
    goto NoPython
)

:Install
pip install -r "requirements.txt"
echo.
pause
goto Exit

:NoPython
echo You need to install Python and PIP before using AutoInstall
set /p INPUT=Do you want to download the installer now? (y, n): 

if "%INPUT%" == "y" (
    goto Download
) else (
    echo.
    pause
    goto Exit
)

:Download
echo Connecting to "https://www.python.org/downloads/" ...
start https://www.python.org/downloads/
echo Done!
echo.
pause
goto Exit

:Exit
