import time
import pyautogui
from typing import Tuple, Optional

class ClickProcessor:
    """Handles automated clicking sequences based on coordinate input."""

    def __init__(self, interval: float = 0.5) -> None:
        """Initializes processor with delay between clicks."""
        self.interval: float = interval

    def perform_click(self, x: int, y: int) -> bool:
        """Executes a single mouse click at specified coordinates."""
        try:
            pyautogui.click(x=x, y=y)
            time.sleep(self.interval)
            return True
        except (pyautogui.FailSafeException, pyautogui.PyAutoGUIException):
            return False

    def run_sequence(self, coordinates: list[Tuple[int, int]], loops: int = 1) -> None:
        """Iterates through a list of coordinates for a set number of loops."""
        for _ in range(loops):
            for x, y in coordinates:
                if not self.perform_click(x, y):
                    break

    def update_interval(self, new_interval: float) -> None:
        """Modifies the delay between click events."""
        if new_interval >= 0:
            self.interval = new_interval