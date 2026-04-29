from django.urls import path
from django.contrib import admin
from .views import ListCabin, DetailCabin, CreateCabin, ModifyCabin, DeleteCabin


app_name = "cabin"

urlpatterns = [
    path('list/', ListCabin.as_view(), name="list_cabin"),
    path('detail/', DetailCabin.as_view(), name="detail_cabin"),
    path('create/', CreateCabin.as_view(), name="create_cabin"),
    path('update/', ModifyCabin.as_view(), name="modify_cabin"),
    path('delete/', DeleteCabin.as_view(), name="delete_cabin"),
    path('admin/', admin.site.urls),
]