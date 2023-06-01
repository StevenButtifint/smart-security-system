import tkinter as tk
import tkinter.font as font
from datetime import datetime

from res.event_widget import EventWidget
from res.video_feed import VideoFeed
from res.detector import Detector
from res.operations import *
from res.constants import *


class GUI:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(DIMENSIONS)
        self.window.title(TITLE)
        self.window.iconbitmap(resource_path(APP_ICON_DIR))
        self.window.config(bg=MAIN_BG)
        set_style()

        video_frame = tk.Frame(self.window, bg="black")
        video_frame.place(relx=0.01, rely=0.055, relw=0.5, relh=0.5, anchor="nw")
        self.video_label = tk.Label(master=video_frame, bg="black", fg="grey", text="Video Feed Disabled")
        self.video_label.place(relx=0.5, rely=0.5, relw=1, relh=1, anchor='c')

        self.videoFeed = VideoFeed(self.video_label)
        self.detector = Detector()

        tools_frame = tk.Frame(self.window, bg=TOOLBAR_BG)
        tools_frame.place(relx=0, rely=0, relw=1, relh=0.041, anchor="nw")

        source_label = tk.Label(tools_frame, text="Source:", bg=TOOLBAR_BG, fg=TOOLBAR_FG)
        source_label.config(font=font.Font(slant="italic", size=13))
        source_label.place(relx=0.005, rely=0.06, anchor="nw")

        self.video_feed_option = tk.StringVar(self.window)
        self.video_feed_option.set(VIDEO_FEED_OPTIONS[0])

        video_feed_menu = tk.OptionMenu(self.window, self.video_feed_option, *VIDEO_FEED_OPTIONS)
        video_feed_menu.config(highlightthickness=0, bg=TOOLBAR_BG)
        video_feed_menu.place(relx=0.06, rely=0, relw=0.07, relh=TOOLS_HEIGHT, anchor="nw")

        self.video_feed_button = tk.Button(master=self.window, text='Enable Video Feed', bg=TOOLBAR_BG, command=lambda: self.toggle_video_feed())
        self.video_feed_button.place(relx=0.13, rely=0.0, relw=0.1, relh=TOOLS_HEIGHT, anchor="nw")

        detector_label = tk.Label(tools_frame, text="Detector:", bg=TOOLBAR_BG, fg=TOOLBAR_FG)
        detector_label.config(font=font.Font(slant="italic", size=13))
        detector_label.place(relx=0.24, rely=0.06, anchor="nw")

        self.detector_option = tk.StringVar(self.window)
        self.detector_option.set(DETECTOR_OPTIONS[0])

        detector_menu = tk.OptionMenu(self.window, self.detector_option, *DETECTOR_OPTIONS)
        detector_menu.config(highlightthickness=0, bg=TOOLBAR_BG)
        detector_menu.place(relx=0.305, rely=0, relw=0.072, relh=TOOLS_HEIGHT, anchor="nw")

        config_button = tk.Button(master=self.window, text='Options', bg=TOOLBAR_BG, command=lambda: self.notebook.select(self.tabs[2]))
        config_button.place(relx=0.377, rely=0.0, relw=0.055, relh=TOOLS_HEIGHT, anchor="nw")


        events_label = tk.Label(tools_frame, text="Events Log", bg=TOOLBAR_BG, fg="white")
        events_label.config(font=font.Font(slant="italic", size=15))
        events_label.place(relx=0.71, rely=0.037, anchor="nw")


    def event_selected(self, event):
        row_id = self.events_view.focus()
        row_content = self.events_view.item(row_id).get("values")
        self.selected_event.set_date(row_content[0])
        self.selected_event.set_time(row_content[1])
        self.selected_event.set_type(row_content[2])
        self.notebook.select(self.tabs[1])


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
