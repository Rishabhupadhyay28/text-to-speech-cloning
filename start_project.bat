@echo off
title TTS + Voice Cloning Project
echo ================================
echo Starting TTS + Voice Cloning Project
echo ================================

:: Step 1: Activate virtual environment
call "%~dp0venv310\Scripts\activate.bat"

:: Step 2: Start FastAPI backend
start cmd /k "cd /d %~dp0 && venv310\Scripts\activate && uvicorn app:app --reload --host 127.0.0.1 --port 8000"

:: Step 3: Start Streamlit frontend
start cmd /k "cd /d %~dp0 && venv310\Scripts\activate && streamlit run ui/app_ui.py"

echo ✅ Both backend and frontend are starting...
pause
