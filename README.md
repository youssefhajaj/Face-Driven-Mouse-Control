# Face-Driven Mouse Control

This project implements a real-time face tracking application using OpenCV and MediaPipe. It captures video from the webcam and utilizes facial landmarks to control the mouse cursor on the screen. The application detects blinks to simulate mouse clicks, providing a hands-free interaction experience. Perfect for accessibility applications and innovative user interfaces.

## Demo Video

Watch the demo of the application in action:

[Download Demo Video](vedio/v.mp4)



## Features

- **Real-time face tracking**: Uses MediaPipe to detect facial landmarks.
- **Mouse control**: Moves the mouse cursor based on eye movements.
- **Blink detection**: Simulates mouse clicks when a blink is detected.
- **Enhanced visualization**: Displays additional landmarks around the eyes for better feedback.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/youssefhajaj/Face-Driven-Mouse-Control.git
   cd Face-Driven-Mouse-Control
2. Install the required packages:
   ```bash
   pip install opencv-python mediapipe pyautogui
3. Usage:
- run the app:
   ```bash
   python your_script_name.py
- Allow camera access when prompted.
- Use your eyes to control the mouse cursor and blink to click.
- Press 'q' to quit the application.
