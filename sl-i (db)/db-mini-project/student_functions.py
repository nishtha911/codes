from db_connection import get_connection
import datetime

def register_student(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Student (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_student(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name FROM Student WHERE email=%s AND password=%s", (email, password))
    result = cursor.fetchone()
    conn.close()
    return result

def view_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    conn.close()
    return courses

def enroll_course(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Enrollment WHERE student_id=%s AND course_id=%s", (student_id, course_id))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return False
    cursor.execute("INSERT INTO Enrollment (student_id, course_id, enroll_date) VALUES (%s, %s, %s)",
                   (student_id, course_id, datetime.date.today()))
    conn.commit()
    conn.close()
    return True

def drop_enrollment(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enrollment WHERE student_id=%s AND course_id=%s", (student_id, course_id))
    conn.commit()
    conn.close()

def view_enrolled_courses(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.course_id, c.course_name, c.department, c.credits
        FROM Course c
        JOIN Enrollment e ON c.course_id = e.course_id
        WHERE e.student_id=%s
    """, (student_id,))
    data = cursor.fetchall()
    conn.close()
    return data
