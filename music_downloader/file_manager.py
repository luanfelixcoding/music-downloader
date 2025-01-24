from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def ensure_folder_exists(folder_path: Path) -> None:
    try:
        folder_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Folder checked/created at: {folder_path}")
    except Exception as unknown_error:
        logger.error(f"Error creating folder {folder_path} : {unknown_error}")
