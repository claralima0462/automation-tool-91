import time
import urllib.request
import urllib.error
import logging

logger = logging.getLogger("autoclicker.core")

def execute_network_request(url: str, max_retries: int = 3, backoff_factor: float = 1.5) -> bytes:
    """Executes an HTTP GET request with exponential backoff retry logic.
    
    Used by automation-tool-91 to fetch remote auto-clicker configurations
    and cloud macro updates safely.
    """
    delay = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Attempt {attempt}/{max_retries}: Fetching data from {url}")
            req = urllib.request.Request(url, headers={"User-Agent": "AutomationTool91/1.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    logger.info("Network operation succeeded")
                    return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as err:
            logger.warning(f"Network request failed on attempt {attempt}: {err}")
            if attempt == max_retries:
                logger.error("Maximum retry limit reached for network operation")
                raise err
            time.sleep(delay)
            delay *= backoff_factor
            
    raise RuntimeError("Unexpected failure in network retry loop")

class ProfileSyncManager:
    """Manages remote profile synchronization for the auto-clicker engine."""
    
    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    def fetch_latest_profile(self) -> str:
        """Downloads the latest click sequence profile using retry logic."""
        raw_data = execute_network_request(self.endpoint_url)
        return raw_data.decode("utf-8")
