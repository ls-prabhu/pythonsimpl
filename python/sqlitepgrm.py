import sqlite3

conn = sqlite3.connect("student.db")


def insertData(data,cursor,connection):
    inscmd ='''INSERT INTO student (name,age) VALUES (?,?)'''
    cursor.execute(inscmd,data)
    connection.commit()

cur = conn.cursor()

cmd1 = ''' CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    age NUMBER
 )'''
cur.execute(cmd1)
conn.commit()



# Insert a new student
insertData(("prabhu",21),cur,conn)
insertData(("arun",21),cur,conn)
insertData(("ram",21),cur,conn)


cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()

