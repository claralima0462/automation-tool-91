import time
import threading
from typing import Optional, Dict

# Core module with performance optimizations for autoclicker
class CoreAutoClicker:
    def __init__(self, click_interval: float = 0.05):
        self.click_interval = click_interval
        self.is_running = False
        self.click_count = 0
        self.start_time: Optional[float] = None
        self._thread: Optional[threading.Thread] = None

    def start_clicking(self, x: int = 100, y: int = 100):
        if self.is_running:
            return
        self.is_running = True
        self.click_count = 0
        self.start_time = time.perf_counter()
        self._thread = threading.Thread(target=self._optimized_click_loop, args=(x, y))
        self._thread.daemon = True
        self._thread.start()

    def _optimized_click_loop(self, x: int, y: int):
        # Use local variables to optimize attribute access in loop
        interval = self.click_interval
        count = 0
        last_tick = time.perf_counter()
        while self.is_running:
            count += 1
            self.click_count = count
            current = time.perf_counter()
            elapsed = current - last_tick
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_tick = time.perf_counter()

    def stop_clicking(self):
        self.is_running = False
        if self._thread is not None and self._thread.is_alive():
            self._thread.join(timeout=2.0)

    def get_performance_stats(self) -> Dict[str, float]:
        if self.start_time is None:
            return {"clicks": 0.0, "cps": 0.0, "runtime": 0.0}
        runtime = time.perf_counter() - self.start_time
        cps = self.click_count / runtime if runtime > 0 else 0.0
        return {
            "clicks": float(self.click_count),
            "cps": round(cps, 2),
            "runtime": round(runtime, 2)
        }

    def update_interval(self, interval: float):
        if 0.01 < interval < 10.0:
            self.click_interval = interval