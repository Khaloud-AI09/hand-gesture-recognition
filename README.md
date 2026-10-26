# AI-Based Hand Gesture Recognition System

A real-time hand gesture recognition system built with Python, OpenCV, and Google's MediaPipe Gesture Recognizer. The application uses a webcam to detect hand gestures and displays the predicted gesture and confidence score on the screen.

## Project Overview

This project demonstrates how computer vision and a pre-trained machine learning model can recognize common hand gestures in real time.

The system processes webcam frames, identifies a hand gesture, and displays the prediction in a live window.

## Supported Gestures

- **Open Hand** — open palm
- **Fist** — closed fist
- **Thumbs Up** — thumb raised
- **Victory / Peace** — index and middle fingers raised

The application may also recognize other gestures supported by the MediaPipe model.

## Technologies Used

- **Python** — application programming
- **OpenCV** — webcam access, image processing, and on-screen display
- **MediaPipe** — pre-trained hand gesture recognition
- **MediaPipe Gesture Recognizer model** — predicts gestures from video frames

## How It Works

1. The application captures video frames from the webcam.
2. Each frame is converted into the image format required by MediaPipe.
3. The pre-trained gesture recognition model analyses the frame.
4. The application displays the predicted gesture and its confidence score.
5. The process repeats in real time until the user presses `Q`.

## Project Structure

```text
hand-gesture-recognition/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── models/
│   └── gesture_recognizer.task
└── screenshots/
    └── gesture-detection.png
```

## Installation and Setup

### 1. Install Python

Install a compatible version of Python 3.12 and ensure Python is available from your terminal.

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd hand-gesture-recognition
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your GitHub repository.

### 3. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

Allow webcam access if prompted. Position a hand clearly in front of the camera with adequate lighting. Press `Q` to close the application.

## Demo and Screenshots

A demonstration video shows the application recognizing hand gestures through a webcam.

Screenshots of the running application are available in the `screenshots/` directory.

## Limitations

- Recognition quality can vary with lighting, camera quality, hand position, and background conditions.
- The application is designed to recognize one hand at a time.
- Predictions depend on the pre-trained MediaPipe model and may occasionally be incorrect.

## Future Improvements

- Add more gesture categories.
- Improve the visual interface.
- Track recognition performance under different lighting conditions.
- Add support for custom gestures.

## Acknowledgements

This project uses the MediaPipe Gesture Recognizer by Google and OpenCV for computer vision.

- MediaPipe documentation: https://developers.google.com/edge/mediapipe/solutions/vision/gesture_recognizer/python
- OpenCV documentation: https://docs.opencv.org/

## Author

Developed as part of **Task 3** of the YR Novatech internship.
