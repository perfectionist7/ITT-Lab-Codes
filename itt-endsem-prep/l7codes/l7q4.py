import sqlite3

conn = sqlite3.connect("database.db")
cgpa = float(input("Enter the CGPA "))
studentid = int(input("Enter the student id to update "))

conn.execute(
    "UPDATE STUDENT SET CGPA =" + str(cgpa) + " WHERE STUDENTID =" + str(studentid)
)
conn.commit()
cursor = conn.execute("SELECT * FROM STUDENT")

for i in cursor:
    print(i)
