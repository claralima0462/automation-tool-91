import logging
from typing import Optional

class AutoClickerLogger:
    """Logger for autoclicker events with type annotations."""

    def __init__(self, log_file: str = "autoclicker.log", level: int = logging.INFO) -> None:
        """Set up logger with file and console output.
        Args:
            log_file: Log file path.
            level: Logging level.
        """
        self.logger = logging.getLogger("autoclicker")
        self.logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        # File handler
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_click(self, x: int, y: int, button: str = "left") -> None:
        """Log click at position.
        Args:
            x: X position.
            y: Y position.
            button: Button name.
        """
        self.logger.info(f"Click at ({x},{y}) button={button}")

    def log_start(self, interval: float) -> None:
        """Log automation start.
        Args:
            interval: Seconds between clicks.
        """
        self.logger.info(f"Started with interval {interval}")

    def log_stop(self, clicks: int) -> None:
        """Log automation stop.
        Args:
            clicks: Clicks performed.
        """
        self.logger.info(f"Stopped after {clicks} clicks")

    def log_error(self, msg: str, exc: Optional[Exception] = None) -> None:
        """Log error.
        Args:
            msg: Error message.
            exc: Optional exception.
        """
        if exc:
            self.logger.error(f"{msg} - {exc}")
        else:
            self.logger.error(msg)