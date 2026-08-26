import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(
    name: str = "automation-tool-91",
    log_dir: str = "logs",
    log_file: str = "autoclicker.log",
    max_size: int = 5242880,  # 5 MB
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Configure logger with rotating file handler for the autoclicker automation tool."""

    # Ensure log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    # Get or create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to avoid duplicates on re-setup
    if logger.hasHandlers():
        logger.handlers.clear()

    # Rotating file handler for persistent logs
    file_handler = RotatingFileHandler(
        filename=log_path,
        maxBytes=max_size,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(level)

    # Stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)

    # Standard formatter with timestamp and level
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Log initial setup message
    logger.debug("Logger setup complete with file rotation enabled")

    return logger

# For direct testing
if __name__ == "__main__":
    logger = setup_logger(level=logging.DEBUG)
    logger.info("Starting automation tool")
    logger.warning("Example warning for rotation test")
    # To force rotation, one could log many times but omitted for brevity