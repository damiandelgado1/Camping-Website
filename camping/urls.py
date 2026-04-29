from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cabin/', include('cabin.urls', namespace="cabin")),
    path('admin/', admin.site.urls),
]