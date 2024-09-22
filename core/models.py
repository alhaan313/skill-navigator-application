# models.py
from django.db import models

class ProgrammingLanguage(models.Model):
    language_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'programminglanguage'  # Specify the existing table name

    def __str__(self):
        return self.language_name


class ECertificate(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='certificates')
    certificate = models.FileField(upload_to='certificates/')

    class Meta:
        db_table = 'ecertificate'  # Specify the existing table name

    def __str__(self):
        return f"Certificate for {self.person.name}"


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    certifications = models.TextField()
    internship_details = models.TextField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    class Meta:
        db_table = 'person'  # Specify the existing table name

    def __str__(self):
        return self.name
