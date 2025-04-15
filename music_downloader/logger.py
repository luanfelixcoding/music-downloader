import logging
import os


def setup_logger(log_file: str = "logs/downloader.log") -> logging.Logger:
    """
    Configures and returns a logger instance.

    Args:
        log_file (str) : Log file to store the actions done by the program.

    Returns:
        Logger instance.
    """
    logger = logging.getLogger("MusicDownloader")
    logger.setLevel(logging.INFO)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Verify if handler already exists
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)

    # Console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(logging.Formatter("%(message)s"))

    # logger.addHandler(console_handler)

    return logger
