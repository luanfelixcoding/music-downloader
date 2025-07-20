# ui/app.py

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

from pathlib import Path
from .widgets import create_input_frame, create_settings_frame, create_action_buttons, create_status_frame
from core.downloader import Downloader
from utils.file_handler import read_song_list


class MusicDownloaderApp(ctk.CTk):
    """Class to handle UI, user interactions, and download logic."""

    def __init__(self):
        super().__init__()

        # ? Window Setup
        self.title("Music Downloader")
        # * To center the window in case if you want
        # self.center_window()
        self.geometry("1000x600")

        # ? Theme and appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ? State Variables
        self.download_path = tk.StringVar(
            value=Path.home() / "Downloads")
        self.download_in_progress = False

        # ? Initialize UI Components from widgets module
        self.create_widgets()

    def center_window(self):
        """Centers the application window on the screen."""
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        """Creates and arranges all the UI widgets in the main window."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # ? Using helper functions from ui.widgets to create frames
        self.song_entry = create_input_frame(self)
        self.format_menu, self.quality_menu, self.path_label = create_settings_frame(
            self, self.download_path, self.select_path)
        self.download_button, self.batch_button = create_action_buttons(
            self, self.start_single_download, self.start_batch_download)
        self.status_log, self.progress_bar = create_status_frame(self)

        self.log_message("Welcome! Ready to download some music...")

    def select_path(self):
        """Opens a dialog to select the download directory."""
        path = filedialog.askdirectory(initialdir=self.download_path.get())
        if path:
            self.download_path.set(path)
            self.log_message(f"Download path set to: {path}")

    def log_message(self, message):
        """Adds a message to the status log in a thread-safe way."""
        def _log():
            self.status_log.configure(state="normal")
            self.status_log.insert("end", f"{message}\n\n")
            self.status_log.configure(state="disabled")
            self.status_log.see("end")
        # Use after() to ensure UI updates happen on the main thread
        self.after(0, _log)

    def update_progress(self, progress_value):
        """Updates the progress bar in a thread-safe way."""
        self.after(0, lambda: self.progress_bar.set(progress_value))

    def set_ui_state(self, enabled):
        """Enables or disables UI elements during download."""
        state = "normal" if enabled else "disabled"
        self.download_button.configure(state=state)
        self.batch_button.configure(state=state)
        self.song_entry.configure(state=state)
        self.format_menu.configure(state=state)
        self.quality_menu.configure(state=state)
        self.download_in_progress = not enabled

    def start_single_download(self):
        """Validates input and initiates a single song download."""
        if self.download_in_progress:
            messagebox.showwarning(
                "Busy", "A download is already in progress.")
            return

        song_input = self.song_entry.get()
        if not song_input:
            messagebox.showerror("Error", "Please enter a song name or URL.")
            return

        self.run_download([song_input])

    def start_batch_download(self):
        """Handles the process of selecting and reading a file for batch download."""
        if self.download_in_progress:
            messagebox.showwarning(
                "Busy", "A download is already in progress.")
            return

        file_path = filedialog.askopenfilename(
            title="Select Song List File",
            filetypes=[("Text files", "*.txt"), ("Excel files", "*.xlsx")]
        )
        if not file_path:
            return

        try:
            songs = read_song_list(file_path)
            if not songs:
                messagebox.showinfo(
                    "Info", "The selected file is empty or contains no song names.")
                return
            self.run_download(songs, Path(file_path).name)
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read the file: {e}")
            self.log_message(f"ERROR: Failed to read file {file_path}.")

    def run_download(self, songs, batch_filename=None):
        """
        Configures and starts the download thread.
        """
        self.set_ui_state(False)
        self.progress_bar.set(0)

        if batch_filename:
            self.log_message(f"Starting batch download from: {batch_filename}")
        else:
            self.log_message(f"Starting download for: {songs[0]}")

        # --- Get settings from UI ---
        settings = {
            "format": self.format_menu.get(),
            "quality": self.quality_menu.get(),
            "path": self.download_path.get()
        }

        # --- Create downloader instance ---
        downloader = Downloader(
            songs=songs,
            settings=settings,
            progress_callback=self.update_progress,
            log_callback=self.log_message,
            completion_callback=self.on_download_complete
        )

        # --- Run download in a separate thread ---
        download_thread = threading.Thread(target=downloader.start)
        download_thread.start()

    def on_download_complete(self):
        """Callback function to run when the download process is finished."""
        self.log_message("All downloads completed!")
        messagebox.showinfo("Success", "All songs have been downloaded!")
        self.set_ui_state(True)
        self.progress_bar.set(0)
