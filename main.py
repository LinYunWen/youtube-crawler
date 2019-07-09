
import os, sys
from pytube import YouTube
from API import API
from op_data import set_data, get_data


api = API()


def complete_data_file():
    channels = get_data('news_channel.json')
    for index, channel in enumerate(channels):
        id = api.get_channel_id(channel)
        if len(id) != 0:
            channels[index]['id'] = id

    set_data(channels, 'news_channel.json')


def main():
    # YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0').streams.first().download()
    yt = YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0')
    print(yt.streams.all())
    # print(get_channel())
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("finish");


if __name__ == "__main__":
    # complete_data_file()
    main()
