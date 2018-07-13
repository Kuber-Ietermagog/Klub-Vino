from django.db import models
from wineinfo.models import Cultivar
# Create your models here.

class SearchModel(models.Model):
    cultivar = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    cellar = models.CharField(max_length=256)
    year = models.IntegerField()
    user_searched = models.CharField(max_length=256)
    wine_id = models.IntegerField()

    def __str__(self):
        return self.name
