from music_downloader.utils import format_song_list
from music_downloader.downloader import MusicDownloader
from music_downloader.logger import setup_logger
from termcolor import colored
import asyncio

logger = setup_logger()


async def main() -> None:
    """Main entry point of the application"""
    try:
        songs = input("Enter song names separated by commas (e.g., Shape of You, Blinding Lights):\n> ").strip()
        if not songs:
            raise ValueError("No songs provided")
        song_list = format_song_list(songs)
        downloader = MusicDownloader()
        await downloader.download_songs(song_list)
    except ValueError as ve:
        logger.error(ve)
        print(colored(f"Error: {ve}", "light_red"))
    except KeyboardInterrupt:
        logger.info("Program interrupted by user.")
        print(colored(f"Program interrupted by user.", "light_yellow"))
    except Exception as unknown_error:
        logger.error(f"Unexpected error: {unknown_error}")
        print(colored(f"Unexpected error: {unknown_error}", "light_red"))


if __name__ == '__main__':
    asyncio.run(main())
