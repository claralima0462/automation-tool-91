import re

def is_valid_click_interval(interval):
    """
    Validate the click interval input.
    :param interval: The interval to validate.
    :return: True if valid, else False.
    """
    return isinstance(interval, (int, float)) and interval > 0


def is_valid_click_count(count):
    """
    Validate the click count input.
    :param count: The count to validate.
    :return: True if valid, else False.
    """
    return isinstance(count, int) and count > 0


def is_valid_position(position):
    """
    Validate the click position input.
    :param position: A tuple representing (x, y) coordinates.
    :return: True if valid, else False.
    """
    return (isinstance(position, tuple) and len(position) == 2
            and all(isinstance(coord, int) for coord in position))


def validate_inputs(click_interval, click_count, click_position):
    """
    Validate all inputs before initiating autoclick.
    :param click_interval: Interval between clicks.
    :param click_count: Total number of clicks to perform.
    :param click_position: Coordinates where to perform clicks.
    :return: A tuple of validation results (interval_valid, count_valid, position_valid).
    """
    interval_valid = is_valid_click_interval(click_interval)
    count_valid = is_valid_click_count(click_count)
    position_valid = is_valid_position(click_position)
    return interval_valid, count_valid, position_valid
