from pytube import YouTube
import tkinter as tk


def youtube_downloader():
    youtube_object = YouTube(entry.get())
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("Some Errors Occurred")
    labelResult.configure(text="Task Completed!")




root = tk.Tk()
lengthInput = tk.IntVar()
strengthInput = tk.IntVar()

root.title("Course Evaluation Project")

lengthLabel = tk.Label(root, text = "Youtube Link Input:").grid(row=0, column=0)
entry = tk.Entry(root, width=100)
entry.grid(row=1, column=0)
copyButton = tk.Button(root, text = "Convert to MP4", width=25, command=youtube_downloader)
copyButton.grid(row=2, column=0)
labelResult = tk.Label(root, text="")
labelResult.grid(row=3, column=0)
root.mainloop()