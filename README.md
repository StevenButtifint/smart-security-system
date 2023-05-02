# Smart Security System
 
### Demo Video
*coming soon*

---

### Table of Contents
- [Description](#description)
- [What I Learned](#what-i-learned)
- [References](#references)

---

### Description

This application provides a means for detecting objects live through a camera or local video file. Events get recorded and displayed to the user allowing them to manage and review events that have occurred. This application uses Python with Tkinter. Objects get identified using the YOLOv5 real-time object detection model. 

---

### What I Learned
- How to optimize the CV2 video capture feed using waitkey. This stopped a buildup of frames on the video feed stack.
- How to track existing object detections using a center point. This enabled new objects to be distinguished from old.
- How to log events into a tkinter ttk treeview widget.

---

### References
- The YOLOv5 model used can be found [here](https://medium.com/mlearning-ai/detecting-objects-with-yolov5-opencv-python-and-c-c7cf13d1483c).




[Back To The Top](#smart-security-system)