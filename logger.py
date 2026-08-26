import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "autoclicker") -> logging.Logger:
    """Configure and return a rotating file logger for automation-tool-91."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate handlers if setup is called multiple times
    if logger.handlers:
        return logger
        
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, f"{name}.log")
    
    # Setup rotating file handler (5MB per file, max 3 backup files)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Setup console handler for real-time monitoring
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Define format and apply to handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()
