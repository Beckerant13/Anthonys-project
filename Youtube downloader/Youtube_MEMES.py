from pytube import YouTube
from sys import argv, exit
import os

if len(argv) < 2:
    print("Usage: python youtube_downloader.py <YouTube_video_link>")
    exit(1)

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

output_folder = 'Youtube memes'
os.makedirs(output_folder, exist_ok=True)

yd.download(output_folder)

print("Download completed!")



