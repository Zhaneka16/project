
from django.contrib import admin
from django.urls import path, re_path, include

from main import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    # пути для файла урл других приложений
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)