class AutomationError(Exception):
    """Base exception for automation-tool-91."""
    pass

class ClickerConfigurationError(AutomationError):
    """Raised when configuration settings are invalid."""
    pass

class InputDeviceError(AutomationError):
    """Raised when the mouse or keyboard input fails."""
    pass

class CoordinateOutOfBoundsError(AutomationError):
    """Raised when clicking outside screen boundaries."""
    def __init__(self, x, y):
        self.message = f"Coordinates ({x}, {y}) are outside valid screen bounds"
        super().__init__(self.message)

class ExecutionTimeoutError(AutomationError):
    """Raised when the clicker fails to trigger within time limits."""
    pass

def validate_coordinates(x, y, max_x, max_y):
    """Check if coordinates are within defined screen resolution."""
    if not (0 <= x <= max_x) or not (0 <= y <= max_y):
        raise CoordinateOutOfBoundsError(x, y)
    return True