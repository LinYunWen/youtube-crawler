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


    def get_channel(self, filter):
        payload = {
            'part': ','.join(self.parts),
            'key': f'{API_KEY}'
        }
        payload.update(filter)
        res = requests.get(f'{self.base_url}/channels', payload)
        return res.json()


    def get_channel_id(self, channel):
        username = channel['username']
        if len(username) != 0:
            res = self.get_channel({ 'forUsername': username })
            items = res['items']
            return channel['id'] if len(items) == 0 else items[0]['id']
        return channel['id']


    # def get_video_ids_in_channel(self, channel):
    #     id = channel['id']
    #     if len(id) == 0: