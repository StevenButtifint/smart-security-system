import tkinter as tk
from res.constants import *


class GUI:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(DIMENSIONS)
        self.window.title(TITLE)
        self.window.iconbitmap(resource_path(APP_ICON_DIR))

        video_frame = tk.Frame(self.window, bg="black")
        video_frame.place(relx=0.01, rely=0.055, relw=0.5, relh=0.5, anchor="nw")
        self.video_label = tk.Label(master=video_frame, bg="black", fg="grey", text="Video Feed Disabled")
        self.video_label.place(relx=0.5, rely=0.5, relw=1, relh=1, anchor='c')


        tools_frame = tk.Frame(self.window, bg=TOOLBAR_BG)
        tools_frame.place(relx=0, rely=0, relw=1, relh=0.041, anchor="nw")



if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
