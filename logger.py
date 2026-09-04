import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation_tool_91', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # Rotating file handler: 5MB per file, keep 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Optional: stream to console for debugging
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
logger = setup_logger()