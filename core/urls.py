# urls.py (in your app directory)
from django.urls import path
from .views import person_create_view, success_view

urlpatterns = [
    path('create/', person_create_view, name='person_create'),
    path('success/', success_view, name='success'),
]
