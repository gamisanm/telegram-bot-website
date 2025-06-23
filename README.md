# 🚀 Telegram Bot Web App

**Telegram-бот на aiogram с Web App внутри Telegram на космическую тему.**

---

## 📦 Установка

1. Установите Python **3.8+**.
2. Создайте виртуальное окружение:
   ```bash
   python3 -m venv venv
   ```
   Активируйте:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```cmd
     venv\Scripts\activate
     ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Настройте `bot/config.py` с токеном от [@BotFather](https://t.me/BotFather) и URL.

---

## ⚙️ Настройка

1. Получите токен у [@BotFather](https://t.me/BotFather).
2. Запустите сервер:
   ```bash
   python3 web/server.py
   ```
3. В файле конфига укажите токен и URL.

---

## ▶️ Запуск

- В одном терминале:
  ```bash
  python3 web/server.py
  ```
- В другом:
  ```bash
  python3 main.py
  ```

Затем откройте Telegram, отправьте команду `/start` и нажмите **"Открыть Web App"**.

---

## 📁 Структура проекта

```
telegram-bot-website/
├── bot/         # Логика бота
├── web/         # Web App файлы
├── requirements.txt
├── README.md
└── main.py
```

---