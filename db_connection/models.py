from django.db import models

# Create your models here.
# models.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'people'  # Map to the existing 'people' table in MySQL

    def __str__(self):
        return self.name
