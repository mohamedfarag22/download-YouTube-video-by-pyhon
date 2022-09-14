
import pytube

print("Download video youtube from web ")

url = input("Enter your link youtube to download : ")

pytube.YouTube(url).streams.get_highest_resolution().download("D:/")

print("video is Downloaded :)")
