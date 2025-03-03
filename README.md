# Finger Counter with Face Detection

A real-time computer vision application that detects and counts fingers while also performing face detection using OpenCV and MediaPipe.

## Features

- Real-time finger counting
- Face detection with bounding box
- Support for multiple hand detection
- Live webcam feed with visual feedback
- Interactive display of finger count

## Prerequisites

Before running this application, make sure you have Python installed on your system. The application has been tested with Python 3.x.

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

- opencv-python==4.8.1.78
- mediapipe==0.10.8
- numpy==1.26.2

## Usage

1. Run the application:

```bash
python finger_counter.py
```

2. Once the application starts:
   - Position your hand in front of the camera
   - Show different finger positions to see the count update in real-time
   - Your face will be detected and highlighted with a green rectangle
   - The finger count will be displayed on the screen

3. To exit the application:
   - Press 'q' on your keyboard

## How It Works

- The application uses MediaPipe's hand landmark detection to identify key points on your hand
- Finger counting is determined by analyzing the position of fingertips relative to their base joints
- Face detection is performed simultaneously using MediaPipe's face detection model
- The webcam feed is processed in real-time to provide immediate visual feedback

## Tips for Best Results

- Ensure good lighting conditions
- Keep your hand at a reasonable distance from the camera
- Position your face clearly in the frame for face detection
- Make clear finger gestures for accurate counting