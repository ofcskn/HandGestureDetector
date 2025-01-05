import cv2

def show_frame(frame, title="Frame"):
    """Displays the frame with a title."""
    cv2.imshow(title, frame)
