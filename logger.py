import logging
import sys
from datetime import datetime

def setup_logger(name: str = "automation-tool-91") -> logging.Logger:
    """
    Configures a standard logger for automation tasks.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Output to stdout for easier monitoring
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Optional: persistent file logging
        log_filename = f"logs/run_{datetime.now().strftime('%Y%m%d')}.log"
        try:
            file_handler = logging.FileHandler(log_filename)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except OSError:
            logger.warning("Could not initialize file logging. Check log directory.")

    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info"):
    """
    Proxy function for standardized event logging.
    """
    levels = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "debug": logger.debug
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)