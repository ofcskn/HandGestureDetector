from django.shortcuts import render

def index(request):
    """Default view for the app."""
    return render(request, 'face_detection/index.html')