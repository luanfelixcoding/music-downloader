def format_song_list(song_input: str) -> list:
    try:
        song_list = [song.strip().lower() for song in song_input.split(',')]
        if not song_list:
            raise ValueError("No valid song names were provided.")
        return song_list
    except Exception as unknown_error:
        raise ValueError(f"Error formatting song list: {unknown_error}")
