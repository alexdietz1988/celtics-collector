from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players", default=1)
    former_teams = models.ManyToManyField(Team, related_name="former_players", blank=True)
    number = models.CharField(default='0', max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name']