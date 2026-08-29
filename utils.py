import json
import os
from typing import List, Dict, Any, Optional

def load_click_data(filepath: str) -> Optional[List[Dict[str, Any]]]:
    """Load click positions and delays from JSON file."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        if validate_click_data(data):
            return data
        return None
    except (json.JSONDecodeError, IOError):
        return None

def save_click_data(filepath: str, clicks: List[Dict[str, Any]]) -> bool:
    """Save list of click data to JSON file."""
    if not validate_click_data(clicks):
        return False
    try:
        with open(filepath, 'w') as file:
            json.dump(clicks, file, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(clicks: List[Dict[str, Any]]) -> bool:
    """Check if click data has required fields with correct types."""
    if not isinstance(clicks, list):
        return False
    required = {'x', 'y', 'delay'}
    for item in clicks:
        if not isinstance(item, dict):
            return False
        if not required.issubset(set(item.keys())):
            return False
        if not (isinstance(item['x'], (int, float)) and
                isinstance(item['y'], (int, float)) and
                isinstance(item['delay'], (int, float))):
            return False
        if item['delay'] < 0:
            return False
    return True

def add_click(clicks: List[Dict[str, Any]], x: float, y: float, delay: float) -> List[Dict[str, Any]]:
    """Add a new click to the list if valid."""
    new_click = {'x': x, 'y': y, 'delay': delay}
    if validate_click_data([new_click]):
        clicks.append(new_click)
    return clicks

def get_click_statistics(clicks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Return statistics like count, average delay, min/max positions."""
    if not clicks:
        return {'count': 0, 'avg_delay': 0, 'total_delay': 0}
    delays = [c['delay'] for c in clicks]
    xs = [c['x'] for c in clicks]
    ys = [c['y'] for c in clicks]
    stats = {
        'count': len(clicks),
        'avg_delay': sum(delays) / len(delays),
        'total_delay': sum(delays),
        'min_x': min(xs),
        'max_x': max(xs),
        'min_y': min(ys),
        'max_y': max(ys)
    }
    return stats

def filter_clicks(clicks: List[Dict[str, Any]], min_delay: float = 0.0) -> List[Dict[str, Any]]:
    """Return clicks with delay at least min_delay."""
    return [c for c in clicks if c['delay'] >= min_delay]
