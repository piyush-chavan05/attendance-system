import customtkinter as ctk
from storage import load_students, save_attendance
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Attendance Manager")
app.geometry("800x600")

title = ctk.CTkLabel(app, text="Attendance Manager", font=("Times New Roman", 32, "bold"), text_color="#3085e0")
title.pack(pady=20)

info_frame = ctk.CTkFrame(app, width=400, height=300, corner_radius=15)
info_frame.pack(expand=True)
info_frame.pack_propagate(False)

name_label = ctk.CTkLabel(info_frame, text="", font=("Arial", 20, "bold"))
name_label.pack(pady=10)
roll_label = ctk.CTkLabel(info_frame, text="", font=("Arial", 16))
roll_label.pack(pady=5)
time_label = ctk.CTkLabel(info_frame, text="", font=("Arial", 16))
time_label.pack(pady=5)
status_label = ctk.CTkLabel(info_frame, text="", font=("Arial", 16))
status_label.pack(pady=5)

students = load_students()
print(f"Students loaded: {students}")

def clear_info():
    name_label.configure(text="")
    roll_label.configure(text="")
    time_label.configure(text="")
    status_label.configure(text="")

def show_student_info(uid):
    student = students.get(uid)
    if student:
        current_time = datetime.now().strftime("%H:%M:%S")
        name_label.configure(text=f"Name: {student['name']}")
        roll_label.configure(text=f"Roll: {student['roll']}")
        time_label.configure(text=f"Time: {current_time}")
        status_label.configure(text="Status: PRESENT")
        save_attendance(student['roll'], student['name'])
    else:
        name_label.configure(text="Unknown Card")
        roll_label.configure(text="")
        time_label.configure(text="")
        status_label.configure(text="")
    app.after(3000, clear_info)