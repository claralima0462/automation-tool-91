import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=5 * 1024 * 1024, backup_count=5):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message')
    log.info('Information message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical error message')
