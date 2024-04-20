from django.urls import path, re_path
from main import views
from .views import TaskAPIView, DesignobjectAPIView, SpotAPIView, DepartmentAPIView, EmployeeAPIView
from .views import TaskAPIDetailView, DesignobjectAPIDetailView, SpotAPIDetailView, DepartmentAPIDetailView, EmployeeAPIDetailView



urlpatterns = [
    path('api/v1/taskdetail/<int:pk>/', TaskAPIDetailView.as_view()),
    path('api/v1/design_objdetail/<int:pk>/', DesignobjectAPIDetailView.as_view()),
    path('api/v1/spotdetail/<int:pk>/', SpotAPIDetailView.as_view()),
    path('api/v1/departmentdetail/<int:pk>/', DepartmentAPIDetailView.as_view()),
    path('api/v1/employeedetail/<int:pk>/', EmployeeAPIDetailView.as_view()),
    path('api/v1/tasklist/', TaskAPIView.as_view()),
    path('api/v1/design_obj_list/', DesignobjectAPIView.as_view()),
    path('api/v1/spotlist/', SpotAPIView.as_view()),
    path('api/v1/departmentlist/', DepartmentAPIView.as_view()),
    path('api/v1/employeelist/', EmployeeAPIView.as_view()),
    path('task2/',views.upload_file),
    path('task/',views.task),
    # path('index/', views.index),
    # path('about/', views.about),
]