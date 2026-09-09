import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": 0
}

def load_config(filepath: str = "config.json") -> dict:
    """loads configuration from json file or returns defaults"""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # merge user settings with defaults to ensure keys exist
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: dict, filepath: str = "config.json") -> None:
    """persists current configuration to disk"""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"failed to save config: {e}")