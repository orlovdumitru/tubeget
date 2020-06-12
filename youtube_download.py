from pytube import YouTube
import os


def downloadYoutube(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    
    yt.download(path)

url = input('Input url:\n')
path = input('Where to store file:\n')
downloadYoutube(url, path)