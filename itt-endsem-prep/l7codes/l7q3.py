import sqlite3

conn = sqlite3.connect("database.db")

regno = int(input("Enter the registration number"))

cursor = conn.execute("SELECT * FROM STUDENT WHERE REGNO =" + str(regno))

for i in cursor:
    print(i)
