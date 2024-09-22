# forms.py
from django import forms
from .models import Person, ProgrammingLanguage

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name', 
            'email', 
            'degree', 
            'specialization', 
            'phone_number', 
            'certifications', 
            'internship_details', 
            'linkedin_profile', 
            'github_profile', 
            'programming_languages', 
            'resume'
        ]
        widgets = {
            'certifications': forms.Textarea(attrs={'rows': 3}),
            'internship_details': forms.Textarea(attrs={'rows': 3}),
        }
