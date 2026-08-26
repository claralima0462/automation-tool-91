import logging
from logging.handlers import RotatingFileHandler
import os

# Logger setup for automation-tool-91 autoclicker
# Implements rotating logs to manage file size

def setup_logger(name="autoclicker", log_dir="logs", log_file="automation.log",
                 max_bytes=5*1024*1024, backup_count=3, level=logging.INFO):
    """Configure and return a logger with file rotation."""

    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers on repeated calls
    if logger.hasHandlers():
        logger.handlers.clear()

    # Rotating file handler configuration
    file_handler = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    logger.info("Logger initialized with rotation")
    return logger

if __name__ == "__main__":
    # Test the logger setup
    logger = setup_logger()
    logger.debug("This debug log goes to file only")
    logger.info("Autoclicker started")
    logger.warning("Low memory warning")
    for i in range(10):
        logger.info(f"Click event number {i}")
