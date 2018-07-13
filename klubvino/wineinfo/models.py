from django.db import models
from django.urls import reverse

# Create your models here.

class Cultivar(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wineinfo:cultivar")

    class Meta:
        ordering = ('name',)


class WineInfo(models.Model):
    cultivar = models.ForeignKey(Cultivar, related_name='wine', on_delete=models.CASCADE)
    pics = models.ImageField(upload_to='wine_pics', blank=True, null=True)
    name = models.CharField(max_length=256)
    cellar = models.CharField(max_length=256)
    year = models.IntegerField()
    price = models.CharField(max_length=256)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wineinfo:cultivar")
