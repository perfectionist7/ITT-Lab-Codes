import sqlite3

s = int(input("Enter the student id"))
regno = int(input("Enter the registration number"))
a = 1
branch = ""
semester = 0
section = ""
while a == 1:
    branch = input("Enter the branch (CSE/IT/CCE)")

    if branch == "CSE" or branch == "IT" or branch == "CCE":
        a = 0
    else:
        print("Invalid Entry, enter cse or it or cce")
        a = 1


a = 1

while a == 1:
    semester = int(input("Enter the semester from 1 to 8"))

    if semester >= 1 and semester <= 8:
        a = 0
    else:
        print("Invalid semester")
        a = 1

while a == 1:
    section = input("Enter the section (A/B/C/D)")

    if section == "A" or section == "B" or section == "C" or section == "D":
        a = 0
    else:
        print("Invalid section")
        a = 1


cgpa = float(input("Enter your cgpa"))

email = input("Enter your email")

conn = sqlite3.connect("database.db")

conn.execute(
    "INSERT INTO STUDENT VALUES ('"
    + str(s)
    + "','"
    + str(regno)
    + "','"
    + branch
    + "','"
    + str(semester)
    + "','"
    + section
    + "','"
    + str(cgpa)
    + "','"
    + email
    + "')"
)

cursor = conn.execute("SELECT * FROM STUDENT")

for i in cursor:
    print(i)
