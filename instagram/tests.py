from django.test import TestCase

from .models import Profile, Image, Comment

class ProfileTestClass(TestCase):
    def setup(self):
        self.james= Profile(profile_photo = 'James')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))


    def test_save_method(self):
        self.james.save.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def update_profile(self):
        self.james.save_profile()
        self.james.update_profile()
        self.assertTrue(len(profiles) > 0)

    def delete_profile_method(self):
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ImageTestClass(TestCase):
    def setUp(self):
        james = Profile(name='james')
        james.save_profile()

        self.new_comment = comment(name = 'testing')
        self.new_comment.save()

        self.post_date= Image(image_name = 'image name', likes = 'show people who have liked', comment = 'comments made by people')
        self.post_date.save()
        self.post_date.comment.add(self.new_comment)

    def teardown(self):
        Profile.objects.all().delete()
        comment.objects.all().delete()
        Image.objects.all().delete()





