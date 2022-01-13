import re
import os
try:
    os.system("pip install pytube")
    from pytube import Playlist
except:
    print("\nError while installing PyTube")

playlist_to_download=input("\nPlaylist to download : ")

playlist = Playlist(playlist_to_download)

cur_dir=input("\nLocation to save the videos : ")

for video in playlist.videos:
    print('\nDownloading : {} \n\tURL : {}'.format(video.title, video.watch_url))
    video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cur_dir)