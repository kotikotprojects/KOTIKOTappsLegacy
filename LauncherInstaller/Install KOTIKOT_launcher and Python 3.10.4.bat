@echo off
@echo ----- Downloadig Install-KOTIKOT_launcher from my GitHub ------------------------------------
powershell -command iwr https://raw.githubusercontent.com/kotikotprojects/KOTIKOTappsLegacy/master/LauncherInstaller/Install-KOTIKOT_launcher.py -OutFile Install-KOTIKOT_launcher.py
@echo ----- If you have Python, just close this window now ----------------------------------------
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
@echo ----- Downloadig Python from official site --------------------------------------------------
@echo ----- python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe ----------------------------------
powershell -command iwr https://python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -OutFile python.exe
@echo ----- After installing python, run Install-KOTIKOT_launcher to install KOTIKOT_launcher -----
@echo off
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
ping -n 3 localhost > nul
@echo ----- Running installer... ------------------------------------------------------------------
@start python.exe