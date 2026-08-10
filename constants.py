import json

# Default configuration constants
DEFAULT_SETTINGS = {
    'max_items': 100,
    'timeout': 30,
    'retry_attempts': 3,
    'log_level': 'INFO',
}

# API endpoint constants
API_ENDPOINTS = {
    'users': 'https://api.example.com/users',
    'posts': 'https://api.example.com/posts',
    'comments': 'https://api.example.com/comments',
}

# Function to save constants to a JSON file
def save_constants_to_json(filepath):
    try:
        with open(filepath, 'w') as json_file:
            json.dump({
                'default_settings': DEFAULT_SETTINGS,
                'api_endpoints': API_ENDPOINTS,
            }, json_file, indent=4)
            print(f'Constants saved to {filepath}')
    except Exception as e:
        print(f'Error saving constants: {e}')