from pathlib import Path

# Configuration
DOWNLOAD_DIR = Path("~/Desktop/musics/").expanduser()
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "192"

# YDL configuration
YDL_OPTS = {
    'format': 'bestaudio/best',
    'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',  # output
    'quiet': True,  # False it will not supress the output
    'progress_hooks': [],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # specifying the software to extract the audio
        'preferredcodec': AUDIO_FORMAT,  # type of the audio
        'preferredquality': AUDIO_QUALITY,  # quality of the audio
    }],
}
