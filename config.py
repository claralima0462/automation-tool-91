import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # click interval in seconds
    "mouse_button": "left",  # mouse button: left, right, middle
    "hotkey": "f8",  # global shortcut to start/stop
    "click_type": "single",  # single or double click
    "repeat_count": 0,  # 0 for infinite, positive integer otherwise
}

class ConfigManager:
    """Manages loading, merging, and saving autoclicker configurations."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from file, falling back to defaults if missing or corrupted."""
        config = DEFAULT_CONFIG.copy()
        if not os.path.exists(self.config_path):
            self.save_config(config)
            return config

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                # Validate and merge loaded keys
                for key, val in user_config.items():
                    if key in config:
                        config[key] = val
        except (json.JSONDecodeError, IOError):
            # Keep defaults on parse failure
            pass
        return config

    def save_config(self, config: Dict[str, Any]) -> None:
        """Persists current configuration changes to disk."""
        try:
            with open(self.config_path, "w") as f:
                json.dump(config, f, indent=4)
        except IOError:
            pass

    def get(self, key: str) -> Any:
        """Retrieves config value with safe fallback to defaults."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
