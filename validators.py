def validate_click_params(interval, count):
    """Validates autoclicker parameters to prevent system freezing."""
    # Ensure interval is a float within a safe range (0.01s to 60s)
    if not isinstance(interval, (int, float)) or not (0.01 <= interval <= 60.0):
        raise ValueError(f"Invalid interval: {interval}. Must be between 0.01 and 60.0 seconds.")

    # Ensure count is a positive integer or -1 for infinite
    if not isinstance(count, int) or (count < 1 and count != -1):
        raise ValueError(f"Invalid count: {count}. Must be -1 or a positive integer.")

    return True

def validate_coordinates(x, y):
    """Validates screen coordinates for pointer events."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Coordinates must be integers.")
    
    if x < 0 or y < 0:
        raise ValueError("Coordinates cannot be negative.")
        
    return True