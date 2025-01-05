import cv2
import mediapipe as mp
from .model import HandModel

class HandTracker:
    """Tracks hand positions using MediaPipe."""
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        """Detects hands and draws landmarks."""
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        hand_positions = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                hand_positions.append(self._extract_coordinates(hand_landmarks))
        return hand_positions

    def _extract_coordinates(self, hand_landmarks):
        """Extracts hand landmark coordinates."""
        return [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]

class FaceDetector:
    """Detects faces using OpenCV."""
    def __init__(self, face_model="haarcascade_frontalface_default.xml"):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_model)

    def detect_faces(self, frame):
        """Detects faces and draws rectangles."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return faces

class DetectionPipeline:
    """Pipeline to detect hands and faces."""
    def __init__(self):
        self.hand_tracker = HandTracker()
        self.face_detector = FaceDetector()

    def detect(self, frame):
        """Detects hands and faces in a frame."""
        hands = self.hand_tracker.detect_hands(frame)
        faces = self.face_detector.detect_faces(frame)
        return {"hands": hands, "faces": faces}
