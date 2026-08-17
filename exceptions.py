class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ConfigError(CustomError):
    """Raised when configuration is incorrect."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ClickError(CustomError):
    """Raised when clicking fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TimeoutError(CustomError):
    """Raised when a timeout occurs."""
    def __init__(self, message='Operation timed out'):
        self.message = message
        super().__init__(self.message)

class InvalidParameterError(CustomError):
    """Raised when a parameter is invalid."""
    def __init__(self, param):
        self.message = f'Invalid parameter: {param}'
        super().__init__(self.message)
