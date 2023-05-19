
# Smart Security System
 
### Demo Image Preview
<img src="https://github.com/stevenbuttifint/smart-security-system/blob/main/demo/demo.JPG?raw=true" width=80% height=90%>


---

### Table of Contents
- [Description](#description)
- [What I Learned](#what-i-learned)
- [References](#references)

---

### Description

This application enables real-time object detection through a live camera feed or local video file. 
Users can manage and review past events. This application was created using Python and Tkinter. The selection of the YOLOv5 real-time object detection model enabled detections to be identified in real time.


---

### What I Learned
- How to optimize the CV2 video capture feed using waitkey. This stopped a buildup of frames on the video feed stack.
- How to track existing object detections using a center point. This enabled new objects to be distinguished from old.
- How to log events into a tkinter ttk treeview widget.

---

### References
- The YOLOv5 model used can be found [here](https://medium.com/mlearning-ai/detecting-objects-with-yolov5-opencv-python-and-c-c7cf13d1483c).




[Back To The Top](#smart-security-system)