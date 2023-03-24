import tkinter as tk


class GUI:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(DIMENSIONS)
        self.window.title(TITLE)


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
