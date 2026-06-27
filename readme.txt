GesturEase makes human computer interaction simple by making use of Hand Gestures and Voice Commands. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures along with a voice assistant. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirements. It leverages models such as CNN implemented by [MediaPipe](https://github.com/google/mediapipe) running on top of pybind11. It works direct on hands by making use of MediaPipe Hand detection. Currently it works on Windows platform.

GesturEase consist of multiple functions:
	Neutral gesture : for stoping execution of current gesture.
	Move cursor : for moving the cursor in desired position. Here, speed of the cursor is proportional to the speed of hand.
	Left click : gesture for single left click
	Right click : gesture for single right click
	Double click : gesture for double click
	Scrolling: Used for horizontal and vertical scroll
	Drag and drop : used for drag and drop functionality
