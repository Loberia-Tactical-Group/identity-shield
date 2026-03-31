@echo off
title Loberia Identity Shield - Active
echo [*] Instalando dependencias...
pip install -r requirements.txt --quiet
echo [*] Iniciando Sentinel...
python core/sentinel.py
pause
