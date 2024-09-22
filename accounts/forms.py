from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # Assuming you have a Profile model for additional fields

# Custom SignupForm that handles user details and additional profile data
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    skills = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'placeholder': 'List your skills'}))
    resume = forms.FileField(required=True, widget=forms.ClearableFileInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'skills', 'resume']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Assuming you have a Profile model to store skills and resume
            profile = Profile(user=user, skills=self.cleaned_data['skills'], resume=self.cleaned_data['resume'])
            profile.save()
        return user
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")