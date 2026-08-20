import sqlite3

conn = sqlite3.connect("student.db")
def leaveSpaces():
    for i in range(15):
        print()


def insertData(data,cursor,connection):
    inscmd ='''INSERT INTO student (name,age) VALUES (?,?)'''
    cursor.execute(inscmd,data)
    connection.commit()


def display(cursor):
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    leaveSpaces()
    for row in rows:
        print(row)



cur = conn.cursor()

cmd1 = ''' CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    age NUMBER
 )'''
cur.execute(cmd1)
conn.commit()


while True:
    choice = int(input(('1. insert data\n2. show all data\n\nenter your choice : ')))

    if(choice==1):
        name = input('enter name: ')
        age = int(input("enter age : "))
        insertData((name,age),cur,conn)
        leaveSpaces()
    elif(choice==2):
        display(cur)