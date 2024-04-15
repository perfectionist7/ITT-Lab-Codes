import sqlite3

conn = sqlite3.connect("database.db")
conn.execute(
    "CREATE TABLE STUDENT( STUDENTID INT PRIMARY KEY, REGNO INT, BRANCH TEXT, SEMESTER INT, SECTION TEXT, CGPA FLOAT, EMAIL TEXT)"
)

conn.execute(
    "INSERT INTO STUDENT VALUES(1,210911082,'IT',6,'C',8.51,'akhandelwal2003@gmail.com')"
)
conn.execute(
    "INSERT INTO STUDENT VALUES(2,210829342,'CSE',5,'A','9.02','sampledata@gmail.com')"
)
conn.execute(
    "INSERT INTO STUDENT VALUES(3,939293939,'CSAI',4,'D','7.92','takingtest@gmail.com')"
)
conn.execute(
    "INSERT INTO STUDENT VALUES(4,9392939,'IT',4,'D','9.88','taksaingtest@gmail.com')"
)

cursor = conn.execute("SELECT * FROM STUDENT ORDER BY CGPA")

for i in cursor:
    print(i)

conn.commit()
print("Created Table Successfully!")
