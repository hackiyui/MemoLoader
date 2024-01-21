@echo off


:CHECK_ADMIN
REM Vérifier les privilèges administratifs
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
ECHO Ce script doit etre execute en tant qu'administrateur.
PAUSE
GOTO CHECK_ADMIN
)


echo Activation de Windows 10 en cours...


REM Désactivez temporairement l'antivirus et le pare-feu
REM Supprimez les commentaires des lignes suivantes si vous souhaitez désactiver temporairement l'antivirus et le pare-feu
taskkill /F /IM antivirus.exe
taskkill /F /IM firewall.exe


REM Attendre 2 secondes
timeout /t 2


cls


echo Activation de Windows 10 en cours...


:CHOICE
REM Choisissez si vous souhaitez désactiver les mises à jour automatiques
set /p disable_updates="Voulez-vous desactiver les mises a jour automatiques ? (Oui/Non): "
if /i "%disable_updates%"=="Oui" (
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 1 /f
net stop wuauserv
) else if /i "%disable_updates%"=="Non" (
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 4 /f
net start wuauserv
) else (
echo Choix invalide. Veuillez entrer "Oui" ou "Non".
GOTO CHOICE
)


REM Attendre 2 secondes
timeout /t 2


cls


echo Activation de Windows 10 en cours...


REM Activez Windows 10
cscript //nologo c:\windows\system32\slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX >nul
cscript //nologo c:\windows\system32\slmgr.vbs /ato >nul


REM Réactivez l'antivirus
REM Supprimez les commentaires des lignes suivantes pour réactiver l'antivirus
taskkill /IM antivirus.exe /F
taskkill /IM firewall.exe /F


cls


echo Activation de Windows 10 terminee avec succes !
pause