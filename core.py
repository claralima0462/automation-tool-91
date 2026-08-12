import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, wait_time=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()  # Return JSON if request is successful
        except RequestException as e:
            attempts += 1
            print(f'Network error: {e}, attempt {attempts}/{max_retries}')
            if attempts < max_retries:
                time.sleep(wait_time)  # Wait before retrying
            else:
                print('Max retries reached; raising exception')
                raise

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Failed to retrieve data: {e}')