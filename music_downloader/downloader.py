from .config import YDL_OPTS, DOWNLOAD_DIR
from .file_manager import ensure_folder_exists
from .logger import setup_logger
from yt_dlp import YoutubeDL, utils
import asyncio

logger = setup_logger()


class MusicDownloader():
    """Handles downloading music using yt_dlp"""

    def __init__(self) -> None:
        self.ydl_opts = {**YDL_OPTS, 'progress_hooks': [self.progress_hook]}

    @staticmethod
    def progress_hook(d: dict) -> None:
        """Display download progress"""
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get(
                'total_bytes_estimated', 0)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            eta = d.get('eta', 0)

            try:
                if total_bytes > 0:
                    percent = (downloaded_bytes / total_bytes) * 100
                    eta = d.get('eta')
                    eta_display = f"{eta:.2f}s" if isinstance(eta, (int, float)) else "N/A"
                    
                    print(f"\rProgress: {percent:.2f}% ETA: {eta_display}s", end="")
            except Exception as calculation_error:
                logger.warning(f"Error in progress calculation: {calculation_error}")

        elif d['status'] == 'finished':
            print("\nDownload Complete!")

    async def download_song(self, song: str) -> None:
        """
        Downloads a single song.

        Args:
            song (str) : song provided by the user.
        """
        ensure_folder_exists(DOWNLOAD_DIR)
        logger.info(f"Starting download: {song}")

        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                await asyncio.to_thread(ydl.download, [f"ytsearch:{song}"])
                logger.info(f"Downloaded: '{song}'")
        except utils.DownloadError as de:
            logger.error(f"Error Downloading '{song}' : {de}")
        except utils.DownloadCancelled as dc:
            logger.error(f"Cancelled by the user : {dc}")
        except Exception as unknown_error:
            logger.error(f"Unexpected error : {unknown_error}")

    async def download_songs(self, songs: list) -> None:
        """
        Downloads multiple songs asynchronously.

        Args:
            songs (list) : song list provided by the user.
        """
        tasks = [self.download_song(song) for song in songs]
        await asyncio.gather(*tasks)
