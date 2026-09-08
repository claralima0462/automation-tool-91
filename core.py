import json
import os
from typing import Dict, Any

def load_click_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "clicks": 0}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker settings to the local filesystem."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_profile_data(data: Dict[str, Any]) -> bool:
    """Basic structure validation for click configuration."""
    required = ["interval", "button"]
    return all(key in data for key in required) and isinstance(data["interval"], (int, float))

def format_click_stats(count: int, duration: float) -> str:
    """String representation of click session performance."""
    avg = count / duration if duration > 0 else 0
    return f"Clicks: {count} | Avg: {avg:.2f} cps"