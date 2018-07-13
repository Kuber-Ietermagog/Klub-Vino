from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/<int:pk>', views.SearchDetailView.as_view(), name='search_detail')
]
