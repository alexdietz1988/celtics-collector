from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Player

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class PlayerList(TemplateView):
    template_name = "player_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = Player.objects.all()
        return context

class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"