def format_song_list(song_input: str) -> list:
    """
    Formats the input string of song names into a list.

    Args:
        song_input (str): Comma-separated song names.

    Returns:
        list: List of trimmed and lowercase song names.

    Raises:
        ValueError: If no valid song names are provided.
    """
    if not song_input or not song_input.strip():
        raise ValueError("Input cannot be empty or whitespace.")

    song_list = [song.lower().strip() for song in song_input.split(",")]

    if not song_list:
        raise ValueError("No valid song names provided after formatting.")

    return song_list
