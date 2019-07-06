import requests
from key import API_KEY, ACCESS_TOKEN


BASE_URL = 'https://www.googleapis.com/youtube/v3'
HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}


def get(url, payload):
    response = requests.get(url, params=payload, headers=HEADERS)
    return response.json()


def get_channel():
    payload = {
        'part': 'snippet%2CcontentDetails%2Cstatistics',
        'forUsername': 'CNN',
        'key': f'{API_KEY}'
    }
    return get(f'{BASE_URL}/channels', payload)
