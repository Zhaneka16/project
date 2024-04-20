from rest_framework import serializers 
from main.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('type_task', 'application_completed')