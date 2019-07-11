
import os, sys
from pytube import YouTube
from op_data import set_data, get_data
from Utils import Utils

utils = Utils()
channels = get_data('data/news_channel.json')


def send_request(download_path, video_id):
    try:
        print(video_id)
        YouTube(f'https://www.youtube.com/watch?v={video_id}').streams.filter(progressive=True, file_extension='mp4').first().download(download_path, video_id)
    except:
        print(f'Error on download {video_id}')
    # yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    # print(yt.streams.filter(progressive=True, file_extension='mp4').all())
    # print(yt.streams.filter(file_extension='mp4').order_by('res'))
    # yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first().download()


def get_videos(channel_id = None, video_ids = None):
    if channel_id == None or video_ids == None:
        return

    download_path = f'result/video/{channel_id}'
    os.makedirs(download_path, exist_ok=True)
    list(map(lambda item: send_request(download_path, item), video_ids))


if __name__ == "__main__":
    get_video()
