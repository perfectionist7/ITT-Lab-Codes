import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("DROP TABLE CUSTOMER")
conn.execute("CREATE TABLE CUSTOMER( ACCNUMBER INT, NAME TEXT, BALANCE INT)")

conn.execute("INSERT INTO CUSTOMER VALUES(1,'Ayush',10000)")
conn.execute("INSERT INTO CUSTOMER VALUES(2,'Piyush',25000)")
conn.execute("INSERT INTO CUSTOMER VALUES(3,'Ronit',50000)")

cursor = conn.execute("SELECT * FROM CUSTOMER")

accno = int(input("Enter the account number"))

cursor = conn.execute("SELECT * FROM CUSTOMER WHERE ACCNUMBER =" + str(accno))

for i in cursor:
    print(i)

print("Balance greater than 20000 are ")
cursor = conn.execute("SELECT * FROM CUSTOMER WHERE BALANCE>20000")
for i in cursor:
    print(i)

cursor = conn.execute(
    "SELECT REGNO, BALANCE FROM STUDENT s JOIN CUSTOMER c ON s.STUDENTID = c.ACCNUMBER"
)

for i in cursor:
    print(i)
