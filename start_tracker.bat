@echo off
cd /D C:\Python\Django\habit_check  
call myvenv\Scripts\activate             
start "" python manage.py runserver     
TIMEOUT /T 5                            
start chrome http://127.0.0.1:8000/habit_tracker/      