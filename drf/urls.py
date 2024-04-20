from django.urls import path, re_path
from drf import views
from .views import TaskAPIView



urlpatterns = [
    path('api/v1/tasklist/', TaskAPIView.as_view()),
]