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

    def set_dot(self, state):
        self.show_dot = state

    def set_label(self, state):
        self.show_label = state

    def update_existing_objects(self, new_dots):
        self.existing_objects = new_dots


    @staticmethod
    def save_last_detection(image, box):
        # save detected area  [ y1:y2, x1:x2 ]
        cv2.imwrite(resource_path(LAST_EVENT_DIR), image[box[1]:box[1] + box[3], box[0]:box[0] + box[2]])
