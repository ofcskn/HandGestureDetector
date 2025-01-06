def gen(camera, type=0):
    """
    Generator function that yields video frames for streaming.
    """
    if type == 1:
        while True:
            frame = camera.get_frame_for_emotion_detecting()
            if frame:
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    if type == 2:
        while True:
            frame = camera.get_frame_for_hand_gesture_detecting()
            if frame:
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    else:
        while True:
            frame = camera.get_frame()
            if frame:
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')