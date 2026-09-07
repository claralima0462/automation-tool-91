import threading
import time
from typing import Callable, Optional

class AutoClicker:
    """Core autoclicker engine managing the clicking thread and state."""
    
    def __init__(self, delay: float = 0.1, click_func: Optional[Callable[[], None]] = None) -> None:
        self.delay = delay
        self.click_func = click_func or self._default_click
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()

    def _default_click(self) -> None:
        """Default click action placeholder when no controller is injected."""
        pass

    def _click_loop(self) -> None:
        """Background loop that performs clicks at specified intervals."""
        while True:
            with self._lock:
                if not self._running:
                    break
            self.click_func()
            time.sleep(self.delay)

    def start(self) -> None:
        """Starts the clicker thread safely if it is not already running."""
        with self._lock:
            if self._running:
                return
            self._running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        """Stops the background clicker thread gracefully."""
        with self._lock:
            self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None

    def update_delay(self, new_delay: float) -> None:
        """Safely updates the delay between click events."""
        if new_delay <= 0:
            raise ValueError("Delay must be greater than zero seconds")
        with self._lock:
            self.delay = new_delay

    @property
    def is_active(self) -> bool:
        """Returns the running state of the autoclicker."""
        with self._lock:
            return self._running