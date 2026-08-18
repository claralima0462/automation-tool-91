import time
import threading

class AutoClicker:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _click_loop(self):
        while self.running:
            self.perform_click()
            time.sleep(self.click_interval)

    def perform_click(self):
        # This is a placeholder for the click action
        print("Click!")  # Replace with actual clicking logic

# Example usage
if __name__ == '__main__':
    clicker = AutoClicker(click_interval=0.05)
    clicker.start()
    time.sleep(1)
    clicker.stop()