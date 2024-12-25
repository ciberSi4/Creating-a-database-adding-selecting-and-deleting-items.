# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создание таблицы Users, если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполнение таблицы данными
for i in range(1, 11):  # Цикл от 1 до 10 включительно
    username = f"User{i}"
    email = f"example{i}@gmail.com"
    age = i * 10
    balance = 1000

    # Использование f-строки для формирования значения balance
    if i % 2 == 1:
        balance = 500

    # Выполнение вставки данных в базу данных
    cursor.execute(f'''
        INSERT INTO Users (username, email, age, balance) 
        VALUES ("{username}", "{email}", {age}, {balance})
    ''')

# Удаление каждой третьей записи начиная с первой
cursor.execute('''
    DELETE FROM Users
    WHERE id % 3 == 1
''')

# Выборка всех записей, кроме тех, у кого возраст равен 60
cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != 60
''')

# Получаем все строки и выводим результат в нужном формате
rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Закрываем соединение с базой данных
conn.commit()
conn.close()