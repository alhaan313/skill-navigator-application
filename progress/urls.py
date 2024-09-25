from django.urls import path, include
from .views import index

urlpatterns = [
    path('course_progress/', index, name='track')
]