from django.db import models
from django.contrib.auth.models import User

class Map(models.Model):
    user = models.ForeignKey('auth.User')
    map_title = models.CharField(max_length=200)
    
class Pin(models.Model):
    #map_id = models.ForeignKey(Map)
    pin_latitude = models.DecimalField(max_digits=8, decimal_places=6)
    pin_longitude = models.DecimalField(max_digits=8, decimal_places=6)
    CATEGORY_CHOICES = (
        ("SL", "Sleep"),
        ("EA", "Eat"),
        ("OU", "Outdoor Activity"),
        ("CU", "Culture"),
        ("SH", "Shopping"),
        ("NL", "Nightlife"),
        ("CO", "Contact"),
        ("OT", "Other"),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    comment = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

