from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('celtics-list', views.CelticsList.as_view(), name="celtics-list"),
    path('celtics-detail', views.CelticsDetail.as_view(), name="celtics-detail")
]