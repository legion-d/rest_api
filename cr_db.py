import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE items (name text, price real)"
cursor.execute(create_table)

items = [
    ("bar_chair",12),
    ("black_chair",15.99)
]
insert_query = "INSERT INTO items VALUES (?,?)"
cursor.executemany(insert_query, items)

connection.commit()

connection.close()