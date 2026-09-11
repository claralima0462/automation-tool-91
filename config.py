import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval_ms": 100,
    "button": "left",
    "repeat": -1,
    "hotkey": "f6"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file or return defaults."""
    if not os.path.exists(config_path):
        _write_default_config(config_path)
        return DEFAULT_CONFIG
    
    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults to ensure keys exist
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def _write_default_config(config_path: str) -> None:
    """Initialize config file with default values."""
    try:
        with open(config_path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    except IOError:
        pass

if __name__ == "__main__":
    # Example usage for development testing
    settings = load_config()
    print(f"Active settings: {settings}")