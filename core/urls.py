from django.urls import path
from django.contrib import admin
from .views import about_site

app_name = "core"

urlpatterns = [
    path('about/', about_site, name="about_us"),
    path('admin/', admin.site.urls),
]