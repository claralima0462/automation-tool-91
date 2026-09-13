class AutomationError(Exception):
    """Base exception for automation-tool-91 errors."""
    pass

class ConfigurationError(AutomationError):
    """Raised when config file is invalid or missing."""
    pass

class HardwareInputError(AutomationError):
    """Raised when mouse or keyboard injection fails."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when an automation sequence times out."""
    pass

class InterruptSignal(AutomationError):
    """Raised when the user interrupts the automation process."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized error reporting for the automation process."""
    if isinstance(exc, AutomationError):
        print(f"[Automation Error]: {exc}")
    else:
        print(f"[Unexpected System Error]: {type(exc).__name__} - {exc}")