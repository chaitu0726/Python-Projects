# Youtube Video Downloader

from pytube import YouTube
import time

SAVE_PATH = "E:/"

LINK = "" # Copy youtube video Link here

try:
	yt = YouTube(LINK)
except:
	print('Conncetion Error')


# Video Length
len_in_seconds = yt.length - 1
original_len = time.strftime("%H:%M:%S", time.gmtime(len_in_seconds)) 
print(original_len)

# Video Dowloading 

try:
    stream = yt.streams.first()
    stream.download(SAVE_PATH) 
except: 
    print("Download Failed !!") 
print('Task Completed!')