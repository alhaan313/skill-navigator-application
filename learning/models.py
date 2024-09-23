from django.db import models

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)

class LearningMaterial(models.Model):
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    content = models.TextField()
