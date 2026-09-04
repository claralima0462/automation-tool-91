import json
import os
from typing import Dict, Any

def load_click_settings(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a local JSON file."""
    default_settings = {
        "interval": 0.1,
        "button": "left",
        "clicks": 1
    }

    if not os.path.exists(filepath):
        return default_settings

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return {**default_settings, **data}
    except (json.JSONDecodeError, IOError):
        return default_settings

def save_click_settings(filepath: str, settings: Dict[str, Any]) -> bool:
    """Persists current clicker configuration to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(settings, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: float) -> float:
    """Ensures click interval stays within safe operational bounds."""
    return max(0.01, min(interval, 60.0))
