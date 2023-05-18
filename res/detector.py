import numpy as np
import cv2
from PIL import Image, ImageTk

from res.constants import *
from res.operations import resource_path


class Detector:
    def __init__(self):
        self.net = cv2.dnn.readNet(MODEL_DIR)
        self.existing_objects = []
        self.class_list = self.get_class_list()
        self.show_dot = False
        self.show_label = False

