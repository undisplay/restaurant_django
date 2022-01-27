@echo off
pushd "%~dp0"
start cmd.exe /C "cd .. && venv\Scripts\activate && python manage.py runserver 0.0.0.0:8999"
timeout 30
start http://127.0.0.1:8999