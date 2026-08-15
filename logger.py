import logging
from logging.handlers import RotatingFileHandler

# Setup logger configuration

def setup_logger(log_file='app.log', max_bytes=10*1024, backup_count=5):
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)  # Set the logger to debug level

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage of the logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and ready to log!')
    logger.debug('This is a debug message.')
    logger.error('This is an error message.')
