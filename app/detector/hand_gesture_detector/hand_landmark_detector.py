import mediapipe as mp
import cv2

class HandLandmarkDetector:
    """Detects hand landmarks using MediaPipe and draws them on the frame."""
    
    def __init__(self):
        # Initialize MediaPipe hands and drawing utilities
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_landmarks(self, frame):
        """Detects hand landmarks and draws them on the frame."""
        # Convert the frame to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        # Check if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks as circles on the hand
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        return results