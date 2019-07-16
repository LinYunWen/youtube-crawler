
import os, sys, argparse, datetime
import isodate
from pytube_api import get_videos
from op_data import set_data, get_data
from Utils import Utils


utils = Utils()
channels = get_data('data/news_channel.json')


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', default='', help='the file path of video id')
    parser.add_argument('--no-prepare', '-np', default=False, action='store_true', help='skip the procedure of preparing')
    parser.add_argument('--unlimited', default=False, action='store_true', help='disable the limit to the number of video')
    return parser.parse_args()


def makedirs():
    os.makedirs('data/video_info', exist_ok=True)
    os.makedirs('data/video_id', exist_ok=True)
    os.makedirs('result/video', exist_ok=True)


def get_video_id(data, type = 'all'):
    if len(data) != 0:
        return data

    result = {}
    for filename in os.listdir('data'):
        if filename == 'news_channel.json':
            continue
        temp = utils.get_data(filename)

        data[filename[: -5]] = temp
    return result


def prepare(arg):
    makedirs()
    if len(arg.file) > 0: return

    utils.complete_data_file()

    for channel in channels:
        id = channel['id']
        temp = utils.get_video_info_in_channel(channel)
        set_data(temp, f'data/video_info/{id}.json')

        text = []
        for video in temp['videos']:
            text.append([video['id'], video['contentDetails']['duration']])
        set_data(text, f'data/video_id/{id}.csv', 'csv')


def is_too_long(str):
    return isodate.parse_duration(str) > datetime.timedelta(seconds=1800)


def load_data(filename):
    data = get_data(filename, 'csv')

    results = []
    for item in data:
        if len(item) > 1:
            if is_too_long(item[1]):
                continue
        results.append(item[0])
    return results


def main(arg):
    if not arg.no_prepare:
        prepare(arg)

    if arg.file == '':
        data = []
        for filename in os.listdir('data/video_id'):
            video_ids = load_data(f'data/video_id/{filename}')
            print(f'download: {filename}')
            get_videos(filename[: -4], video_ids)

    else:
        data = load_data(arg.file)
        get_videos(arg.file[: -4], video_ids)


if __name__ == "__main__":
    arg = parse_argv()
    utils.arg = arg
    main(arg)
