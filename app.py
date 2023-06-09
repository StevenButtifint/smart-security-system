import tkinter as tk
import tkinter.font as font
from datetime import datetime

from res.event_widget import EventWidget
from res.video_feed import VideoFeed
from res.detector import Detector
from res.operations import *
from res.constants import *


class GUI:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(DIMENSIONS)
        self.window.title(TITLE)
        self.window.iconbitmap(resource_path(APP_ICON_DIR))
        self.window.config(bg=MAIN_BG)
        set_style()

        video_frame = tk.Frame(self.window, bg="black")
        video_frame.place(relx=0.01, rely=0.055, relw=0.5, relh=0.5, anchor="nw")
        self.video_label = tk.Label(master=video_frame, bg="black", fg="grey", text="Video Feed Disabled")
        self.video_label.place(relx=0.5, rely=0.5, relw=1, relh=1, anchor='c')

        self.videoFeed = VideoFeed(self.video_label)
        self.detector = Detector()

        tools_frame = tk.Frame(self.window, bg=TOOLBAR_BG)
        tools_frame.place(relx=0, rely=0, relw=1, relh=0.041, anchor="nw")

        source_label = tk.Label(tools_frame, text="Source:", bg=TOOLBAR_BG, fg=TOOLBAR_FG)
        source_label.config(font=font.Font(slant="italic", size=13))
        source_label.place(relx=0.005, rely=0.06, anchor="nw")

        self.video_feed_option = tk.StringVar(self.window)
        self.video_feed_option.set(VIDEO_FEED_OPTIONS[0])

        video_feed_menu = tk.OptionMenu(self.window, self.video_feed_option, *VIDEO_FEED_OPTIONS)
        video_feed_menu.config(highlightthickness=0, bg=TOOLBAR_BG)
        video_feed_menu.place(relx=0.06, rely=0, relw=0.07, relh=TOOLS_HEIGHT, anchor="nw")

        self.video_feed_button = tk.Button(master=self.window, text='Enable Video Feed', bg=TOOLBAR_BG, command=lambda: self.toggle_video_feed())
        self.video_feed_button.place(relx=0.13, rely=0.0, relw=0.1, relh=TOOLS_HEIGHT, anchor="nw")

        detector_label = tk.Label(tools_frame, text="Detector:", bg=TOOLBAR_BG, fg=TOOLBAR_FG)
        detector_label.config(font=font.Font(slant="italic", size=13))
        detector_label.place(relx=0.24, rely=0.06, anchor="nw")

        self.detector_option = tk.StringVar(self.window)
        self.detector_option.set(DETECTOR_OPTIONS[0])

        detector_menu = tk.OptionMenu(self.window, self.detector_option, *DETECTOR_OPTIONS)
        detector_menu.config(highlightthickness=0, bg=TOOLBAR_BG)
        detector_menu.place(relx=0.305, rely=0, relw=0.072, relh=TOOLS_HEIGHT, anchor="nw")

        config_button = tk.Button(master=self.window, text='Options', bg=TOOLBAR_BG, command=lambda: self.notebook.select(self.tabs[2]))
        config_button.place(relx=0.377, rely=0.0, relw=0.055, relh=TOOLS_HEIGHT, anchor="nw")

        clear_events_button = tk.Button(master=self.window, text='Clear Events', bg=TOOLBAR_BG, command=lambda: self.clear_event_log())
        clear_events_button.place(relx=0.45, rely=0.0, relw=0.07, relh=TOOLS_HEIGHT, anchor="nw")

        events_label = tk.Label(tools_frame, text="Events Log", bg=TOOLBAR_BG, fg="white")
        events_label.config(font=font.Font(slant="italic", size=15))
        events_label.place(relx=0.71, rely=0.037, anchor="nw")

        details_frame = tk.Frame(self.window)
        details_frame.place(relx=0, rely=1, relw=0.52, relh=0.43, anchor="sw")

        self.notebook = ttk.Notebook(details_frame)
        self.tabs = []

        for tab_name in TAB_OPTIONS:
            new_tab = tk.Frame(self.notebook, bg=TAB_BG_SELECTED)
            self.notebook.add(new_tab, text=tab_name)
            self.tabs.append(new_tab)

        self.notebook.pack(expand=1, fill="both")

        self.last_event = EventWidget(self.tabs[0])
        self.selected_event = EventWidget(self.tabs[1])

        events_label = tk.Label(self.tabs[2], text="Detector Options", bg=TAB_BG_SELECTED, fg="black")
        events_label.config(font=font.Font(slant="italic", size=15))
        events_label.place(relx=0.03, rely=0.1, anchor="w")

        dot_check = tk.BooleanVar(False)
        dot_checkbox = tk.Checkbutton(self.tabs[2], text="Show Detection Dots", background=TAB_BG_SELECTED, variable=dot_check)
        dot_checkbox.config(command=lambda: self.detector.set_dot(dot_check.get()), font=font.Font(size=14))
        dot_checkbox.place(relx=0.03, rely=0.2, anchor='w')

        label_check = tk.BooleanVar(False)
        label_checkbox = tk.Checkbutton(self.tabs[2], text="Show Detection Labels", background=TAB_BG_SELECTED, variable=label_check)
        label_checkbox.config(command=lambda: self.detector.set_label(label_check.get()), font=font.Font(size=14))
        label_checkbox.place(relx=0.03, rely=0.3, anchor='w')

        about_label = tk.Label(self.tabs[3], text=ABOUT_TEXT, bg=TAB_BG_SELECTED, fg="black")
        about_label.config(font=font.Font(slant="italic", size=15))
        about_label.place(relx=0.5, rely=0.2, anchor="n")

        events_frame = tk.Frame(self.window)
        events_frame.place(relx=1, rely=1, relw=0.48, relh=0.961, anchor="se")

        self.events_view = ttk.Treeview(events_frame, columns=EVENT_COLUMN_NAMES, show='headings', style="Custom.Treeview")
        for index, name in enumerate(EVENT_COLUMN_NAMES):
            self.events_view.heading(name, text=name)
            self.events_view.column(name, width=EVENT_COLUMN_WIDTHS[index], anchor='c')
        self.events_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.events_view.bind('<Button-1>', self.event_selected)
        self.events_view.tag_configure('event', background=EVENT_RECORD)
        self.events_view.tag_configure('alert', background='red')

        scrollbar = ttk.Scrollbar(events_frame, orient=tk.VERTICAL, command=self.events_view.yview)
        self.events_view.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.window.mainloop()

    def toggle_video_feed(self):
        if self.videoFeed.active:
            self.stop_video_feed()
            self.video_feed_button.config(bg=TOOLBAR_BG, text='Enable Video Feed')

        else:
            self.start_video_feed()
            self.video_feed_button.config(bg=TOOLBAR_BG, text='Disable Video Feed')

    def update_feed(self):
        if self.videoFeed.active:
            self.videoFeed.update_image()

            new_detections = self.detector.scan_frame(self.videoFeed.get_last_frame(), self.video_label)

            if new_detections:
                current_dt = datetime.now()
                current_date = current_dt.strftime("%d/%m/%Y")
                current_time = current_dt.strftime("%H:%M:%S")

                for detection in new_detections:
                    self.events_view.insert("", 'end', values=(current_date, current_time, detection[0], detection[1]), tag='event')

                self.last_event.set_type(new_detections[-1][0])
                self.last_event.set_date(current_date)
                self.last_event.set_time(current_time)
                self.last_event.set_preview()

            self.window.update()
            self.window.after(0, func=lambda: self.update_feed())
        else:
            self.videoFeed.end_feed()

    def start_video_feed(self):
        if self.video_feed_option.get() == VIDEO_FEED_OPTIONS[0]:
            self.videoFeed.start_feed(0)
        elif self.video_feed_option.get() == VIDEO_FEED_OPTIONS[1]:
            self.videoFeed.start_feed(1)
        elif self.video_feed_option.get() == VIDEO_FEED_OPTIONS[2]:
            self.videoFeed.start_feed(2)
        elif self.video_feed_option.get() == VIDEO_FEED_OPTIONS[3]:
            self.videoFeed.start_feed(resource_path("res/local.mp4"))
        self.update_feed()

    def stop_video_feed(self):
        self.videoFeed.pause_feed()

    def clear_event_log(self):
        for e in self.events_view.get_children():
            self.events_view.delete(e)
        self.last_event.clear_labels()
        self.window.update()

    def event_selected(self, event):
        row_id = self.events_view.focus()
        row_content = self.events_view.item(row_id).get("values")
        self.selected_event.set_date(row_content[0])
        self.selected_event.set_time(row_content[1])
        self.selected_event.set_type(row_content[2])
        self.notebook.select(self.tabs[1])


if __name__ == '__main__':
    root = tk.Tk()
    GUI(root)
