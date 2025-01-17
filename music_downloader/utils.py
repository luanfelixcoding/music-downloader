def format_song_list(song_input: str) -> list:
    return [song.strip().lower() for song in song_input.split(',')]
