# Telegram Bot Website

Telegram-бот, который отправляет ссылку на веб-сайт.

## Установка
1. Установите Python 3.8+.
2. Создайте виртуальное окружение: `python -m venv venv`.
3. Активируйте окружение: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Mac/Linux).
4. Установите зависимости: `pip install -r requirements.txt`.
5. Настройте `bot/config.py` с вашим токеном бота и URL сайта.
6. Запустите бота: `python main.py`.

## Настройка
- Получите токен бота у @BotFather в Telegram.
- Обновите `BOT_TOKEN` и `WEBSITE_URL` в `bot/config.py`.