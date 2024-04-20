from django.shortcuts import render
from django.http import HttpResponse
from main.models import Design_object, Spot, Task
from .serializers import TaskSerializer
from rest_framework import generics





class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer