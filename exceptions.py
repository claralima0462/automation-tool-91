from typing import Optional

class AutomationError(Exception):
    """Base exception class for all automation-tool-91 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ClickerConfigurationError(AutomationError):
    """Raised when the configuration parameters are invalid."""
    pass

class CoordinateOutOfBoundsError(AutomationError):
    """Raised when click coordinates fall outside screen bounds."""
    def __init__(self, x: int, y: int) -> None:
        super().__init__(f"Coordinates ({x}, {y}) are outside screen bounds.", 400)

class ExecutionTimeoutError(AutomationError):
    """Raised when an automation sequence exceeds its duration limit."""
    def __init__(self, duration: float) -> None:
        super().__init__(f"Execution timed out after {duration} seconds.", 408)

class DriverConnectionError(AutomationError):
    """Raised when input driver fails to interface with OS."""
    def __init__(self, driver_name: str) -> None:
        super().__init__(f"Failed to connect to input driver: {driver_name}", 503)