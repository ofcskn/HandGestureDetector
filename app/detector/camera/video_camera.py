import cv2

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