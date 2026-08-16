from time import sleep
from typing import Callable, Optional

class Autoclicker:
    def __init__(self, click_interval: float) -> None:
        """
        Initialize the Autoclicker with a click interval.

        :param click_interval: Time in seconds between clicks.
        """
        self.click_interval = click_interval
        self.is_running = False

    def start(self, click_action: Callable[[], None]) -> None:
        """
        Start the autoclicker, calling the click action at the specified interval.

        :param click_action: A callable that defines the click action.
        """
        self.is_running = True
        while self.is_running:
            click_action()
            sleep(self.click_interval)

    def stop(self) -> None:
        """
        Stop the autoclicker.
        """
        self.is_running = False

# Example usage
if __name__ == '__main__':
    autoclicker = Autoclicker(0.1)
    def mock_click():
        print('Click!')
    autoclicker.start(mock_click)
    sleep(1)  # Let it run for a second
    autoclicker.stop()
