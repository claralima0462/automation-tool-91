import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    """Sets up a logger with rotation."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler for logging
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready to use.')