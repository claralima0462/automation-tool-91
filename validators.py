import re

class ClickConfigValidator:
    """Validates autoclicker configuration parameters."""
    
    @staticmethod
    TOLERANCE_MIN = 1
    TOLERANCE_MAX = 1000
    
    @classmethod
    def validate_interval(cls, interval: float) -> float:
        """Ensure click interval is safe and positive."""
        try:
            val = float(interval)
        except (TypeError, ValueError):
            raise ValueError("Interval must be a numeric value.")
            
        if val < 0.01:
            raise ValueError("Interval cannot be less than 10ms for safety.")
        return val

    @classmethod
    def validate_coordinates(cls, x: int, y: int) -> tuple[int, int]:
        """Ensure screen coordinates are within integer bounds."""
        try:
            coord_x = int(x)
            coord_y = int(y)
        except (TypeError, ValueError):
            raise ValueError("Coordinates must be integers.")
            
        if coord_x < 0 or coord_y < 0:
            raise ValueError("Coordinates cannot be negative.")
            
        return coord_x, coord_y

    @classmethod
    def validate_hotkey(cls, hotkey: str) -> str:
        """Validate hotkey string format."""
        if not isinstance(hotkey, str) or not hotkey.strip():
            raise ValueError("Hotkey must be a non-empty string.")
            
        cleaned = hotkey.strip().lower()
        if not re.match(r'^[a-z0-9_\+\-]+$', cleaned):
            raise ValueError(f"Invalid hotkey format: {hotkey}")
            
        return cleaned
