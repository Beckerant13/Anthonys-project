from yt_dlp import YoutubeDL
from sys import argv, exit
import os

if len(argv) < 2:
    print("Usage: python Youtube_downloader.py <YouTube_video_link>")
    exit(1)
    
link = argv[1]

output_folder = 'yt vids'
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
}

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(link, download=True)

print("Download completed!")


