import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval_seconds": 0.1,
    "mouse_button": "left",
    "click_type": "single",
    "hotkey_toggle": "f6",
    "max_clicks": 0,
    "random_delay_ms": 10,
    "target_coordinates": None,
}


class ConfigLoader:
    """Handles loading, saving, and managing autoclicker configuration settings."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, falling back to defaults if missing or invalid."""
        if not self.config_path.exists():
            self.save()
            return self._config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_data = json.load(f)
                if isinstance(user_data, dict):
                    self._config = {**DEFAULT_CONFIG, **user_data}
        except (json.JSONDecodeError, OSError):
            # Fall back to default config if file reading or parsing fails
            self._config = DEFAULT_CONFIG.copy()

        return self._config

    def save(self) -> None:
        """Save current active settings to the JSON configuration file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self._config, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._config.get(key, default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update specific settings and persist changes to disk."""
        self._config.update(new_settings)
        self.save()
