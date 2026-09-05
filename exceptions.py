class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""
    def __init__(self, message: str = "An automation error occurred"):
        self.message = message
        super().__init__(self.message)


class TargetNotFoundError(AutoClickerError):
    """Raised when a visual target or UI element cannot be located."""
    def __init__(self, target_name: str):
        self.target_name = target_name
        super().__init__(f"Target element '{target_name}' could not be found on screen.")


class InvalidRegionError(AutoClickerError):
    """Raised when screen coordinates or boundary regions are invalid."""
    def __init__(self, coordinates: tuple):
        self.coordinates = coordinates
        super().__init__(f"Invalid screen coordinates or region boundaries: {coordinates}")


class ClickTimeoutError(AutoClickerError):
    """Raised when an automated action exceeds the allowed execution time."""
    def __init__(self, action_name: str, timeout: float):
        self.action_name = action_name
        self.timeout = timeout
        super().__init__(f"Action '{action_name}' timed out after {timeout} seconds.")


class ActionCancelledError(AutoClickerError):
    """Raised when an ongoing automation task is interrupted or cancelled."""
    def __init__(self, reason: str = "User requested cancellation"):
        self.reason = reason
        super().__init__(f"Automation task cancelled: {reason}")
