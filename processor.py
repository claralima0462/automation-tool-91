import time

class Processor:
    def __init__(self):
        self.click_interval = 1.0  # Default to 1 second

    def start_clicking(self, num_clicks):
        if not self.validate_input(num_clicks):
            raise ValueError('Invalid number of clicks. Must be a positive integer.')
        for _ in range(num_clicks):
            self.perform_click()
            time.sleep(self.click_interval)

    def perform_click(self):
        print('Click!')  # Simulate a click in your autoclicker

    def validate_input(self, num_clicks):
        return isinstance(num_clicks, int) and num_clicks > 0

# Example usage
if __name__ == '__main__':
    processor = Processor()
    try:
        processor.start_clicking(5)  # Change this number as needed
    except ValueError as e:
        print(e)