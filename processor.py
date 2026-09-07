import time
import threading
from typing import Callable

class EventProcessor:
    """Handles click event throttling using a high-frequency loop."""
    def __init__(self, interval: float = 0.001):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def execute_optimized_loop(self, action: Callable[[], None], duration: float) -> None:
        """Executes action with microsecond-precise sleeping."""
        self.running = True
        start_time = time.perf_counter()
        
        # Cached reference to minimize attribute lookups
        sleep = time.sleep
        clock = time.perf_counter
        
        try:
            while self.running and (clock() - start_time) < duration:
                loop_start = clock()
                action()
                
                # Dynamic sleep adjustment to account for execution drift
                elapsed = clock() - loop_start
                sleep_time = self.interval - elapsed
                
                if sleep_time > 0:
                    sleep(sleep_time)
        finally:
            self.running = False

    def stop(self):
        with self._lock:
            self.running = False