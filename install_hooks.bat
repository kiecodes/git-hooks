@echo off

:: ====================================================================
:: Name        : install_hooks.bat
:: Description : Installs a commit-msg hook for git
:: Author      : Various
:: Notes       : Need to be executed as an administrator
:: Revision    : June 2020 - Initial version
:: ====================================================================

set LIB_DIR=submodules

if exist .git\hooks\commit-msg del /F .git\hooks\commit-msg
mklink .git\hooks\commit-msg ..\..\src\commit-msg.py

if exist .git\hooks\%LIB_DIR% rmdir /S /Q .git\hooks\%LIB_DIR%
mklink /D .git\hooks\%LIB_DIR% ..\..\src\%LIB_DIR%