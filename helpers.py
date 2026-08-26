import time
import random

def get_random_delay(min_delay: float, max_delay: float) -> float:
    """Generate a randomized delay to mimic human behavior."""
    return random.uniform(min_delay, max_delay)

def human_sleep(min_delay: float, max_delay: float) -> None:
    """Sleep for a random duration between bounds."""
    delay = get_random_delay(min_delay, max_delay)
    time.sleep(delay)

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Ensure click coordinates are within screen bounds."""
    return 0 <= x <= screen_width and 0 <= y <= screen_height

def clamp_value(val: int, minimum: int, maximum: int) -> int:
    """Clamp a numeric value between a minimum and maximum."""
    return max(minimum, min(val, maximum))
