from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cabin/', include('cabin.urls', namespace="cabin")),
    path('client/', include('client.urls', namespace="client")),
    path('reservation/', include('reservation.urls', namespace="reservation")),
    path('admin/', admin.site.urls),
]