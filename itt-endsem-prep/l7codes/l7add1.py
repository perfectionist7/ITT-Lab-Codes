import sqlite3

conn = sqlite3.connect("database.db")
# conn.execute("DROP TABLE CUSTOMER")
# conn.execute("CREATE TABLE CUSTOMER( PHONENUMBER INT, EMAILID TEXT)")


phonenumber = 0

a = 1

while a == 1:
    phonenumber = input("Enter the phone number")
    if phonenumber.isnumeric() and len(phonenumber) == 10:
        a = 0
    else:
        print("Invalid phonne number ")

a = 1

while a == 1:
    emailid = input("Enter the email id")
    if "@" in emailid and ".com" in emailid:
        a = 0
    else:
        print("Invalid email id entered")

conn.execute("INSERT INTO CUSTOMER VALUES (" + str(phonenumber) + ",'" + emailid + "')")
conn.commit()
cursor = conn.execute("SELECT * FROM CUSTOMER")

for i in cursor:
    print(i)
