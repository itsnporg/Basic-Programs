# GUI youtube video downloader using python, pytube, tkinter
from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import width
import pytube


# Creating window
window=Tk()
window.title("Youtube Video Downloader")
window.geometry("400x200")
window.resizable(0, 0)


labelframe=ttk.Frame(window)
label=ttk.Label(labelframe, text="Youtube Video Downloader", font=('Arial', 20))
label.grid(row=0, column=0)
labelframe.grid(row=0, column=0, padx=25, pady=10)

centerframe=ttk.Frame(window)
urllabel=ttk.Label(centerframe, text="Enter Video Url: ")
text_box=ttk.Entry(centerframe, width=40)
download_button=ttk.Button(centerframe, text="Download Video")

urllabel.grid(row=0, column=0)
text_box.grid(row=0, column=1)
download_button.grid(row=1, column=1, pady=15)
centerframe.grid(row=1, column=0, pady=15)

def download_video():
    try:
        url=text_box.get()
        yt=pytube.YouTube(url)
        video=yt.streams.filter(only_video=True).first()
        video.download()
        messagebox.showinfo("Download Success", "Video Downloaded Successfully")
    except:
        messagebox.showerror("Error", "Please Enter Valid Url")

download_button.config(command=download_video)

window.mainloop()
