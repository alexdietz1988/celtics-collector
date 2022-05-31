from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerList.as_view(), name="player_list"),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name="player_detail"),
    path('players/new', views.PlayerCreate.as_view(), name="player_create"),
    path('players/<int:pk>/update', views.PlayerUpdate.as_view(), name="player_update"),
    path('players/<int:pk>/delete', views.PlayerDelete.as_view(), name="player_delete")
]