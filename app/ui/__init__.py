import customtkinter as ctk
from datetime import datetime
from storage import load_students, save_attendance
from ui.sidebar import create_sidebar
from ui.id_card import create_id_card
from ui.stats import create_stats_panel, refresh_stats

# ── App setup ──────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Attendance Manager")
app.geometry("1000x650")
app.minsize(900, 550)

# ── Layout: Sidebar + Main ────────────────────────────────

# Sidebar (left)
sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=0,
                             fg_color="#0f0f23")
sidebar_frame.pack(side="left", fill="y")
sidebar_frame.pack_propagate(False)

sidebar_buttons = create_sidebar(sidebar_frame)

# Main content (right)
main_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="#16162b")
main_frame.pack(side="right", fill="both", expand=True)

# ── Build main content ─────────────────────────────────────

id_card_refs = create_id_card(main_frame)
stats_refs = create_stats_panel(main_frame)


# ── Show student info (called when RFID scanned) ──────────
def clear_info():
    id_card_refs["name"].configure(text="Waiting for card...")
    id_card_refs["roll"].configure(text="")
    id_card_refs["time"].configure(text="")
    id_card_refs["status"].configure(text="")


def show_student_info(uid):
    """Look up the scanned UID, update the ID card, and save attendance."""
    students = load_students()
    clear_info()
    student = students.get(uid)

    if student:
        name = student["name"]
        roll = student["roll"]
        now = datetime.now().strftime("%I:%M:%S %p")

        id_card_refs["name"].configure(text=name)
        id_card_refs["roll"].configure(text=roll)
        id_card_refs["time"].configure(text=now)
        id_card_refs["status"].configure(text="✅ Present",
                                         text_color="#00d26a")

        save_attendance(roll, name)
        refresh_stats(stats_refs)
    else:
        id_card_refs["name"].configure(text="Unknown")
        id_card_refs["roll"].configure(text="—")
        id_card_refs["time"].configure(text="—")
        id_card_refs["status"].configure(text="❌ Not Registered",
                                         text_color="#ff4444")

    app.after(3000, clear_info)