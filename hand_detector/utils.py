class GestureRecognizer:
    """Recognizes hand gestures."""
    def detect_gestures(self, hand_positions):
        """Detects simple gestures based on hand positions."""
        gestures = []
        for hand in hand_positions:
            if len(hand) > 8:  
                gestures.append("Thumbs Up")
            else:
                gestures.append("Unknown Gesture")
        return gestures
