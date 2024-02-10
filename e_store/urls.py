from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mall_of_america.urls')),
    path('', include('users.urls')),
]