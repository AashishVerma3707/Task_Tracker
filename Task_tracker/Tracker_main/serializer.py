from .models import CustomUser,Team,Task
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields="__all__"



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields =  "__all__"