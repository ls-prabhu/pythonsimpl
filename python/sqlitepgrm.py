import sqlite3

conn = sqlite3.connect("student.db")

cur = conn.cursor()

cmd1 = ''' CREATE TABLE IF NOT EXISTS student(
    name TEXT
)'''
cur.execute(cmd1)
conn.commit()
conn.close()

