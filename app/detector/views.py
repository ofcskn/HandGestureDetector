from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2

from .camera.streaming import gen
from .camera.video_camera import VideoCamera


def index(request):
    """Default view for the app."""
    return render(request, 'detector/index.html')

def emotion_detector(request):
    return StreamingHttpResponse(gen(VideoCamera(), 1), content_type='multipart/x-mixed-replace; boundary=frame')

def hand_gesture_detector(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
