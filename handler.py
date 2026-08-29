import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(log_name: str = "automation-tool-91", log_level: int = logging.INFO) -> logging.Logger:
    """Configure logger with rotating file handler for autoclicker tool."""
    logger = logging.getLogger(log_name)
    # Prevent adding multiple handlers if called repeatedly
    if logger.hasHandlers():
        return logger
    logger.setLevel(log_level)
    # Ensure logs directory exists
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    log_file = logs_dir / "autoclicker.log"
    # Rotating file handler: max 5MB, keep 3 backups
    max_bytes = 5 * 1024 * 1024
    backup_count = 3
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    # Stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    # Common formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    # Log initial message
    logger.info("Logger initialized with rotation for autoclicker")
    return logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("This is a debug message")
    logger.info("Automation started")
    logger.warning("Potential issue detected")
    # Simulate some logs
    for i in range(5):
        logger.info(f"Click event {i+1} recorded")
