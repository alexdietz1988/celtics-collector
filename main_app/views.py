from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Celtic

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class CelticsList(TemplateView):
    template_name = "celtics-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["celtics"] = Celtic.objects.all()
        return context

class CelticsDetail(TemplateView):
    template_name = "celtics-detail.html"