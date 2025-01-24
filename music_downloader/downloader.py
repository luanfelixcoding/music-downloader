from .config import YDL_OPTS, DOWNLOAD_DIR
from .file_manager import ensure_folder_exists
from termcolor import colored
import yt_dlp
import logging

logger = logging.getLogger(__name__)


def progress_hook(d: dict) -> None:
    """Handles download progress."""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', d.get('total_bytes_estimate', 0))
        downloaded_bytes = d.get('downloaded_bytes', 0)
        speed = d.get('speed', 0)
        eta = d.get('eta', 0)

        try:
            if total_bytes > 0:
                percent = (downloaded_bytes / total_bytes) * 100
                print(f"\rProgress: {percent:.2f}, Speed: {
                    speed / 1024:.2f} KB/s, ETA: {eta:.2f} seconds", end="")
            else:
                print("\rProgress: Calculating...", end="")
        except Exception as calculation_error:
            logger.warning(f"Error in progress calculation: {
                           calculation_error}")

    elif d['status'] == 'finished':
        print("\nDownload Complete!")


def download_music(song_names: list) -> None:
    """
    Downloads a list of songs using yt_dlp

    Args:
        song_names (list): List of song names to download
    """
    ensure_folder_exists(DOWNLOAD_DIR)

    # Add progress hooks dynamically
    ydl_opts_with_hooks = {**YDL_OPTS, 'progress_hooks': [progress_hook]}

    for song in song_names:
        try:
            logger.info(f"Starting download for '{song}'...")
            yt_search = f"ytsearch:{song}"
            with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
                ydl.download([yt_search])
                logger.info(f"'{song}' downloaded successfully!")
        except yt_dlp.utils.DownloadError as download_error:
            logger.error(f"Failed to download '{song}' : {download_error}")
        except Exception as unknown_error:
            logger.error(f"Unexpected error while downloading '{
                         song}' : {unknown_error}")
