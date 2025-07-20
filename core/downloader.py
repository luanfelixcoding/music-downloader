# core/downloader.py

import yt_dlp

from pathlib import Path
from .config import ydl_opts, quality_options


class Downloader:
    """Class to acquire all the download logic. Central class."""

    def __init__(self, songs, settings, progress_callback, log_callback, completion_callback):
        self.songs = songs
        self.settings = settings
        self.progress_callback = progress_callback
        self.log_callback = log_callback
        self.completion_callback = completion_callback
        self.current_filename = ""

    def progress_hook(self, d):
        """Hook for yt-dlp to report progress."""
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                progress = d['downloaded_bytes'] / total_bytes
                self.progress_callback(progress)
        elif d['status'] == 'finished':
            self.current_filename = d.get('filename', '')
            self.progress_callback(1)  # ? Ensures bar is full on completion
            self.log_callback(
                f"Processing '{Path(self.current_filename).name}'...")

    def start(self):
        """Configures yt-dlp and starts the download loop."""
        audio_quality = quality_options.get(self.settings['quality'])
        audio_format = self.settings['format']

        download_path_template = Path(
            self.settings['path']) / '%(title)s.%(ext)s'

        ydl_opts['outtmpl'] = str(download_path_template)

        ydl_opts['postprocessors'][0]['preferredquality'] = audio_quality
        ydl_opts['postprocessors'][0]['preferredcodec'] = audio_format
        ydl_opts['progress_hooks'] = [self.progress_hook]

        total_songs = len(self.songs)
        for i, song in enumerate(self.songs):
            self.log_callback(
                f"({i+1}/{total_songs}) Searching for '{song}'...")
            self.progress_callback(0)  # ? Reset for new song
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([song])
                self.log_callback(f"SUCCESS: Download complete for '{song}'!")
            except yt_dlp.utils.DownloadError:
                self.log_callback(
                    f"ERROR downloading '{song}': Could not find song. Please try a more specific name or a direct URL.")
            except Exception as e:
                self.log_callback(f"FATAL ERROR downloading '{song}': {e}")

        # ? Signal completion
        self.completion_callback()


if __name__ == '__main__':
    downloader = Downloader()
    downloader.start()
