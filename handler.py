import logging
import time

logger = logging.getLogger(__name__)

def process_click_sequence(interval: float, count: int):
    """Executes the autoclicker logic with input validation."""
    
    # Input validation for core parameters
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f"Invalid interval: {interval}. Must be >= 0.01 seconds.")
        return

    if not isinstance(count, int) or count <= 0:
        logger.error(f"Invalid count: {count}. Must be a positive integer.")
        return

    logger.info(f"Starting sequence: {count} clicks at {interval}s interval")

    try:
        for i in range(count):
            # Simulating click operation
            logger.debug(f"Executing click {i + 1}/{count}")
            time.sleep(interval)
            
    except Exception as e:
        logger.exception(f"Sequence interrupted: {e}")

def main():
    # Example usage
    config = {"interval": 0.5, "count": 10}
    process_click_sequence(config["interval"], config["count"])

if __name__ == "__main__":
    main()