def format_song_list(song_input: str) -> list:
    """
    Formats the input string of song names into a list.

    Args:
        song_input (str): Comma-separated song names. 

    Returns:
        list: List of trimmed and lowercase song names.
    """
    try:
        song_list = [song.strip().lower() for song in song_input.split(',')]
        if not song_list:
            raise ValueError("No valid song names provided.")
        return song_list
    except Exception as unknown_error:
        raise ValueError(f"Error formatting song list: {unknown_error}")
