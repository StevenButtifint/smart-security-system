import os
import cv2

from tkinter import ttk

from res.constants import *

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


def set_style():
    a = ttk.Style()
    a.map(a)
    a.theme_use("clam")
    a.configure('.',
                relief='flat',
                borderwidth=0,
                highlightthickness=0)

    a.map("Custom.Treeview", background=[('selected', EVENT_RECORD)])

    a.configure("Treeview",
                foreground=TREE_HEADING_BG,
                fieldbackground=TREE_COLUMNS_BG,
                borderwidth=0,
                highlightthickness=0,
                bordercolor=TOOLBAR_BG,
                lightcolor=TOOLBAR_BG)

    a.configure('Treeview.map',
                background=[("selected", EVENT_RECORD), ("!selected", EVENT_RECORD)])

    a.configure('Treeview.Heading',
                background=TREE_HEADING_BG,
                foreground=TREE_HEADING_FG)

    a.layout("TNotebook", [])

    a.configure("TNotebook",
                background=NOTEBOOK_BG,
                highlightbackground="#848a98",
                tabmargins=0)

    a.configure("TNotebook.Tab",
                background=TAB_BG,
                foreground=TAB_FG,
                padding=[29, 5, 29, 2],
                font=('Arial', '16'),
                focuscolor=a.configure(".")["background"])

    a.map("TNotebook.Tab",
          padding=[("selected", [29, 5, 29, 2])],
          background=[("selected", TAB_BG_SELECTED)])
