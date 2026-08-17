class ClickerException(Exception):
    """Base exception for the autoclicker tool."""
    pass

class ConfigurationError(ClickerException):
    """Raised when there is a configuration issue."""
    pass

class InvalidClickRateError(ClickerException):
    """Raised when the click rate is invalid."""
    
    def __init__(self, rate: float) -> None:
        super().__init__(f"Invalid click rate: {rate}")
        self.rate = rate

class ClickerNotReadyError(ClickerException):
    """Raised when the autoclicker is not ready to start clicking."""
    pass

class ClickerAlreadyRunningError(ClickerException):
    """Raised when an attempt is made to start the clicker that is already running."""
    pass
