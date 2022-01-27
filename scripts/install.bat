@echo off
pushd "%~dp0"
call cmd.exe /C "cd .. && python -m venv venv && venv\Scripts\activate && python -m pip install --upgrade pip && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata fixtures\user.json"
start shortcut_creator.bat
call start.bat