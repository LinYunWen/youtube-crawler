
import os, sys
from pytube import YouTube
from api import get_channel


def main():
    # YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0').streams.first().download()
    yt = YouTube('https://www.youtube.com/watch?v=83qcqPGrFc0')
    print(yt.streams.all())
    print(get_channel())
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("finish");


if __name__ == "__main__":
    main()
