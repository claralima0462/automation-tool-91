# Constants used throughout the autoclicker

# Default click interval in seconds
DEFAULT_CLICK_INTERVAL = 0.1

# Mouse button options
LEFT_BUTTON = 1
RIGHT_BUTTON = 2
MIDDLE_BUTTON = 3

# Key constants for controlling the autoclicker
START_KEY = 's'
STOP_KEY = 'e'
RESET_KEY = 'r'

# Screen resolution constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Set the maximum number of clicks allowed
MAX_CLICKS = 10000

# Log file configuration
LOG_FILE_PATH = "autoclicker.log"
LOG_LEVEL = "DEBUG"

# Configuration for the autoclicker
CONFIG = {
    'click_interval': DEFAULT_CLICK_INTERVAL,
    'max_clicks': MAX_CLICKS,
    'screen_resolution': (SCREEN_WIDTH, SCREEN_HEIGHT),
    'log_file': LOG_FILE_PATH,
    'log_level': LOG_LEVEL,
}