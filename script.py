# import re
# import os
# try:
#     os.system("pip install pytube")
#     # from pytube import Playlist
#     import pytube
# except:
#     print("\nError while installing PyTube")

# print("Download type :")
# print("1. Video")
# print("2. Playlist")
# ch=input("Select from above choices:")
# if ch=="1" or ch=="Video":
#     video_url=input("\nVideo url to download : ")
#     yt = pytube.YouTube(video_url)
#     cur_dir=input("\nLocation to save the video : ")
#     yt.streams.get_highest_resolution().download(cur_dir)

# elif ch=="2" or ch=="Playlist":
#     playlist_to_download=input("\nPlaylist to download : ")

#     playlist = pytube.Playlist(playlist_to_download)

#     cur_dir=input("\nLocation to save the videos : ")

#     for video in playlist.videos:
#         print('\nDownloading : {} \nURL : {}'.format(video.title, video.watch_url))
#         # video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cur_dir)
#         yt = pytube.YouTube(video.watch_url)
#         yt.streams.get_highest_resolution().download(cur_dir)
# else:
#     print("Invalid input check again!")
import re
import os
try:
    os.system("pip install pytube")
    # from pytube import Playlist
    import pytube
except:
    print("\nError while installing PyTube")

print("Download type :")
print("1. Video")
print("2. Playlist")
ch=input("Select from above choices:")
if ch=="1" or ch=="Video":
    video_url=input("\nVideo url to download : ")
    yt = pytube.YouTube(video_url)
    cur_dir=input("\nLocation to save the video : ")
    yt.streams.get_highest_resolution().download(cur_dir)

elif ch=="2" or ch=="Playlist":
    playlist_to_download="https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q"

    playlist = pytube.Playlist(playlist_to_download)

    cur_dir=input("\nLocation to save the videos : ")
    x = [ video for video in playlist.videos ]

    for video in x[64:]:
        print('\nDownloading : {} \nURL : {}'.format(video.title, video.watch_url))
        # video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cur_dir)
        yt = pytube.YouTube(video.watch_url)
        yt.streams.get_highest_resolution().download(cur_dir)
else:
    print("Invalid input check again!")