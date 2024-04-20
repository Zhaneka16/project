from django.contrib import admin

# Register your models here.

from .models import Task, Design_object, Spot, Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    search_fields = ['department_name']
    list_filter = ['department_name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'email','departments']
    search_fields = ['user', 'department']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['type_task', 'data', 'application_completed', 'description',]
    filter_vertical = ['design_objects_type']
    search_fields = ['type_task']
    list_filter = ['type_task', 'data']

@admin.register(Design_object)
class DesignobjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_completed']
    search_fields = ['name']


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ['spot', 'design_objects']
    search_fields = ['spot', 'design_objects']


