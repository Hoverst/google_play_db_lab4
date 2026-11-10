# Play Store API (Lab 4)

Flask + MySQL back-end для `play_store` бази даних. Реалізовано всі CRUD операції для таблиць (GET all, GET by id, POST, PUT, PATCH, DELETE) та ендпоінти для зовнішніх ключів з типом M:1 та M:M.

## Стек

- Python 3.10+
- Flask
- MySQL база даних: `play_store` (schema у `data.sql`)

## Як запустити

1. Створення та активація віртуального середовища venv:

cmd:
python -m venv venv
venv\Scripts\activate

2. Для встановлення залежностей:

pip install -r requirements.txt

3. У  `config/app.yml` треба прописати свій пароль від mySQL server

4. Запустити Flask сервер:

python app.py

Має бути такий порт: `http://127.0.0.1:5000`

5. Можна запустити тестування у Postman, якщо імпортувати проект, налаштувати змінну baseUrl на `http://127.0.0.1:5000` та відкрити Local Items 

Додатково: файл data.sql містить скрипт для створення таблиць у mySQL та файл seed.sql для заповнення створених таблиць даними 