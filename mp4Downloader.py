from pytube import YouTube

def youtube_downloader():
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("Some Errors Occurred")
    print("Done !")

link = input("Enter youtube url: ")
youtube_downloader()

