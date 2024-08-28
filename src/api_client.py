# src/api_client.py

import requests

def fetch_data_from_api(url):
    """
    Fetch data from a given API endpoint.
    
    :param url: The API endpoint URL.
    :return: A tuple containing the status code and the JSON response (or None if the request fails).
    """
    if url is None:
        url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status is 4xx, 5xx
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None
