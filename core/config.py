# core/config.py

from pathlib import Path

# ? Default Variables
DEFAULT_PATH = Path.home() / "Downloads"
DEFAULT_AUDIO_FORMAT = "mp3"
DEFAULT_AUDIO_QUALITY = "192"

# ? You can change to whatever you want
"""
- 320 kbps 
- 192 kbps 
- 128 kbps
- 96 kbps
- 32 kbps
- 16 kbps
"""
quality_options = {
    "Best (320k)": "320",
    "Standard (192k)": "192",
    "Low (128k)": "128",
}

# ? YDL default configuration
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
