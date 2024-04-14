from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('spot/',views.spot),
    path('design_object/',views.design_object),
    path('index/', views.index),
    # path('about/', views.about),
    re_path(r'^about/$', views.about),
    re_path(r'^g+', views.ggg),
    re_path(r'^contacts?', views.contacts),
    re_path(r'^number=\d+', views.numbers),
    re_path(r'^arhive/\d{4}/$', views.arhive), #oграничение количества символов
    path('vse-proyekty/arhitektura/', views.vse_proyekty),
]