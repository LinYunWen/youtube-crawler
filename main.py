
import os, sys
from pytube import YouTube
from op_data import set_data, get_data
from Utils import Utils

utils = Utils()
channels = get_data('data/news_channel.json')


def main():
    # YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0').streams.first().download()
    # yt = YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0')
    # print(yt.streams.all())
    # print(get_channel())

    for channel in channels:
        id = channel['id']
        set_data(utils.get_video_info_in_channel(channel), f'data/{id}.json')
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


if __name__ == "__main__":
    # complete_data_file()
    main()
