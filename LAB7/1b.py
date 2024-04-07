#!/usr/bin/python
import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
conn.execute(
    "INSERT INTO STUDENT VALUES (1, 191, 'IT', 6, 'C', 8.22, 'ayush@gmail.com' )"
)
conn.execute(
    "INSERT INTO STUDENT VALUES (2, 192, 'IT', 6, 'B', 8.72, 'piyush@gmail.com' )"
)
conn.execute(
    "INSERT INTO STUDENT VALUES (3, 193, 'CSE', 4, 'A', 7.81, 'rohit@gmail.com' )"
)
conn.execute(
    "INSERT INTO STUDENT VALUES (4, 194, 'EEE', 4, 'A', 9.88, 'sagar@gmail.com' )"
)
conn.commit()
print("Records created successfully")
conn.close()
