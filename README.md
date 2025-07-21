# Music Downloader

Music Downloader is a Python-based tool for downloading music from YouTube using the `yt-dlp` library. This project simplifies the process of downloading and organizing audio files, providing features like file management, configuration customization, and utility functions.

## Features
- Project initialized and maintained with **UV** for fast and reliable dependencies.
- Modern Graphic User Interface (GUI) developed with `CustomTkinter` for a modern, lightweight and responsive visual experience.
- Able to choose the **quality** (`320k`, `192k`, `128k`) of the audio while downloading the song.
- Able to choose the **type** (`.mp3`, `.mp4`, `.wav`, `.flac`) of the audio to download.
- Customizable download settings through the `ui/app.py` during execution.
- Lightweight and easy-to-use.
- Import a playlist from `.txt` or `.xlsx` files to download multiple tracks automatically.
- Clear separation between download logic (`core`), interface (`ui`) and utilities (`utils`) easy to maintain and expand.

## Project Structure

```
music-downloader/
├── core/
│   ├── __init__.py         # Core package initialization
│   ├── config.py           # Define global project settings
│   └── downloader.py       # Logic of downloading songs by receiving commands
├── ui/
│   ├── __init__.py         # Ui package initialization
│   ├── app.py              # Central interface initialization point
│   └── widgets.py          # Contains reusable interface components
├── utils/
│   ├── __init__.py         # Utils package initialization
│   └── file_handler.py     # Reads .txt or .xlsx files containing song lists
├── .gitignore              # List of files and folders to ignore by Git
├── .python-version         # Indicates the version of Python used in the project
├── main.py                 # Main script
├── pyproject.toml          # Project configuration file
├── README.md               # Documentation
├── structure.md            # Folder structure
├── TODO                    # List of pending tasks or future improvements to be made to the project
└── uv.lock                 # File containing dependencies information
```

## Installation

1. **Install FFmpeg on [oficial site](https://ffmpeg.org/download.html) or you can watch this [video](https://www.youtube.com/watch?v=4jx2_j5Seew).**

2. **Install UV package manager on [official site](https://docs.astral.sh/uv/getting-started/installation/) or you can watch this [video](https://www.youtube.com/watch?v=6pttmsBSi8M).**
 
3. **Clone the Repository:**
   ```
   git clone https://github.com/luanfelixcoding/music-downloader.git
   cd music-downloader
   ```

4. **Create and Activate a Virtual Environment** (optional but recommended):
   ```
    uv venv .venv
   .venv/Scripts/activate   # On Linux/Mac: source .venv/bin/activate
   ```

5. **Install Dependencies**:
   ```
   uv pip install 'git+https://github.com/luanfelixcoding/music-downloader.git'
   # Install your project as a pyproject package + dependencies
   ```
   

6. **Update Package** (if necessary):
   ```
   uv pip add -U yt-dlp
   ```

7. **Run the main file**:
    ```
    uv run main.py
    ```
