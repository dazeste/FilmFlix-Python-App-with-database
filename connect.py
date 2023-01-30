import sqlite3 as sql

# connect(filePathToDatabase)
conn = sql.connect(r"C:\JustIT\week_11_Python\filmflix.db")

cursor = conn.cursor()
