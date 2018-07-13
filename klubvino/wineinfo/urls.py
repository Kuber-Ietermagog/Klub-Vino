from django.urls import path
from wineinfo import views

app_name = 'wineinfo'

urlpatterns = [
    path('cultivar/', views.CultivarView.as_view(), name='cultivar'),
    path('cultivar/<int:pk>', views.WynInfoView.as_view(), name='detail'),
    path('create/', views.CultivarCreateView.as_view(), name='create'),
    path('create_wine/', views.WineCreateView.as_view(), name='create_wine'),
    path('update_wine/<int:pk>', views.WineUpdateView.as_view(), name='update_wine'),
    path('delete_wine/<int:pk>', views.WineDeleteView.as_view(), name='delete_wine'),
]
