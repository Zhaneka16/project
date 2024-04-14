from django.contrib import admin

# Register your models here.

from .models import Task, Design_object, Spot, Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['type_task', 'data', 'application_completed']


@admin.register(Design_object)
class DesignobjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_completed']


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ['spot']


