# 🎓 RFID Attendance Manager

A modern desktop attendance system using RFID cards and Arduino, with a Python dashboard UI.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Hardware | Arduino Uno + MFRC522 RFID Sensor |
| Communication | Serial Port (pyserial) |
| UI | Python + CustomTkinter |
| Storage | JSON |

---

## 📁 Project Structure
RFID-Attendance-Manager/
├── arduino/
│   └── rfid_attendance/
│       └── rfid_attendance.ino
├── app/
│   ├── main.py
│   ├── storage.py
│   └── ui/
│       ├── init.py
│       ├── sidebar.py
│       ├── id_card.py
│       └── stats.py
├── .gitignore
└── README.md

---

## ⚙️ Setup and Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd RFID-Attendance-Manager
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install pyserial customtkinter
```

### 4. Create students.json in root
```json
{
    "YOUR_CARD_UID": {"name": "Student Name", "roll": "ROLL-01"}
}
```

### 5. Upload Arduino code
- Open `arduino/rfid_attendance/rfid_attendance.ino` in Arduino IDE
- Install MFRC522 library via Library Manager
- Upload to Arduino Uno

### 6. Run the app
```bash
python app/main.py
```

---

## 🔌 Arduino Wiring

| MFRC522 Pin | Arduino Pin |
|---|---|
| SDA | 10 |
| SCK | 13 |
| MOSI | 11 |
| MISO | 12 |
| RST | 9 |
| 3.3V | 3.3V |
| GND | GND |

---

## 👥 How It Works

1. Student taps RFID card on the reader
2. Arduino reads the card UID and sends it via Serial
3. Python receives the UID and looks it up in students.json
4. Student info appears on the dashboard
5. Attendance is saved to attendance.json with date and time
6. Info disappears after 3 seconds, ready for next scan

---

## 📌 Notes

- Change COM3 in main.py to your Arduino's actual COM port
- Find COM port in Device Manager → Ports (COM & LPT)
- Close Arduino IDE Serial Monitor before running the app
- students.json and attendance.json are not tracked by git for privacy
