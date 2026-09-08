import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation-tool-91', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # 5MB log file limit with 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Initialize global logger instance
logger = setup_logger()