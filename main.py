
import cv2
import mediapipe as mp
import time
from pathlib import Path

# Find the AI model inside the project folder
MODEL_PATH = Path(__file__).parent / "models" / "gesture_recognizer.task"

# Convert MediaPipe's labels into friendly names
GESTURE_NAMES = {
    "Open_Palm": "Open Hand",
    "Closed_Fist": "Fist",
    "Thumb_Up": "Thumbs Up",
    "Victory": "Victory / Peace",
    "Pointing_Up": "Pointing Up",
    "Thumb_Down": "Thumbs Down",
    "ILoveYou": "I Love You",
}

# Configure the AI gesture recognizer
options = mp.tasks.vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(
        model_asset_path=str(MODEL_PATH)
    ),
    running_mode=mp.tasks.vision.RunningMode.VIDEO,
    num_hands=1,
)

def main():
    if not MODEL_PATH.exists():
        print("AI model not found:", MODEL_PATH)
        return

    # Start the webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print("Could not open the webcam.")
        print("Close other apps using the camera and try again.")
        return

    start_time = time.perf_counter()
    last_timestamp = -1

    try:
        with mp.tasks.vision.GestureRecognizer.create_from_options(
            options
        ) as recognizer:

            while True:
                success, frame = camera.read()

                if not success:
                    print("Could not read a webcam frame.")
                    break

                # Mirror the image so it feels like a mirror
                frame = cv2.flip(frame, 1)

                # OpenCV uses BGR; MediaPipe expects RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=rgb_frame
                )

                # Video timestamps must continually increase
                timestamp_ms = int(
                    (time.perf_counter() - start_time) * 1000
                )
                timestamp_ms = max(timestamp_ms, last_timestamp + 1)
                last_timestamp = timestamp_ms

                # Ask the AI to identify the gesture
                result = recognizer.recognize_for_video(
                    image, timestamp_ms
                )

                gesture_text = "No hand detected"
                confidence_text = ""

                if result.gestures and result.gestures[0]:
                    prediction = result.gestures[0][0]
                    label = prediction.category_name
                    confidence = prediction.score

                    if label != "None":
                        gesture_text = GESTURE_NAMES.get(
                            label, label.replace("_", " ")
                        )
                        confidence_text = (
                            f"Confidence: {confidence * 100:.1f}%"
                        )

                # Display the result on the webcam window
                cv2.putText(
                    frame, "AI HAND GESTURE RECOGNITION",
                    (20, 35), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2
                )

                cv2.putText(
                    frame, f"Gesture: {gesture_text}",
                    (20, 85), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2
                )

                cv2.putText(
                    frame, confidence_text,
                    (20, 125), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2
                )

                cv2.putText(
                    frame, "Press Q to quit",
                    (20, frame.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 255, 255), 2
                )

                cv2.imshow("Hand Gesture Recognition", frame)

                # Press Q to close the program
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    except Exception as error:
        print("Something went wrong:", error)

    finally:
        camera.release()
        cv2.destroyAllWindows()
        print("Webcam closed.")

if __name__ == "__main__":
    main()
