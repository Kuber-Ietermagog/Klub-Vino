from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, related_name="main_user", on_delete=models.CASCADE)

    # additional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    slag_spreek = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.user.username
