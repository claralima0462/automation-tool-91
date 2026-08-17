import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=0.5):
    """
    Makes a GET request to the specified URL with retry logic.
    
    :param url: URL to make the GET request.
    :param max_retries: Maximum number of retries before failing.
    :param backoff_factor: Factor by which to increase wait time between retries.
    :return: Response object if successful.
    """
    tries = 0
    while tries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            tries += 1
            if tries == max_retries:
                print(f'Failed to fetch {url} after {max_retries} attempts.')
                raise
            wait_time = backoff_factor * (2 ** tries)
            print(f'Retrying {url} in {wait_time:.1f} seconds...')
            time.sleep(wait_time)