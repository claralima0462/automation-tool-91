import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()  # Assuming the response is JSON
        except RequestException as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_retries:
                time.sleep(delay)
            else:
                print("All attempts failed.")
                raise  # Reraise the last exception

# Example usage of the retry_request function:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as ex:
        print(f"Failed to fetch data: {ex}")