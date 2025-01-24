# Music Downloader

Music Downloader is a Python-based tool for downloading music from YouTube using the `yt_dlp` program. This project simplifies the process of downloading and organizing audio files, providing features like file management, configuration customization, and utility functions for seamless integration.

## Features

- Download high-quality audio from YouTube.
- Customizable download settings through `config.py`.
- Organize downloaded files using the `file_manager.py` module.
- Unit tests included for downloader and file management functionalities.
- Lightweight and easy-to-use.

## Project Structure

```
music_downloader/
├── music_downloader/
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Configuration settings
│   ├── downloader.py        # Core downloading functionality
│   ├── file_manager.py      # File management utilities
│   └── utils.py             # Helper functions
├── tests/
│   ├── __init__.py          # Test package initialization
│   ├── test_downloader.py   # Unit tests for downloader.py
│   └── test_file_manager.py # Unit tests for file_manager.py
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── main.py                   # Main Package to run the script
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/luanfelixcoding/music-downloader.git
   cd music_downloader
   ```

2. **Create and Activate a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv/Scripts/activate   # On Linux/Mac: source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configuration**:
   Update the `music_downloader/config.py` file to customize download settings, such as file paths and audio quality.

2. **Run the Main file**:
   ```bash
   python main.py
   ```

3. **File Management**:
   Use `file_manager.py` to organize downloaded files or clean up directories.

## Configuration

Modify `config.py` to adjust the following:

- **Download directory**: Path to save downloaded audio files.
- **Audio quality settings**: Set preferred audio formats or bitrate.
- **Logging options**: Configure logging levels and output locations.

Example `config.py` snippet:
```python
DOWNLOAD_DIR = "downloads/"
AUDIO_FORMAT = "mp3"
LOG_LEVEL = "INFO"
```

## Testing

Run unit tests to ensure everything works as expected:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you encounter any issues or have suggestions for improvement. Happy downloading!
