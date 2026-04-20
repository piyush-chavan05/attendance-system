import threading
from ui import app, show_student_info

def read_serial():
    import serial
    try:
        ser = serial.Serial("COM5", 9600)
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                app.after(0, lambda uid=line: show_student_info(uid))
    except Exception as e:
        print(f"Serial error: {e}")

t = threading.Thread(target=read_serial)
t.daemon = True
t.start()


app.mainloop()