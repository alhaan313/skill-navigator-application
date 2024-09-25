from django.urls import path
from .views import batch_allocation

urlpatterns = [
    path('batch/', batch_allocation)
]