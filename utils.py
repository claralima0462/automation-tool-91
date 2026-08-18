import json
from typing import Any, Dict

def load_config(file_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    :param file_path: Path to the JSON configuration file.
    :return: Configuration data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)
            return config_data
    except FileNotFoundError:
        print(f'Configuration file not found: {file_path}')
        return {}
    except json.JSONDecodeError:
        print('Error decoding JSON from the configuration file.')
        return {}


def save_config(file_path: str, config_data: Dict[str, Any]) -> None:
    """
    Save configuration to a JSON file.
    
    :param file_path: Path to the JSON configuration file.
    :param config_data: Configuration data as a dictionary.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(config_data, file, indent=4)
    except IOError:
        print(f'Error writing to configuration file: {file_path}')


def update_config(file_path: str, updates: Dict[str, Any]) -> None:
    """
    Update existing configuration with new values.
    
    :param file_path: Path to the JSON configuration file.
    :param updates: New configuration values as a dictionary.
    """
    config_data = load_config(file_path)
    config_data.update(updates)
    save_config(file_path, config_data)
