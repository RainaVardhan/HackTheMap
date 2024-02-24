from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import UserProfile, TravelPlace, TravelEntry, EntryDetail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
    # Assuming you have a User profile for the logged-in user
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                return redirect('home', user_profile_id=user_profile.id)  # Redirect to the home page or any desired page
    else:
        form = AuthenticationForm()

    return render(request, 'VoyageVault/login.html', {'form': form})

@login_required
def home(request, user_profile_id):
    # Assuming you have a User profile for the logged-in user
    user_profile = get_object_or_404(UserProfile, id=user_profile_id, user=request.user)
    visited_places = TravelPlace.objects.filter(user_profile=user_profile).distinct()
    return render(request, 'VoyageVault/homepage.html', {'user_profile': user_profile, 'visited_places': visited_places})
@login_required
def place_detail(request, place_id):
    place = get_object_or_404(TravelPlace, pk=place_id)
    entries = TravelEntry.objects.filter(place=place)
    return render(request, 'entry_list.html', {'place': place, 'entries': entries})

@login_required
def entry_detail(request, entry_id):
    entry = get_object_or_404(TravelEntry, pk=entry_id)
    entry_details = EntryDetail.objects.filter(entry=entry)
    return render(request, 'entry.html', {'entry': entry, 'entry_details': entry_details})
