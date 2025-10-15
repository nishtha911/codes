from db_connection import get_connection

def add_course(course_name, department, credits, max_students):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Course (course_name, department, credits, max_students) VALUES (%s, %s, %s, %s)",
                   (course_name, department, credits, max_students))
    conn.commit()
    conn.close()

def remove_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Course WHERE course_id=%s", (course_id,))
    conn.commit()
    conn.close()

def update_course(course_id, name, department, credits, max_students):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Course
        SET course_name=%s, department=%s, credits=%s, max_students=%s
        WHERE course_id=%s
    """, (name, department, credits, max_students, course_id))
    conn.commit()
    conn.close()

def view_all_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, s.email, c.course_name, c.department, e.enroll_date
        FROM Enrollment e
        JOIN Student s ON e.student_id = s.student_id
        JOIN Course c ON e.course_id = c.course_id
    """)
    data = cursor.fetchall()
    conn.close()
    return data
