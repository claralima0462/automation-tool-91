import time
import threading

class AutoClicker:
    def __init__(self, delay):
        self.delay = delay
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._click_loop).start()

    def stop(self):
        self.running = False

    def _click_loop(self):
        while self.running:
            self.perform_click()
            time.sleep(self.delay)

    def perform_click(self):
        print('Click!')  # Replace with actual click action

if __name__ == '__main__':
    autoclicker = AutoClicker(delay=1)
    autoclicker.start()
    time.sleep(5)
    autoclicker.stop()