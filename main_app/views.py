from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class CelticsList(TemplateView):
    template_name = "celtics-list.html"

class CelticsDetail(TemplateView):
    template_name = "celtics-detail.html"