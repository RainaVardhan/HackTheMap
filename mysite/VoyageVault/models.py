from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class TravelPlace(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

# class Homepage(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
class TravelEntry(models.Model):
    place = models.ForeignKey(TravelPlace, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    # You might want to use a library like django-imagekit for handling images
    # For simplicity, here, I'm just allowing a URL for an image
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.place} - {self.date}"

class EntryDetail(models.Model):
    entry = models.ForeignKey(TravelEntry, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.entry} - {self.description[:20]}"
