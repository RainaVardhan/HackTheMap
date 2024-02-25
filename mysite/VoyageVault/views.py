from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import UserProfile, TravelPlace, TravelEntry, Activity
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TravelPlaceForm, TravelEntryForm, SignUpForm, ActivityForm

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
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Create a new user
            user = User.objects.create_user(username=username, password=password)

            # Authenticate the user and log them in
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login_page')
    else:
        form = SignUpForm()

    return render(request, 'VoyageVault/signup.html', {'form': form})
@login_required
def home(request, user_profile_id):
    # Assuming you have a User profile for the logged-in user
    user_profile = get_object_or_404(UserProfile, id=user_profile_id, user=request.user)
    visited_places = TravelPlace.objects.filter(user_profile=user_profile).distinct()
    return render(request, 'VoyageVault/homepage.html', {'user_profile': user_profile, 'visited_places': visited_places})
@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')
@login_required
def place_detail(request, place_id):
    place = get_object_or_404(TravelPlace, pk=place_id)
    entries = TravelEntry.objects.filter(place=place)
    return render(request, 'VoyageVault/entry_list.html', {'place': place, 'entries': entries})


@login_required
def entry_detail(request, day_id):
    day = get_object_or_404(TravelEntry, pk=day_id)
    activities = day.activities.all()  # Assuming you have a related_name='activities' in your Activity model
    place = day.place
    user_profile = place.user_profile
    return render(request, 'VoyageVault/entry.html', {'day': day, 'activities': activities, 'place': place, 'user_profile': user_profile})


@login_required
def add_place(request):
    if request.method == 'POST':
        form = TravelPlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user_profile = request.user.userprofile
            place.save()
            return redirect('home', user_profile_id=request.user.userprofile.id)
    else:
        form = TravelPlaceForm()

    return render(request, 'VoyageVault/add_place.html', {'form': form})
@login_required
def delete_place(request, place_id):
    place = get_object_or_404(TravelPlace, pk=place_id, user_profile=request.user.userprofile)
    place.delete()
    return redirect('home', user_profile_id=request.user.userprofile.id)
@login_required
def add_entry(request, place_id):
    place = get_object_or_404(TravelPlace, pk=place_id)

    if request.method == 'POST':
        form = TravelEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.place = place
            entry.save()
            return redirect('place_detail', place_id=place.id)
    else:
        form = TravelEntryForm()

    return render(request, 'VoyageVault/add_entry.html', {'form': form, 'place': place})
@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(TravelEntry, pk=entry_id, place__user_profile=request.user.userprofile)
    entry.delete()
    return redirect('place_detail', place_id=entry.place.id)
@login_required
def add_activity(request, day_id):
    day = TravelEntry.objects.get(pk=day_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.day = day
            activity.save()
            return redirect('entry_detail', day_id=day_id)  # Redirect to the same page to add more activities
    else:
        form = ActivityForm()
    return render(request, 'VoyageVault/add_activity.html', {'form': form, 'day': day})
