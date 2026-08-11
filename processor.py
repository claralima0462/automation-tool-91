import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    raise NetworkError(f'Failed to fetch data from {url} after {max_retries} attempts')

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)