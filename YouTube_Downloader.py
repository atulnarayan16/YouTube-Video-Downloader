from tkinter import *
import pytube
from PIL import ImageTk, Image
root = Tk()
root.configure(bg='red')
root.title('Youtube Downloader', )
h = Label(root, text="YOUTUBE DOWNLOADER", font=('Times New Roman', 15, 'bold'))
h.pack()


def click(*args):
    e.delete(0, 'end')



e = Entry(root, width=60)
e.insert(0, 'Enter URL of YouTube Video ')
e.pack(padx= 60,pady=60)
e.bind("<Button-1>", click)

def click():
    SAVE_PATH = "PATH TO SAVE VIDEO"
    url = e.get()

    yt = pytube.YouTube(url)
    highresvid = yt.streams.get_highest_resolution()
    highresvid.download(SAVE_PATH)
    lab = Label(root, text="Video Downloaded", bg="green")
    lab.pack()


b1 = Button(text="Download", command=click)
b1.pack(padx=20,pady=20)
root.mainloop()
