import tkinter as tk
from tkinter import messagebox
import student_functions as sf
import admin_functions as af

# ---------- LOGIN WINDOW ----------
def login_window():
    win = tk.Tk()
    win.title("Student Enrollment Management System")
    win.geometry("400x300")

    tk.Label(win, text="Email").pack()
    email_entry = tk.Entry(win)
    email_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def login_student_func():
        student = sf.login_student(email_entry.get(), password_entry.get())
        if student:
            win.destroy()
            student_dashboard(student[0], student[1])
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(win, text="Login as Student", command=login_student_func).pack(pady=5)

    def login_admin_func():
        if email_entry.get() == "admin" and password_entry.get() == "admin":
            win.destroy()
            admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Admin Credentials")

    tk.Button(win, text="Login as Admin", command=login_admin_func).pack(pady=5)

    tk.Button(win, text="Register as Student", command=lambda: register_window(win)).pack(pady=5)
    win.mainloop()

# ---------- REGISTER WINDOW ----------
def register_window(parent):
    reg_win = tk.Toplevel(parent)
    reg_win.title("Student Registration")
    reg_win.geometry("400x300")

    tk.Label(reg_win, text="Name").pack()
    name_entry = tk.Entry(reg_win)
    name_entry.pack()

    tk.Label(reg_win, text="Email").pack()
    email_entry = tk.Entry(reg_win)
    email_entry.pack()

    tk.Label(reg_win, text="Password").pack()
    pass_entry = tk.Entry(reg_win, show="*")
    pass_entry.pack()

    def register_func():
        if sf.register_student(name_entry.get(), email_entry.get(), pass_entry.get()):
            messagebox.showinfo("Success", "Registration Successful!")
            reg_win.destroy()
        else:
            messagebox.showerror("Error", "Email already exists")

    tk.Button(reg_win, text="Register", command=register_func).pack(pady=10)

# ---------- STUDENT DASHBOARD ----------
def student_dashboard(student_id, student_name):
    dash = tk.Tk()
    dash.title(f"Student Dashboard - {student_name}")
    dash.geometry("600x500")

    def load_courses():
        courses = sf.view_courses()
        course_list.delete(0, tk.END)
        for c in courses:
            course_list.insert(tk.END, f"{c[0]} - {c[1]} ({c[2]}, Credits: {c[3]})")

    def enroll_func():
        selected = course_list.get(course_list.curselection())
        course_id = int(selected.split(" - ")[0])
        if sf.enroll_course(student_id, course_id):
            messagebox.showinfo("Success", "Enrolled Successfully!")
            load_enrolled_courses()
        else:
            messagebox.showerror("Error", "Already Enrolled!")

    def drop_func():
        selected = enrolled_list.get(enrolled_list.curselection())
        course_id = int(selected.split(" - ")[0])
        sf.drop_enrollment(student_id, course_id)
        messagebox.showinfo("Success", "Course Dropped!")
        load_enrolled_courses()

    def load_enrolled_courses():
        enrolled_courses = sf.view_enrolled_courses(student_id)
        enrolled_list.delete(0, tk.END)
        for e in enrolled_courses:
            enrolled_list.insert(tk.END, f"{e[0]} - {e[1]} ({e[2]}, Credits: {e[3]})")

    tk.Label(dash, text="Available Courses").pack()
    course_list = tk.Listbox(dash, width=70)
    course_list.pack()
    tk.Button(dash, text="Enroll Selected Course", command=enroll_func).pack(pady=5)
    tk.Button(dash, text="Refresh Course List", command=load_courses).pack(pady=5)

    tk.Label(dash, text="Your Enrolled Courses").pack()
    enrolled_list = tk.Listbox(dash, width=70)
    enrolled_list.pack()
    tk.Button(dash, text="Drop Selected Course", command=drop_func).pack(pady=5)
    tk.Button(dash, text="Refresh Enrolled Courses", command=load_enrolled_courses).pack(pady=5)

    load_courses()
    load_enrolled_courses()
    dash.mainloop()

# ---------- ADMIN DASHBOARD ----------
def admin_dashboard():
    admin = tk.Tk()
    admin.title("Admin Dashboard")
    admin.geometry("700x500")

    tk.Label(admin, text="Course Name").pack()
    name_entry = tk.Entry(admin)
    name_entry.pack()

    tk.Label(admin, text="Department").pack()
    dept_entry = tk.Entry(admin)
    dept_entry.pack()

    tk.Label(admin, text="Credits").pack()
    credits_entry = tk.Entry(admin)
    credits_entry.pack()

    tk.Label(admin, text="Max Students").pack()
    max_entry = tk.Entry(admin)
    max_entry.pack()

    def add_course_func():
        af.add_course(name_entry.get(), dept_entry.get(), int(credits_entry.get()), int(max_entry.get()))
        messagebox.showinfo("Success", "Course Added!")

    tk.Button(admin, text="Add Course", command=add_course_func).pack(pady=5)

    def view_enrollments_func():
        data = af.view_all_enrollments()
        enroll_list.delete(0, tk.END)
        for d in data:
            enroll_list.insert(tk.END, f"{d[0]} ({d[1]}) -> {d[2]} [{d[3]}] on {d[4]}")

    tk.Button(admin, text="View All Enrollments", command=view_enrollments_func).pack(pady=5)
    enroll_list = tk.Listbox(admin, width=100)
    enroll_list.pack()

    admin.mainloop()

# Start app
login_window()
