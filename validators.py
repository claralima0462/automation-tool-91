from typing import Dict, Any, Tuple

class ValidationError(ValueError):
    """Exception raised for invalid click configuration parameters."""
    pass

def validate_click_action(action: Dict[str, Any], screen_resolution: Tuple[int, int] = (3840, 2160)) -> bool:
    """
    Validates the configuration dictionary for a single autoclicker action.
    
    Raises ValidationError if validation fails, otherwise returns True.
    """
    # Validate coordinates presence and type
    coords = action.get("coords")
    if not isinstance(coords, (list, tuple)) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple or list of (x, y) coordinates.")
    
    x, y = coords
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError("Coordinate values must be integers.")
        
    # Validate screen boundary limits
    max_x, max_y = screen_resolution
    if not (0 <= x <= max_x) or not (0 <= y <= max_y):
        raise ValidationError(f"Coordinates ({x}, {y}) exceed target screen limits ({max_x}x{max_y}).")
    
    # Validate click interval/delay
    delay = action.get("delay", 0.1)
    if not isinstance(delay, (int, float)) or delay < 0.001:
        raise ValidationError("Delay must be a positive number of at least 0.001 seconds.")
        
    # Validate click repetition count
    clicks = action.get("clicks", 1)
    if not isinstance(clicks, int) or clicks < 1:
        raise ValidationError("Click count must be an integer of 1 or greater.")
        
    # Validate mouse button input
    button = action.get("button", "left")
    valid_buttons = {"left", "right", "middle"}
    if button not in valid_buttons:
        raise ValidationError(f"Invalid mouse button '{button}'. Must be one of: {', '.join(valid_buttons)}")
        
    return True