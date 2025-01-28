from pathlib import Path
from .logger import setup_logger

logger = setup_logger()


def ensure_folder_exists(folder_path: Path) -> None:
    """
    Ensures the given folder exists, creating it if necessary.

    Args:
        folder_path (Path) : Path to the folder to check or create it.
    """
    try:
        folder_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Folder verified: {folder_path}")
    except Exception as unknown_error:
        logger.error(f"Failed to ensure folder exists: {unknown_error}")
