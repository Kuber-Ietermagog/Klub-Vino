from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from . import models
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
## Cultivar views
class CultivarView(ListView):
    context_object_name = 'cultivars'
    model = models.Cultivar

class CultivarCreateView(CreateView):
    fields = ('name',)
    model = models.Cultivar

## Wine info views
class WynInfoView(DetailView):
    context_object_name = 'wyn_goed'
    model = models.Cultivar
    template_name = 'wineinfo/wyn_detail.html'

class WineCreateView(CreateView):
    fields = "__all__"
    model = models.WineInfo

class WineUpdateView(UpdateView):
    fields = "__all__"
    model = models.WineInfo

class WineDeleteView(DeleteView):
    model = models.WineInfo
    success_url = reverse_lazy('wineinfo:cultivar')
