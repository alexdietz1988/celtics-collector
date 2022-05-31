from django.db import models

# Create your models here.

class Player(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    number = models.IntegerField(default=-1)
    position = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    height_in_inches = models.IntegerField(default=0)
    weight_in_lbs = models.IntegerField(default=0)
    college = models.CharField(max_length=250)
    salary_in_dollars = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name']