import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("DROP TABLE NEWDB")
conn.execute("CREATE TABLE NEWDB( ID INT , SALARY INT, NAME TEXT)")

conn.execute("INSERT INTO NEWDB VALUES (1,42000,'AYUSH')")
conn.execute("INSERT INTO NEWDB VALUES (2,50000,'PIYUSH') ")
conn.execute("INSERT INTO NEWDB VALUES (1,26000,'PRISONER')")

cursor = conn.execute("SELECT SUM(SALARY),ID FROM NEWDB GROUP BY ID")

for i in cursor:
    print(f"{i[0]:<12} {i[1]:<12}")

conn.close()
