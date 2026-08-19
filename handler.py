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
            return response.json()  # Return JSON data if successful
        except requests.exceptions.HTTPError as err:
            raise NetworkError(f'HTTP error occurred: {err}')
        except requests.exceptions.ConnectionError:
            print(f'Connection error, retrying {retries + 1}/{max_retries}...')
            time.sleep(backoff_factor * (2 ** retries))  # Exponential backoff
            retries += 1
        except requests.exceptions.Timeout:
            print('Request timed out, retrying...')
            retries += 1
    raise NetworkError('Max retries exceeded')

# Example usage:
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except NetworkError as ne:
#         print(f'Failed to retrieve data: {ne}')
