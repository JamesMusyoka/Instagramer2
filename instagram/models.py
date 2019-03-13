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


class Image(models.Model):
    photo = models.ImageField(upload_to='articles/', blank=True)
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length =100)
    

class Comment(models.Model):
    comment = models.CharField(max_length =100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.comment

