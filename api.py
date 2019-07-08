import requests
from key.key import API_KEY, ACCESS_TOKEN


BASE_URL = 'https://www.googleapis.com/youtube/v3'
HEADERS = {
    # 'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}


def get(url, payload):
    response = requests.get(url, params=payload, headers=HEADERS)
    return response.json()


def get_channel():
    parts = ['snippet','contentDetails', 'statistics']
    payload = {
        'part': ','.join(parts),
        'forUsername': 'CNN',
        'key': f'{API_KEY}'
    }
    return get(f'{BASE_URL}/channels', payload)
