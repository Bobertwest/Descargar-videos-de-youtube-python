from pytube import YouTube

link = input("Enter your video url: ")

yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("enter the desire format")
dn_option = int(input("Enter option: "))

dn_video = videos[dn_option]
dn_video.download()

print("download successfully")
