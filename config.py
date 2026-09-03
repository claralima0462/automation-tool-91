import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_delay": 0.1,         # in seconds
    "mouse_button": "left",     # left, right, middle
    "click_type": "single",     # single, double
    "start_hotkey": "f1",
    "stop_hotkey": "f2",
    "repeat_count": 0           # 0 for infinite
}

class ConfigManager:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or returns defaults if not found."""
        if not os.path.exists(self.filepath):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        
        try:
            with open(self.filepath, "r") as f:
                loaded = json.load(f)
                # Merge loaded config with defaults to ensure all keys exist
                config = DEFAULT_CONFIG.copy()
                config.update(loaded)
                return config
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults on error
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Saves the configuration dictionary to a JSON file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(config_data, f, indent=4)
        except IOError as e:
            # Print a warning and proceed without breaking runtime execution
            print(f"Warning: Could not save configuration to {self.filepath}: {e}")

    def get(self, key: str) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def update(self, key: str, value: Any) -> None:
        """Updates a configuration value and saves it to disk."""
        self.config[key] = value
        self.save_config(self.config)
