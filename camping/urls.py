from django.contrib import admin
from django.urls import path, include
from .views import main_page, about_site, form_contact

urlpatterns = [
    path('', main_page, name="home"),
    path('about/', about_site, name="about_site"),
    path('contact/', form_contact, name="contact"),
    path('client/', include('client.urls', namespace="client")),
    path('cabin/', include('cabin.urls', namespace="cabin")),
    path('reservation/', include('reservation.urls', namespace="reservation")),
    path('admin/', admin.site.urls),
]