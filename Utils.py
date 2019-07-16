from API import API
from op_data import set_data, get_data

resultsPerPage = 100
channels = get_data('data/news_channel.json')


class Utils():
    def __init__(self):
        self.api = API()
        self.arg = []
        self.channels = get_data('data/news_channel.json')


    def get_channel_id(self, channel):
        username = channel['username']
        if len(username) != 0:
            res = self.api.get_channels({
                'part': 'id',
                'forUsername': username
            })
            items = res['items']
            return channel['id'] if len(items) == 0 else items[0]['id']
        return channel['id']


    def complete_data_file(self):
        for index, channel in enumerate(channels):
            id = self.get_channel_id(channel)
            if len(id) != 0:
                channels[index]['id'] = id

        set_data(channels, 'data/news_channel.json')


    def get_video_info_in_channel(self, channel):
        infos = []
        videos = self.get_videos_in_channel(channel)
        return {
            'title': channel['title'],
            'num': len(videos),
            'videos': videos
        }


    def get_videos_in_channel(self, channel):
        results = []
        totalResults = 0
        nextPageToken = ''

        i = 0
        while True:
            res = self.api.search({
                'pageToken': nextPageToken,
                'channelId': channel['id'],
                'maxResults': resultsPerPage,
                'order': 'date',
                'type': 'video'
            })
            results.extend(
                self.get_videos_info(
                    list(map(lambda item: item['id']['videoId'], res['items']))
                )
            )

            totalResults = res['pageInfo']['totalResults']
            if 'nextPageToken' not in res:
                break
            nextPageToken = res['nextPageToken']
            i += 1

            if not arg.unlimited or i > 10:
                break
        return results


    def get_videos_info(self, ids):
        videos = self.api.get_videos({
            'part': 'snippet,contentDetails,statistics',
            'id': ','.join(ids),
            'maxResults': resultsPerPage
        })
        def remove_keys(video):
            for key in ['kind', 'etag']:
                video.pop(key)
            for key in ['channelId', 'thumbnails', 'channelTitle', 'liveBroadcastContent', 'localized']:
                video['snippet'].pop(key)
            return video

        return list(map(remove_keys, videos['items']))


