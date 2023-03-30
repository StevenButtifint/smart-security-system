import tkinter as tk
from PIL import Image, ImageTk

import cv2

from res.constants import *


class EventWidget:
    def __init__(self, parent):
        self.window = parent

        last_event_frame = tk.Frame(self.window, background=EVENT_PREVIEW)
        last_event_frame.place(relx=0.25, rely=0.5, relw=0.4, relh=0.8, anchor="c")

        self.event_frame = tk.Label(last_event_frame, text="No Preview", bg=EVENT_PREVIEW, font=('Corbel', 12))
        self.event_frame.place(relx=0.5, rely=0.5, anchor="c")

