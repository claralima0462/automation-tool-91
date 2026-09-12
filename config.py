import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # in seconds
    "button": "left",       # left, right, middle
    "click_type": "single", # single, double
    "hotkey": "f10",        # key to start/stop
    "hold_time": 0.05,      # click duration
    "random_delay": 0.0,    # max random delay in seconds
}

class ConfigManager:
    """Manages loading, saving, and validation of the autoclicker configuration."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file, falling back to defaults for missing keys."""
        if not os.path.exists(self.filepath):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                config = DEFAULT_CONFIG.copy()
                config.update(loaded)
                return config
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Saves the current configuration to the JSON file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4)
        except IOError as e:
            print(f"Failed to write configuration: {e}")

    def get(self, key: str) -> Any:
        """Retrieves a configuration value."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
