def classify_gesture(landmarks):
    """
    Classifies hand gesture based on the positions of landmarks.
    Input: landmarks - List of 21 hand landmark points (x, y, z)
    Output: gesture - Detected gesture as a string
    """
    # Define landmarks for easy access
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    # Thumbs Up (like)
    if thumb_tip.y < index_tip.y and thumb_tip.y < pinky_tip.y:
        return "like"  # Thumbs up gesture

    # Thumbs Down (dislike)
    elif thumb_tip.y > index_tip.y and thumb_tip.y > pinky_tip.y:
        return "dislike"  # Thumbs down gesture

    # Peace Sign (victory)
    elif index_tip.y < middle_tip.y and pinky_tip.y < thumb_tip.y and thumb_tip.x < index_tip.x:
        return "peace"  # Peace sign gesture

    # "Call Me" gesture (pinky and thumb extended)
    elif index_tip.y > thumb_tip.y and middle_tip.y > thumb_tip.y and ring_tip.y > thumb_tip.y:
        if pinky_tip.x < index_tip.x and thumb_tip.x < pinky_tip.x:
            return "call me"  # Call me gesture (thumb and pinky extended)

    # Finger Guns (bang bang)
    elif index_tip.y < thumb_tip.y and pinky_tip.y < thumb_tip.y and ring_tip.y < middle_tip.y:
        return "bang bang"  # Finger guns gesture (index and thumb extended)

    # Stop Gesture (open hand)
    elif abs(thumb_tip.x - pinky_tip.x) < 0.1 and abs(index_tip.y - wrist.y) < 0.1:
        return "stop"  # Stop gesture (open palm)

    # OK Gesture (circle made with thumb and index finger)
    elif abs(thumb_tip.x - index_tip.x) < 0.05 and abs(thumb_tip.y - index_tip.y) < 0.05:
        return "ok"  # OK gesture (thumb and index form a circle)

    # Rock on Gesture (thumb and pinky extended, other fingers folded)
    elif index_tip.y > thumb_tip.y and middle_tip.y > index_tip.y and ring_tip.y > middle_tip.y:
        if abs(pinky_tip.x - thumb_tip.x) < 0.2 and abs(index_tip.x - pinky_tip.x) > 0.5:
            return "rock"  # Rock on gesture (thumb and pinky extended)

    # Wave Gesture (index and middle fingers moving in a wave-like motion)
    if abs(index_tip.y - middle_tip.y) < 0.1 and index_tip.x > middle_tip.x:
        return "wave"  # Waving gesture (index and middle fingers)

    # Closed Fist
    if abs(thumb_tip.x - wrist.x) < 0.1 and abs(index_tip.x - wrist.x) < 0.1 and abs(middle_tip.x - wrist.x) < 0.1:
        return "fist"  # Closed fist gesture

    # Pinch Gesture (thumb and index finger touching)
    if abs(thumb_tip.x - index_tip.x) < 0.1 and abs(thumb_tip.y - index_tip.y) < 0.1:
        return "pinch"  # Pinch gesture (thumb and index tip touch)

    # Rock Gesture (three fingers up)
    if abs(index_tip.x - middle_tip.x) < 0.1 and abs(middle_tip.x - ring_tip.x) < 0.1:
        return "rock"  # Rock gesture (three fingers up)

    # Shaka Gesture (thumb and pinky extended)
    if abs(thumb_tip.y - pinky_tip.y) < 0.1 and thumb_tip.x > pinky_tip.x:
        return "shaka"  # Shaka gesture (thumb and pinky extended)

    # Unknown Gesture
    return "unknown"  # Return unknown if no gesture is detected