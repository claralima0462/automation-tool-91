import time

def delay(seconds: float) -> None:
    """Pause execution for a specified number of seconds."""
    time.sleep(seconds)


def click_at(x: int, y: int) -> None:
    """Simulate a mouse click at the given coordinates."""
    import pyautogui
    pyautogui.click(x, y)


def get_cursor_position() -> tuple[int, int]:
    """Retrieve the current position of the mouse cursor."""
    import pyautogui
    return pyautogui.position()


def is_point_within_area(x: int, y: int, area: tuple[int, int, int, int]) -> bool:
    """Check if the point (x, y) is within the given rectangular area."""
    area_x, area_y, area_width, area_height = area
    return area_x <= x <= (area_x + area_width) and area_y <= y <= (area_y + area_height)


def perform_click_with_delay(x: int, y: int, delay_time: float) -> None:
    """Click at the specified coordinates after a delay."""
    delay(delay_time)
    click_at(x, y)
