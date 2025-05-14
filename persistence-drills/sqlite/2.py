import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
"""

cursor.execute(create_table_sql)

conn.commit()
conn.close()

print("products table created successfully.")