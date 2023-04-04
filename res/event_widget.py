import tkinter as tk
from PIL import Image, ImageTk

from res.constants import *


class EventWidget:
    def __init__(self, parent):
        self.window = parent

        last_event_frame = tk.Frame(self.window, background=EVENT_PREVIEW)
        last_event_frame.place(relx=0.25, rely=0.5, relw=0.4, relh=0.8, anchor="c")

        self.event_frame = tk.Label(last_event_frame, text="No Preview", bg=EVENT_PREVIEW, font=('Corbel', 12))
        self.event_frame.place(relx=0.5, rely=0.5, anchor="c")

        type_title = tk.Label(self.window, text="Type:", bg=TAB_BG_SELECTED, font=('Corbel', 16))
        type_title.place(relx=0.6, rely=0.25, anchor="e")
        self.type = tk.Label(self.window, text=EMPTY_TYPE, bg=TAB_BG_SELECTED, font=('Corbel', 16))
        self.type.place(relx=0.6, rely=0.25, anchor="w")

        time_title = tk.Label(self.window, text="Time:", bg=TAB_BG_SELECTED, font=('Corbel', 16))
        time_title.place(relx=0.6, rely=0.35, anchor="e")
        self.time = tk.Label(self.window, text=EMPTY_TIME, bg=TAB_BG_SELECTED, font=('Corbel', 16))
        self.time.place(relx=0.6, rely=0.35, anchor="w")

        date_title = tk.Label(self.window, text="Date:", bg=TAB_BG_SELECTED, font=('Corbel', 16))
        date_title.place(relx=0.6, rely=0.45, anchor="e")
        self.date = tk.Label(self.window, text=EMPTY_DATE, bg=TAB_BG_SELECTED, font=('Corbel', 16))
        self.date.place(relx=0.6, rely=0.45, anchor="w")

    def clear_type(self):
        self.type.config(text=EMPTY_TYPE)

    def clear_time(self):
        self.time.config(text=EMPTY_TIME)

    def clear_date(self):
        self.date.config(text=EMPTY_DATE)

    def clear_labels(self):
        self.clear_type()
        self.clear_date()
        self.clear_time()

