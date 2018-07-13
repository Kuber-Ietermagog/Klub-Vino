from django.db import models
from django.urls import reverse

# Create your models here.
class ChatLog(models.Model):
    profile_pic = models.ImageField()
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp', )
