from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Department(models.Model):
    department_name = models.CharField(max_length=255)


    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы' 



class Employee(models.Model):
    email = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, related_name='employee_user', on_delete=models.PROTECT)
    departments = models.ForeignKey(to=Department, on_delete=models.PROTECT, related_name='employee_dep')


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники' 
        db_table='Employee'

      


class Design_object(models.Model):
    name = models.CharField(max_length=255)
    project_completed = models.BooleanField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект проектирования'
        verbose_name_plural = 'Объекты проектирования'       



class Spot(models.Model):
    design_objects = models.ForeignKey(to=Design_object, on_delete=models.CASCADE, related_name='spots')
    spot = models.CharField(max_length=255)

    def __str__(self):
        return self.spot

    class Meta:
        verbose_name = 'Пятно'
        verbose_name_plural = 'Пятна'


class Task(models.Model):
    type_task = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    application_completed = models.BooleanField(blank=True, null=True)
    design_objects_type = models.ManyToManyField(to=Design_object)
    description = models.CharField(max_length=255, null = True)

    def __str__(self):
        return self.type_task

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')