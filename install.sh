#!/bin/bash
set -e

echo "========================================="
echo "  VICCA Bot — Установка на сервер"
echo "========================================="

# 1. Обновление системы
echo "[1/8] Обновление системы..."
apt update -y && apt upgrade -y

# 2. Установка PostgreSQL
echo "[2/8] Установка PostgreSQL..."
apt install -y postgresql postgresql-contrib

# 3. Установка Python
echo "[3/8] Установка Python..."
apt install -y python3 python3-pip python3-venv

# 4. Запуск PostgreSQL
echo "[4/8] Настройка PostgreSQL..."
systemctl start postgresql
systemctl enable postgresql

# Создание пользователя и базы данных
sudo -u postgres psql -c "CREATE USER vicca WITH PASSWORD 'vicca_secure_2024';" 2>/dev/null || echo "User vicca уже существует"
sudo -u postgres psql -c "CREATE DATABASE vicca_bot OWNER vicca;" 2>/dev/null || echo "Database vicca_bot уже существует"

# 5. Настройка бота
echo "[5/8] Настройка бота..."
cd /root/vicca_bot

# 6. Виртуальное окружение
echo "[6/8] Создание виртуального окружения..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 7. Создание systemd сервиса
echo "[7/8] Создание systemd сервиса..."
cat > /etc/systemd/system/vicca-bot.service << 'SERVICEEOF'
[Unit]
Description=VICCA Telegram Bot
After=network.target postgresql.service

[Service]
User=root
WorkingDirectory=/root/vicca_bot
ExecStart=/root/vicca_bot/venv/bin/python bot.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
SERVICEEOF

# 8. Запуск
echo "[8/8] Запуск бота..."
systemctl daemon-reload
systemctl enable vicca-bot
systemctl start vicca-bot

echo ""
echo "========================================="
echo "  VICCA Bot успешно установлен!"
echo "========================================="
echo ""
echo "Команды управления:"
echo "  systemctl status vicca-bot   — статус"
echo "  systemctl restart vicca-bot  — перезапуск"
echo "  systemctl stop vicca-bot     — остановить"
echo "  journalctl -u vicca-bot -f   — логи"
echo ""
echo "Токен бота и настройки: /root/vicca_bot/.env"
echo "========================================="
