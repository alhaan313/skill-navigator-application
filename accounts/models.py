
from django.db import models
from django.contrib.auth.models import User

# Profile model to store additional fields like skills and resume
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=500, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

