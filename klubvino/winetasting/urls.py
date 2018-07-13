from django.urls import path
from winetasting import views

app_name = 'winetasting'

urlpatterns = [
    path('tasting/', views.TastingMainView.as_view(), name='tasting'),
    path('create_tasting/', views.TastingCreateView.as_view(), name='create_tasting'),
    path('update_tasting/<int:pk>', views.TastingUpdateView.as_view(), name='update_tasting'),
    path('tasting/<int:pk>', views.WineTastingDetailView.as_view(), name='detail'),
    path('mystery_wine/', views.MysteryWineCreateView.as_view(), name='mystery_wine'),
    path('mystery_update/<int:pk>', views.MysteryWineUpdateView.as_view(), name='mystery_update'),
    path('results/', views.ResultView.as_view(), name='results'),
    path('results/<int:pk>', views.ResultUpdateView.as_view(), name='result_update'),
]
