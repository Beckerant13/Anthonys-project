from pytube import YouTube
from sys import argv 
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

output_folder = 'Youtube_memes'

os.makedirs(output_folder, exist_ok=True)

yd.download(output_folder)

print("Download completed!")


