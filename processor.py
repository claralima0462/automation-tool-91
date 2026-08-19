import time
from threading import Thread
from pynput.mouse import Button, Controller

class AutoClicker:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self.mouse_controller = Controller()
        self.running = False

    def start_clicking(self):
        self.running = True
        while self.running:
            self.mouse_controller.click(Button.left)
            time.sleep(self.click_interval)

    def stop_clicking(self):
        self.running = False

    def run(self):
        click_thread = Thread(target=self.start_clicking)
        click_thread.start()

if __name__ == '__main__':
    clicker = AutoClicker(click_interval=0.5)
    try:
        clicker.run()
        # Run for 10 seconds
        time.sleep(10)
    finally:
        clicker.stop_clicking()  
        click_thread.join()  # Ensure clicking stops before exiting
