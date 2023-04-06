import numpy as np
from multiprocessing import Process, Queue
from queue import Empty
import cv2
import cv2 as cv
from PIL import Image, ImageTk
import time
import tkinter as tk

from .operations import image_capture


class VideoFeed:
    def __init__(self, image_frame):
        self.queue = Queue()
        self.active = False
        self.process = None
        self.last_frame = None
        self.image_frame = image_frame

    def update_image(self):
        frame = self.queue.get()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        a = Image.fromarray(im)
        a = a.resize((600, 338))
        b = ImageTk.PhotoImage(image=a)
        self.image_frame.configure(image=b)
        self.image_frame._image_cache = b
        self.set_last_frame(a)

    def set_last_frame(self, frame):
        self.last_frame = frame

    def get_last_frame(self):
        return self.last_frame

