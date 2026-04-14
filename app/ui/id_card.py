import customtkinter as ctk


def create_id_card(parent):
    """Create the ID card display panel in the main content area."""

    # Main card frame with rounded corners
    card_frame = ctk.CTkFrame(parent, corner_radius=15,
                              fg_color="#1a1a2e", border_width=2,
                              border_color="#3085e0")
    card_frame.pack(pady=30, padx=40, fill="x")

    # Title bar
    title_label = ctk.CTkLabel(card_frame, text="🪪  Student ID Card",
                               font=("Arial", 18, "bold"),
                               text_color="#3085e0")
    title_label.pack(pady=(20, 15))

    # Divider
    divider = ctk.CTkFrame(card_frame, height=2, fg_color="#3085e0",
                           corner_radius=0)
    divider.pack(fill="x", padx=20, pady=(0, 20))

    # Content row: photo + info
    content_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
    content_frame.pack(padx=50, pady=(0, 25), fill="x")
    content_frame.columnconfigure(1, weight=1)

    # --- Photo placeholder ---
    
    photo_frame = ctk.CTkFrame(content_frame, width=150, height=200,
                               corner_radius=12, fg_color="#2a2a4a",
                               border_width=1, border_color="#3085e0")
    photo_frame.grid(row=0, column=0, padx=(0, 25), sticky="n")
    photo_frame.pack_propagate(False)


    photo_icon = ctk.CTkLabel(photo_frame, text="👤",
                              font=("Arial", 100))
    photo_icon.place(relx=0.5, rely=0.5, anchor="center")

    # --- Info fields ---
    info_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    info_frame.grid(row=0, column=1, sticky="nsew")

    # Name row
    name_label_key = ctk.CTkLabel(info_frame, text="Name",
                                  font=("Arial", 18),
                                  text_color="#888888")
    name_label_key.pack(anchor="w")
    name_label_val = ctk.CTkLabel(info_frame, text="—",
                                  font=("Arial", 24, "bold"),
                                  text_color="#ffffff")
    name_label_val.pack(anchor="w", pady=(0, 10))

    # Roll row
    roll_label_key = ctk.CTkLabel(info_frame, text="Roll No.",
                                  font=("Arial", 18),
                                  text_color="#888888")
    roll_label_key.pack(anchor="w")
    roll_label_val = ctk.CTkLabel(info_frame, text="—",
                                  font=("Arial", 20),
                                  text_color="#cccccc")
    roll_label_val.pack(anchor="w", pady=(0, 10))

    # Time row
    time_label_key = ctk.CTkLabel(info_frame, text="Scanned At",
                                  font=("Arial", 18),
                                  text_color="#888888")
    time_label_key.pack(anchor="w")
    time_label_val = ctk.CTkLabel(info_frame, text="—",
                                  font=("Arial", 20),
                                  text_color="#cccccc")
    time_label_val.pack(anchor="w", pady=(0, 10))

    # Status row
    status_label_key = ctk.CTkLabel(info_frame, text="Status",
                                    font=("Arial", 18),
                                    text_color="#888888")
    status_label_key.pack(anchor="w")
    status_label_val = ctk.CTkLabel(info_frame, text="Waiting for scan...",
                                    font=("Arial", 20, "bold"),
                                    text_color="#666666")
    status_label_val.pack(anchor="w")

    # Return references so we can update them
    return {
        "name": name_label_val,
        "roll": roll_label_val,
        "time": time_label_val,
        "status": status_label_val,
    }
