from typing import Union, Tuple

def validate_coordinates(x: int, y: int) -> bool:
    """Verify that screen coordinates are within non-negative bounds.

    Args:
        x: The horizontal screen position.
        y: The vertical screen position.

    Returns:
        bool: True if coordinates are valid, False otherwise.
    """
    return x >= 0 and y >= 0

def validate_interval(interval: Union[int, float]) -> bool:
    """Ensure the click interval is a positive value to prevent system freeze.

    Args:
        interval: Time in seconds between clicks.

    Returns:
        bool: True if interval is greater than zero.
    """
    return isinstance(interval, (int, float)) and interval > 0

def sanitize_input(raw_data: Tuple[str, str]) -> Tuple[int, int]:
    """Convert raw string input from user interface into integer coordinates.

    Args:
        raw_data: A tuple of two strings containing numeric characters.

    Returns:
        Tuple[int, int]: Sanitized integer coordinates.

    Raises:
        ValueError: If input strings are not numeric.
    """
    try:
        return int(raw_data[0]), int(raw_data[1])
    except (ValueError, TypeError):
        return 0, 0