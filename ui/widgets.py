# ui/widgets.py

import customtkinter as ctk


def create_input_frame(parent):
    """Creates the main frame for song input."""
    main_frame = ctk.CTkFrame(parent, corner_radius=15)
    main_frame.grid(row=0, column=0, padx=90, pady=20, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=1)

    title_label = ctk.CTkLabel(
        main_frame, text="Music Downloader", font=ctk.CTkFont(size=28, weight="bold"))
    title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))

    song_entry = ctk.CTkEntry(
        main_frame, placeholder_text="Enter Song Name or YouTube URL", height=40, font=ctk.CTkFont(size=14))
    song_entry.grid(row=1, column=0, columnspan=3,
                    padx=20, pady=10, sticky="ew")
    return song_entry


def create_settings_frame(parent, path_var, path_command):
    """Creates the frame for download settings (format, quality, path)."""
    settings_frame = ctk.CTkFrame(parent, corner_radius=15)
    settings_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    settings_frame.grid_columnconfigure((0, 1, 2), weight=1)

    # ? Audio Format
    format_label = ctk.CTkLabel(
        settings_frame, text="Audio Format:", font=ctk.CTkFont(slant="roman", size=15))
    format_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    format_menu = ctk.CTkOptionMenu(settings_frame, values=[
                                    "mp3", "m4a", "wav", "flac"], font=ctk.CTkFont(size=13))
    format_menu.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    # ? Audio Quality
    quality_label = ctk.CTkLabel(
        settings_frame, text="Audio Quality:", font=ctk.CTkFont(size=15))
    quality_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    quality_menu = ctk.CTkOptionMenu(settings_frame, values=[
                                     "Best (320k)", "Standard (192k)", "Low (128k)"], font=ctk.CTkFont(size=13))
    quality_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    # ? Download Path
    path_button = ctk.CTkButton(settings_frame, text="Choose Download Folder",
                                command=path_command, font=ctk.CTkFont(size=14))
    path_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
    path_label = ctk.CTkLabel(settings_frame, textvariable=path_var, font=ctk.CTkFont(
        size=12), wraplength=300, justify="center")
    path_label.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

    return format_menu, quality_menu, path_label


def create_action_buttons(parent, download_cmd, batch_cmd):
    """Creates the main action buttons for downloading."""
    action_frame = ctk.CTkFrame(parent, corner_radius=15)
    action_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
    action_frame.grid_columnconfigure((0, 1), weight=1)

    download_button = ctk.CTkButton(action_frame, text="Download Song", height=45,
                                    command=download_cmd, font=ctk.CTkFont(size=16, weight="bold"))
    download_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    batch_button = ctk.CTkButton(action_frame, text="Download from File (.txt, .xlsx)",
                                 height=45, font=ctk.CTkFont(size=15), command=batch_cmd, fg_color="#4a4a4a", hover_color="#555555")
    batch_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    return download_button, batch_button


def create_status_frame(parent):
    """Creates the frame for the status log and progress bar."""
    status_frame = ctk.CTkFrame(parent, corner_radius=15)
    status_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
    status_frame.grid_columnconfigure(0, weight=1)
    status_frame.grid_rowconfigure(0, weight=1)

    status_log = ctk.CTkTextbox(status_frame, font=ctk.CTkFont(
        size=13), wrap="word", state="disabled", corner_radius=10)
    status_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    progress_bar = ctk.CTkProgressBar(parent, orientation="horizontal")
    progress_bar.set(0)
    progress_bar.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")

    return status_log, progress_bar
