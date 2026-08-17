import time
import random

class AutoClicker:
    def __init__(self, click_interval=1.0, max_clicks=100):
        self.click_interval = click_interval
        self.max_clicks = max_clicks

    def validate_input(self, interval, clicks):
        if not isinstance(interval, (int, float)) or interval <= 0:
            raise ValueError('Click interval must be a positive number.')
        if not isinstance(clicks, int) or clicks <= 0:
            raise ValueError('Max clicks must be a positive integer.')

    def start_clicking(self):
        try:
            self.validate_input(self.click_interval, self.max_clicks)
            for _ in range(self.max_clicks):
                print('Click!')
                time.sleep(self.click_interval)
        except ValueError as ve:
            print(f'Input Error: {ve}')
        except Exception as e:
            print(f'Unexpected Error: {e}')

if __name__ == '__main__':
    autoclicker = AutoClicker(0.5, 10)
    autoclicker.start_clicking()