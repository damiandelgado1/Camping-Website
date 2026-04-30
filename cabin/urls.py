from django.urls import path
from django.contrib import admin
from .views import ListCabin, DetailCabin, CreateCabin, DeleteCabin


app_name = "cabin"

urlpatterns = [
    path('list/', ListCabin.as_view(), name="cabin_list"),
    path('detail/', DetailCabin.as_view(), name="cabin_detail"),
    path('create/', CreateCabin.as_view(), name="create_cabin"),
    path('delete/', DeleteCabin.as_view(), name="delete_cabin"),
    path('admin/', admin.site.urls),
]