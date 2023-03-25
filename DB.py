import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE users(
        username text,
        password text,
        record integer
    )""")
cursor.execute("INSERT INTO users VALUES ('ohad', 'ohad123', '200')")
connection.commit()
connection.close()