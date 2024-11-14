from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']
        
class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(user=user, role='doctor')
        return user

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(user=user, role='patient')
        return user

class PharmacistRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(user=user, role='pharmacist')
        return user

class PharmacistLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class DoctorLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']



class PatientLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']