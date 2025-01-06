import cv2
import time
from detector.hand_gesture_detector.hand_landmark_detector import HandLandmarkDetector
from detector.hand_gesture_detector.gesture_classifier import classify_gesture
from detector.emotion_detector.face_detector import FaceDetector

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # Use 0 for the default camera

    def __del__(self):
        self.video.release()

    def get_frame(self):
        """
        Captures a frame from the camera and returns it in JPEG format.
        """
        ret, frame = self.video.read()
        if ret:
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        return None
    
    def get_frame_for_emotion_detecting(self):
        ret, frame = self.video.read()
        if ret:
            face_detector = FaceDetector()
            face_detector.detect_emotion(frame)
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        return None
    
    def get_frame_for_hand_gesture_detecting(self):
        ret, frame = self.video.read()
        
        if ret:
            # Convert the frame to RGB (for hand detector processing)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
           
            hand_detector = HandLandmarkDetector()
            
            # Detect hand landmarks
            results = hand_detector.detect_landmarks(rgb_frame)

            # Check if hands are detected
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Classify gesture for each detected hand
                    gesture = classify_gesture(hand_landmarks.landmark)
                    
                    # Draw landmarks on the frame
                    hand_detector.mp_draw.draw_landmarks(frame, hand_landmarks, hand_detector.mp_hands.HAND_CONNECTIONS)
                    
                    # Display the gesture on the frame
                    cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Encode the frame as JPEG
            _, jpeg = cv2.imencode('.jpg', frame)
            if _:
                time.sleep(0.03)  # 30 milliseconds (roughly 30 fps)
                return jpeg.tobytes()
        
        return None