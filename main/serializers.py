from rest_framework import serializers 
from .models import Task, Design_object, Spot, Department, Employee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('type_task', 'application_completed', 'description')


class DesignobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design_object
        fields = ('name', 'project_completed',)


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('spot',)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_name',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('email',)

