import requests
from key.key import API_KEY, ACCESS_TOKEN


class API():
    def __init__(self):
        self.base_url = 'https://www.googleapis.com/youtube/v3'
        self.header = {
            # 'Authorization': f'Bearer {ACCESS_TOKEN}',
            'Accept': 'application/json'
        }
        self.parts = ['snippet','contentDetails', 'statistics']


    def get(self, url, payload):
        response = requests.get(url, params=payload, headers=self.header)
        return response.json()


    def search(self, params):
        payload = { 'part': 'snippet', 'key': f'{API_KEY}' }
        payload.update(params)
        res = requests.get(f'{self.base_url}/search', payload)
        return res.json()


    def get_videos(self, params):
        payload = { 'key': f'{API_KEY}' }
        payload.update(params)
        res = requests.get(f'{self.base_url}/videos', payload)
        return res.json()


    def get_channels(self, params):
        payload = { 'key': f'{API_KEY}' }
        payload.update(params)
        res = requests.get(f'{self.base_url}/channels', payload)
        return res.json()


    def download_captions(videoId, params):
        payload = { 'key': f'{API_KEY}' }
        payload.update(params)
        res = requests.get(f'{self.base_url}/captions/{videoId}', payload)
        return res.json()

