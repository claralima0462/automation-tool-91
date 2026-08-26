import time
import threading
from typing import Optional, Callable

class Core:
    """Core module for autoclicker with performance optimizations."""

    def __init__(self, clicks_per_second: float = 10.0, max_duration: Optional[float] = None):
        self.clicks_per_second = clicks_per_second
        self.max_duration = max_duration
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._click_count = 0
        self._on_click: Optional[Callable] = None
        # Precompute interval for performance
        self._interval = 1.0 / clicks_per_second if clicks_per_second > 0 else 0.1

    def set_click_callback(self, callback: Callable[[], None]):
        self._on_click = callback

    def start(self):
        if self._running:
            return
        self._running = True
        self._click_count = 0
        self._thread = threading.Thread(target=self._optimized_loop, daemon=True)
        self._thread.start()

    def _optimized_loop(self):
        start_time = time.perf_counter()
        last_click_time = start_time
        while self._running:
            current_time = time.perf_counter()
            if self.max_duration is not None and (current_time - start_time) >= self.max_duration:
                self._running = False
                break
            time_since_last = current_time - last_click_time
            if time_since_last >= self._interval:
                self._perform_click()
                last_click_time = current_time
            else:
                # Minimal sleep to lower CPU usage while maintaining accuracy
                sleep_time = self._interval - time_since_last
                time.sleep(max(0, min(sleep_time, 0.01)))

    def _perform_click(self):
        self._click_count += 1
        if self._on_click is not None:
            self._on_click()

    def stop(self):
        self._running = False
        if self._thread is not None and self._thread.is_alive():
            self._thread.join(timeout=2.0)

    def get_click_count(self) -> int:
        return self._click_count

    def is_running(self) -> bool:
        return self._running

if __name__ == "__main__":
    def example_click():
        print("Click executed")

    core = Core(clicks_per_second=20.0, max_duration=1.0)
    core.set_click_callback(example_click)
    core.start()
    time.sleep(1.5)
    core.stop()
    print(f"Total optimized clicks: {core.get_click_count()}")