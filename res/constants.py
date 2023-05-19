# WINDOW
TITLE = "Smart Security System"
DIMENSIONS = "1200x800"


# WIDGETS
VIDEO_FEED_OPTIONS = ["CAM 1", "CAM 2", "CAM 3", "MP4"]
DETECTOR_OPTIONS = ["YOLOv5s"]
TAB_OPTIONS = ["Last Event", "Selected Event", "Options", "About"]
EVENT_COLUMN_NAMES = ["Date", "Time", "Class", "Note"]
EVENT_COLUMN_WIDTHS = [2, 2, 50, 200]
TOOLS_HEIGHT = 0.04


# Directories
APP_ICON_DIR = "res/icons/app_icon.ico"
LAST_EVENT_DIR = "res/detections/last_event.png"
MODEL_DIR = "res/yolov5s.onnx"
CLASSES_DIR = "res/classes.txt"

# Colours
MAIN_BG = "#999999"
TOOLBAR_BG = "#777777"
TOOLBAR_FG = "#cccccc"
TREE_HEADING_BG = "#888888"
TREE_HEADING_FG = "black"
TREE_COLUMNS_BG = "#aaaaaa"
NOTEBOOK_BG = TOOLBAR_BG
TAB_BG = TOOLBAR_BG
TAB_FG = "black"
TAB_BG_SELECTED = "#bbbbbb"
EVENT_PREVIEW = "#aaaaaa"
EVENT_RECORD = "#bbbbbb"


# Detection
OBJECT_TYPES = ["person", "bicycle", "car", "motorbike", "bus", "truck"]


# Strings
EMPTY_TYPE = "None"
EMPTY_TIME = "--:--:--"
EMPTY_DATE = "--/--/----"
ABOUT_TEXT = "Log events in real time using\nobject detection.\n\n\nCreated 2023\nby Steven B.\n\n"
