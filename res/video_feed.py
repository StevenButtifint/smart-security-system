from multiprocessing import Process, Queue


class VideoFeed:
    def __init__(self, image_frame):
        self.queue = Queue()
        self.active = False
        self.process = None
        self.last_frame = None
        self.image_frame = image_frame
