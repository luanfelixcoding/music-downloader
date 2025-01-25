from music_downloader.utils import format_song_list
from music_downloader.downloader import download_music
from termcolor import colored
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler('logs/downloader.log'),
        logging.StreamHandler(),
    ]
)


def main():
    """Main function to handle user input and song downloading."""
    try:
        songs = input(
            "Enter the names of the songs (comma-separated): ").strip()
        if not songs:
            raise ValueError("The song list cannot be empty")
        song_list = format_song_list(songs)
        download_music(song_list)
    except ValueError as value_error:
        print(colored(f"\nInput error: {value_error}", "light_red"))
    except KeyboardInterrupt:
        print(colored("\nProgram finished by the user", "light_red"))
    except Exception as unknown_error:
        print(colored(f"\nAn unexpected error occurred: {
              unknown_error}", "light_red"))


if __name__ == "__main__":
    main()
