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

    def scan_frame(self, captured_frame, display_frame):
        image = np.asarray(captured_frame)
        blob, input_image = self.format_image(image)

        predictions = self.get_predictions(blob)
        class_ids, confidences, boxes, class_id = self.filter_predictions(predictions, input_image)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.25, 0.45)
        result_class_ids, result_boxes = self.get_detection_results(indexes, class_ids, boxes)

        new_dots = []
        new_detections = []

        for i in range(len(result_class_ids)):
            if self.class_list[class_id] in OBJECT_TYPES:
                box = result_boxes[i]

                # if there is an existing object dot in the area then its not a new object
                if not self.is_existing(box):
                    new_detections.append((self.class_list[class_id], "A " + self.class_list[class_id] + " was detected."))
                    self.save_last_detection(image, box)

                self.draw_detection_box(image, box)
                self.save_dot(box, new_dots)

                if self.show_dot:
                    self.draw_dot(image, box)

                if self.show_label:
                    self.draw_detection_label(image, box, result_class_ids[i])

        self.update_existing_objects(new_dots)
        self.update_display_image(display_frame, image)
        return new_detections


    @staticmethod
    def get_class_list():
        with open(resource_path(CLASSES_DIR), "r") as f:
            class_list = [cname.strip() for cname in f.readlines()]
        return class_list

    @staticmethod
    def save_last_detection(image, box):
        # save detected area  [ y1:y2, x1:x2 ]
        cv2.imwrite(resource_path(LAST_EVENT_DIR), image[box[1]:box[1] + box[3], box[0]:box[0] + box[2]])
