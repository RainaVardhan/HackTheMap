# forms.py
from django.contrib.auth.models import User

from django import forms
from .models import TravelPlace, TravelEntry, Activity

# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TravelPlaceForm(forms.ModelForm):
    class Meta:
        model = TravelPlace
        fields = ['name']

class TravelEntryForm(forms.ModelForm):
    class Meta:
        model = TravelEntry
        fields = ['date', 'description', 'rating']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'rating', 'image']
