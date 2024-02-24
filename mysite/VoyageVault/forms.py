# forms.py
from django import forms
from .models import TravelPlace, TravelEntry

class TravelPlaceForm(forms.ModelForm):
    class Meta:
        model = TravelPlace
        fields = ['name']

class TravelEntryForm(forms.ModelForm):
    class Meta:
        model = TravelEntry
        fields = ['date', 'description', 'rating', 'image_url']
