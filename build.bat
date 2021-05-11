WHERE pyinstaller
IF %ERRORLEVEL% NEQ 0 goto pyinstallernotfound
cd projects
pyinstaller -F 1_qec.py
pyinstaller -F 2_test.py
pyinstaller -F 3_exchange.py
pyinstaller -F 4_seabattle.py
pyinstaller -F 5_drugs.py
pyinstaller -F 6_english.py
pyinstaller -F 7_tictactoe.py
cls
goto end
:pyinstallernotfound
echo pyinstaller is not found on your machine!
echo type 'pip install pyinstaller' in cmd, if you have installed Python, and try again!
:end
echo Compiling successfully finished!