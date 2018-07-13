from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your models here.

class WineTasting(models.Model):

    date = models.DateTimeField()
    hosted_by = models.CharField(max_length=250)
    cultivar = models.CharField(max_length=250)
    location = models.CharField(max_length=250, default='')
    qty_wines = models.IntegerField()
    created_by = models.CharField(max_length=256, default='')
    close_tasting = models.BooleanField(default=False)


    def __str__(self):
        return '{}, {}'.format(str(self.date), self.location)

    def get_absolute_url(self):
        return reverse("winetasting:tasting")

    class Meta:
        ordering = ('date',)

class WineTastingInfo(models.Model):

    date = models.ForeignKey(WineTasting, related_name='proe_wyn', on_delete=models.CASCADE)
    cultivar = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    wine_code_name = models.CharField(max_length=10)
    points = models.DecimalField(decimal_places=2, max_digits=4, blank=True, default=0)
    comments = models.TextField(blank=True)

    def __str__(self):
        return '{}, {}, {}'.format(str(self.date), self.wine_code_name, self.username)

    def get_absolute_url(self):
        return reverse("winetasting:detail",kwargs={'pk':self.date.id})

    class Meta:
        ordering = ('wine_code_name', )

class WineTastingResults(models.Model):

    relative_date = models.DateTimeField(blank=True, null=True)
    cultivar = models.CharField(max_length=256)
    wine_code_name = models.CharField(max_length=256)
    pics = models.ImageField(upload_to='wine_pics', blank=True, null=True)
    real_name = models.CharField(max_length=256)
    cellar = models.CharField(max_length=256)
    year = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=256)
    total = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.wine_code_name

    def get_absolute_url(self):
        return reverse("winetasting:tasting")

    class Meta:
        ordering = ('-total', )
