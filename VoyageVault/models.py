from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

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

    def __str__(self):
        return f"{self.place} - {self.date}"

class Activity(models.Model):
    day = models.ForeignKey(TravelEntry, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField("Activity Name", max_length=100)
    image = models.ImageField(upload_to='activity_images/', null=True, blank=True)
    description = models.TextField("Description")
    rating = models.IntegerField("Rating", choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name

