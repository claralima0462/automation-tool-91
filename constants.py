CACHE_SIZE = 128
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 5
API_ENDPOINT = 'https://api.example.com'
STATUS_SUCCESS = 'success'
STATUS_FAILURE = 'failure'
ERROR_MESSAGES = {
    'timeout': 'The request has timed out.',
    'not_found': 'The requested resource was not found.',
    'unauthorized': 'You do not have permission to access this resource.',
}

# Response codes for REST API
HTTP_OK = 200
HTTP_NOT_FOUND = 404
HTTP_UNAUTHORIZED = 401
HTTP_SERVER_ERROR = 500

# Commonly used file extensions
FILE_EXTENSIONS = {
    'json': '.json',
    'xml': '.xml',
    'txt': '.txt',
    'csv': '.csv',
}

# Default settings for the application
DEFAULT_SETTINGS = {
    'language': 'en',
    'theme': 'light',
    'notifications': True,
}

# Network configurations
NETWORK_CONFIG = {
    'max_connections': 10,
    'keep_alive': True,
    'timeout': DEFAULT_TIMEOUT,
}