import time
import random
from validators import validate_input

class AutoClicker:
    def __init__(self, click_interval=1, click_count=10):
        self.click_interval = click_interval
        self.click_count = click_count

    def start_clicking(self):
        for _ in range(self.click_count):
            if not validate_input(self.click_interval, self.click_count):
                print('Invalid input parameters. Stopping the clicker.')
                return
            self.perform_click()
            time.sleep(self.click_interval)

    def perform_click(self):
        print('Performed a click!')

if __name__ == '__main__':
    click_interval = random.uniform(0.5, 2.0)
    click_count = random.randint(1, 20)
    clicker = AutoClicker(click_interval, click_count)
    clicker.start_clicking()