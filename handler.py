import time
import random

class Clicker:
    def __init__(self, delay=1):
        self.delay = delay

    def perform_click(self):
        try:
            # Simulating mouse click action
            if self.delay < 0:
                raise ValueError("Delay must be non-negative")
            print(f"Click performed after {self.delay} seconds.")
            time.sleep(self.delay)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def random_clicks(self, count):
        try:
            if count < 1:
                raise ValueError("Count must be at least 1")
            for _ in range(count):
                self.perform_click()
                # Randomly determining the next delay between clicks
                self.delay = random.uniform(0.5, 2.0)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    clicker = Clicker()
    clicker.random_clicks(5)