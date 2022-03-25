from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class CustomUser(AbstractUser):
    Team_member= models.BooleanField(default=True)
    Team_leader= models.BooleanField(default=False)
    Availability=models.BooleanField(default=True)
    def __str__(self):
        return self.username

class Team(models.Model):
    name=models.CharField(max_length=30,unique=True)
    team_members=models.ManyToManyField(CustomUser)


class Task(models.Model):
    task_name=models.CharField(max_length=30 , unique=True)
    priority=models.CharField(max_length=30)
    star_date=models.DateField(("Date"), default=date.today)
    end_date=models.DateField(("Date"), default=date.today)
    team_members=models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    CHOICES = (
        ('Assigned', "Assigned"),
        ('In_progress', "In progress"),
        ('under_review', "under review"),
        ('done', "done"))
    status=models.CharField(max_length=30, choices=CHOICES, default="Assigned")
