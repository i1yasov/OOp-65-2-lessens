# import sqlite3
# #A4
# connect = sqlite3.connect('users.db')
# # Рука с ручкой
# cursor = connect.cursor()
# cursor.execute('''
#     CREATE TABLE  IF NOT EXISTS users(
#         name VARCHAR (50) NOT NULL,
#         age INTEGER NOT NULL,
#         hobby TEXT
# ''')
# connect.commit()
# # CRUD Create - READ -Update -Delete
# def create_user(name, age, hobby):
#     cursor.execute(f'INSERT INTO users (name, age, hoppy)   VALUES ("{name}", "{age}", "{hobby}")')
#     connect.commit()
#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?) ',
#         (name, age, hobby)
#     )
import sqlite3

# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()

# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")')
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )

    connect.commit()
    print('Пользователь добавлен!!')


create_user("John Doe", 33, "Горы!!")
