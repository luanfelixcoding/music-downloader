# core/config.py

from pathlib import Path

# ? Default Variables
DEFAULT_PATH = Path.home() / "Downloads"
DEFAULT_AUDIO_FORMAT = "mp3"
DEFAULT_AUDIO_QUALITY = "192"

quality_options = {
    "Best (320k)": "320",
    "Standard (192k)": "192",
    "Low (128k)": "128",
}

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': DEFAULT_PATH,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': DEFAULT_AUDIO_FORMAT,
        'preferredquality': DEFAULT_AUDIO_QUALITY,
    }],
    'noplaylist': True,
    'progress_hooks': [],
    'default_search': 'ytsearch',
    'quiet': True,
    'no_warnings': True,
}
