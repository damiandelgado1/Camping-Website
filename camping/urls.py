from django.contrib import admin
from django.urls import path, include
from .views import main_page

urlpatterns = [
    path('', main_page, name="home"),
    path('client/', include('client.urls', namespace="client")),
    path('cabin/', include('cabin.urls', namespace="cabin")),
    path('core/', include('core.urls', namespace="core")),
    path('reservation/', include('reservation.urls', namespace="reservation")),
    path('admin/', admin.site.urls),
]