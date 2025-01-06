from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default view,
    path('emotion_detector/', views.emotion_detector, name='emotion_detector'),
    path('hand_gesture_detector/', views.hand_gesture_detector, name='hand_gesture_detector'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('upload/success/', views.upload_success, name='upload_success'), 
]