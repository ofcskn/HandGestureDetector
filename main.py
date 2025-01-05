import cv2
from hand_detector.detection import DetectionPipeline
from hand_detector.utils import GestureRecognizer

def main():
    # Initialize pipeline and gesture recognizer
    pipeline = DetectionPipeline()
    gesture_recognizer = GestureRecognizer()

    cap = cv2.VideoCapture(0)
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read from camera.")
                break

            # Perform detection
            detections = pipeline.detect(frame)
            gestures = gesture_recognizer.detect_gestures(detections["hands"])

            print(f"Detected Gestures: {gestures}")

            # Show detection results
            cv2.imshow("Hand and Face Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
