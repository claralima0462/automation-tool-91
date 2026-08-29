import time
from typing import Optional

import pyautogui

class AutoClickerCore:
    """Core class handling the autoclicker operations."""

    def __init__(self, interval: float = 1.0, button: str = "left") -> None:
        """Initialize with click interval and button.

        Args:
            interval: Seconds between consecutive clicks. Must be positive.
            button: Mouse button for clicking. Defaults to 'left'.
        """
        if interval <= 0:
            raise ValueError("Interval must be greater than zero")
        self.interval: float = interval
        self.button: str = button
        self.is_running: bool = False

    def start_clicking(self, duration: Optional[float] = None) -> None:
        """Begin the autoclicking process.

        Args:
            duration: Optional total duration in seconds. If not provided,
                      continues until stop is called.
        """
        self.is_running = True
        start_time: float = time.time()
        while self.is_running:
            # Execute the click action
            pyautogui.click(button=self.button)
            time.sleep(self.interval)
            if duration is not None:
                elapsed: float = time.time() - start_time
                if elapsed >= duration:
                    self.stop_clicking()
                    break

    def stop_clicking(self) -> None:
        """Stop the ongoing clicking operation."""
        self.is_running = False

    def get_status(self) -> bool:
        """Return current running status.

        Returns:
            True if clicking is active, False otherwise.
        """
        return self.is_running

# Utility function for direct use
def run_autoclicker(interval: float, duration: Optional[float] = None, button: str = "left") -> None:
    """Run autoclicker using the core class.

    Args:
        interval: Click interval in seconds.
        duration: Optional run duration.
        button: Mouse button to click.
    """
    core = AutoClickerCore(interval=interval, button=button)
    core.start_clicking(duration=duration)
