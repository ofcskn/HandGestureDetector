import cv2
from face_detector.face_detector import FaceDetector
from hand_detector.hand_landmark_detector import HandLandmarkDetector
from hand_detector.gesture_classifier import classify_gesture

def main():
    # Initialize the face detector and hand landmark detector
    face_detector = FaceDetector()
    hand_detector = HandLandmarkDetector()
    
    cap = cv2.VideoCapture(0)  # Use the default webcam
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from camera.")
            break
        
        # Flip the frame for mirror view
        frame = cv2.flip(frame, 1)

        # Detect faces
        # faces = face_detector.detect_faces(frame)
        
        # Detect emotion
        frame_with_emotions = face_detector.detect_emotion(frame)

        # Detect hand landmarks (if a face is detected)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand_detector.detect_landmarks(rgb_frame)

        # Check if any hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Classify gesture for each detected hand
                gesture = classify_gesture(hand_landmarks.landmark)
                
                # Draw landmarks on the frame
                hand_detector.mp_draw.draw_landmarks(frame, hand_landmarks, hand_detector.mp_hands.HAND_CONNECTIONS)

                # Display the gesture on the frame
                cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the frame with face and gesture detection
        cv2.imshow("Hand Gesture and Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
