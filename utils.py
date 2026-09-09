import random
from typing import Tuple


def parse_interval(interval_str: str) -> float:
    """Convert a human-readable interval string into seconds.

    Supported units: 'ms' (milliseconds), 's' (seconds), 'm' (minutes).

    Args:
        interval_str: A string representing time duration (e.g., '500ms',
          '2s').

    Returns:
        The duration in seconds as a float.

    Raises:
        ValueError: If the format is invalid or unit is unsupported.
    """
    interval_str = interval_str.strip().lower()
    if interval_str.endswith("ms"):
        try:
            return float(interval_str[:-2]) / 1000.0
        except ValueError:
            pass
    elif interval_str.endswith("s"):
        try:
            return float(interval_str[:-1])
        except ValueError:
            pass
    elif interval_str.endswith("m"):
        try:
            return float(interval_str[:-1]) * 60.0
        except ValueError:
            pass
    else:
        try:
            return float(interval_str)
        except ValueError:
            pass

    raise ValueError(f"Invalid interval format: {interval_str}")


def calculate_jitter(base_delay: float, jitter_percentage: float) -> float:
    """Apply a random jitter to a delay to simulate human behavior.

    Args:
        base_delay: The baseline delay in seconds.
        jitter_percentage: The maximum percentage variance (0.0 to 1.0).

    Returns:
        The adjusted delay in seconds.

    Raises:
        ValueError: If jitter_percentage is out of bounds.
    """
    if not (0.0 <= jitter_percentage <= 1.0):
        raise ValueError("Jitter percentage must be between 0.0 and 1.0")

    max_delta = base_delay * jitter_percentage
    return base_delay + random.uniform(-max_delta, max_delta)


def is_within_bounds(
    coords: Tuple[int, int], screen_resolution: Tuple[int, int]
) -> bool:
    """Verify if the target coordinates are within the screen resolution bounds.

    Args:
        coords: A tuple of (x, y) coordinates.
        screen_resolution: A tuple of (width, height) representing resolution.

    Returns:
        True if coordinates are within bounds, False otherwise.
    """
    x, y = coords
    width, height = screen_resolution
    return 0 <= x < width and 0 <= y < height
