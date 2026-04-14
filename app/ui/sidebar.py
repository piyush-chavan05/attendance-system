import customtkinter as ctk


def create_sidebar(parent):
    """Create the left sidebar with logo and navigation buttons."""

    # App name / logo
    logo_label = ctk.CTkLabel(parent, text="📋 Attendance\n   Manager",
                              font=("Arial", 20, "bold"),
                              text_color="#3085e0")
    logo_label.pack(pady=(30, 5))

    # Subtle tagline
    tagline = ctk.CTkLabel(parent, text="RFID-based tracking",
                           font=("Arial", 10),
                           text_color="#555555")
    tagline.pack(pady=(0, 25))

    # Separator
    sep = ctk.CTkFrame(parent, height=1, fg_color="#2a2a4a")
    sep.pack(fill="x", padx=15, pady=(0, 15))

    # Navigation buttons
    buttons = {}

    dashboard_btn = ctk.CTkButton(parent, text="  📊  Dashboard",
                                  fg_color="#3085e0",
                                  hover_color="#2570c0",
                                  anchor="w",
                                  height=38,
                                  corner_radius=8,
                                  font=("Arial", 14))
    dashboard_btn.pack(fill="x", padx=10, pady=3)
    buttons["dashboard"] = dashboard_btn

    students_btn = ctk.CTkButton(parent, text="  👥  Students",
                                 fg_color="transparent",
                                 hover_color="#2a2a4a",
                                 anchor="w",
                                 height=38,
                                 corner_radius=8,
                                 font=("Arial", 14))
    students_btn.pack(fill="x", padx=10, pady=3)
    buttons["students"] = students_btn

    records_btn = ctk.CTkButton(parent, text="  📋  Records",
                                fg_color="transparent",
                                hover_color="#2a2a4a",
                                anchor="w",
                                height=38,
                                corner_radius=8,
                                font=("Arial", 14))
    records_btn.pack(fill="x", padx=10, pady=3)
    buttons["records"] = records_btn

    return buttons