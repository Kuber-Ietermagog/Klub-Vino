from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class EventEntry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="")
    last_update_by = models.CharField(max_length=100, default="", blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_calendar:events")


    class Meta:
        ordering = ('-date', )
