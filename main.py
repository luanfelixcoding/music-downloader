from music_downloader.utils import format_song_list
from music_downloader.downloader import download_music


def main():
    songs = input("Enter the names of the songs (comma-separated): ")
    song_list = format_song_list(songs)
    download_music(song_list)


if __name__ == "__main__":
    main()
