from django.urls import path
from django.contrib import admin
from .views import create_reservation, cancel_reservation


app_name = "reservation"

urlpatterns = [
    path('create', create_reservation, name="create_reservation"),
    path('cancel', cancel_reservation, name="cancel_reservation"),
    path('admin/', admin.site.urls),
]