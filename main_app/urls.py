from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerList.as_view(), name="player_list"),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name="player_detail"),
    path('players/new', views.PlayerCreate.as_view(), name="player_create")
]