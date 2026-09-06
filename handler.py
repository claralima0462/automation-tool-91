import pyautogui
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-91')

class ClickHandler:
    """Handles click operations and safety constraints."""

    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.is_running = False

    def start_clicking(self, clicks: int):
        """Executes click sequence with interrupt capability."""
        self.is_running = True
        logger.info(f"Starting sequence: {clicks} clicks")
        
        try:
            for i in range(clicks):
                if not self.is_running:
                    break
                pyautogui.click()
                time.sleep(self.interval)
        except pyautogui.FailSafeException:
            logger.warning("Fail-safe triggered: stopping execution")
            self.stop_clicking()

    def stop_clicking(self):
        """Graceful halt of click operations."""
        self.is_running = False
        logger.info("Handler stopped by user")

    def set_interval(self, seconds: float):
        """Updates timing between click events."""
        if seconds > 0:
            self.interval = seconds
        else:
            logger.error("Invalid interval: must be positive")