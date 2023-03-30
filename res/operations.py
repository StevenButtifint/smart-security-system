import os
import cv2


def image_capture(queue, source):
   vidFile = cv2.VideoCapture(source)
   while True:
      try:
         flag, frame = vidFile.read()
         if flag == 0:
            break
         queue.put(frame)
         cv2.waitKey(200)
      except:
         continue


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
