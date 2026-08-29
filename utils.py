"""Utility functions for autoclicker data handling."""

import json
import time
from datetime import datetime
from typing import List, Dict, Any, Optional

def save_data(data: List[Dict[str, Any]], filename: str = "autoclicker_data.json") -> bool:
    """Save autoclicker click data to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except (IOError, TypeError) as e:
        print(f"Failed to save data: {e}")
        return False

def load_data(filename: str = "autoclicker_data.json") -> List[Dict[str, Any]]:
    """Load autoclicker click data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except (IOError, json.JSONDecodeError) as e:
        print(f"Failed to load data: {e}")
        return []

def record_click(data: List[Dict[str, Any]], x: int, y: int, interval: Optional[float] = None) -> List[Dict[str, Any]]:
    """Record a new click event with position and timestamp."""
    click_event = {
        "timestamp": time.time(),
        "datetime": datetime.now().isoformat(),
        "position": {"x": x, "y": y},
        "interval": interval
    }
    data.append(click_event)
    return data

def calculate_statistics(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate basic statistics from click data."""
    if not data:
        return {"total_clicks": 0, "average_interval": 0.0, "duration": 0.0}

    total_clicks = len(data)
    timestamps = [event["timestamp"] for event in data]
    intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    avg_interval = sum(intervals) / len(intervals) if intervals else 0.0
    duration = timestamps[-1] - timestamps[0] if len(timestamps) > 1 else 0.0

    return {
        "total_clicks": total_clicks,
        "average_interval": round(avg_interval, 4),
        "duration": round(duration, 2),
        "clicks_per_second": round(total_clicks / duration, 2) if duration > 0 else 0.0
    }

def export_to_csv(data: List[Dict[str, Any]], filename: str = "clicks.csv") -> bool:
    """Export click data to a simple CSV file."""
    try:
        with open(filename, 'w') as f:
            f.write("timestamp,datetime,x,y,interval\n")
            for event in data:
                pos = event["position"]
                f.write(f"{event['timestamp']},{event['datetime']},{pos['x']},{pos['y']},{event.get('interval', '')}\n")
        return True
    except IOError as e:
        print(f"Failed to export CSV: {e}")
        return False
