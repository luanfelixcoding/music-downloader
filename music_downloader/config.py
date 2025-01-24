DOWNLOAD_DIR = "~/Desktop/musics/"
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "192"
LOG_LEVEL = "INFO"


def progress_hook(d):
    """Handles progress updates for downloads."""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', d.get('total_bytes_estimate', 0))
        downloaded_bytes = d.get('downloaded_bytes', 0)
        speed = d.get('speed', 0)
        eta = d.get('eta', 0)

        if total_bytes > 0:
            percent = (downloaded_bytes / total_bytes) * 100
            print(f"\rProgress: {percent:.2f}, Speed: {
                speed / 1024:.2f} KB/s, ETA: {eta:.2f} seconds", end="")
        else:
            print("\rProgress: Calculating...", end="")

    elif d['status'] == 'finished':
        print("\nDownload Complete!")


YDL_OPTS = {
    'format': 'bestaudio/best',
    'outtmpl': f'{DOWNLOAD_DIR}%(title)s.%(ext)s',  # output
    'quiet': True,  # False it will not supress the output
    'progress_hooks': [progress_hook],  # the progress bar
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # specifying the software to extract the audio
        'preferredcodec': AUDIO_FORMAT,  # type of the audio
        'preferredquality': AUDIO_QUALITY,  # quality of the audio
    }],
}
