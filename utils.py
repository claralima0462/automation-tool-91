import random
import time
from typing import Tuple, Optional


def parse_coordinates(coord_str: str) -> Optional[Tuple[int, int]]:
    """Parse string representation of coordinates (e.g. '100,200') into an integer tuple."""
    if not coord_str or "," not in coord_str:
        return None
    try:
        x_str, y_str = coord_str.split(",", 1)
        return int(x_str.strip()), int(y_str.strip())
    except ValueError:
        return None


def calculate_jitter_delay(base_delay: float, jitter_percent: float = 0.1) -> float:
    """Calculate a randomized delay interval to simulate human clicking variance."""
    if base_delay <= 0:
        return 0.0
    variance = base_delay * max(0.0, min(jitter_percent, 1.0))
    return max(0.001, base_delay + random.uniform(-variance, variance))


def format_duration(seconds: float) -> str:
    """Format total seconds into a readable time string (e.g., '1h 15m 30s')."""
    if seconds < 0:
        return "0s"
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)

    parts = []
    if hrs > 0:
        parts.append(f"{hrs}h")
    if mins > 0:
        parts.append(f"{mins}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)


def safe_sleep(duration: float, step: float = 0.05) -> bool:
    """Sleep in small intervals to keep the thread responsive."""
    start_time = time.time()
    while time.time() - start_time < duration:
        remaining = duration - (time.time() - start_time)
        time.sleep(min(step, remaining))
    return True
