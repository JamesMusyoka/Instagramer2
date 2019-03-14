from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo= models.ImageField(default='1', upload_to='profile/', blank=True)
    bio = models.CharField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['profile_photo']

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    # @classmethod
    # search_by_name(cls, search_term):
    # profile = cls.objects.filter(title_icontains=search_term)
    # return profile

    def __str__(self):
        return f'{self.user} Profile'


class Image(models.Model):
    photo = models.ImageField(upload_to='articles/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length =100)
    

    def __str__(self):
        return self.profile.username

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images  

class Comment(models.Model):
    comment = models.CharField(max_length =100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(Profile, related_name='userlikes')
    image = models.ForeignKey(Image, related_name='imagelikes')

