from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chatbot-home'),
    path('get_response/', views.get_response, name='get_response'),
    path('about/', views.about, name='chatbot-about'),
    path('courses/', views.courses, name='chatbot-courses'),
]