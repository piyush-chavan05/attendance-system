import threading
from ui import app, show_student_info

def read_serial():
    import serial
    try:
        ser = serial.Serial("COM3", 9600)
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                app.after(0, lambda uid=line: show_student_info(uid))
    except Exception as e:
        print(f"Serial error: {e}")

t = threading.Thread(target=read_serial)
t.daemon = True
t.start()

# test line - remove after hardware is connected
app.after(1000, lambda: show_student_info("46e10a2957980"))

app.mainloop()