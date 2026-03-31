#!/bin/bash
echo "[*] Instalando dependencias..."
pip3 install -r requirements.txt --quiet
echo "[*] Iniciando Sentinel..."
python3 core/sentinel.py
