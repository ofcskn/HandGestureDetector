import cv2

class FaceDetector:
    """Detects faces in video frames using Haar Cascades."""
    
    def __init__(self, cascade_path="haarcascade_frontalface_default.xml"):
        # Load the pre-trained Haar Cascade classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)

    def detect_faces(self, frame):
        """Detect faces and return bounding boxes for detected faces."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)  # Minimum size of detected faces
        )

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
        
        return faces  # Return the list of detected face coordinates
