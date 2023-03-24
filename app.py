import tkinter as tk
from res.constants import *


class GUI:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(DIMENSIONS)
        self.window.title(TITLE)
        self.window.iconbitmap(resource_path(APP_ICON_DIR))


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
