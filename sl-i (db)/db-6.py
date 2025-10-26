import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dblab"
)

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(roll INT PRIMARY KEY, name VARCHAR(50))")

while True:
    print("\n1. Add\n2. Show\n3. Update\n4. Delete\n5. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        r = int(input("Roll No: "))
        n = input("Name: ")
        cur.execute("INSERT INTO students VALUES (%s,%s)", (r,n))
        con.commit()
        print("Record Added!")

    elif ch == 2:
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)

    elif ch == 3:
        r = int(input("Roll to Update: "))
        n = input("New Name: ")
        cur.execute("UPDATE students SET name=%s WHERE roll=%s", (n,r))
        con.commit()
        print("Record Updated!")

    elif ch == 4:
        r = int(input("Roll to Delete: "))
        cur.execute("DELETE FROM students WHERE roll=%s", (r,))
        con.commit()
        print("Record Deleted!")

    elif ch == 5:
        break

    else:
        print("Invalid choice!")

con.close()
