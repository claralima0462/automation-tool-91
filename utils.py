import random
import time


def calculate_jitter(x: int, y: int, max_jitter: int = 5) -> tuple:
    """Adds a small random offset to coordinates to mimic human behavior."""
    if max_jitter <= 0:
        return x, y
    jitter_x = random.randint(-max_jitter, max_jitter)
    jitter_y = random.randint(-max_jitter, max_jitter)
    return x + jitter_x, y + jitter_y


def get_random_sleep(base_interval: float, variance: float = 0.1) -> float:
    """Calculates a randomized sleep duration based on a base interval."""
    if variance <= 0:
        return max(0.0, base_interval)
    min_val = max(0.0, base_interval - variance)
    max_val = base_interval + variance
    return random.uniform(min_val, max_val)


def parse_duration(duration_str: str) -> float:
    """Parses basic duration strings like '500ms' or '2s' to seconds."""
    clean_str = duration_str.strip().lower()
    try:
        if clean_str.endswith("ms"):
            return float(clean_str[:-2]) / 1000.0
        if clean_str.endswith("s"):
            return float(clean_str[:-1])
        return float(clean_str)
    except ValueError:
        raise ValueError(f"Invalid duration format: {duration_str}")
