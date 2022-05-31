from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
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

class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'number']
    template_name = "player_create.html"
    success_url = "/"

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'number']
    template_name = "player_update.html"
    success_url = "/"