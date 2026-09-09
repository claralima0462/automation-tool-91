import pyautogui
import time
import random

def perform_click(x: int, y: int, interval: float = 0.0) -> None:
    """Executes a mouse click at specified screen coordinates."""
    pyautogui.click(x, y)
    if interval > 0:
        time.sleep(interval)

def perform_random_click(min_x: int, max_x: int, min_y: int, max_y: int) -> None:
    """Executes a click at random coordinates within a range."""
    target_x = random.randint(min_x, max_x)
    target_y = random.randint(min_y, max_y)
    pyautogui.click(target_x, target_y)

def move_and_drag(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5) -> None:
    """Performs a mouse drag operation from start to end points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')

def get_screen_resolution() -> tuple:
    """Returns current primary monitor resolution as (width, height)."""
    return pyautogui.size()

def safe_exit_check() -> bool:
    """Checks if the mouse is in the corner to trigger emergency stop."""
    try:
        return pyautogui.position() == (0, 0)
    except pyautogui.FailSafeException:
        return True