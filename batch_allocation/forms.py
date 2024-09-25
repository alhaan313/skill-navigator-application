# forms.py
from django import forms
from .models import batch

class BatchForm(forms.ModelForm):
    class Meta:
        model = batch
        fields = ['name', 'resume']