from unittest.mock import patch, MagicMock
from music_downloader.downloader import MusicDownloader
from music_downloader.file_manager import ensure_folder_exists
from pathlib import Path
import pytest
