import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log') -> logging.Logger:
    """Initializes a rotating file logger for the tool."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotation: 1MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1_048_576, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

# Default project logger instance
app_logger = setup_logger('automation-tool-91')