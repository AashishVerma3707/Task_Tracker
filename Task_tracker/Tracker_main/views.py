from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import CustomUser,Team, Task
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import CustomUserSerializer,TeamSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from .task import *

from django.contrib.auth.decorators import login_required


class TeamViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    def get_queryset(self):
        team=Team.objects.all()
        return team

    def create(self, request, *args, **kwargs):
        data = request.data

        new_team = Team.objects.create(
            name=data["name"])

        new_team.save()

        for Cuser in data["team_members"]:
            customUser_obj = CustomUser.objects.get(id=Cuser["id"])
            new_team.team_members.add(customUser_obj)

        return Response({"success": True,"msg":"Team created successfully"})






class AvailabilityApi(APIView):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        def get(self, request, team_id):
            l=[]
            model = Team.objects.get(id=team_id)
            serializer = TeamSerializer(model)
            for i in serializer.data["team_members"]:
                l.append({i["username"]:i["Availability"]})
            return JsonResponse({"success":"True","Data":l})
    except Exception as e:
        pass


class TaskAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request):


        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            y=CustomUser.objects.get(id=serializer.data["team_members"])
            if y.Availability==False:
                l={"success": False ,"msg":"team member is not available"}
                return Response(l)
            return Response({"success": True,"msg":"Task created successfully"})
        else:
            return Response({"success": False,"msg":"Incorrect parameters"})



class Update_taskAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, task_id):

        model = Task.objects.get(id=task_id)
        serializer = TaskSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True,"msg":"Task updated succesfully"})
        else:
            return Response({"success":False,"msg":"Incorrect parameters"})


def mail_index(request):
    send_mail_task.delay(24*60*60)
    return JsonResponse({})