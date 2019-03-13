from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='profile/', blank=True)
    bio = models.CharField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user} Profile'
    class Meta:
        ordering = ['profile_photo']

