import pytest
from music_downloader.utils import format_song_list


def test_format_song_list_basic() -> None:
    input_data = "Song A, Song B, Song C"
    expected = ["song a", "song b", "song c"]
    assert format_song_list(input_data) == expected


def test_format_song_list_whitespace() -> None:
    input_data = "   Hello , World  ,  Test "
    expected = ["hello", "world", "test"]
    assert format_song_list(input_data) == expected


def test_format_song_list_empty() -> None:
    with pytest.raises(ValueError):
        format_song_list("")
