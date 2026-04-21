import sqlite3
connection = sqlite3.connect('grode.db')
cursor = connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL
        )
''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS grodes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INTEGER NOT NULL,
            name VARCHAR(50) NOT NULL,
            subject VARCHAR(50) NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')
def creade_user(name, age):
    (

    )