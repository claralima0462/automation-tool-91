"""Validation utilities for autoclicker configuration and input parameters."""

from typing import Tuple, Optional


class ValidationError(Exception):
    """Raised when configuration parameters fail validation checks."""
    pass


def validate_coordinates(x: int, y: int, screen_bounds: Optional[Tuple[int, int]] = None) -> Tuple[int, int]:
    """Validate click coordinates against screen boundaries and edge cases."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError(f"Coordinates must be integers, got ({type(x).__name__}, {type(y).__name__})")
    
    if x < 0 or y < 0:
        raise ValidationError(f"Coordinates cannot be negative: ({x}, {y})")
        
    if screen_bounds:
        max_x, max_y = screen_bounds
        if x > max_x or y > max_y:
            raise ValidationError(f"Coordinates ({x}, {y}) exceed screen bounds ({max_x}, {max_y})")
            
    return x, y


def validate_interval(interval: float, min_interval: float = 0.001) -> float:
    """Validate click interval to prevent system lockup from extremely high frequency."""
    try:
        val = float(interval)
    except (ValueError, TypeError):
        raise ValidationError(f"Interval must be a valid number, got {interval}")

    if val < 0:
        raise ValidationError(f"Interval cannot be negative: {val}")

    if val < min_interval:
        raise ValidationError(f"Interval {val}s is below safety threshold of {min_interval}s")

    return val


def validate_click_count(count: int) -> int:
    """Validate repetition count for clicks."""
    if not isinstance(count, int):
        raise ValidationError(f"Click count must be an integer, got {type(count).__name__}")
    if count < 0:
        raise ValidationError(f"Click count cannot be negative: {count}")
    return count
