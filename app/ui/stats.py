import customtkinter as ctk
from datetime import datetime
from storage import load_attendance


def create_stats_panel(parent):
    """Create the 'Today's Attendance' stats panel below the ID card."""

    # Section header
    header_frame = ctk.CTkFrame(parent, fg_color="transparent")
    header_frame.pack(fill="x", padx=40, pady=(10, 5))

    title = ctk.CTkLabel(header_frame, text="📅  Today's Attendance",
                         font=("Arial", 16, "bold"),
                         text_color="#3085e0")
    title.pack(side="left")

    count_label = ctk.CTkLabel(header_frame, text="0 Present",
                               font=("Arial", 14),
                               text_color="#888888")
    count_label.pack(side="right")

    # Scrollable list frame
    list_frame = ctk.CTkScrollableFrame(parent, fg_color="#1a1a2e",
                                        corner_radius=12,
                                        border_width=1,
                                        border_color="#2a2a4a")
    list_frame.pack(fill="both", expand=True, padx=40, pady=(5, 20))

    # Store references for refresh
    refs = {
        "count_label": count_label,
        "list_frame": list_frame,
    }

    # Initial load
    refresh_stats(refs)

    return refs


def refresh_stats(refs):
    """Reload today's attendance data and update the list."""
    list_frame = refs["list_frame"]
    count_label = refs["count_label"]

    # Clear existing rows
    for widget in list_frame.winfo_children():
        widget.destroy()

    attendance = load_attendance()
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = attendance.get(today, {})

    count = len(today_data)
    count_label.configure(text=f"{count} Present")

    if count == 0:
        empty = ctk.CTkLabel(list_frame,
                             text="No attendance recorded yet today.",
                             font=("Arial", 13),
                             text_color="#666666")
        empty.pack(pady=20)
        return

    for roll, info in today_data.items():
        row = ctk.CTkFrame(list_frame, fg_color="#2a2a4a",
                           corner_radius=10, height=45)
        row.pack(fill="x", padx=5, pady=3)
        row.pack_propagate(False)

        # Status icon
        icon = ctk.CTkLabel(row, text="✅", font=("Arial", 16))
        icon.pack(side="left", padx=(15, 8))

        # Name
        name = ctk.CTkLabel(row, text=info["name"],
                            font=("Arial", 14, "bold"),
                            text_color="#ffffff")
        name.pack(side="left")

        # Roll
        roll_lbl = ctk.CTkLabel(row, text=f"({roll})",
                                font=("Arial", 12),
                                text_color="#888888")
        roll_lbl.pack(side="left", padx=(8, 0))

        # Time (right-aligned)
        time_str = info["time"]
        try:
            t = datetime.strptime(time_str, "%H:%M:%S")
            time_display = t.strftime("%I:%M %p")
        except ValueError:
            time_display = time_str

        time_lbl = ctk.CTkLabel(row, text=time_display,
                                font=("Arial", 13),
                                text_color="#3085e0")
        time_lbl.pack(side="right", padx=(0, 15))
