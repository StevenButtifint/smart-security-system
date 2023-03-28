import tkinter as tk
from PIL import Image, ImageTk

import cv2

from res.constants import *


class EventWidget:
    def __init__(self, parent):
        self.window = parent

