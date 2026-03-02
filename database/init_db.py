import sqlite3

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

with open("schema.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Database created successfully!")