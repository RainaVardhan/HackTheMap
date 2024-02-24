from django.contrib import admin

from .models import UserProfile, TravelPlace, TravelEntry, EntryDetail

admin.site.register(UserProfile)
admin.site.register(TravelPlace)
admin.site.register(TravelEntry)
admin.site.register(EntryDetail)
