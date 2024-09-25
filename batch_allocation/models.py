from django.db import models

# Create your models here.
class batch(models.Model):
    name = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return self.name