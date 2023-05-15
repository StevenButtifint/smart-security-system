from multiprocessing import Process, Queue
import cv2
from PIL import Image, ImageTk

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

    def start_feed(self, source):
        self.active = True
        self.process = Process(target=image_capture, args=(self.queue, source,))
        self.process.start()

    def pause_feed(self):
        self.active = False

    def end_feed(self):
        self.process.terminate()
        self.image_frame.config(image='')
