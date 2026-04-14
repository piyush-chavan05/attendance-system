import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_students():
    path = os.path.join(BASE_DIR, "students.json")
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading students: {e}")
        return {}

def load_attendance():
    path = os.path.join(BASE_DIR, "attendance.json")
    try:
        with open(path, "r") as f:
            content = f.read()
            if not content:
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}

def save_attendance(roll, name):
    path = os.path.join(BASE_DIR, "attendance.json")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    attendance = load_attendance()
    if date not in attendance:
        attendance[date] = {}
    attendance[date][roll] = {"name": name, "time": time}
    with open(path, "w") as f:
        json.dump(attendance, f, indent=4)