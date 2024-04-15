import sqlite3

conn = sqlite3.connect("database.db")

print("Enter your option \n")


while 1:
    print(
        "1. INSERT INTO TABLE\n2.SEARCH INTO THE TABLE\n3.CALCULATE COUNT\n4.CALCULATE AVERAGE\n5.DISPLAY TABLE\n6.EXIT"
    )

    n = int(input())
    if n == 1:
        studentid = input("Enter the student ID")
        regno = input("Enter the reg no")
        branch = input("Enter the branch")
        semester = input("Enter the semester")
        section = input("Enter the section")
        cgpa = input("Enter the cgpa")
        email = input("Enter the email")
        conn.execute(
            "INSERT INTO STUDENT VALUES ("
            + studentid
            + ","
            + regno
            + ",'"
            + branch
            + "',"
            + semester
            + ",'"
            + section
            + "',"
            + cgpa
            + ",'"
            + email
            + "')"
        )
        print("Inserted Sucessfully!")
        conn.commit()
    elif n == 2:
        num = input("Enter the student id u want to search")
        cursor = conn.execute("SELECT * FROM STUDENT WHERE STUDENTID=" + num)
        for i in cursor:
            print(
                f"{i[0]:<12} {i[1]:<12} {i[2]:<12} {i[3]:<12} {i[4]:<12} {i[5]:<12} {i[6]:<12}"
            )
    elif n == 3:
        cursor = conn.execute("SELECT COUNT(STUDENTID) FROM STUDENT")
        for i in cursor:
            print(i)
    elif n == 4:
        cursor = conn.execute("SELECT AVG(CGPA), BRANCH FROM STUDENT GROUP BY BRANCH")
        for i in cursor:
            print(f"{i[0]:<12} {i[1]:<12}")
    elif n == 5:
        cursor = conn.execute("SELECT * FROM STUDENT")
        for i in cursor:
            print(f"{i[0]:<12}{i[1]:<12}{i[2]:<12}{i[3]:<12}")
    elif n == 6:
        break


conn.close()


# //WHERE strftime('%Y', date='2024')
