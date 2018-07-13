from django.urls import path
from event_calendar import views

app_name = 'event_calendar'

urlpatterns = [
    path('events', views.EventMainView.as_view(), name='events'),
    path('event_detail/<int:pk>', views.EventInfoView.as_view(), name='event_detail'),
    path('create_event/', views.EventCreateView.as_view(), name='create_event'),
    path('update_event/<int:pk>', views.EventUpdateView.as_view(), name='update_event'),
    path('delete_event/<int:pk>', views.EventDeleteView.as_view(), name='delete_event'),
]
