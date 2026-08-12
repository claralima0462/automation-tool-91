import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'click_button': 'left',
    'screen_resolution': [1920, 1080]
}

CONFIG_FILE_PATH = 'config.json'


def load_config(file_path=CONFIG_FILE_PATH):
    """Load configuration from a JSON file, or return defaults if not found."""
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
            return {**DEFAULT_CONFIG, **config}
        except (json.JSONDecodeError, TypeError) as e:
            print(f'Error loading config: {e}')
            return DEFAULT_CONFIG


if __name__ == '__main__':
    config = load_config()
    print(config)