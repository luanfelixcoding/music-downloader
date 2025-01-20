import yt_dlp
from .config import YDL_OPTS
from .file_manager import ensure_folder_exists
from termcolor import colored


def download_music(song_names: list) -> None:
    folder_name = "musics"
    ensure_folder_exists(folder_name)

    for song in song_names:
        try:
            print(f"\nDownloading {song}")
            yt_search = f"ytsearch:{song}"
            with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
                ydl.download([yt_search])
                print(colored(f"'{song.capitalize()}' downloaded and converted to .mp3 inside the '{
                    folder_name}' folder!", "light_blue"))
        except ConnectionError:
            print(f"Network error while downloading {
                  song}. Please check your connection.")
        except FileNotFoundError:
            print(f"Error: The file or path for {song} could not be found.")
        except Exception as unknow_error:
            print(f"An error occurred while downloading {
                  song}: {unknow_error}")
