import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.execute(
    "SELECT SUM(CGPA) AS TOT_CGPA, BRANCH FROM STUDENT GROUP BY BRANCH"
)

for i in cursor:
    if i[0] > 9.5 and i[0] < 20:
        grade = "A"
    elif i[0] > 8 and i[0] < 9.5:
        grade = "B"
    else:
        grade = "C"
    print("The grade for " + str(i[1]) + " in branch " + str(i[0]) + " is " + grade)
