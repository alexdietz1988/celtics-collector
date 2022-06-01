from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, Team

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        context["players"] = Player.objects.all()
        return context

class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"

class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'number', 'team']
    template_name = "player_create.html"
    success_url = "/"

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'number', 'team', 'former_teams']
    template_name = "player_update.html"
    success_url = "/"

class PlayerDelete(DeleteView):
    model = Player
    template_name = "player_delete.html"
    success_url = "/"