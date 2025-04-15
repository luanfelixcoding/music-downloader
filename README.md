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
│   ├── downloader.py        # Core downloading functionality and class
│   ├── file_manager.py      # File management utilities
│   ├── logger.py            # Centralized logging setup
│   └── utils.py             # Helper functions
├── tests/
│   ├── __init__.py          # Test package initialization
│   ├── test_downloader.py   # Unit tests for downloader.py
│   ├── test_file_manager.py # Unit tests for file_manager.py
│   └── test_utils.py        # Unit tests for utils.py
├── logs/
│   └── downloader.log       # Logs for debugging and tracking issues 
├── main.py                  # Main entry point of the application
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Installation

1. **Install FFmpeg on [oficial site](https://ffmpeg.org/download.html) or you can watch this [video](https://www.youtube.com/watch?v=4jx2_j5Seew)**
 
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/luanfelixcoding/music-downloader.git
   cd music_downloader
   ```

3. **Create and Activate a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv/Scripts/activate   # On Linux/Mac: source venv/bin/activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Update Package**:
   ```bash
   pip install -U yt-dlp
   ```

## Usage

1. **Configuration**:
   Update the `music_downloader/config.py` file to customize download settings, such as file paths and audio quality.

2. **File Management**:
   Use `file_manager.py` to organize downloaded files or clean up directories.
   
3. **Run the Main file**:
   ```bash
   python main.py
   ```

## Configuration

Modify `config.py` to adjust the following:

- **Download directory**: Path to save downloaded audio files.
- **Audio quality settings**: Set preferred audio formats or bitrate.

Example `config.py` snippet:
```python
# Configuration
DOWNLOAD_DIR = Path("~/Desktop/musics/").expanduser()
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "192"
```

## Testing

Run unit tests to ensure everything works as expected:

```bash
pytest tests/
```

Feel free to reach out if you encounter any issues or have suggestions for improvement. Happy downloading!
