import time
from typing import Dict, Any, Union

class ClickProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.is_running = False

    def validate_inputs(self) -> Dict[str, Union[int, float, str]]:
        """Validates the click configuration inputs before execution."""
        delay = self.config.get("delay", 0.1)
        clicks = self.config.get("clicks", 10)
        button = self.config.get("button", "left")

        if not isinstance(delay, (int, float)) or delay <= 0:
            raise ValueError("Click delay must be a positive number.")
        
        if not isinstance(clicks, int) or clicks < 0:
            raise ValueError("Click count must be a non-negative integer.")
        
        valid_buttons = {"left", "right", "middle"}
        if not isinstance(button, str) or button.lower() not in valid_buttons:
            raise ValueError(f"Button must be one of {valid_buttons}")

        return {
            "delay": float(delay),
            "clicks": int(clicks),
            "button": button.lower()
        }

    def run_loop(self) -> int:
        """Executes the main autoclicker loop after validating inputs."""
        validated = self.validate_inputs()
        delay = validated["delay"]
        clicks = validated["clicks"]
        button = validated["button"]

        self.is_running = True
        completed_clicks = 0

        print(f"Starting autoclicker: {clicks} clicks, {delay}s interval, button '{button}'")
        
        while self.is_running and completed_clicks < clicks:
            time.sleep(delay)
            completed_clicks += 1
            print(f"Click {completed_clicks}/{clicks} ({button}) executed")

        self.is_running = False
        return completed_clicks