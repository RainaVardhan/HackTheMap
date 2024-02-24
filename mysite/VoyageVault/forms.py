# forms.py
from django import forms
from .models import TravelPlace, TravelEntry, Activity

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
